# algo_ELECTRE

## Méthodes PROMETHEE

**PROMETHEE I** fournit un préordre partiel des candidats.

Tous les degrés de préférence multicritère ainsi calculés sont rassemblés dans la table à l'aide les poids.

Classer les actions dans l'ordre des flux positifs et négatifs. En déduire un classement de Pareto (maximiser Φ + and minimiser Φ - ) des actions, qui sera un préordre partiel.


**PROMETHEE II** fournit un préordre total des candidats.

Classer les actions dans l'ordre des flux net, on obtient un préordre total.

## Méthodes ELECTRE

Tester avec le fichier test.csv

**ELECTRE I** pour les problèmatiques de choix/sélection

Evaluer la condition de non-discordance (ou non-veto) pour chaque couple d'action à l'aide les veto, aussi vous pouvez lui donner un seuil enfin d'avoir un noyau N.

Lorsque s = 0.6, Le noyau est alors N = {A1, A3, A5}.

**ELECTRE II** pour les problématiques de classement

La table de non discordance est inchangée mais la table de concordance est ici calculée de manière différente.

Avec cette nouvelle table de concordance, A4 surclasse toutes les autres actions lorsque seuil est inférieur ou égal à 0.58. Dans ce cas N = {A4}.

Lorsque 0.58 < s ≤ 0.6, N = {A3, A4}.

Lorsque 0.6 < s ≤ 0.8, N = {A1, A3, A4}.

Lorsque 0.8 < s ≤ 0.83, N = {A1, A2, A3, A4, A5}.
