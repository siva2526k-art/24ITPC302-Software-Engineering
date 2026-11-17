# ⚡ 24ITPC302: 1-Day High-Yield Exam Cram & Mastery Plan
### Course: 24ITPC302 – Software Engineering (Regulations 2024)
### Target: Maximum Score in Tomorrow's Examination

This intensive 1-day study plan is reverse-engineered from your faculty's exact priority question list. It is divided into **Tonight's Deep Mastery (7:30 PM – 1:45 AM)** and **Tomorrow Morning's Formula & Diagram Recall (6:30 AM – 8:30 AM)**.

---

## 🕒 TIMETABLE OVERVIEW

```
  TONIGHT: FOUNDATION & HIGH-WEIGHTAGE UNITS (7:30 PM – 1:45 AM)
  -------------------------------------------------------------------------------
  7:30 PM - 09:00 PM  |  BLOCK 1: UNIT 1 — The 6 Process & Agile Models (30M Scope)
  9:00 PM - 10:30 PM  |  BLOCK 2: UNIT 2 — Requirements, SRS, Petri Nets (25M Scope)
  10:30 PM - 11:15 PM |  DINNER BREAK & MENTAL RESET
  11:15 PM - 12:30 AM |  BLOCK 3: UNIT 3 — Design Pyramid, Architecture, 12 Concepts
  12:30 AM - 01:45 AM |  BLOCK 4: UNIT 5 — COCOMO & Earned Value Numericals (Guaranteed 13M)
  01:45 AM - 06:30 AM |  REST & MEMORY CONSOLIDATION (4.5 – 5 Hours Sleep)

  TOMORROW MORNING: REVISION & DIAGRAM RECALL (6:30 AM – 8:30 AM)
  -------------------------------------------------------------------------------
  6:30 AM - 07:30 AM  |  BLOCK 5: UNIT 6 & 4 — RMMM Plan, CASE OMS & Cyclomatic V(G)
  7:30 AM - 08:30 AM  |  BLOCK 6: FORMULA BANK & 2-MARK RAPID FIRE DRILL
  8:30 AM onwards     |  TRANSIT & EXAM HALL CONFIDENCE
```

---

## 🌙 TONIGHT: DEEP DIVE REVISION SPRINT

### 🔹 BLOCK 1 (7:30 PM – 9:00 PM) | UNIT 1: Process Models & Agile
*Read Section 1 of [CAT_1_2026_SE_SOLUTIONS.md](file:///C:/Users/siva2/OneDrive/Desktop/soft/question_papers/CAT_1_2026_SE_SOLUTIONS.md)*

1. **Agile Manifesto & 4 Values (15 Mins):**
   - Memorize the 4 tradeoffs: *Individuals/Interactions*, *Working Software*, *Customer Collaboration*, *Responding to Change*.
   - Recall 4 key principles (Continuous delivery, welcome change, daily collaboration, simplicity).
2. **Boehm's Spiral Model (20 Mins):**
   - **Diagram:** Draw the 4 quadrants on paper: (I) Objective Setting $\to$ (II) Risk Analysis $\to$ (III) Engineering Development $\to$ (IV) Planning & Customer Review.
   - **Key examiner phrase:** State why it is *"Risk-Driven"* (effort spent is governed by risk severity; stops project early if risk is fatal).
3. **Extreme Programming (XP) (20 Mins):**
   - **Pair Programming:** Define Driver (tactical typing) vs. Navigator (strategic review). State 3 benefits (15–20% fewer defects, continuous review, no single failure point).
   - **Test-Driven Development (TDD):** Define Red-Green-Refactor.
4. **Waterfall, V-Model & Incremental (25 Mins):**
   - **Waterfall:** 5 phases, blocking states, late working software, compilers/legacy systems.
   - **V-Model:** Left wing = Verification; Right wing = Validation; Defect Prevention Principle.
   - **Incremental:** Increment 1 = Core product; Successive = Added features.

---

### 🔹 BLOCK 2 (9:00 PM – 10:30 PM) | UNIT 2: Requirements & Petri Nets
*Read Section 2 of [CAT_1_2026_SE_SOLUTIONS.md](file:///C:/Users/siva2/OneDrive/Desktop/soft/question_papers/CAT_1_2026_SE_SOLUTIONS.md)*

1. **IEEE 830-1998 Standard SRS Template (25 Mins):**
   - Practice the 3-section outline from memory:
     - *1. Introduction* (Purpose, Scope, Definitions, References, Overview)
     - *2. Overall Description* (Perspective, Functions, User classes, Constraints, Assumptions)
     - *3. Specific Requirements* (External Interfaces [UI, HW, SW, Comm], Functional, Performance, Constraints, System Attributes).
   - Memorize the 6 qualities: *Unambiguous, Complete, Consistent, Verifiable, Modifiable, Traceable*.
2. **Requirements Engineering Process & RTM (20 Mins):**
   - 4 steps: Feasibility Study $\to$ Elicitation/Analysis $\to$ Specification $\to$ Validation.
   - Draw an **RTM Table** (Req ID $\to$ Design Module $\to$ Code File $\to$ Test Case ID).
3. **Petri Nets & Concurrency Modeling (25 Mins):**
   - Formal 5-tuple: $\mathbf{PN = (P, T, F, W, M_0)}$.
   - Transition Enabling Rule ($M(p) \ge W(p, t)$) and Firing Rule.
   - Draw Producer-Consumer ($N=1$ buffer) and trace $M_0 \to M_1 \to M_2$.
4. **Functional vs Non-Functional (FURPS+) (15 Mins):**
   - FURPS+ breakdown: Functionality, Usability, Reliability, Performance, Supportability, "+".
   - Testable metrics: Response latency $< 1.5$s, Throughput $\ge 3500$ TPS, Availability $\ge 99.99\%$.

---

### 🍽️ 10:30 PM – 11:15 PM | Dinner, Hydration & Mental Break

---

### 🔹 BLOCK 3 (11:15 PM – 12:30 AM) | UNIT 3: Software Design & Architecture
*Read Section 3 of [CAT_1_2026_SE_SOLUTIONS.md](file:///C:/Users/siva2/OneDrive/Desktop/soft/question_papers/CAT_1_2026_SE_SOLUTIONS.md)*

1. **Pressman's 4-Level Software Design Pyramid (25 Mins):**
   - Draw the pyramid on paper:
     - Level 1 (Base): **Data/Class Design** (transforms analysis classes into DB schema).
     - Level 2: **Architectural Design** (subsystems and messaging patterns).
     - Level 3: **Interface Design** (user UI, external APIs, internal interfaces).
     - Level 4 (Apex): **Component-Level Design** (algorithms, flowcharts, PDL).
   - Heuristics: $3 \le \text{Fan-Out} \le 7$ (span of control); **Maximize Fan-In** (reusability).
2. **Architectural Styles & Patterns (25 Mins):**
   - *Data-Centered (Repository):* Draw central store + clients. (Bottleneck trade-off).
   - *Data-Flow (Pipe-and-Filter):* Draw pipes + filter boxes. (Parallelizable, bad for GUI).
   - *Layered (Call-and-Return):* UI $\to$ Business Logic $\to$ Data Access $\to$ DB.
   - *Event-Driven (Pub-Sub):* Event broker + decoupled publishers/subscribers.
3. **The 12 Pressman Design Concepts (20 Mins):**
   - Abstraction, Architecture, Patterns, Separation of Concerns, Modularity, Information Hiding (Parnas), Functional Independence, Refinement (Wirth), Aspects, Refactoring, OOP, Design Classes.
   - **Cohesion Ranking:** *Coincidental $\to$ Logical $\to$ Temporal $\to$ Procedural $\to$ Communicational $\to$ Sequential $\to$* **Functional (Best)**.
   - **Coupling Ranking:** *Content (Worst) $\to$ Common $\to$ Control $\to$ Stamp $\to$* **Data (Best)** $\to$ *Uncoupled*.

---

### 🔹 BLOCK 4 (12:30 AM – 1:45 AM) | UNIT 5: Sizing, COCOMO & Earned Value (Guaranteed 13M)
*Read Section 2 of [CAT_2_2026_SE_SOLUTIONS.md](file:///C:/Users/siva2/OneDrive/Desktop/soft/question_papers/CAT_2_2026_SE_SOLUTIONS.md)*

1. **Basic COCOMO I Equations & 35 KLOC Numerical (35 Mins):**
   - Formulas: $E = a \cdot (KLOC)^b \text{ PM}, \quad D = c \cdot (E)^d \text{ Months}, \quad P = E / D$.
   - **Organic ($a=2.4, b=1.05, c=2.5, d=0.38$):** $E = 100.2\text{ PM}, D = 14.4\text{ Mos}, P \approx 7\text{ Staff}$.
   - **Embedded ($a=3.6, b=1.20, c=2.5, d=0.32$):** $E = 255.7\text{ PM}, D = 14.8\text{ Mos}, P \approx 18\text{ Staff}$.
2. **Earned Value Analysis (EVA) Complete Numerical (30 Mins):**
   - Formulas: $CV = EV - AC, \quad SV = EV - PV, \quad CPI = EV / AC, \quad SPI = EV / PV, \quad EAC = BAC / CPI$.
   - Numerical: Given $BAC=\$150\text{k}, PV=\$75\text{k}, EV=\$60\text{k}, AC=\$70\text{k}$:
     - $CV = -\$10\text{k}$ (Over budget), $SV = -\$15\text{k}$ (Behind schedule).
     - $CPI = 0.857, \ SPI = 0.800$.
     - $EAC = \$175,000$ (overrun $\$25\text{k}$), $ETC = \$105,000$.
3. **Risk Exposure & Leverage (10 Mins):**
   - $RE = P \times C \mid RRL = \frac{RE_{\text{before}} - RE_{\text{after}}}{\text{Cost of Action}} = \frac{20\text{k} - 4\text{k}}{6\text{k}} = 2.67 > 1.0 \implies$ Approved!

---

### 😴 1:45 AM – 6:30 AM | SLEEP & RECHARGE
*Do not stay up all night! 4.5 hours of sleep is critical so you don't make arithmetic mistakes on COCOMO and EVA formulas.*

---

## ☀️ TOMORROW MORNING: EXAM-DAY FORMULA & RECALL

### 🔹 BLOCK 5 (6:30 AM – 7:30 AM) | UNIT 6 & UNIT 4 High-Yield Topics
*Read [CAT_2_2026_SE_SOLUTIONS.md](file:///C:/Users/siva2/OneDrive/Desktop/soft/question_papers/CAT_2_2026_SE_SOLUTIONS.md)*

1. **Unit 6: RMMM Plan Table (25 Mins):**
   - 3 pillars: Mitigation (avoidance), Monitoring (triggers), Management (contingency).
   - Re-read the Staff Turnover table (Pair programming, 50 hrs/wk trigger, contract backup).
2. **Unit 6: CASE Tools Architecture & OMS (15 Mins):**
   - Draw UI Layer $\to$ Tool Integration $\to$ OMS Central Repository. Upper vs Lower vs I-CASE.
3. **Unit 4: Cyclomatic Complexity $V(G)$ & Basis Paths (20 Mins):**
   - 3 Formulas: $V(G) = E - N + 2P = P' + 1 = \text{Enclosed Regions} + 1$.
   - Review `findMax(a, b, c)`: $N=6, E=7 \implies V(G) = 3$. Independent paths 1, 2, 3.
   - Boundary Value Analysis (BVA): $\{a, a+1, \text{nom}, b-1, b\}$.
   - Stubs (Top-Down) vs Drivers (Bottom-Up).

---

### 🔹 BLOCK 6 (7:30 AM – 8:30 AM) | THE 10-MINUTE CHEAT SHEET MEMORIZATION
*Review [SOFTWARE_ENGINEERING_FORMULA_AND_METRICS_BANK.md](file:///C:/Users/siva2/OneDrive/Desktop/soft/formula_bank/SOFTWARE_ENGINEERING_FORMULA_AND_METRICS_BANK.md)*

- **COCOMO Constants Table:**
  - Organic: $a=2.4, b=1.05, c=2.5, d=0.38$
  - Semidetached: $a=3.0, b=1.12, c=2.5, d=0.35$
  - Embedded: $a=3.6, b=1.20, c=2.5, d=0.32$
- **Function Point Formula:** $FP = UFC \times [0.65 + 0.01 \sum F_i]$.
- **EVA Rules:** $CV < 0 \implies$ Over Budget; $SV < 0 \implies$ Behind Schedule; $CPI < 1.0 \implies$ Inefficient.
- **Golden Rules:** Maximize Cohesion (Functional), Minimize Coupling (Data).

---

## 🎯 EXAM HALL TACTICS (HOW TO GET 95+ MARKS)

1. **First 5 Minutes:**
   - Scan Part B questions. Immediately identify the questions from your priority list (Spiral, XP, SRS, Petri Net, Design Pyramid, COCOMO, EVA, RMMM).
2. **Diagrams First:**
   - Examiners in Anna University and autonomous colleges award 50% of the marks based on diagrams. Draw the diagram **first** (boxed with labels), then write the explanation below it.
3. **Equations Boxed:**
   - Always put final numerical answers inside a neat box:  
     $$\boxed{V(G) = 3} \qquad \boxed{E = 100.23 \text{ PM}} \qquad \boxed{CPI = 0.857}$$
4. **Time Management:**
   - Part A (5 questions): 20 Minutes (4 mins per question).
   - Part B (3 questions): 65 Minutes (~21 mins per 13-Mark question).
   - Final Review: 5 Minutes (check arithmetic units like Person-Months, TPS, %).
