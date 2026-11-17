# 24ITPC302: Formula & Concept Checklist (Quick Exam Audit)

Use this checklist before entering the examination hall to verify your mastery of all essential concepts and quantitative formulas.

---

## 📋 Conceptual & Architectural Checklist

### Module I: Software Process & Agile
- [ ] Define Software Engineering vs Programming.
- [ ] List historical causes of the Software Crisis.
- [ ] Explain Waterfall Model linear sequential phases and blocking states.
- [ ] Detail V-Model dual-pathway verification vs validation mapping.
- [ ] Explain Boehm's Spiral Model 4 quadrants and risk-driven nature.
- [ ] State RAD Model 60–90 day cycle and component reuse requirements.
- [ ] List 4 values and 12 principles of the Agile Manifesto.
- [ ] Explain Extreme Programming (XP) lifecycle, Pair Programming, and TDD.

### Module II: Requirements Analysis & Specification
- [ ] Distinguish Functional vs Non-Functional requirements (FURPS+).
- [ ] Outline IEEE 830 standard SRS document structure (Sections 1, 2, 3).
- [ ] Explain 4 types of Feasibility: Technical, Economic, Operational, Schedule.
- [ ] Define 4 steps of Requirements Engineering (Feasibility, Elicitation, Validation, Management).
- [ ] Draw DFD symbols (Process, Store, Entity, Flow) and explain balancing rules.
- [ ] Explain Petri Net components (Places, Transitions, Tokens, Marking) and transition firing rules.
- [ ] Write Data Dictionary notation (`+`, `[ | ]`, `{ }`, `( )`).

### Module III: Software Design
- [ ] Define Abstraction, Modularity, and Information Hiding (Parnas).
- [ ] Define Cohesion; list and explain all 7 levels (Coincidental $\to$ Functional).
- [ ] Define Coupling; list and explain all 6 levels (Content $\to$ Data).
- [ ] Explain Fan-In (maximize) vs Fan-Out (minimize/control: 3 to 7).
- [ ] Compare Architectural Styles: Data-Centered, Layered, Pipe-and-Filter.
- [ ] Describe the complete Transform Mapping procedure from DFD to Structure Chart.
- [ ] State Theo Mandel's 3 Golden Rules for User Interface Design.

### Module IV: Testing & Maintenance
- [ ] Define Verification ("right product?") vs Validation ("product right?").
- [ ] Explain Error $\to$ Fault $\to$ Failure progression.
- [ ] Draw Control Flow Graph (CFG) from code and compute Cyclomatic Complexity $V(G)$.
- [ ] Derive linearly independent basis paths and design test cases.
- [ ] Apply Equivalence Class Partitioning and Boundary Value Analysis ($a, a+1, \text{nom}, b-1, b$).
- [ ] Distinguish Unit, Integration (Top-Down with stubs vs Bottom-Up with drivers), Validation, and System testing.
- [ ] List 4 maintenance types (Corrective, Adaptive, Perfective [50%], Preventive).
- [ ] Detail Software Reengineering Process: Reverse Engineering $\to$ Restructuring $\to$ Forward Engineering.

---

## 🔢 Quantitative / Formula Checklist

- [ ] **Cyclomatic Complexity:**
  $$V(G) = E - N + 2P = P' + 1 = R$$
- [ ] **Function Point (FP):**
  $$FP = UFC \times VAF = UFC \times \left(0.65 + 0.01 \sum_{i=1}^{14} F_i\right)$$
  - Weights for $EI$ (3, 4, 6), $EO$ (4, 5, 7), $EQ$ (3, 4, 6), $ILF$ (7, 10, 15), $EIF$ (5, 7, 10).
- [ ] **Basic COCOMO I:**
  $$E = a(KLOC)^b \text{ [PM]}, \quad D = c(E)^d \text{ [Months]}, \quad P = E/D$$
  - Organic: $a=2.4, b=1.05, c=2.5, d=0.38$
  - Semidetached: $a=3.0, b=1.12, c=2.5, d=0.35$
  - Embedded: $a=3.6, b=1.20, c=2.5, d=0.32$
- [ ] **Intermediate COCOMO:** $E = a(KLOC)^b \times EAF$ where $EAF = \prod CD_i$.
- [ ] **PERT / CPM Critical Path:** Early dates ($ES, EF$), Late dates ($LS, LF$), Float/Slack $= LS - ES = 0$.
- [ ] **Earned Value Analysis (EVA):**
  - $CV = EV - AC$
  - $SV = EV - PV$
  - $CPI = EV / AC$
  - $SPI = EV / PV$
  - $EAC = BAC / CPI$
- [ ] **Risk Exposure:** $RE = P \times C$.
- [ ] **Risk Reduction Leverage:** $RRL = \frac{RE_{\text{before}} - RE_{\text{after}}}{\text{Cost of Action}}$.
