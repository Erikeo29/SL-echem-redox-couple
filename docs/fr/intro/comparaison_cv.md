# Comparaison des études

**Sommaire :**
1. Tableau de synthèse de comparaison CV vs EIS
2. Différences fondamentales
3. Complémentarité

---

## 1. Tableau de synthèse de comparaison CV vs EIS

| Critère | Étude 1 : CV couple redox sur Au | Étude 2 : EIS couple redox sur Au |
| :--- | :--- | :--- |
| **Domaine** | **Temps** | **Fréquence** |
| **Espèces redox** | En solution ($Fe(CN)_6^{3-/4-}$) | En solution ($Fe(CN)_6^{3-/4-}$) |
| **Transport** | Diffusion (loi de Fick) | Diffusion 1D (Warburg) |
| **Variable** | $c(x,y,t)$ concentration | $Z(\omega)$ impédance complexe |
| **Cinétique** | Butler-Volmer classique | Circuit de Randles + CPE |
| **Sortie** | I=f(E) voltammogramme | Nyquist + Bode |
| **Paramètres étudiés** | $k^0$, $\alpha$, $\nu$ | $n$, $k^0$, $D$, $c$, $Q_0$ |
| **Métriques clés** | Ipa, Ipc, ΔEp | Rct, σ, Cdl, ω_max |
| **Solveur** | Firedrake + Newton (FEM 2D) | numpy (algébrique) |
| **Dépendances** | Firedrake, GMSH, scipy | numpy, matplotlib |

---

## 2. Différences fondamentales

### Transport vs. impédance

L'étude 1 résout un problème de diffusion spatio-temporel : la concentration évolue dans l'espace (couche de diffusion) et dans le temps. Le courant de pic suit la loi de Randles-Ševčík : $I_p \propto \sqrt{\nu}$.

L'étude 2 sonde le même couple redox mais dans le domaine fréquentiel. Elle extrait $R_{ct}$ (inversement proportionnel à $k^0$) et $\sigma$ (lié à $D$), des grandeurs inaccessibles en CV.

### Réversibilité

- Étude 1 : le système peut être réversible ($\Delta E_p \approx 59$ mV) si $k^0$ est suffisamment élevé.
- Étude 2 : la réversibilité se lit dans le diamètre de l'arc Nyquist ($R_{ct}$ faible = réaction rapide).

---

## 3. Complémentarité

Ces deux études couvrent  deux grandes approches de caractérisation d'un couple redox type ferro/ferricyanure :
- **Processus contrôlé par diffusion** (étude 1) : diagnostic de réversibilité, effet de $\nu$ (vitesse de balayage)
- **Analyse fréquentielle d'un couple redox** (étude 2) : influence de $k^0$, $D$, $c$ sur l'impédance

L'EIS extrait des grandeurs inaccessibles en CV : **Rct** (résistance de transfert de charge), **Cdl** (capacité de double couche) et **σ** (coefficient de Warburg).
