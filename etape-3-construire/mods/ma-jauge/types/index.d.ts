export type Mesure = { contexte: number | null; h5: number | null; j7: number | null }

declare module 'claude-code' {
  interface PluginState {
    'ma-jauge': { mesure: Mesure | null }
  }
}
