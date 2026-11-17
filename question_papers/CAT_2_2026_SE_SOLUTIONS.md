# 24ITPC302: CAT-II Model Examination Question Paper & Detailed Solutions
### Sri Sai Ram Engineering College (Autonomous) — Regulations 2024
### Department of Information Technology & Computer Science and Engineering
**Course:** 24ITPC302 – Software Engineering | **Max Marks:** 50 | **Duration:** 1 ½ Hours  
**Coverage:** Units IV, V, VI (Syllabus Faculty Priority Questions)

---

## PART – A (5 × 2 = 10 Marks) — Answer ALL Questions

### Q1: Define McCabe's Cyclomatic Complexity V(G) and state its three calculation formulas. [2 Marks | K2]
**Answer:**
Cyclomatic Complexity $V(G)$ defines the upper bound on the number of linearly independent paths through program source code.
1. *Edges and Nodes:* $\mathbf{V(G) = E - N + 2P}$ (where $P=1$).
2. *Predicate Nodes:* $\mathbf{V(G) = P' + 1}$ (where $P'$ is decision nodes).
3. *Enclosed Regions:* $\mathbf{V(G) = \text{Enclosed Regions} + 1}$ (outer region).

---

### Q2: Differentiate between Test Drivers and Test Stubs in Integration Testing. [2 Marks | K2]
**Answer:**
- **Test Driver:** A dummy calling program that invokes the module under test and passes test data. Used in **Bottom-Up Integration Testing**.
- **Test Stub:** A dummy called program that simulates the behavior of a subordinate submodule. Used in **Top-Down Integration Testing**.

---

### Q3: State the governing effort and time equations for Basic COCOMO I in Organic and Embedded modes. [2 Marks | K2]
**Answer:**
- **Organic Mode:** $\mathbf{E = 2.4 \cdot (KLOC)^{1.05} \text{ PM}}, \quad \mathbf{D = 2.5 \cdot (E)^{0.38} \text{ Months}}$
- **Embedded Mode:** $\mathbf{E = 3.6 \cdot (KLOC)^{1.20} \text{ PM}}, \quad \mathbf{D = 2.5 \cdot (E)^{0.32} \text{ Months}}$

---

### Q4: In Earned Value Analysis (EVA), define Cost Variance (CV) and Schedule Variance (SV). How are negative values interpreted? [2 Marks | K2]
**Answer:**
- **Cost Variance:** $CV = EV - AC$. $CV < 0 \implies$ **Over Budget (Cost Overrun)**.
- **Schedule Variance:** $SV = EV - PV$. $SV < 0 \implies$ **Behind Schedule (Delayed)**.

---

### Q5: Define Risk Exposure (RE) and state the formula for Risk Reduction Leverage (RRL). [2 Marks | K2]
**Answer:**
- **Risk Exposure:** $\mathbf{RE = P \times C}$ (Probability $\times$ Impact Cost).
- **Risk Reduction Leverage:** $\mathbf{RRL = \frac{RE_{\text{before}} - RE_{\text{after}}}{\text{Cost of Action}}}$. An action is cost-justified if $RRL > 1.0$.

---

## PART – B (3 × 13 or 14 = 40 Marks) — Answer Either (a) OR (b) from each Question

### Q6 (a): White-Box Basis Path Testing & Cyclomatic Complexity [13 Marks | K3 | Unit 4]
**For the following method:**
```java
int findMax(int a, int b, int c) {
    int max = a;
    if (b > max)
        max = b;
    if (c > max)
        max = c;
    return max;
}
```
**(i) Draw the Control Flow Graph (CFG) and determine Cyclomatic Complexity V(G) using three independent methods. [7 Marks]**  
**(ii) Derive the set of linearly independent basis paths and construct a complete test suite with input vectors and expected outputs. [6 Marks]**

#### Solution:
**(i) CFG & 3 Independent $V(G)$ Calculations:**
- **Nodes ($N=6$):** Node 1 (entry, `max=a`), Node 2 (`b>max`), Node 3 (`max=b`), Node 4 (`c>max`), Node 5 (`max=c`), Node 6 (`return max`).
- **Edges ($E=7$):** $1\to 2, \ 2\to 3, \ 2\to 4, \ 3\to 4, \ 4\to 5, \ 4\to 6, \ 5\to 6$.
1. *Edges/Nodes:* $V(G) = E - N + 2P = 7 - 6 + 2(1) = \mathbf{3}$.
2. *Predicate Nodes:* Nodes 2 and 4 are predicates $\implies V(G) = P' + 1 = 2 + 1 = \mathbf{3}$.
3. *Enclosed Regions:* 2 enclosed regions $+ 1$ unbounded outer region $= \mathbf{3}$.

**(ii) Linearly Independent Basis Paths & Test Suite:**
| Path | Node Traversal Sequence | Branch Condition Covered | Test Input $(a, b, c)$ | Expected Output |
| :---: | :--- | :--- | :---: | :---: |
| **Path 1** | $1 \to 2 \to 4 \to 6$ | Both IF conditions False | $(10, 5, 2)$ | $10$ |
| **Path 2** | $1 \to 2 \to 3 \to 4 \to 6$ | First IF True, Second False | $(5, 10, 2)$ | $10$ |
| **Path 3** | $1 \to 2 \to 4 \to 5 \to 6$ | First IF False, Second True | $(5, 2, 10)$ | $10$ |

*Conclusion:* Exactly 3 test cases guarantee 100% statement and branch coverage.

---

### OR

### Q6 (b): Black-Box Testing & Integration Strategies [13 Marks | K3 | Unit 4]
**(i) Explain Black-Box Boundary Value Analysis (BVA) and Equivalence Class Partitioning for an input age range $[18, 60]$. [7 Marks]**  
**(ii) Compare Top-Down and Bottom-Up Integration Testing strategies. Explain the role of Stubs and Drivers. [6 Marks]**

#### Solution:
**(i) BVA & Equivalence Partitioning:**
- **Equivalence Classes:** Valid: $18 \le x \le 60$; Invalid: $x < 18$ and $x > 60$.
- **Boundary Value Analysis (BVA):** Tests at extremes $\{a, a+1, \text{nominal}, b-1, b\} \implies \{18, 19, 35, 59, 60\}$ plus robust invalid values $\{17, 61\}$.

**(ii) Top-Down vs Bottom-Up Integration:**
| Dimension | Top-Down Integration | Bottom-Up Integration |
| :--- | :--- | :--- |
| **Direction** | From root control module down to leaves. | From leaf utility modules up to control root. |
| **Test Harness** | Requires **Test Stubs** to simulate children. | Requires **Test Drivers** to simulate parents. |
| **Advantages** | Early working prototype demonstration. | Early verification of critical utility/data modules. |

---

### Q7 (a): Barry Boehm's COCOMO I Sizing & Estimation [13 Marks | K3 | Unit 5]
**A software project is estimated to be $35 \text{ KLOC}$. Compute Effort, Duration, Staff Size, and Productivity if developed in (i) Organic Mode, and (ii) Embedded Mode under Barry Boehm's Basic COCOMO I model. [13 Marks]**

#### Solution:
$$\mathbf{E = a \cdot (KLOC)^b \quad \text{[PM]}}, \qquad \mathbf{D = c \cdot (E)^d \quad \text{[Months]}}, \qquad \mathbf{P = \frac{E}{D} \quad \text{[Staff]}}$$

**(i) Organic Mode ($a=2.4, b=1.05, c=2.5, d=0.38$):**
- $E = 2.4 \times (35)^{1.05} = 2.4 \times 41.761 = \mathbf{100.23 \text{ Person-Months}}$
- $D = 2.5 \times (100.23)^{0.38} = 2.5 \times 5.764 = \mathbf{14.41 \text{ Months}}$
- Staff Size: $P = \frac{100.23}{14.41} = \mathbf{6.96 \approx 7 \text{ Persons}}$
- Productivity: $\frac{35,000 \text{ LOC}}{100.23 \text{ PM}} = \mathbf{349.2 \text{ LOC/PM}}$

**(ii) Embedded Mode ($a=3.6, b=1.20, c=2.5, d=0.32$):**
- $E = 3.6 \times (35)^{1.20} = 3.6 \times 71.026 = \mathbf{255.69 \text{ Person-Months}}$
- $D = 2.5 \times (255.69)^{0.32} = 2.5 \times 5.922 = \mathbf{14.81 \text{ Months}}$
- Staff Size: $P = \frac{255.69}{14.81} = \mathbf{17.26 \approx 18 \text{ Persons}}$
- Productivity: $\frac{35,000 \text{ LOC}}{255.69 \text{ PM}} = \mathbf{136.9 \text{ LOC/PM}}$

---

### OR

### Q7 (b): Albrecht's Function Point (FP) Model & Sizing [13 Marks | K3 | Unit 5]
**(i) Explain Albrecht's Function Point (FP) Model. Detail the 5 information domain characteristics and 14 technical complexity factors. [7 Marks]**  
**(ii) A system has $UFC = 369$. All 14 complexity factors are rated 3. Compute VAF, FP, and estimated Java size (53 LOC/FP). [6 Marks]**

#### Solution:
**(i) FP Model & Components:**
$$\mathbf{FP = UFC \times VAF = UFC \times \left(0.65 + 0.01 \sum_{i=1}^{14} F_i\right)}$$
- **5 Information Domains:** External Inputs ($EI$), External Outputs ($EO$), External Inquiries ($EQ$), Internal Logical Files ($ILF$), External Interface Files ($EIF$).
- **14 Complexity Factors ($F_i$):** Rated 0 to 5 (Data communication, distributed processing, performance, transaction rate, online entry, end-user efficiency, online update, complex processing, reusability, installation ease, operational ease, multiple sites, facilitate change).

**(ii) Numerical Solution:**
- $\sum_{i=1}^{14} F_i = 14 \times 3 = 42 \implies VAF = 0.65 + 0.01(42) = \mathbf{1.07}$
- $FP = 369 \times 1.07 = \mathbf{394.83 \text{ Function Points}}$
- Estimated Java Size: $394.83 \times 53 = \mathbf{20,926 \text{ LOC} \ (20.93 \text{ KLOC})}$.

---

### Q8 (a): Earned Value Analysis (EVA) Health Audit & Forecasting [14 Marks | K3 | Unit 5]
**A project has $BAC = \$150,000$ and planned duration of 10 months. At Month 5, records reveal:**
- $PV = \$75,000, \quad EV = \$60,000, \quad AC = \$70,000$.  
**Calculate $CV, SV, CPI, SPI, EAC$, and $ETC$. Audit project health and recommend management action. [14 Marks]**

#### Solution:
- **Cost Variance ($CV$):**
  $$CV = EV - AC = 60,000 - 70,000 = \mathbf{-\$10,000} \quad \text{[Over budget by \$10,000]}$$
- **Schedule Variance ($SV$):**
  $$SV = EV - PV = 60,000 - 75,000 = \mathbf{-\$15,000} \quad \text{[Behind schedule by \$15,000]}$$
- **Cost Performance Index ($CPI$):**
  $$CPI = \frac{EV}{AC} = \frac{60,000}{70,000} = \mathbf{0.857} \quad \text{[\$0.86 value delivered per \$1.00 spent]}$$
- **Schedule Performance Index ($SPI$):**
  $$SPI = \frac{EV}{PV} = \frac{60,000}{75,000} = \mathbf{0.800} \quad \text{[Progressing at 80\% of planned velocity]}$$
- **Estimate at Completion ($EAC$):**
  $$EAC = \frac{BAC}{CPI} = \frac{150,000}{0.8571} = \mathbf{\$175,000} \quad \text{[Projected \$25,000 overrun]}$$
- **Estimate to Complete ($ETC$):**
  $$ETC = EAC - AC = 175,000 - 70,000 = \mathbf{\$105,000}$$
- **Audit & Action:** Critical health status. Management must freeze scope creep, reallocate senior engineers to critical path activities, and renegotiate deadlines.

---

### OR

### Q8 (b): The RMMM Plan & CASE Environment Architecture [14 Marks | K3 | Unit 6]
**(i) What is an RMMM Plan? Construct a complete RMMM table for the scenario: "Key Senior Developers Quit during Construction". [7 Marks]**  
**(ii) Illustrate the architecture of an integrated CASE environment, detailing the central role of the Object Management System (OMS) repository. [7 Marks]**

#### Solution:
**(i) RMMM Table for Senior Developer Turnover:**
| RMMM Pillar | Operational Procedures & Action Items |
| :--- | :--- |
| **Mitigation (Avoidance)** | Enforce Pair Programming so knowledge is distributed; mandate detailed documentation; retention bonuses. |
| **Monitoring (Triggers)** | Track overtime hours (> 50 hrs/wk = burnout trigger); conduct monthly 1-on-1s; monitor commit frequency. |
| **Management (Contingency)**| Promote junior pair partner immediately; activate contract on-demand staffing; de-scope non-critical features. |

**(ii) CASE Environment Architecture & OMS:**
```
[ User Interface Layer (GUI / IDE) ]
           |
[ Tool Integration Services: Data, Control, Presentation ]
           |
[ Upper CASE: DFD/UML ]  <--->  [ Lower CASE: Compilers/Tests ]  <--->  [ Management: Jira/Gantt ]
           \                           |                           /
            +--------------------------+--------------------------+
                                       |
          [ OBJECT MANAGEMENT SYSTEM (OMS) CENTRAL REPOSITORY ]
          (Metadata, Version History, RTM Traceability, Shared Schema)
```
- **OMS Role:** Centralized relational database storing all project artifacts (requirements, models, code, tests). Ensures data consistency, prevents tool conflicts, and powers automated bidirectional traceability.
