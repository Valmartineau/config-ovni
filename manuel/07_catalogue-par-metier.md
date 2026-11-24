<!-- Produit par outils/depuis_le_site.py à partir de la page Config OVNI (site a9c0064). Ne pas modifier à la main : relancer le script. -->

# 7. Le catalogue selon votre métier

Des skills d'autres auteurs, installés depuis leur source d'origine : rien n'est recopié ici. 83 entrées. Relecture par OVNI le 10/11/2026 : consignes principales et scripts lus, aucun skill exécuté. Une mise à jour d'un skill annule sa relecture. **Les commandes d'installation n'ont pas été lancées par OVNI : lisez avant.**

## Par métier

- **Méthode de travail** : superpowers, claude-code-setup, code-review, the-fool, feature-forge, spec-miner
- **Design et interface** : frontend-design, apple-design, design-motion-principles, web-asset-generator, krea-generate, krea-marketing, json-canvas
- **Communication et commerce** : the-fool, web-asset-generator, krea-generate, krea-marketing, small-business, wordpress-pro, shopify-expert, salesforce-developer, defuddle
- **Gestion d'entreprise** : the-fool, small-business
- **Notes et documents** : obsidian-markdown, obsidian-bases, obsidian-cli, json-canvas, defuddle, code-documenter, atlassian-mcp
- **Développement** : superpowers, code-review, feature-forge, spec-miner, frontend-design, apple-design, design-motion-principles, wordpress-pro, shopify-expert, salesforce-developer, code-documenter, atlassian-mcp, code-simplifier, fullstack-dev-skills, fullstack-guardian, api-designer, architecture-designer, cli-developer, code-reviewer, debugging-wizard, test-master, playwright-expert, legacy-modernizer, mcp-developer, javascript-pro, typescript-pro, python-pro, golang-pro, rust-engineer, java-architect, kotlin-specialist, csharp-developer, dotnet-core-expert, cpp-pro, php-pro, swift-expert, react-expert, react-native-expert, nextjs-developer, vue-expert, vue-expert-js, angular-architect, flutter-expert, nestjs-expert, fastapi-expert, django-expert, rails-expert, laravel-specialist, spring-boot-engineer, graphql-architect, websocket-engineer, microservices-architect, game-developer, embedded-systems
- **Données et IA** : prompt-engineer, rag-architect, fine-tuning-expert, ml-pipeline, pandas-pro, sql-pro, postgres-pro, database-optimizer, spark-engineer
- **Infrastructure et sécurité** : security-reviewer, secure-code-guardian, devops-engineer, sre-engineer, monitoring-expert, chaos-engineer, cloud-architect, kubernetes-specialist, terraform-engineer

## Les fiches

### superpowers

Cadre le travail avant de coder : idée, plan, tests, vérification, relecture.

Source : https://github.com/obra/superpowers · licence MIT · version bb92a77 · relu le 10/11/2026  
Métiers : Méthode de travail, Développement  
À noter : installe 15 skills d'un coup ; exécute du code sur votre machine.

À savoir :

- Ajoute une règle au début de chaque session : Claude doit utiliser ces skills au moindre doute. Vos propres consignes restent prioritaires.
- Une fois un plan lancé, Claude enchaîne les tâches sans vous consulter et tranche seul les ambiguïtés. Il s'arrête avant une action irréversible ou sensible, un merge, un push ou une publication.
- L'atelier visuel ouvre une page sur votre machine, avec un logo chargé depuis primeradiant.com, sauf si la variable SUPERPOWERS_DISABLE_TELEMETRY vaut 1.

Installer :

```
claude plugin marketplace add anthropics/claude-plugins-official
claude plugin install superpowers@claude-plugins-official
```

Retirer :

```
claude plugin uninstall superpowers@claude-plugins-official
```

### claude-code-setup

Analyse votre projet et propose les automatisations utiles.

Source : https://github.com/anthropics/claude-plugins-official · licence Apache-2.0 · version ea686ba · relu le 10/11/2026  
Métiers : Méthode de travail  

Installer :

```
claude plugin marketplace add anthropics/claude-plugins-official
claude plugin install claude-code-setup@claude-plugins-official
```

Retirer :

```
claude plugin uninstall claude-code-setup@claude-plugins-official
```

### code-review

Relit une modification et signale les erreurs.

Source : https://github.com/anthropics/claude-plugins-official · licence Apache-2.0 · version ea686ba · relu le 10/11/2026  
Métiers : Méthode de travail, Développement  

À savoir :

- Publie des commentaires sur GitHub seulement si vous ajoutez --comment.

Installer :

```
claude plugin marketplace add anthropics/claude-plugins-official
claude plugin install code-review@claude-plugins-official
```

Retirer :

```
claude plugin uninstall code-review@claude-plugins-official
```

### the-fool

Joue l'avocat du diable sur une idée, un plan, une décision.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Méthode de travail, Communication et commerce, Gestion d'entreprise  

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill the-fool -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove the-fool -g -a claude-code -y
```

### feature-forge

Transforme un besoin flou en spécification de fonctionnalité.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Méthode de travail, Développement  

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill feature-forge -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove feature-forge -g -a claude-code -y
```

### spec-miner

Retrouve les règles métier d'un code qui n'a pas de documentation.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Méthode de travail, Développement  

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill spec-miner -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove spec-miner -g -a claude-code -y
```

### frontend-design

Donne une vraie direction visuelle aux interfaces créées.

Source : https://github.com/anthropics/claude-plugins-official · licence Apache-2.0 · version ea686ba · relu le 10/11/2026  
Métiers : Design et interface, Développement  

Installer :

```
claude plugin marketplace add anthropics/claude-plugins-official
claude plugin install frontend-design@claude-plugins-official
```

Retirer :

```
claude plugin uninstall frontend-design@claude-plugins-official
```

### apple-design

Applique les principes d'interface et de mouvement d'Apple au web.

Source : https://github.com/emilkowalski/skills · licence MIT · version 715c180 · relu le 10/11/2026  
Métiers : Design et interface, Développement  

Installer :

```
npx skills@1.7.6 add emilkowalski/skills --skill apple-design -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove apple-design -g -a claude-code -y
```

### design-motion-principles

Crée des animations soignées, ou audite celles qui existent.

Source : https://github.com/kylezantos/design-motion-principles · licence MIT · version 4a9ca87 · relu le 10/11/2026  
Métiers : Design et interface, Développement  

Installer :

```
npx skills@1.7.6 add kylezantos/design-motion-principles --skill design-motion-principles -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove design-motion-principles -g -a claude-code -y
```

### web-asset-generator

Génère favicons, icônes d'application et images de partage.

Source : https://github.com/alonw0/web-asset-generator · licence MIT · version c6d56dc · relu le 10/11/2026  
Métiers : Design et interface, Communication et commerce  
À noter : exécute du code sur votre machine.

À savoir :

- Peut installer ses dépendances Python avec --break-system-packages, sans vous demander : cela modifie le Python de votre système.
- L'option emoji ajoute la bibliothèque pilmoji, que nous n'avons pas relue.

Installer :

```
npx skills@1.7.6 add alonw0/web-asset-generator --skill web-asset-generator -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove web-asset-generator -g -a claude-code -y
```

### krea-generate

Génère et retouche images et vidéos avec Krea.

Source : https://github.com/krea-ai/skills · licence MIT · version 9239bb4 · relu le 10/11/2026  
Métiers : Design et interface, Communication et commerce  
À noter : exécute du code sur votre machine ; se branche à des services extérieurs ; compte nécessaire : Krea.

À savoir :

- Vos fichiers locaux sont envoyés chez Krea pour être traités. Les générations consomment des crédits payants.
- Consigne : préférer l'action à l'analyse. Vérifie les nouvelles versions sur GitHub sans envoyer de données et sans rien installer.

Installer :

```
npx skills@1.7.6 add krea-ai/skills --skill krea-generate -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove krea-generate -g -a claude-code -y
```

### krea-marketing

Produit des visuels de campagne et de produit avec Krea.

Source : https://github.com/krea-ai/skills · licence MIT · version 9239bb4 · relu le 10/11/2026  
Métiers : Design et interface, Communication et commerce  
À noter : se branche à des services extérieurs ; compte nécessaire : Krea.

À savoir :

- Demande votre accord avant un lancement ou une dépense. Un connecteur Meta Ads est possible, en option.

Installer :

```
npx skills@1.7.6 add krea-ai/skills --skill krea-marketing -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove krea-marketing -g -a claude-code -y
```

### small-business

Le pilotage d'une petite entreprise : trésorerie, relances, clôture du mois, contrats, prospects, campagnes, avis clients.

Source : https://github.com/anthropics/knowledge-work-plugins · licence Apache-2.0 · version 1.35.1 (e605d8d) · relu le 10/11/2026  
Métiers : Gestion d'entreprise, Communication et commerce  
À noter : installe 44 skills d'un coup (ad-manager, ap-processor, brand-style, build-agent, build-connector, business-pulse, call-list, canva-creator, cash-flow-snapshot, close-month, content-strategy, contract-review, crm-autopilot, grant-rfp-writer, grow-pipeline, growth-pulse, hiring-screener, inbox-manager, inventory-planner, invoice-chase, job-post-builder, lead-finder, lead-triage, marketing-monday, monday-brief, month-end-prep, outreach-composer, pay-the-bills, payroll-prep, plan-payroll, proposal-builder, reactivate, report-builder, report-pack, restock, review-reputation, seo-ai-visibility, smb-onboard, smb-router, social-content-engine, speed-to-lead, tax-prep, tax-season-organizer, ticket-deflector) ; se branche à des services extérieurs.

À savoir :

- Déclare 35 connecteurs distants : paiement, compta, paie, CRM, mail, agenda, Drive, messagerie. Une fois un compte connecté, ses données passent par le service concerné.
- Demande votre accord pour les envois de mails, paiements, remboursements et publications. La paie n'est jamais lancée à votre place.
- Écrit sans redemander : classement et archivage de mails, jamais de suppression (inbox-manager) ; contacts et journal d'activité du CRM (crm-autopilot) ; profil QuickBooks (content-strategy) ; écriture comptable après une paie que vous avez soumise (payroll-prep).
- speed-to-lead écrit aux prospects au nom du dirigeant, avec la consigne de ne pas dire que la réponse est automatisée. À vous de juger si cela vous convient.
- month-end-prep peut lire ~/Documents/Receipts et enregistre sur le Bureau ; job-post-builder cherche aussi sur le Bureau.

Installer :

```
claude plugin marketplace add anthropics/knowledge-work-plugins
claude plugin install small-business@knowledge-work-plugins
```

Retirer :

```
claude plugin uninstall small-business@knowledge-work-plugins
```

### wordpress-pro

Thèmes, extensions et sites WordPress.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Communication et commerce, Développement  

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill wordpress-pro -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove wordpress-pro -g -a claude-code -y
```

### shopify-expert

Boutiques, thèmes et applications Shopify.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Communication et commerce, Développement  

À savoir :

- Ses étapes publient directement (shopify theme push, shopify app deploy) sans prévoir de confirmation.

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill shopify-expert -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove shopify-expert -g -a claude-code -y
```

### salesforce-developer

Développement et automatisations Salesforce.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Communication et commerce, Développement  

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill salesforce-developer -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove salesforce-developer -g -a claude-code -y
```

### obsidian-markdown

Écrit des notes Obsidian correctes : liens, encadrés, propriétés.

Source : https://github.com/kepano/obsidian-skills · licence MIT · version 3ccff53 · relu le 10/11/2026  
Métiers : Notes et documents  

Installer :

```
npx skills@1.7.6 add kepano/obsidian-skills --skill obsidian-markdown -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove obsidian-markdown -g -a claude-code -y
```

### obsidian-bases

Crée des vues de type base de données dans Obsidian.

Source : https://github.com/kepano/obsidian-skills · licence MIT · version 3ccff53 · relu le 10/11/2026  
Métiers : Notes et documents  

Installer :

```
npx skills@1.7.6 add kepano/obsidian-skills --skill obsidian-bases -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove obsidian-bases -g -a claude-code -y
```

### obsidian-cli

Pilote votre vault Obsidian depuis le terminal.

Source : https://github.com/kepano/obsidian-skills · licence MIT · version 3ccff53 · relu le 10/11/2026  
Métiers : Notes et documents  

À savoir :

- La commande obsidian eval exécute du JavaScript dans l'application.

Installer :

```
npx skills@1.7.6 add kepano/obsidian-skills --skill obsidian-cli -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove obsidian-cli -g -a claude-code -y
```

### json-canvas

Crée des cartes et des schémas au format Canvas.

Source : https://github.com/kepano/obsidian-skills · licence MIT · version 3ccff53 · relu le 10/11/2026  
Métiers : Notes et documents, Design et interface  

Installer :

```
npx skills@1.7.6 add kepano/obsidian-skills --skill json-canvas -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove json-canvas -g -a claude-code -y
```

### defuddle

Extrait le texte propre d'une page web, sans le superflu.

Source : https://github.com/kepano/obsidian-skills · licence MIT · version 3ccff53 · relu le 10/11/2026  
Métiers : Notes et documents, Communication et commerce  

À savoir :

- Peut installer un programme global (npm install -g defuddle) et ouvre les adresses que vous lui donnez.

Installer :

```
npx skills@1.7.6 add kepano/obsidian-skills --skill defuddle -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove defuddle -g -a claude-code -y
```

### code-documenter

Rédige la documentation d'un code ou d'une API.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Notes et documents, Développement  

À savoir :

- Fait lancer des outils tiers avec npx, téléchargés au moment de l'usage.

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill code-documenter -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove code-documenter -g -a claude-code -y
```

### atlassian-mcp

Travaille avec Jira et Confluence.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Notes et documents, Développement  

À savoir :

- Lance un serveur tiers avec uvx, qui utilise vos jetons Atlassian.

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill atlassian-mcp -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove atlassian-mcp -g -a claude-code -y
```

### code-simplifier

Simplifie le code récent sans changer ce qu'il fait.

Source : https://github.com/anthropics/claude-plugins-official · licence Apache-2.0 · version ea686ba · relu le 10/11/2026  
Métiers : Développement  

À savoir :

- Ses consignes le font agir de lui-même juste après l'écriture de code, sans qu'on le demande.

Installer :

```
claude plugin marketplace add anthropics/claude-plugins-official
claude plugin install code-simplifier@claude-plugins-official
```

Retirer :

```
claude plugin uninstall code-simplifier@claude-plugins-official
```

### fullstack-dev-skills

Les 67 spécialistes techniques d'un coup. Mieux vaut prendre seulement ceux qu'il vous faut, listés ici.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · **non relu**  
Métiers : Développement  
À noter : installe 67 skills d'un coup.

À savoir :

- Non relu : il s'installe depuis une autre version que les skills à l'unité (0.4.20) et ajoute 10 commandes de gestion de projet que nous n'avons pas lues.

Installer :

```
claude plugin marketplace add Jeffallan/claude-skills
claude plugin install fullstack-dev-skills@fullstack-dev-skills
```

Retirer :

```
claude plugin uninstall fullstack-dev-skills@fullstack-dev-skills
```

### fullstack-guardian

Construit une fonctionnalité complète, interface et serveur.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Développement  

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill fullstack-guardian -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove fullstack-guardian -g -a claude-code -y
```

### api-designer

Conçoit des API claires et bien documentées.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Développement  

À savoir :

- Fait lancer des outils tiers avec npx, téléchargés au moment de l'usage.

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill api-designer -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove api-designer -g -a claude-code -y
```

### architecture-designer

Compare des architectures et documente le choix.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Développement  

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill architecture-designer -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove architecture-designer -g -a claude-code -y
```

### cli-developer

Crée des outils en ligne de commande.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Développement  

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill cli-developer -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove cli-developer -g -a claude-code -y
```

### code-reviewer

Relit le code : qualité, sécurité, dette.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Développement  

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill code-reviewer -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove code-reviewer -g -a claude-code -y
```

### debugging-wizard

Cherche méthodiquement la cause d'un bug.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Développement  

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill debugging-wizard -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove debugging-wizard -g -a claude-code -y
```

### test-master

Écrit et organise les tests.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Développement  

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill test-master -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove test-master -g -a claude-code -y
```

### playwright-expert

Automatise les tests dans le navigateur.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Développement  

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill playwright-expert -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove playwright-expert -g -a claude-code -y
```

### legacy-modernizer

Modernise un vieux code sans tout casser.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Développement  

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill legacy-modernizer -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove legacy-modernizer -g -a claude-code -y
```

### mcp-developer

Construit des serveurs MCP.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Développement  

À savoir :

- Fait lancer des outils tiers avec npx, téléchargés au moment de l'usage.

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill mcp-developer -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove mcp-developer -g -a claude-code -y
```

### javascript-pro

JavaScript moderne.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Développement  

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill javascript-pro -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove javascript-pro -g -a claude-code -y
```

### typescript-pro

TypeScript et ses types avancés.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Développement  

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill typescript-pro -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove typescript-pro -g -a claude-code -y
```

### python-pro

Python moderne.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Développement  

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill python-pro -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove python-pro -g -a claude-code -y
```

### golang-pro

Go et la concurrence.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Développement  

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill golang-pro -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove golang-pro -g -a claude-code -y
```

### rust-engineer

Rust et la sûreté mémoire.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Développement  

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill rust-engineer -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove rust-engineer -g -a claude-code -y
```

### java-architect

Applications Java d'entreprise.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Développement  

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill java-architect -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove java-architect -g -a claude-code -y
```

### kotlin-specialist

Kotlin, serveur et Android.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Développement  

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill kotlin-specialist -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove kotlin-specialist -g -a claude-code -y
```

### csharp-developer

C# et .NET.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Développement  

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill csharp-developer -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove csharp-developer -g -a claude-code -y
```

### dotnet-core-expert

API et services .NET Core.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Développement  

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill dotnet-core-expert -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove dotnet-core-expert -g -a claude-code -y
```

### cpp-pro

C++ moderne et performance.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Développement  

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill cpp-pro -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove cpp-pro -g -a claude-code -y
```

### php-pro

PHP moderne.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Développement  

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill php-pro -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove php-pro -g -a claude-code -y
```

### swift-expert

Applications Swift pour Apple.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Développement  

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill swift-expert -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove swift-expert -g -a claude-code -y
```

### react-expert

Interfaces React.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Développement  

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill react-expert -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove react-expert -g -a claude-code -y
```

### react-native-expert

Applications mobiles en React Native.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Développement  

À savoir :

- Fait lancer des outils tiers avec npx, téléchargés au moment de l'usage.

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill react-native-expert -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove react-native-expert -g -a claude-code -y
```

### nextjs-developer

Sites et applications Next.js.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Développement  

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill nextjs-developer -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove nextjs-developer -g -a claude-code -y
```

### vue-expert

Interfaces Vue en TypeScript.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Développement  

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill vue-expert -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove vue-expert -g -a claude-code -y
```

### vue-expert-js

Interfaces Vue en JavaScript.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Développement  

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill vue-expert-js -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove vue-expert-js -g -a claude-code -y
```

### angular-architect

Applications Angular.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Développement  

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill angular-architect -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove angular-architect -g -a claude-code -y
```

### flutter-expert

Applications mobiles Flutter.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Développement  

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill flutter-expert -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove flutter-expert -g -a claude-code -y
```

### nestjs-expert

Serveurs NestJS.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Développement  

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill nestjs-expert -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove nestjs-expert -g -a claude-code -y
```

### fastapi-expert

API Python avec FastAPI.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Développement  

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill fastapi-expert -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove fastapi-expert -g -a claude-code -y
```

### django-expert

Applications Django.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Développement  

À savoir :

- Ses étapes modifient la base de données (migrations) : à relire avant de lancer.

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill django-expert -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove django-expert -g -a claude-code -y
```

### rails-expert

Applications Ruby on Rails.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Développement  

À savoir :

- Ses étapes modifient la base de données (migrations) : à relire avant de lancer.

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill rails-expert -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove rails-expert -g -a claude-code -y
```

### laravel-specialist

Applications Laravel.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Développement  

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill laravel-specialist -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove laravel-specialist -g -a claude-code -y
```

### spring-boot-engineer

Services Spring Boot.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Développement  

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill spring-boot-engineer -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove spring-boot-engineer -g -a claude-code -y
```

### graphql-architect

Schémas et API GraphQL.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Développement  

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill graphql-architect -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove graphql-architect -g -a claude-code -y
```

### websocket-engineer

Échanges en temps réel.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Développement  

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill websocket-engineer -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove websocket-engineer -g -a claude-code -y
```

### microservices-architect

Découpage en microservices.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Développement  

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill microservices-architect -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove microservices-architect -g -a claude-code -y
```

### game-developer

Développement de jeux vidéo.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Développement  

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill game-developer -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove game-developer -g -a claude-code -y
```

### embedded-systems

Programmes pour microcontrôleurs et objets.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Développement  

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill embedded-systems -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove embedded-systems -g -a claude-code -y
```

### prompt-engineer

Écrit et évalue des instructions pour modèles.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Données et IA  

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill prompt-engineer -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove prompt-engineer -g -a claude-code -y
```

### rag-architect

Conçoit une recherche documentaire pour IA.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Données et IA  

À savoir :

- Ses exemples envoient vos textes à OpenAI et Cohere.

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill rag-architect -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove rag-architect -g -a claude-code -y
```

### fine-tuning-expert

Spécialise un modèle sur vos données.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Données et IA  

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill fine-tuning-expert -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove fine-tuning-expert -g -a claude-code -y
```

### ml-pipeline

Automatise l'entraînement de modèles.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Données et IA  

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill ml-pipeline -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove ml-pipeline -g -a claude-code -y
```

### pandas-pro

Nettoie et analyse des tableaux de données.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Données et IA  

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill pandas-pro -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove pandas-pro -g -a claude-code -y
```

### sql-pro

Écrit et optimise des requêtes SQL.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Données et IA  

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill sql-pro -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove sql-pro -g -a claude-code -y
```

### postgres-pro

Administre et optimise PostgreSQL.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Données et IA  

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill postgres-pro -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove postgres-pro -g -a claude-code -y
```

### database-optimizer

Accélère les bases de données.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Données et IA  

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill database-optimizer -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove database-optimizer -g -a claude-code -y
```

### spark-engineer

Traite de gros volumes avec Spark.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Données et IA  

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill spark-engineer -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove spark-engineer -g -a claude-code -y
```

### security-reviewer

Audite un code et classe les failles.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Infrastructure et sécurité  

À savoir :

- Lance des outils d'analyse sur votre code (semgrep, bandit, npm audit).

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill security-reviewer -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove security-reviewer -g -a claude-code -y
```

### secure-code-guardian

Écrit un code sûr : connexion, droits, validation.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Infrastructure et sécurité  

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill secure-code-guardian -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove secure-code-guardian -g -a claude-code -y
```

### devops-engineer

Déploiement automatique et conteneurs.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Infrastructure et sécurité  

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill devops-engineer -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove devops-engineer -g -a claude-code -y
```

### sre-engineer

Fiabilité, objectifs de service, incidents.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Infrastructure et sécurité  

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill sre-engineer -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove sre-engineer -g -a claude-code -y
```

### monitoring-expert

Journaux, métriques et alertes.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Infrastructure et sécurité  

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill monitoring-expert -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove monitoring-expert -g -a claude-code -y
```

### chaos-engineer

Provoque des pannes pour tester la résistance.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Infrastructure et sécurité  

À savoir :

- Ses exemples déclenchent de vraies pannes, y compris sur un espace nommé production et sans mode d'essai. À réserver à un environnement prévu pour ça.

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill chaos-engineer -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove chaos-engineer -g -a claude-code -y
```

### cloud-architect

Conçoit et chiffre une infrastructure cloud.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Infrastructure et sécurité  

À savoir :

- Ses exemples créent des rôles AWS : à lire avant de les exécuter.

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill cloud-architect -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove cloud-architect -g -a claude-code -y
```

### kubernetes-specialist

Déploiements Kubernetes.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Infrastructure et sécurité  

À savoir :

- Peut annuler un déploiement si besoin (kubectl rollout undo). Ses annexes installent des outils avec curl | sh.

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill kubernetes-specialist -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove kubernetes-specialist -g -a claude-code -y
```

### terraform-engineer

Infrastructure décrite en Terraform.

Source : https://github.com/Jeffallan/claude-skills · licence MIT · version 078a25c · relu le 10/11/2026  
Métiers : Infrastructure et sécurité  

À savoir :

- Attend votre accord avant terraform apply, mais pas avant terraform state rm.

Installer :

```
npx skills@1.7.6 add Jeffallan/claude-skills --skill terraform-engineer -g -a claude-code -y
```

Retirer :

```
npx skills@1.7.6 remove terraform-engineer -g -a claude-code -y
```
