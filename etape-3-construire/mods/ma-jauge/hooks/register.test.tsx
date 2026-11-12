import { expect, test } from 'claude-code/testing'

const BANDE = { plugin: 'ma-jauge', component: 'AbovePrompt', props: { hasSurvey: false } } as const

test('la jauge montre le contexte et les deux quotas, et prévient à 85 %', async ($, on) => {
  const toasts: string[] = []
  on('ui.toast', (_, e) => { toasts.push(String((e as { text?: string }).text ?? JSON.stringify(e))); return { value: undefined } })
  on('session.measure', (_, e) => e)
  await $.session.measure({
    context: { window: 200000, tokens: 180000, percent: 90 },
    rateLimits: [{ kind: 'five_hour', percentUsed: 23.5 }, { kind: 'seven_day', percentUsed: 7 }],
    changed: ['context', 'rateLimits'],
  })
  const ui = await $.ui.mount({ ...BANDE, surface: 'terminal' })
  const t = await ui.find({ type: 'Text', text: /Contexte/ })
  expect(t?.text).toContain('90 %')
  expect(t?.text).toContain('5 h ▰▰▱▱▱▱▱▱▱▱ 24 %')
  expect(t?.text).toContain('7 j')
  expect(toasts.join(' ')).toContain('Contexte à 90 % : pensez à /compact')
  await ui.unmount()
})
