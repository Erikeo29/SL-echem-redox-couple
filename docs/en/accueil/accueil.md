&nbsp;

**Author's note** — *This project was designed entirely by the author, from a blank page through to its deployment online. The content was developed based on the author's own knowledge, supplemented by online research for the documentary part, definition of physical concepts, implementation of relevant numerical tools...*

*For the (very many!) topics beyond the author's initial area of expertise, artificial intelligence and automation tools were used to conduct in-depth internet research (parameterization of physical model equations, selection and use of numerical libraries), writing, testing and debugging code (Python, C++), creating this application's interface, automatic French/English translation...*

*Nonetheless, all results presented in this project are derived from analytical and deterministic physical models solved by recognized and validated numerical solvers. The objective is to enable advanced multiphysics modeling using free and open-source tools.*

*The data used is public and freely available on the internet. This work is made available to be freely used, reproduced and improved for learning purposes or for the use of the physical and numerical models presented here.*

&nbsp;

**Contents:**
1. Objective
2. Available studies
3. Navigation
4. Methodological note

---

## 1. Objective

This application gathers **electrochemical** simulations solved in Python. The objective is to visualize and compare results from parametric studies for two complementary electrochemical systems, covering both the time domain (cyclic voltammetry) and the frequency domain (impedance).

---

## 2. Available studies

### Study 1: CV of a redox couple on Au

Modeling of unsteady mass transport coupled with Butler-Volmer kinetics. The $Fe(CN)_6^{3-} / Fe(CN)_6^{4-}$ system is solved by finite elements (Firedrake) in 2D geometry. The parametric study covers the kinetic constant $k^0$, transfer coefficient $\alpha$ and scan rate $\nu$.

### Study 2: EIS of a redox couple on Au

Electrochemical impedance spectroscopy on a pure gold electrode with a ferro/ferricyanide-type redox couple. The model uses a Randles circuit with CPE and Warburg impedance. The parametric study covers 5 parameters ($n$, $k^0$, $D$, $c$, $Q_0$) for 48 simulations. The extracted metrics ($R_{ct}$, $\sigma$, $C_{dl,eff}$) are complementary to Study 1.

---

## 3. Navigation

Navigation through the different pages of this application is structured with the following tools:

1. **Side menu (left)**: navigation tool between the different sections of the project:
   - **Introduction**: scientific context and system presentation.
   - **Study comparison**: summary table of the two approaches.
   - **Modeling results**: each study contains Physics (description of the physical models and numerical methods used), Code (codes entirely developed in this project and available for duplication) and Results (visual simulations) tabs.
   - **Appendices**: conclusion, glossary, key equations, bibliographical references and a history page on the main researchers and scientists who developed the physical and numerical concepts presented.

2. **Floating navigation buttons (right)**: quick scroll up/down.

3. **AI Assistant (side menu)**: answers questions about the physics or numerical methods.

---

## 4. Methodological note

The results presented come from **pre-computed** simulations. The project was carried out on a standard laptop: Linux environment via WSL2, 1.5-3.5 GHz processor, 6 CPU / 12 threads, 32 GB RAM. Computation times range from a few seconds (Study 2, algebraic calculation) to 60 seconds (Study 1, 2D FEM) per unit simulation.

This application is therefore a **results viewer**, not a real-time simulator. Indeed, running these simulations requires specific environment configurations and Python packages (Firedrake, numpy). The codes are available in the "Code" tabs of each study so they can be copied and used to reproduce these simulations on other machines.
