&nbsp;

**Note de l'auteur** — *Ce projet a été conçu intégralement par l'auteur, depuis une page blanche jusqu'à sa mise en ligne. Le contenu a été élaboré sur la base de ses connaissances complétées par des recherches en ligne pour la partie documentaire, définition des concepts physiques, mise en oeuvre des outils numériques pertinents... Pour les sujets (très nombreux !) dépassant son domaine de compétence initial, des outils d'intelligence artificielle et d'automatisation ont été utilisés pour réaliser des recherches internet approfondies (paramétrage des équations des modèles physiques, sélection et utilisation des bibliothèques numériques), la rédaction, le test et la correction des codes (Python, C++), la création de l'interface de cette application, la traduction automatique français / anglais... Il n'en demeure pas moins que tous les résultats présentés dans ce projet sont issus de modèles physiques analytiques et déterministes résolus par des solveurs numériques reconnus et validés. L'objectif est de permettre la réalisation de modélisations multiphysiques avancées au moyen d'outils open-source et gratuits. Les données utilisées sont publiques et disponibles en accès libres sur internet. Ce travail est mis à disposition pour être librement utilisé, reproduit et amélioré à des fins d'apprentissage ou d'exploitation des modèles physiques et numériques présentés.*

&nbsp;

**Sommaire :**
1. Objectif
2. Études disponibles
3. Navigation
4. Note méthodologique

---

## 1. Objectif

Cette application regroupe des simulations **électrochimiques** résolues en Python. L'objectif est de visualiser et comparer les résultats d'études paramétriques pour deux systèmes électrochimiques complémentaires, couvrant le domaine temporel (voltamétrie cyclique) et le domaine fréquentiel (impédance).

---

## 2. Études disponibles

### Étude 1 : CV d'un couple redox sur Au

Modélisation du transport de masse instationnaire couplé à la cinétique de Butler-Volmer. Un système rédox de type ferro/ferricyanure $Fe(CN)_6^{3-} / Fe(CN)_6^{4-}$ est résolu par éléments finis (sous Firedrake) en géométrie 2D. L'étude paramétrique porte sur la constante cinétique $k^0$, le coefficient de transfert $\alpha$ et la vitesse de balayage $\nu$.

### Étude 2 : EIS d'un couple redox sur Au

Spectroscopie d'impédance électrochimique sur une électrode d'or pure avec un couple redox type ferro/ferricyanure. Le modèle utilise un circuit de Randles avec CPE et impédance de Warburg. L'étude paramétrique porte sur 5 paramètres ($n$, $k^0$, $D$, $c$, $Q_0$). Les métriques extraites ($R_{ct}$, $\sigma$, $C_{dl,eff}$) sont complémentaires de l'étude 1.

---

## 3. Navigation

La navigation dans les différentes pages de cette application est structurée avec les outils suivants :

1. **Menu latéral (à gauche)** : outil de navigation entre les différentes sections du projet :
   - **Introduction** : contexte scientifique et présentation des systèmes.
   - **Comparaison des études** : tableau synthétique des deux approches.
   - **Résultats de modélisation** : chaque étude contient des onglets Physique (description des modèles physiques et de résolution numérique utilisés), Code (codes entièrement développés dans ce projet et pouvant être dupliqué) et Résultats (modélisations visuelles).
   - **Annexes** : conclusion, lexique, équations clés, références bibliographiques et une page d'histoire sur les principaux chercheurs et scientifiques ayant développés les concepts physiques et numériques présentés.

2. **Boutons de navigation flottants (à droite)** : déplacement rapide haut/bas de page.

3. **Assistant IA (menu latéral)** : réponses aux questions sur la physique ou les méthodes numériques.

---

## 4. Note méthodologique

Les résultats présentés proviennent de simulations **pré-calculées**. Le projet a été réalisé sur un PC portable standard : environnement Linux via WSL2, processeur 1.5-3.5 GHz, 6 CPU / 12 threads, 32 Go de RAM. Les temps de calcul varient de quelques secondes (étude 2, calcul algébrique) à 60 secondes (étude 1, FEM 2D) par simulation unitaire.

Cette application est donc un **visualiseur de résultats**, non un simulateur en temps réel. En effet, la réalisation de ces simulations nécessite des configurations spécifiques d'environnements et de packages Python (Firedrake, numpy). Les codes sont disponibles dans les onglets "Code" de chaque étude afin de permettre leur reproduction sur d'autres machines.
