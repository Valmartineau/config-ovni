// Config OVNI, étape 3 : une jauge au-dessus de l'invite. Elle lit les chiffres du moteur, rien ne sort de la machine.
import { atom, read, update } from 'claude-code'
import type { Register } from 'claude-code'

import type { Mesure } from '../types'

const mesure = atom({ plugin: 'ma-jauge', key: 'mesure' } as const, null)
const SEUIL = 85

const barre = (p: number) => {
  const n = Math.max(0, Math.min(10, Math.round(p / 10)))
  return '▰'.repeat(n) + '▱'.repeat(10 - n)
}
const morceau = (nom: string, p: number | null) => (p === null ? '' : `${nom} ${barre(p)} ${Math.round(p)} %`)

export const register: Register = on => {
  on('session.measure', async ($, e, next) => {
    const avant = await read($, mesure)
    const quota = (kind: string) => e.rateLimits.find(r => r.kind === kind)?.percentUsed ?? null
    const m: Mesure = { contexte: e.context.percent ?? null, h5: quota('five_hour'), j7: quota('seven_day') }
    await update($, mesure, () => m)
    if (m.contexte !== null && m.contexte >= SEUIL && (avant?.contexte ?? 0) < SEUIL) {
      $.ui.toast(`Contexte à ${m.contexte} % : pensez à /compact`)
    }
    return next(e)
  })

  on('ui.render', { component: 'AbovePrompt' }, async ($, e, next) => {
    const m = await read($, mesure)
    if (!m || e.props.hasSurvey) return next(e)
    const { Box, Text } = $.ui.resolve(e)
    const ligne = [morceau('Contexte', m.contexte), morceau('5 h', m.h5), morceau('7 j', m.j7)].filter(Boolean).join('   ')
    const plein = (m.contexte ?? 0) >= SEUIL
    return (
      <Box flexDirection="column">
        <Text color={plein ? 'red' : undefined} dimColor={!plein}>{ligne}</Text>
        {await next(e)}
      </Box>
    )
  })
}
