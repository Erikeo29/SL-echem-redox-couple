**Sommaire :**
1. Architecture
2. Éléments de circuit
3. Paramètres physiques et dérivés
4. Simulation EIS
5. Extraction de métriques
6. Étude paramétrique
7. Dépendances

---

## 1. Architecture

Le code est structuré en 4 modules Python :

| Fichier | Rôle |
|---------|------|
| `circuit_elements.py` | Éléments d'impédance (R, CPE, Warburg, Randles) |
| `parameters_eis.py` | Paramètres physiques, calcul de Rct et σ, combinaisons |
| `eis_simulation.py` | Simulation principale + tracés Nyquist/Bode + extraction métriques |
| `parametric_study_eis.py` | Orchestrateur des 48 runs + analyse de sensibilité |

---

## 2. Éléments de circuit (`circuit_elements.py`)

### CPE (Constant Phase Element)

Modélise une capacité non idéale — la surface d'Au poli n'étant pas parfaitement plane.

```python
def Z_CPE(omega, Q0, n):
    """Z = 1 / (Q₀ (jω)^n), avec n clampé dans [0, 1]."""
    n = np.clip(n, 0.0, 1.0)
    return 1.0 / (Q0 * (1j * omega) ** n)
```

### Warburg (diffusion semi-infinie)

Traduit le transport des espèces redox depuis le bulk vers l'électrode.

```python
def Z_W(omega, sigma):
    """Z = σ/√ω × (1 - j) — droite à 45° sur le Nyquist."""
    return sigma / np.sqrt(omega) * (1.0 - 1j)
```

### Circuit de Randles complet

Assemblage en série/parallèle : Rs en série avec (CPE en parallèle avec Rct + Warburg).

```python
def Z_Randles(omega, Rs, Rct, Q0, n, sigma):
    """Rs → [ CPE_dl ‖ ( Rct + W ) ]"""
    Zcpe = Z_CPE(omega, Q0, n)
    Zw = Z_W(omega, sigma)
    Z_faradaic = Rct + Zw
    Z_parallel = 1.0 / (1.0 / Zcpe + 1.0 / Z_faradaic)
    return Rs + Z_parallel
```

---

## 3. Paramètres physiques et dérivés (`parameters_eis.py`)

### Calcul de Rct depuis k⁰

La résistance de transfert de charge dépend directement de la cinétique du couple redox.

```python
# Rct = RT / (n² F² A k⁰ c)
self.Rct = (R_CONST * T) / (n**2 * F_CONST**2 * A * k0 * c)
```

### Calcul de σ depuis D

Le coefficient de Warburg traduit la limitation par la diffusion.

```python
# σ = RT / (n² F² A √2) × 2 / (√D · c)
self.sigma = (R_CONST * T) / (n**2 * F_CONST**2 * A * np.sqrt(2)) \
    * 2.0 / (np.sqrt(D) * c)
```

### Conversion Q₀ vers SI

L'utilisateur entre Q₀ en µF/cm² ; la conversion en F·s^(n-1) tient compte de la surface.

```python
A_cm2 = A_ELECTRODE * 1e4   # m² → cm²
self.Q0_SI = Q0_uF_cm2 * 1e-6 * A_cm2
```

---

## 4. Simulation EIS (`eis_simulation.py`)

### Génération des fréquences

Espacement logarithmique sur [0.01 Hz, 100 kHz], 10 points par décade → 70 points.

```python
f = np.logspace(np.log10(f_min), np.log10(f_max), n_total)
omega = 2.0 * np.pi * f
```

### Calcul de l'impédance

Un seul appel à Z_Randles avec les paramètres du circuit.

```python
circuit = params.to_circuit_dict()   # {Rs, Rct, Q0, n, sigma}
Z = Z_Randles(omega, **circuit)
```

### Tracé Nyquist avec auto-zoom

Quand la queue Warburg domine (σ >> Rct), un inset zoome automatiquement sur le semicercle HF.

```python
if params.Rct > 0 and Z_re_span > 5 * params.Rct:
    ax_inset = ax.inset_axes([0.55, 0.05, 0.42, 0.42])
    ax_inset.plot(Z.real[mask], -Z.imag[mask], "r.-")
```

---

## 5. Extraction de métriques

### Détection du sommet du semicercle

On cherche le maximum local de $-\text{Im}(Z)$ pour identifier $\omega_{max}$.

```python
maxima = _find_local_maxima(-Z.imag)
idx_max = maxima[0] if maxima else int(np.argmax(-Z.imag))
omega_max = omega[idx_max]
```

### Mesure de Rct et Cdl

Le diamètre du semicercle donne Rct ; la fréquence au sommet donne Cdl.

```python
Rct_measured = 2.0 * (Z_real[idx_max] - Rs_measured)
Cdl_eff = 1.0 / (omega_max * Rct_measured)
```

### Régression de Warburg

La pente $\text{Re}(Z)$ vs $1/\sqrt{\omega}$ à basse fréquence donne σ.

```python
sigma_fit = np.polyfit(1.0 / np.sqrt(omega[:n_low]), Z_real[:n_low], 1)[0]
```

---

## 6. Étude paramétrique (`parametric_study_eis.py`)

### Combinaisons

**48 simulations** : 2 × 3 × 2 × 2 × 2 (n_elec × k⁰ × D × c × Q₀).

```python
FACTOR_LEVELS = {
    "n_elec": (1, 3),
    "k0":     (1e-5, 1e-4, 1e-3),    # m/s
    "D":      (7e-10, 7e-9),           # m²/s
    "conc":   (1.0, 10.0),            # mol/m³
    "Q0":     (10.0, 100.0),          # µF/cm²
}
```

### Analyse de sensibilité

Effets principaux = différence entre la moyenne aux niveaux extrêmes de chaque facteur.

### Matrice d'interaction

Interaction = variation de l'effet d'un facteur selon le niveau d'un autre facteur.

---

## 7. Dépendances

- **numpy** : calcul d'impédance complexe
- **matplotlib** : diagrammes Nyquist et Bode
- **Pillow** : assemblage de la planche Nyquist
- Pas de solveur FEM — calcul purement algébrique
