# Données électrochimiques

**Sommaire :**
1. Constantes fondamentales
2. Couple ferro/ferricyanide (études 1 & 2)
3. Hypothèses et limites des modèles

---

## 1. Constantes fondamentales

| Constante | Symbole | Valeur | Unité |
|-----------|---------|--------|-------|
| Constante de Faraday | $F$ | 96 485 | C/mol |
| Constante des gaz | $R$ | 8.314 | J/(mol·K) |
| Température standard | $T$ | 298.15 | K (25°C) |
| $f = F/RT$ | $f$ | 38.94 | V⁻¹ |

---

## 2. Couple ferro/ferricyanide (études 1 & 2)

### Réaction électrochimique

$$\text{Fe(CN)}_6^{3-} + e^- \rightleftharpoons \text{Fe(CN)}_6^{4-}$$

### Paramètres cinétiques

| Paramètre | Symbole | Valeur | Unité | Remarque |
|-----------|---------|--------|-------|----------|
| Potentiel standard | $E^0$ | **+0.36** | V vs Ag/AgCl | Réversible |
| Constante de vitesse | $k^0$ | 1×10⁻⁵ | m/s | Quasi-réversible |
| Coefficient de transfert | $\alpha$ | 0.5 | — | Symétrique |
| Nombre d'électrons | $n$ | 1 | — | — |
| Coefficient de diffusion | $D$ | 7.6×10⁻¹⁰ | m²/s | Identique ox/red |

### Équation de Butler-Volmer

$$i = i_0 \left[ \exp\left(\alpha f \eta\right) - \exp\left(-(1-\alpha) f \eta\right) \right]$$

où $\eta = E - E^0$ est la surtension et $i_0 = nFAk^0 c$ le courant d'échange.

---

## 3. Hypothèses et limites des modèles

### Étude 1 & 2 — Couple redox en solution

| Hypothèse | Justification | Limitation |
|-----------|---------------|------------|
| Diffusion 1D semi-infinie | Électrode plane, solution calme | Ignore convection naturelle |
| Espèces en excès | Électrolyte support >> espèces actives | Pas de migration |
| $D_{ox} = D_{red}$ | Simplification | Peut affecter $\Delta E_p$ |

---
