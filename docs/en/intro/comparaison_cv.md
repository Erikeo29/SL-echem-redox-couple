# Study comparison

**Contents:**
1. Summary table
2. Fundamental differences
3. Complementarity

---

## 1. Summary table

| Criterion | Study 1: CV redox couple on Au | Study 2: EIS redox couple on Au |
| :--- | :--- | :--- |
| **Domain** | Time | **Frequency** |
| **Redox species** | In solution ($Fe(CN)_6^{3-/4-}$) | In solution ($Fe(CN)_6^{3-/4-}$) |
| **Transport** | Diffusion (Fick's law) | 1D diffusion (Warburg) |
| **Variable** | $c(x,y,t)$ concentration | $Z(\omega)$ complex impedance |
| **Solver** | Firedrake + Newton (2D FEM) | numpy (algebraic) |
| **Kinetics** | Classical Butler-Volmer | Randles circuit + CPE |
| **Output** | I(E) voltammogram | Nyquist + Bode |
| **Studied parameters** | $k^0$, $\alpha$, $\nu$ | $n$, $k^0$, $D$, $c$, $Q_0$ |
| **Key metrics** | Ipa, Ipc, ΔEp, ratio | Rct, σ, Cdl, ω_max |
| **Dependencies** | Firedrake, GMSH, scipy | numpy, matplotlib |

---

## 2. Fundamental differences

### Transport vs. impedance

Study 1 solves a spatio-temporal diffusion problem: concentration evolves in space (diffusion layer) and time. Peak current follows the Randles-Ševčík equation: $I_p \propto \sqrt{\nu}$.

Study 2 probes the same redox couple but in the frequency domain. It extracts $R_{ct}$ (inversely proportional to $k^0$) and $\sigma$ (related to $D$), quantities inaccessible through CV.

### Reversibility

- Study 1: the system can be reversible ($\Delta E_p \approx 59$ mV) if $k^0$ is large enough.
- Study 2: reversibility is read from the Nyquist arc diameter (low $R_{ct}$ = fast reaction).

---

## 3. Complementarity

These two studies cover the two main approaches for characterizing the ferro/ferricyanide redox couple:
- **Diffusion-controlled process** (Study 1): reversibility diagnosis, effect of $\nu$
- **Frequency analysis of a redox couple** (Study 2): influence of $k^0$, $D$, $c$ on impedance

EIS extracts quantities inaccessible through CV: **Rct** (charge transfer resistance), **Cdl** (double layer capacitance) and **σ** (Warburg coefficient).
