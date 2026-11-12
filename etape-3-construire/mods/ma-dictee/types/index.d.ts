export type Etat = 'repos' | 'ecoute' | 'transcription' | 'local'

declare module 'claude-code' {
  interface PluginState {
    'ma-dictee': { etat: Etat; derniere: string | null; reponseLocale: string | null }
  }
}
