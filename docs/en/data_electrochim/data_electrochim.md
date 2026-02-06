# Electrochemical Data

**Contents:**
1. Fundamental constants
2. Ferro/ferricyanide couple (studies 1 & 2)
3. Model hypotheses and limitations

---

## 1. Fundamental constants

| Constant | Symbol | Value | Unit |
|----------|--------|-------|------|
| Faraday constant | $F$ | 96,485 | C/mol |
| Gas constant | $R$ | 8.314 | J/(mol·K) |
| Standard temperature | $T$ | 298.15 | K (25°C) |
| $f = F/RT$ | $f$ | 38.94 | V⁻¹ |

---

## 2. Ferro/ferricyanide couple (studies 1 & 2)

### Electrochemical reaction

$$\text{Fe(CN)}_6^{3-} + e^- \rightleftharpoons \text{Fe(CN)}_6^{4-}$$

### Kinetic parameters

| Parameter | Symbol | Value | Unit | Note |
|-----------|--------|-------|------|------|
| Standard potential | $E^0$ | **+0.36** | V vs Ag/AgCl | Reversible |
| Rate constant | $k^0$ | 1×10⁻⁵ | m/s | Quasi-reversible |
| Transfer coefficient | $\alpha$ | 0.5 | — | Symmetric |
| Electron number | $n$ | 1 | — | — |
| Diffusion coefficient | $D$ | 7.6×10⁻¹⁰ | m²/s | Same for ox/red |

### Butler-Volmer equation

$$i = i_0 \left[ \exp\left(\alpha f \eta\right) - \exp\left(-(1-\alpha) f \eta\right) \right]$$

where $\eta = E - E^0$ is the overpotential and $i_0 = nFAk^0 c$ the exchange current.

---

## 3. Model hypotheses and limitations

### Studies 1 & 2 — Solution redox couple

| Hypothesis | Justification | Limitation |
|------------|---------------|------------|
| 1D semi-infinite diffusion | Planar electrode, quiescent solution | Ignores natural convection |
| Excess species | Supporting electrolyte >> active species | No migration |
| $D_{ox} = D_{red}$ | Simplification | May affect $\Delta E_p$ |
