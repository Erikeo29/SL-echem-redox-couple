
## 1. Summary of studied parameters

| Parameter | Tested values |
|-----------|---------------|
| k⁰ (m/s) | 1e-06, 1e-05, 1e-04, 1e-03 |
| α | 0.3, 0.5, 0.7 |
| scan_rate (V/s) | 0.1, 0.2, 0.5 |

**Fixed parameters**:
- D = 7.0e-9 m²/s
- c_bulk = 1.0 mol/m³ (1 mM)
- E0 = 0.16 V vs Ag/AgCl (sat. KCl)
- n = 1 electron
- T = 298.15 K (25°C)

---

## 2. Main results

### 2.1 Effect of k⁰ on ΔEp

| k⁰ (m/s) | Mean ΔEp (mV) | Regime |
|-----------|---------------|--------|
| 1e-06 | 667 | Irreversible |
| 1e-05 | 400 | Irreversible |
| 1e-04 | 152 | Quasi-reversible |
| 1e-03 | 84 | Reversible |

![ΔEp vs k⁰](delta_Ep_vs_k0.png)

**Interpretation**:
- k⁰ < 1e-5 m/s: irreversible regime (ΔEp > 200 mV)
- 1e-5 < k⁰ < 1e-3 m/s: quasi-reversible regime (100 < ΔEp < 200 mV)
- k⁰ > 1e-3 m/s: reversible/Nernstian regime (ΔEp ~ 59–80 mV)

### 2.2 Effect of α on the Ipa/Ipc ratio

| α | Mean ratio | Trend |
|-------|------------|-------|
| 0.3 | 0.76 | Ipa < Ipc |
| 0.5 | 0.95 | Symmetric |
| 0.7 | 1.20 | Ipc > Ipa |

**Interpretation**:
- α = 0.5: optimal symmetry (ratio close to 1.0)
- α < 0.5: relatively weaker anodic peak
- α > 0.5: relatively weaker cathodic peak

### 2.3 Randles-Ševčík verification

The linearity of Ip vs √(scan_rate) is verified for all tested k⁰ values, confirming a semi-infinite diffusion regime.

![Ip vs √scan_rate — Randles-Ševčík validation](Ip_vs_sqrt_scanrate.png)

---

## 3. Conclusions

### 3.1 Optimal parameters for realistic CV simulation

To simulate the Fe(CN)₆ system behavior with characteristics close to experimental data:

| Parameter | Recommended value | Justification |
|-----------|-------------------|---------------|
| k⁰ | 1e-4 m/s | Quasi-reversible regime, ΔEp ~ 120–180 mV |
| α | 0.5 | Peak symmetry |
| scan_rate | 0.1 V/s | Electrochemical standard |

### 3.2 Model validation

- The Butler-Volmer model correctly captures the irreversible → reversible transition.
- The effect of α on asymmetry is consistent with theory.
- The Randles-Ševčík relationship is satisfied.
