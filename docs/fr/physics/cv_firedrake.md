**Sommaire :**
1. Principe de la voltamétrie cyclique
2. Équations fondamentales
3. Forme du signal et interprétation
4. Diagnostic de réversibilité
5. Configuration du modèle Firedrake
6. Références bibliographiques

---

La voltamétrie cyclique (CV) est la méthode électrochimique la plus utilisée pour caractériser les systèmes redox. Cette section présente les fondements théoriques nécessaires à l'interprétation des résultats de simulation.

## 1. Principe de la voltamétrie cyclique

### 1.1 Le système redox étudié

Nous étudions le couple **Ferri/Ferrocyanure** : $Fe(CN)_6^{3-} / Fe(CN)_6^{4-}$

Ce système est une référence en électrochimie car :
- Réaction à 1 électron ($n = 1$)
- Couple quasi-réversible (cinétique rapide)
- Espèces stables en solution aqueuse
- Potentiel standard $E^0 \approx 0.36$ V vs Ag/AgCl

### 1.2 Le balayage de potentiel

Le principe consiste à :
1. Appliquer un potentiel triangulaire $E(t)$ à l'électrode de travail
2. Mesurer le courant résultant $I(t)$
3. Tracer le **voltammogramme** : $I = f(E)$

Le signal de potentiel suit :

$$ E(t) = \begin{cases} E_{start} + v \cdot t & \text{Aller (oxydation)} \\ E_{vertex} - v \cdot t & \text{Retour (réduction)} \end{cases} $$

où $v$ est la **vitesse de balayage** (V/s).

---

## 2. Équations fondamentales

### 2.1 Transport de masse : loi de Fick

Dans une solution support en excès, la migration est négligée. Le transport des espèces électroactives est régi par la **diffusion** :

$$ \frac{\partial c_i}{\partial t} = D_i \nabla^2 c_i $$

| Paramètre | Symbole | Valeur typique |
|-----------|---------|----------------|
| Coefficient de diffusion | $D$ | $7 \times 10^{-9}$ m²/s |
| Concentration bulk | $c^*$ | 1 mM (1 mol/m³) |

### 2.2 Cinétique à l'électrode : Butler-Volmer

Le flux molaire à la surface de l'électrode est défini par l'équation de **Butler-Volmer** :

$$ J = k^0 \left[ c_R \exp\left(\frac{\alpha n F}{RT} \eta\right) - c_O \exp\left(-\frac{(1-\alpha) n F}{RT} \eta\right) \right] $$

avec la **surtension** $\eta = E(t) - E^{0'}$.

| Paramètre | Symbole | Signification |
|-----------|---------|---------------|
| Constante cinétique | $k^0$ | Vitesse de réaction standard (m/s) |
| Coefficient de transfert | $\alpha$ | Symétrie de la barrière d'activation |
| Constante de Faraday | $F$ | 96485 C/mol |
| Température | $T$ | 298.15 K |

---

## 3. Forme du signal et interprétation

### 3.1 Origine de la forme "en bec de canard"

L'allure caractéristique du voltammogramme résulte d'une **compétition** entre deux phénomènes :

1. **Montée du courant** (contrôle cinétique) : l'augmentation de $|\eta|$ accélère exponentiellement le transfert d'électrons (loi de Butler-Volmer).

2. **Pic et chute** (contrôle diffusif) : La consommation de l'espèce réactive à la surface crée une **couche de diffusion** dont l'épaisseur croît avec le temps :

$$ \delta(t) \propto \sqrt{D \cdot t} $$

Le courant de pic apparaît quand le gradient de concentration atteint un maximum.

### 3.2 Courants de pic

- **$I_{pa}$** : Courant de pic anodique (oxydation du Ferrocyanure)
- **$I_{pc}$** : Courant de pic cathodique (réduction du Ferricyanure)

Le ratio $|I_{pa}/I_{pc}|$ est un indicateur de la **réversibilité chimique** du système.

---

## 4. Diagnostic de réversibilité

### 4.1 L'Écart de pic ($\Delta e_p$)

C'est la différence de potentiel entre les pics : $\Delta E_p = |E_{pa} - E_{pc}|$

| Régime | $\Delta E_p$ | Caractéristique |
|--------|--------------|-----------------|
| **Réversible** (Nernstien) | $\approx 59/n$ mV | $k^0$ très élevé |
| **Quasi-réversible** | 59-200 mV | Cinétique modérée |
| **Irréversible** | > 200 mV | $k^0$ faible |

### 4.2 Influence de $k^0$ sur la réponse

- $k^0 > 10^{-3}$ m/s : Système réversible
- $10^{-5} < k^0 < 10^{-3}$ m/s : Quasi-réversible
- $k^0 < 10^{-5}$ m/s : Irréversible

### 4.3 Équation de randles-Ševčík

Pour un système réversible contrôlé par diffusion, le courant de pic suit :

$$ I_p = (2.69 \times 10^5) \, n^{3/2} \, A \, D^{1/2} \, c^* \, v^{1/2} $$

**Diagnostic** :
- Si $I_p \propto \sqrt{v}$ : processus contrôlé par **diffusion**
- Si $I_p \propto v$ : processus impliquant des espèces **adsorbées**

---

## 5. Configuration du modèle Firedrake

### 5.1 Maillage

| Aspect | Configuration |
|--------|---------------|
| **Géométrie** | 2D axisymétrique |
| **Générateur** | GMSH (non-structuré) |
| **Raffinement** | Local à l'interface électrode/électrolyte (µm) |

### 5.2 Éléments finis

| Paramètre | Choix |
|-----------|-------|
| **Type d'éléments** | Lagrange P2 (quadratiques) |
| **Justification** | Précision sur les gradients de concentration |

### 5.3 Résolution numérique

Le système non-linéaire issu de Butler-Volmer est résolu à chaque pas de temps :

| Paramètre | Valeur |
|-----------|--------|
| **Schéma temporel** | Euler implicite (Backward Euler) |
| **Solveur non-linéaire** | Newton-Raphson (`snes_type=newtonls`) |
| **Préconditionnement** | LU (`pc_type=lu`) |

---

## 6. Références bibliographiques

*Pour la liste complète des références, consultez la section Références bibliographiques dans le menu Annexes.*
