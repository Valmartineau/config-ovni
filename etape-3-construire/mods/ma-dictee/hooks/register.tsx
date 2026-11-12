// Config OVNI, étape 3, version souveraine. Trois gestes, et aucun ne quitte la machine :
// Dicter : le micro (SoX) puis whisper.cpp, le texte arrive dans l'invite, à relire avant Entrée.
// Lire : la dernière réponse, par la voix du système.
// Local : ce qui est écrit dans l'invite part à l'agent Hermes de l'étape 2, jamais à Claude.
// Mac et Linux. Sous Windows, prenez Handy pour la dictée.
import { atom, read, update } from 'claude-code'
import type { EngineInterface, Register } from 'claude-code'

import type { Etat } from '../types'

const etat = atom({ plugin: 'ma-dictee', key: 'etat' } as const, 'repos')
const derniere = atom({ plugin: 'ma-dictee', key: 'derniere' } as const, null)
const reponseLocale = atom({ plugin: 'ma-dictee', key: 'reponseLocale' } as const, null)
const PANNEAU = 'agent-local'

// Les chemins se règlent par variables d'environnement, sinon ces valeurs.
let whisper = 'whisper-cli'
let modele = ''
let wav = '/tmp/ma-dictee.wav'

/** Le texte d'une réponse, sans la mise en forme qui se lit mal à voix haute. */
export const aDire = (t: string) => t.replace(/```[\s\S]*?```/g, ' (bloc de code) ').replace(/[*_`#>|]/g, '').replace(/\s+/g, ' ').trim()

async function env($: EngineInterface, nom: string): Promise<string> {
  const r = await $.process.run(['printenv', nom]).catch(() => null)
  return r?.exitCode === 0 ? r.stdout.trim() : ''
}

async function dicter($: EngineInterface) {
  if ((await read($, etat)) !== 'repos') return
  await update($, etat, () => 'ecoute' as Etat)
  try {
    // S'arrête après 2 secondes de silence, 60 secondes au plus.
    const rec = await $.process.run(['rec', '-q', '-c', '1', '-r', '16000', '-b', '16', wav, 'silence', '1', '0.1', '2%', '1', '2.0', '2%', 'trim', '0', '60'], { timeoutMs: 70_000 })
    if (rec.exitCode !== 0) throw new Error('micro : installez SoX, et autorisez le micro pour votre terminal')
    await update($, etat, () => 'transcription' as Etat)
    const w = await $.process.run([whisper, '-m', modele, '-l', 'fr', '-nt', '-np', '-f', wav], { timeoutMs: 120_000 })
    const texte = w.stdout.trim()
    if (w.exitCode !== 0 || !texte) throw new Error('whisper.cpp : vérifiez le programme et le modèle (étape 3 du tuto)')
    await $.prompt.fill({ text: `${texte} `, mode: 'insert' })
  } catch (err) {
    $.ui.toast(`Dictée impossible. ${err instanceof Error ? err.message : ''}`)
  } finally {
    await $.process.run(['rm', '-f', wav]).catch(() => null) // l'audio n'est jamais gardé
    await update($, etat, () => 'repos' as Etat)
  }
}

async function lire($: EngineInterface) {
  const t = await read($, derniere)
  if (!t) return $.ui.toast('Pas encore de réponse à lire.')
  await $.audio.speak(t).catch(() => $.ui.toast('Aucune voix du système disponible.'))
}

async function local($: EngineInterface) {
  const { text } = await $.prompt.read()
  const question = text.trim()
  if (!question) return $.ui.toast("Écrivez d'abord votre question dans l'invite, puis Local au lieu d'Entrée.")
  if ((await read($, etat)) !== 'repos') return
  await $.prompt.fill({ text: '', mode: 'replace' }) // la question quitte l'invite : elle ne sera jamais envoyée à Claude
  await update($, etat, () => 'local' as Etat)
  await update($, reponseLocale, () => null)
  void $.ui.open({ id: PANNEAU, title: 'Agent local' })
  try {
    const r = await $.process.run(['hermes', '-z', question], { timeoutMs: 600_000 })
    await update($, reponseLocale, () => (r.exitCode === 0 ? r.stdout.trim() : `Hermes n'a pas répondu (code ${r.exitCode}). Voyez l'étape 2 du manuel.`))
  } catch {
    await update($, reponseLocale, () => "Hermes est introuvable ou trop lent. Faites d'abord l'étape 2 du manuel.")
  } finally {
    await update($, etat, () => 'repos' as Etat)
  }
}

const LIBELLE: Record<Etat, string> = { repos: '', ecoute: 'J’écoute… (2 s de silence pour finir)', transcription: 'Transcription locale…', local: 'L’agent local réfléchit…' }

export const register: Register = on => {
  on('session.start', async ($, e, next) => {
    whisper = (await env($, 'MA_DICTEE_WHISPER')) || 'whisper-cli'
    modele = (await env($, 'MA_DICTEE_MODELE')) || `${await env($, 'HOME')}/.ma-dictee/ggml-large-v3-turbo-q5_0.bin`
    wav = `${((await env($, 'TMPDIR')) || '/tmp').replace(/\/$/, '')}/ma-dictee.wav`
    await update($, etat, () => 'repos' as Etat)
    await $.command.register({ name: 'dicter', description: 'Dicter dans l’invite, transcription locale' })
    await $.command.register({ name: 'lire', description: 'Lire la dernière réponse avec la voix du système' })
    await $.command.register({ name: 'local', description: 'Envoyer l’invite à l’agent local, jamais à Claude' })
    return next(e)
  })

  on('command.run', { command: 'dicter' }, async $ => { void dicter($); return {} })
  on('command.run', { command: 'lire' }, async $ => { void lire($); return {} })
  on('command.run', { command: 'local' }, async $ => { void local($); return {} })

  on('turn.complete', async ($, e, next) => {
    const fin = await next(e)
    if (e.reason === 'answer' && fin.text) await update($, derniere, () => aDire(fin.text))
    return fin
  })

  on('ui.render', { component: 'AbovePrompt' }, async ($, e, next) => {
    if (e.props.hasSurvey) return next(e)
    const { Box, Button, Text } = $.ui.resolve(e)
    const maintenant = await read($, etat)
    return (
      <Box flexDirection="column">
        <Box>
          <Button key="dicter" label="● Dicter" dimColor={maintenant !== 'repos'} onPress={() => void dicter($)} />
          <Text> </Text>
          <Button key="lire" label="▶ Lire" onPress={() => void lire($)} />
          <Text> </Text>
          <Button key="local" label="⌂ Local" dimColor={maintenant !== 'repos'} onPress={() => void local($)} />
          <Text dimColor> {LIBELLE[maintenant] || 'rien ne sort de la machine'}</Text>
        </Box>
        {await next(e)}
      </Box>
    )
  })

  on('ui.render', { component: 'Pane', requestId: PANNEAU }, async ($, e) => {
    const { Box, Text } = $.ui.resolve(e)
    const r = await read($, reponseLocale)
    return (
      <Box flexDirection="column">
        <Text dimColor>Réponse de votre agent local. Elle reste ici : elle n'entre pas dans la conversation avec Claude.</Text>
        <Text>{r ?? 'L’agent local réfléchit…'}</Text>
      </Box>
    )
  })
}
