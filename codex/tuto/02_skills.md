# 02 — Skills : le même format que Claude Code

Un skill est un dossier avec un fichier `SKILL.md` : un en-tête (`name`,
`description`) puis des consignes. Codex et Claude Code partagent ce format.

## Où les ranger

| Dossier | Portée |
|---|---|
| `~/.agents/skills/<nom>/` | Vous, partout |
| `<projet>/.agents/skills/<nom>/` | Le projet |

Attention : **ce n'est pas `~/.codex/skills`**. Codex lit `~/.agents/skills`.

## Les appeler

- `/skills` liste les skills installés.
- `$nom` dans votre message appelle un skill précis : `$to-do acheter du café`.
- Codex peut aussi en charger un seul quand la `description` correspond à votre demande.

## Ce qui change par rapport à Claude Code

| Claude Code | Codex |
|---|---|
| `/nom` | `$nom` |
| `$ARGUMENTS` dans le skill | Pas d'équivalent : le skill lit votre message |
| `disable-model-invocation: true` | `agents/openai.yaml` → `policy.allow_implicit_invocation: false` |
| `argument-hint`, `allowed-tools` | Pas d'équivalent documenté : retirés |
| `` !`commande` `` (exécutée au chargement) | Pas d'équivalent : retiré |

Les skills du kit sont déjà convertis. Pour les vôtres : `outils/vers_codex.py`
du dépôt config-ovni montre la conversion.

## Les 10 skills du kit

`porte`, `lisible`, `session-note`, `bye`, `to-do`, `micom`, `audit-acces`,
`souverainete-check`, `animejs`, `boussole`.

`porte`, `bye`, `micom` et `lisible` ne se lancent **que si vous les appelez** :
ils agissent ou changent la façon d'écrire.

Deux skills du kit Claude ne passent pas : `fermer-sessions` (il gère les sessions
d'arrière-plan de Claude Code) et `statusline-aide` (Codex n'a pas de status line
par script).

## Faire

```bash
mkdir -p ~/.agents/skills
cp -R skills/* ~/.agents/skills/
```

Nouvelle session, puis `/skills`.

## Réussi si

`/skills` liste les 9, et « note cette idée : ranger le garage » déclenche `to-do`.

## Retirer

`rm -rf ~/.agents/skills/<nom>`
