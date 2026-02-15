**Contents:**
1. Principles of Cyclic Voltammetry
2. Fundamental Equations
3. Signal Shape and Interpretation
4. Reversibility Diagnostics
5. Firedrake Model Configuration
6. Bibliographical References

---

Cyclic voltammetry (CV) is the most widely used electrochemical method for characterizing redox systems. This section presents the theoretical foundations necessary for interpreting simulation results.

## 1. Principles of Cyclic Voltammetry

### 1.1 The Redox System Under Study

We study the **Ferri/Ferrocyanide** couple: $Fe(CN)_6^{3-} / Fe(CN)_6^{4-}$

This system is a reference in electrochemistry because:
- 1-electron reaction ($n = 1$)
- Quasi-reversible couple (fast kinetics)
- Stable species in aqueous solution
- Standard potential $E^0 \approx 0.16$ V vs Ag/AgCl (sat.) at 25°C

### 1.2 Potential Sweep

The principle consists of:
1. Applying a triangular potential $E(t)$ to the working electrode
2. Measuring the resulting current $I(t)$
3. Plotting the **voltammogram**: $I = f(E)$

The potential signal follows:

$$ E(t) = \begin{cases} E_{start} + v \cdot t & \text{Forward (oxidation)} \\ E_{vertex} - v \cdot t & \text{Reverse (reduction)} \end{cases} $$

where $v$ is the **scan rate** (V/s).

---

## 2. Fundamental Equations

### 2.1 Mass Transport: Fick's Law

In a supporting electrolyte excess, migration is neglected. The transport of electroactive species is governed by **diffusion**:

$$ \frac{\partial c_i}{\partial t} = D_i \nabla^2 c_i $$

| Parameter | Symbol | Typical Value |
|-----------|--------|---------------|
| Diffusion coefficient | $D$ | $7.6 \times 10^{-10}$ m²/s |
| Bulk concentration | $c^*$ | 1 mM (1 mol/m³) |

### 2.2 Electrode Kinetics: Butler-Volmer

The molar flux at the electrode surface is defined by the **Butler-Volmer** equation:

$$ J = k^0 \left[ c_R \exp\left(\frac{\alpha n F}{RT} \eta\right) - c_O \exp\left(-\frac{(1-\alpha) n F}{RT} \eta\right) \right] $$

where the **overpotential** is $\eta = E(t) - E^{0'}$.

| Parameter | Symbol | Meaning |
|-----------|--------|---------|
| Kinetic constant | $k^0$ | Standard reaction rate (m/s) |
| Transfer coefficient | $\alpha$ | Symmetry of activation barrier |
| Faraday constant | $F$ | 96485 C/mol |
| Temperature | $T$ | 298.15 K |

---

## 3. Signal Shape and Interpretation

### 3.1 Origin of the "Duck-Beak" Shape

The characteristic voltammogram shape results from a **competition** between two phenomena:

1. **Current rise** (kinetic control): Increasing $|\eta|$ exponentially accelerates electron transfer (Butler-Volmer equation).

2. **Peak and decay** (diffusion control): Consumption of reactive species at the surface creates a **diffusion layer** whose thickness grows with time:

$$ \delta(t) \propto \sqrt{D \cdot t} $$

The peak current appears when the concentration gradient reaches its maximum.

### 3.2 Peak Currents

- **$I_{pa}$**: Anodic peak current (Ferrocyanide oxidation)
- **$I_{pc}$**: Cathodic peak current (Ferricyanide reduction)

The ratio $|I_{pa}/I_{pc}|$ is an indicator of the **chemical reversibility** of the system.

---

## 4. Reversibility Diagnostics

### 4.1 Peak Separation ($\Delta E_p$)

This is the potential difference between peaks: $\Delta E_p = |E_{pa} - E_{pc}|$

| Regime | $\Delta E_p$ | Characteristic |
|--------|--------------|----------------|
| **Reversible** (Nernstian) | $\approx 59/n$ mV | Very high $k^0$ |
| **Quasi-reversible** | 59-200 mV | Moderate kinetics |
| **Irreversible** | > 200 mV | Low $k^0$ |

### 4.2 Effect of $k^0$ on Response

- $k^0 > 10^{-3}$ m/s: Reversible system
- $10^{-5} < k^0 < 10^{-3}$ m/s: Quasi-reversible
- $k^0 < 10^{-5}$ m/s: Irreversible

### 4.3 Randles-Ševčík Equation

For a reversible, diffusion-controlled system, the peak current follows:

$$ I_p = (2.69 \times 10^5) \, n^{3/2} \, A \, D^{1/2} \, c^* \, v^{1/2} $$

**Diagnostics**:
- If $I_p \propto \sqrt{v}$: **diffusion**-controlled process
- If $I_p \propto v$: process involving **adsorbed** species

---

## 5. Firedrake Model Configuration

### 5.1 Mesh

| Aspect | Configuration |
|--------|---------------|
| **Geometry** | 2D axisymmetric |
| **Generator** | GMSH (unstructured) |
| **Refinement** | Local at electrode/electrolyte interface (µm) |

### 5.2 Finite Elements

| Parameter | Choice |
|-----------|--------|
| **Element type** | Lagrange P2 (quadratic) |
| **Justification** | Accuracy on concentration gradients |

### 5.3 Numerical Solution

The nonlinear system from Butler-Volmer is solved at each time step:

| Parameter | Value |
|-----------|-------|
| **Time scheme** | Backward Euler (implicit) |
| **Nonlinear solver** | Newton-Raphson (`snes_type=newtonls`) |
| **Preconditioning** | LU (`pc_type=lu`) |

---

## 6. Bibliographical References

*For the complete reference list, see the Bibliographical References section in the Appendices menu.*
