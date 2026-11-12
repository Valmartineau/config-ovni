import { expect, test } from 'claude-code/testing'

const PANNEAU = { plugin: 'ma-dictee', component: 'Pane', requestId: 'agent-local', props: { title: 'Agent local', isFocused: false, bodyColumns: 60, placement: 'dock', scroll: { offset: 0, bodyRows: 20 }, view: {} } } as const
const attendre = async (ok: () => boolean) => { for (let i = 0; i < 200 && !ok(); i++) await new Promise(r => setTimeout(r, 5)) }

function machine(on: Parameters<Parameters<typeof test>[1]>[1], lances: string[][], remplis: { text: string; mode?: string }[], envois: string[]) {
  on('command.register', (_, e) => ({ value: { command: (e as { name: string }).name } }))
  on('session.start', (_, e) => ({ cwd: (e as { cwd: string }).cwd }))
  on('ui.toast', () => ({ value: undefined }))
  on('ui.open', () => ({ value: { isPlaced: true } }))
  on('prompt.read', () => ({ value: { text: 'Résume mon contrat client', cursor: 0 } }))
  on('prompt.fill', (_, e) => { const { text, mode } = e as { text: string; mode?: string }; remplis.push({ text, mode }); return { isFilled: true } })
  on('prompt.submit', (_, e) => { envois.push(JSON.stringify(e)); return { value: {} } })
  on('process.run', (_, e) => {
    const argv = (e as { argv: string[] }).argv
    lances.push(argv)
    const out = argv[0] === 'printenv' ? (argv[1] === 'HOME' ? '/home/moi\n' : '') : argv[0] === 'whisper-cli' ? ' Bonjour depuis mon micro.\n' : argv[0] === 'hermes' ? 'Voici le résumé, fait chez vous.\n' : ''
    return { value: { exitCode: argv[0] === 'printenv' && !out ? 1 : 0, stdout: out, stderr: '' } }
  })
}

test('Dicter : micro, whisper.cpp local, texte inséré dans l’invite, audio effacé', async ($, on) => {
  const lances: string[][] = [], remplis: { text: string; mode?: string }[] = [], envois: string[] = []
  machine(on, lances, remplis, envois)
  await $.session.start({ cwd: '/', surface: 'terminal', isInteractive: true })
  await $.command.run({ command: 'dicter', args: '' })
  await attendre(() => lances.some(a => a[0] === 'rm'))
  expect(lances.find(a => a[0] === 'whisper-cli')).toEqual(['whisper-cli', '-m', '/home/moi/.ma-dictee/ggml-large-v3-turbo-q5_0.bin', '-l', 'fr', '-nt', '-np', '-f', '/tmp/ma-dictee.wav'])
  expect(remplis).toEqual([{ text: 'Bonjour depuis mon micro. ', mode: 'insert' }])
  expect(lances.at(-1)).toEqual(['rm', '-f', '/tmp/ma-dictee.wav'])
  expect(envois).toEqual([])
})

test('Local : la question quitte l’invite sans être envoyée, la réponse reste dans le panneau', async ($, on) => {
  const lances: string[][] = [], remplis: { text: string; mode?: string }[] = [], envois: string[] = []
  machine(on, lances, remplis, envois)
  await $.session.start({ cwd: '/', surface: 'terminal', isInteractive: true })
  await $.command.run({ command: 'local', args: '' })
  await attendre(() => lances.some(a => a[0] === 'hermes'))
  expect(lances.find(a => a[0] === 'hermes')).toEqual(['hermes', '-z', 'Résume mon contrat client'])
  expect(remplis).toEqual([{ text: '', mode: 'replace' }])
  expect(envois).toEqual([])
  const ui = await $.ui.mount({ ...PANNEAU, surface: 'terminal' })
  await attendre(() => false)
  expect((await ui.find({ type: 'Text', text: /résumé/ }))?.text).toBe('Voici le résumé, fait chez vous.')
  await ui.unmount()
})
