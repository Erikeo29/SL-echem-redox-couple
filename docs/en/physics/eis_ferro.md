**Contents:**
1. Objective
2. EIS principle
3. Equivalent circuit: Randles with CPE
4. Impedance elements
5. Charge transfer and diffusion equations
6. Parametric study: 48 simulations
7. Extracted metrics
8. Bibliographic references

---

## 1. Objective

Quantify the influence of the intrinsic properties of a redox couple (ferro/ferricyanide type)
on the impedance response of a pure gold (Au) electrode, through a systematic parametric study.

The electrode is fixed (pure Au) and we vary the *redox couple properties*: number of electrons, rate constant, diffusion coefficient, concentration, and double layer capacitance.

---

## 2. EIS principle

A small sinusoidal potential perturbation ($\Delta E = 10$ mV) is superimposed on the equilibrium potential:

$$E(t) = E_{eq} + \Delta E \cdot \sin(\omega t)$$

The current response is phase-shifted by an angle $\varphi$:

$$I(t) = \Delta I \cdot \sin(\omega t + \varphi)$$

The complex impedance is defined as:

$$Z(\omega) = \frac{\Delta E}{\Delta I} \cdot e^{j\varphi} = Z'(\omega) + j Z''(\omega)$$

Frequency sweep covers $f \in [0.01$ Hz$, 100$ kHz$]$ with logarithmic spacing (10 points/decade, 70 points).

### Graphical representations

| Diagram | Axes | Information |
|---------|------|-------------|
| **Nyquist** | $-\text{Im}(Z)$ vs $\text{Re}(Z)$ | Arc shapes → mechanisms |
| **Bode magnitude** | $\log\lvert Z\rvert$ vs $\log(f)$ | Limiting resistances |
| **Bode phase** | $-\varphi$ vs $\log(f)$ | Time constants |

![Annotated Nyquist and Bode diagrams](../../../assets/eis/png/nyquist_bode_annotated.png)

*Figure — Example EIS spectrum (Randles circuit): the Nyquist diagram (left) shows the charge transfer semicircle and the 45° Warburg line; the Bode diagrams (center, right) show resistance plateaus and the phase peak.*

---

## 3. Equivalent circuit: Randles with CPE

A single circuit for the entire study (no passive film on pure Au):

![Randles circuit with CPE](../../../assets/eis/png/randles_circuit.png)

- **$R_s$**: solution resistance (50 Ω, fixed) — ohmic drop in KCl 0.1 M electrolyte
- **$CPE_{dl}$**: non-ideal electrochemical double layer ($n_{CPE} = 0.92$ for polished Au)
- **$R_{ct}$**: charge transfer resistance — reflects redox reaction kinetics
- **$Z_W$**: Warburg impedance — reflects diffusion limitation of species

---

## 4. Impedance elements

| Element | Expression | Parameters |
|---------|------------|------------|
| Resistance | $Z_R = R$ | $R$ (Ω) |
| CPE | $Z_{CPE} = \frac{1}{Q_0 (j\omega)^n}$ | $Q_0$ (F·s^(n-1)), $n \in [0,1]$ |
| Warburg | $Z_W = \frac{\sigma}{\sqrt{\omega}}(1-j)$ | $\sigma$ (Ω·s⁻⁰·⁵) |

**CPE** (*Constant Phase Element*): models a non-ideal capacitance. When $n = 1$, the CPE is a pure capacitor; when $n < 1$, it reflects microscopic surface heterogeneity. On polished Au, $n \approx 0.92$.

**Complete Randles circuit**:

$$Z(\omega) = R_s + \frac{1}{\frac{1}{Z_{CPE}} + \frac{1}{R_{ct} + Z_W}}$$

---

## 5. Charge transfer and diffusion equations

### Charge transfer resistance

$$R_{ct} = \frac{RT}{n_{el}^2 F^2 A \, k^0 \, c}$$

| Symbol | Quantity | Value / unit |
|--------|----------|--------------|
| $R$ | Gas constant | 8.314 J/(mol·K) |
| $T$ | Temperature | 293.15 K (20°C) |
| $n_{el}$ | Electrons transferred | 1 or 3 |
| $F$ | Faraday constant | 96 485 C/mol |
| $A$ | Working electrode surface area | $1.77 \times 10^{-6}$ m² |
| $k^0$ | Standard rate constant | $10^{-5}$ to $10^{-3}$ m/s |
| $c$ | Electroactive species concentration | 1 or 10 mol/m³ |

### Warburg coefficient

For an equimolar couple ($c_O = c_R = c$, $D_O = D_R = D$):

$$\sigma = \frac{RT}{n_{el}^2 F^2 A \sqrt{2}} \cdot \frac{2}{\sqrt{D} \cdot c}$$

### Effective capacitance

$$C_{dl,eff} = \frac{1}{\omega_{max} \cdot R_{ct}}$$

---

## 6. Parametric study: 48 simulations

| Parameter | Symbol | Levels | SI unit | Physical effect |
|-----------|--------|--------|---------|-----------------|
| Electrons transferred | $n_{el}$ | 1, 3 | — | n=3 divides $R_{ct}$ and $\sigma$ by 9 ($n^2$ factor) |
| Rate constant | $k^0$ | $10^{-5}$, $10^{-4}$, $10^{-3}$ | m/s | High $k^0$ → small $R_{ct}$ (reversible) |
| Diffusion coeff. | $D$ | $7 \times 10^{-10}$, $7 \times 10^{-9}$ | m²/s | High $D$ → small $\sigma$ (fast diffusion) |
| Concentration | $c$ | 1, 10 | mol/m³ | High $c$ → small $R_{ct}$ and $\sigma$ |
| DL capacitance | $Q_0$ | 10, 100 | µF/cm² | Affects $\omega_{max}$ and $C_{dl,eff}$, not $R_{ct}$ |

**Fixed temperature**: $T = 293.15$ K (20°C).

**Electrode surface area**: $A = 1.77 \times 10^{-6}$ m² (same as Studies 1–3).

**Total**: $2 \times 3 \times 2 \times 2 \times 2 = 48$ runs

---

## 7. Extracted metrics

| Metric | Extraction | Unit |
|--------|-----------|------|
| $R_s$ | HF intercept of $\text{Re}(Z)$ | Ω |
| $R_{ct}$ | Semicircle diameter | Ω |
| $\omega_{max}$ | Angular frequency at semicircle apex | rad/s |
| $C_{dl,eff}$ | $1/(\omega_{max} \cdot R_{ct})$ | F |
| $\sigma_{fit}$ | Warburg slope | Ω·s⁻⁰·⁵ |
| $-\varphi_{max}$ | Maximum phase | ° |

---

## 8. Bibliographic references

*For the complete list of references, see the Bibliographic References section in the Appendices menu.*
