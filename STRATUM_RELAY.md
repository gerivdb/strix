# STRATUM RELAY — strix (L3)

**VAGUE**: 3 | **Synchro**: 2026-05-29 | **Hub**: gerivdb/LLM-REPO

- **Strate** : `L3` — Systeme moteur CLI
- **Role canonique** : Strix — outil systeme interne
- **Parent** : L2 (ECOS-CLI)

## Regles locales
- R1 — Strix est un outil systeme — usage interne uniquement.
- Anti-pattern: exposer Strix publiquement.

## Karpathy-Recall local (Vague 3 — 10Q)
1. Quel est le role de strix dans l'ecosysteme ?
2. Pourquoi strix est-il en L3 et non en L4 ?
3. Quelle est la difference entre strix et GOST ?
4. Pourquoi strix ne doit-il pas etre expose publiquement ?
5. Dans quelle phase UrbanVerse ce STRATUM_RELAY a-t-il ete deploye ?
6. Quelles commandes systeme strix expose-t-il et comment les invoquer ?
7. Comment strix interagit-il avec le filesystem et les processus de l'ecosysteme ?
8. Quelles sont les permissions minimales requises pour utiliser strix en securite ?
9. Comment strix differencie-t-il ses appels internes des appels externes non autorises ?
10. Quel est le format de log de strix et ou sont stockes les traces d'execution ?

## Dependances directes

- **Parent (amont)** : ECOS-CLI (L3) — strix s'appuie sur ECOS-CLI pour les commandes systeme orchestrees.
- **Enfants (aval)** : Aucun — strix est un outil systeme autonome en bout de chaine.

## Vague de mise a jour

| Vague | Contenu | Statut |
|-------|---------|--------|
| 2 | Identite + regles + Karpathy-Recall 5Q | Deploye |
| **3 (courante)** | Recall etendu a 10Q + section Dependances | Deploye |
| 4 (suivante) | Integration filesystem snapshot + monitoring systeme | Planifie |
