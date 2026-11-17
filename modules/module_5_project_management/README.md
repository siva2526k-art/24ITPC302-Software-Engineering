# Module V: Project Management

**Course Code:** 24ITPC302 | **Lecture Periods:** 7  
**Core Reference:** Roger S. Pressman (Ch 24–27), Ian Sommerville (Ch 22–23), Rajib Mall (Ch 5)

---

## 🎯 Executive Summary & Learning Outcomes
This module addresses the management dimensions of software engineering: software sizing (LOC and Function Points), empirical cost and effort estimation (COCOMO I and II), Make/Buy decision analysis, project timeline scheduling (WBS, Gantt, PERT/CPM, Critical Path), and project tracking via Earned Value Analysis (EVA).

---

## 📖 Key Syllabus Topics & Deep-Dive Concepts

### 1. The 4 P's of Software Project Management
1. **People:** The most critical asset; recruiting, team structure (Democratized / Egoless vs Controlled Decentralized vs Controlled Centralized / Chief Programmer).
2. **Product:** Defining the scope, functional boundaries, performance constraints, and alternative technical solutions.
3. **Process:** Choosing the appropriate software engineering process model (Agile, Spiral, Waterfall) tailored to project constraints.
4. **Project:** Planning, monitoring, risk control, resource allocation, and quality management.

---

### 2. Software Sizing & Effort Estimation

#### Lines of Code (LOC) vs Function Points (FP)
- **LOC Advantages:** Easy to measure post-completion, widely supported by automated tools.
- **LOC Disadvantages:** Highly dependent on programming language, rewards verbose code, difficult to estimate early during requirement analysis.
- **Function Points (Albrecht):** Language-independent metric computed directly from the SRS.

#### Albrecht Function Point (FP) Model
$$\mathbf{FP = UFC \times \left(0.65 + 0.01 \sum_{i=1}^{14} F_i\right)}$$

1. **Unadjusted Function Count ($UFC$):**
   - External Inputs ($EI$): Data entering from outside (Simple: 3, Average: 4, Complex: 6).
   - External Outputs ($EO$): Reports, screens leaving system (Simple: 4, Average: 5, Complex: 7).
   - External Inquiries ($EQ$): Immediate request-response queries (Simple: 3, Average: 4, Complex: 6).
   - Internal Logical Files ($ILF$): Master data maintained internally (Simple: 7, Average: 10, Complex: 15).
   - External Interface Files ($EIF$): Files accessed from external systems (Simple: 5, Average: 7, Complex: 10).
2. **Value Adjustment Factor ($VAF$):**
   - 14 General System Characteristics ($F_1$ to $F_{14}$ each rated $0$ to $5$): Data communications, distributed processing, performance, heavily used configuration, transaction rate, online data entry, end-user efficiency, online update, complex processing, reusability, installation ease, operational ease, multiple sites, facilitate change.

---

### 3. Make / Buy Decision Analysis
Should an organization build a software system in-house or acquire a commercial off-the-shelf (COTS) package?
- Evaluated via **Decision Tree Analysis**:
  - Expected Cost $= \sum (\text{Probability}_i \times \text{Cost}_i)$.
  - Factors: In-house development cost, maintenance cost over 5 years, customization cost for COTS, licensing fees, support availability, strategic IP value.

---

### 4. COCOMO Models (Barry Boehm)

#### Basic COCOMO I
$$E = a \cdot (KLOC)^b \quad \text{[Person-Months]}, \qquad D = c \cdot (E)^d \quad \text{[Months]}, \qquad P = \frac{E}{D} \quad \text{[Staff Persons]}$$

| Mode | Team & Problem Characteristics | $a$ | $b$ | $c$ | $d$ |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Organic** | Small, experienced team, well-understood problem ($< 50$ KLOC). | **2.4** | **1.05** | **2.5** | **0.38** |
| **Semidetached** | Intermediate team size, mixed experience, medium complexity ($50 - 300$ KLOC). | **3.0** | **1.12** | **2.5** | **0.35** |
| **Embedded** | Tight hardware/software constraints, strict regulations, flight/medical systems. | **3.6** | **1.20** | **2.5** | **0.32** |

#### Intermediate COCOMO I
Includes an **Effort Adjustment Factor ($EAF$)** from 15 cost drivers (Rating: Very Low to Extra High):
$$\mathbf{E = a \cdot (KLOC)^b \times EAF}, \qquad \text{where } EAF = \prod_{i=1}^{15} CD_i$$

#### COCOMO II
Modernized for 3 development stages:
1. *Application Composition Model:* Pre-architecture stage using Object Points.
2. *Early Design Model:* Evaluates architectural alternatives using Unadjusted Function Points.
3. *Post-Architecture Model:* Full estimation with 17 cost drivers and 5 scale factors ($B$).

---

### 5. Project Scheduling & Timeline Tracking
- **Work Breakdown Structure (WBS):** Hierarchical decomposition of project work into discrete work packages and deliverables.
- **Gantt Charts:** Horizontal bar chart displaying task durations, start/end dates, dependencies, and milestones.
- **PERT / CPM Network Analysis:**
  - Identifies earliest start ($ES$), earliest finish ($EF$), latest start ($LS$), latest finish ($LF$).
  - **Float / Slack:** $\text{Slack} = LS - ES = LF - EF$.
  - **Critical Path:** The sequence of dependent tasks where **$\text{Slack} = 0$**. Determines the minimum total duration of the project. Any delay on the critical path delays the entire delivery!

---

### 6. Earned Value Analysis (EVA)
Quantitative technique to monitor cost and schedule progress against the project baseline:

$$\mathbf{CV = EV - AC \quad (\text{Cost Variance})}, \qquad \mathbf{SV = EV - PV \quad (\text{Schedule Variance})}$$
$$\mathbf{CPI = \frac{EV}{AC} \quad (\text{Cost Performance Index})}, \qquad \mathbf{SPI = \frac{EV}{PV} \quad (\text{Schedule Performance Index})}$$
$$\mathbf{EAC = \frac{BAC}{CPI} \quad (\text{Estimate at Completion})}$$

- If $CPI = 1.0, SPI = 1.0 \implies$ Exactly on budget and schedule.
- If $CPI < 1.0 \implies$ Project is experiencing cost overruns.
- If $SPI < 1.0 \implies$ Project is lagging behind schedule.

---

## 🎯 Model University Questions & Combos
- **Combo 5.1 (13M):** A project has the following functional characteristics: 50 inputs (simple), 40 outputs (average), 35 inquiries (average), 6 internal files (complex), 4 external files (simple). All 14 complexity factors are rated 3. Calculate total Function Points and estimated KLOC in Java (53 LOC/FP). Hence, determine development effort and duration under Organic mode using Basic COCOMO.
- **Combo 5.2 (13M):** Explain the Earned Value Analysis (EVA) method. For a project with Budget at Completion $BAC = \$150,000$, calculate $CV, SV, CPI, SPI$, and $EAC$ when $PV = \$60,000, EV = \$55,000, AC = \$65,000$. Provide project management recommendations based on these metrics.
