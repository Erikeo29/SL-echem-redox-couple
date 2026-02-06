**Contents:**
1. Architecture
2. Circuit elements
3. Physical parameters and derived quantities
4. EIS simulation
5. Metrics extraction
6. Parametric study
7. Dependencies

---

## 1. Architecture

The code is structured in 4 Python modules:

| File | Role |
|------|------|
| `circuit_elements.py` | Impedance elements (R, CPE, Warburg, Randles) |
| `parameters_eis.py` | Physical parameters, Rct and σ computation, combinations |
| `eis_simulation.py` | Main simulation + Nyquist/Bode plots + metrics extraction |
| `parametric_study_eis.py` | 48-run orchestrator + sensitivity analysis |

---

## 2. Circuit elements (`circuit_elements.py`)

### CPE (Constant Phase Element)

Models a non-ideal capacitance — polished Au surface is not perfectly flat.

```python
def Z_CPE(omega, Q0, n):
    """Z = 1 / (Q₀ (jω)^n), with n clamped to [0, 1]."""
    n = np.clip(n, 0.0, 1.0)
    return 1.0 / (Q0 * (1j * omega) ** n)
```

### Warburg (semi-infinite diffusion)

Represents species transport from bulk to the electrode surface.

```python
def Z_W(omega, sigma):
    """Z = σ/√ω × (1 - j) — 45° line on the Nyquist plot."""
    return sigma / np.sqrt(omega) * (1.0 - 1j)
```

### Complete Randles circuit

Series/parallel assembly: Rs in series with (CPE parallel with Rct + Warburg).

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

## 3. Physical parameters and derived quantities (`parameters_eis.py`)

### Rct from k⁰

Charge transfer resistance depends directly on the redox couple kinetics.

```python
self.Rct = (R_CONST * T) / (n**2 * F_CONST**2 * A * k0 * c)
```

### σ from D

Warburg coefficient reflects diffusion limitation.

```python
self.sigma = (R_CONST * T) / (n**2 * F_CONST**2 * A * np.sqrt(2)) \
    * 2.0 / (np.sqrt(D) * c)
```

### Q₀ to SI conversion

User enters Q₀ in µF/cm²; conversion to F·s^(n-1) accounts for electrode area.

```python
A_cm2 = A_ELECTRODE * 1e4
self.Q0_SI = Q0_uF_cm2 * 1e-6 * A_cm2
```

---

## 4. EIS simulation (`eis_simulation.py`)

### Frequency generation

Logarithmic spacing over [0.01 Hz, 100 kHz], 10 points per decade → 70 points.

```python
f = np.logspace(np.log10(f_min), np.log10(f_max), n_total)
omega = 2.0 * np.pi * f
```

### Impedance computation

Single call to Z_Randles with circuit parameters.

```python
circuit = params.to_circuit_dict()
Z = Z_Randles(omega, **circuit)
```

### Nyquist plot with auto-zoom

When the Warburg tail dominates (σ >> Rct), an inset automatically zooms on the HF semicircle.

```python
if params.Rct > 0 and Z_re_span > 5 * params.Rct:
    ax_inset = ax.inset_axes([0.55, 0.05, 0.42, 0.42])
    ax_inset.plot(Z.real[mask], -Z.imag[mask], "r.-")
```

---

## 5. Metrics extraction

### Semicircle apex detection

Local maximum of $-\text{Im}(Z)$ identifies $\omega_{max}$.

```python
maxima = _find_local_maxima(-Z.imag)
omega_max = omega[maxima[0]]
```

### Rct and Cdl measurement

Semicircle diameter gives Rct; apex frequency gives Cdl.

```python
Rct_measured = 2.0 * (Z_real[idx_max] - Rs_measured)
Cdl_eff = 1.0 / (omega_max * Rct_measured)
```

### Warburg regression

Slope of $\text{Re}(Z)$ vs $1/\sqrt{\omega}$ at low frequency gives σ.

```python
sigma_fit = np.polyfit(1.0 / np.sqrt(omega[:n_low]), Z_real[:n_low], 1)[0]
```

---

## 6. Parametric study (`parametric_study_eis.py`)

**48 simulations**: 2 × 3 × 2 × 2 × 2 (n_elec × k⁰ × D × c × Q₀).

```python
FACTOR_LEVELS = {
    "n_elec": (1, 3),
    "k0":     (1e-5, 1e-4, 1e-3),
    "D":      (7e-10, 7e-9),
    "conc":   (1.0, 10.0),
    "Q0":     (10.0, 100.0),
}
```

---

## 7. Dependencies

- **numpy**: complex impedance computation
- **matplotlib**: Nyquist and Bode diagrams
- **Pillow**: Nyquist planche assembly
- No FEM solver — purely algebraic computation
