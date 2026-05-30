# STRATUM RELAY — strix (L3)

**VAGUE**: 4 | **Synchro**: 2026-05-30 | **Hub**: gerivdb/LLM-REPO

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

## Agents locaux (Vague 4)

```yaml
# .roomodes — profil agent strix
agent: strix-ops
strate: L3
role: Internal system tool
rules: strix/rules/system_rules.yaml
hub_ref: ECOS-CLI
```

L'agent `strix-ops` execute les commandes systeme internes, filtre les requetes externes non autorisees, et mainten le log d'execution.

## Auto-conformite (Vague 4)

- **Guard 1 — Internal only** : Strix refuse toute requete provenant d'une source externe non authentifiee.
- **Guard 2 — No public exposure** : Aucune commande ou endpoint de strix n'est expose publiquement.
- **Guard 3 — Execution logging** : Chaque execution de commande systeme est journallee pour audit.

## Vague de mise a jour

| Vague | Contenu | Statut |
|-------|---------|--------|
| 2 | Identite + regles + Karpathy-Recall 5Q | Deploye |
| 3 | Recall etendu a 10Q + section Dependances | Deploye |
| **4 (courante)** | Agents locaux + auto-conformite | Deploye |

---

*Genere par `VERSUS/urban_ontology_verse/TOOLS/relay_propagator.py` v4.0*
*UrbanVerse v4.0.0 — gerivdb/VERSUS (L8)*
*IntentHash: 0xPHASE8_STRIX_V4_20260530*