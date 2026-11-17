# 24ITPC302: Software Engineering Formula & Metrics Bank

This compendium contains all governing mathematical formulas, quantitative metrics, and calculation models for **24ITPC302 – Software Engineering**.

---

## 1. Module IV: Testing & Basis Path Metrics

### Cyclomatic Complexity ($V(G)$)
For any program control flow graph $G = (V, E)$:

1. **Method 1 (Edges and Nodes):**
   $$\mathbf{V(G) = E - N + 2P}$$
   where $E$ = number of flow graph edges, $N$ = number of nodes, and $P$ = number of connected components ($P = 1$ for a single program/routine $\implies V(G) = E - N + 2$).

2. **Method 2 (Predicate / Decision Nodes):**
   $$\mathbf{V(G) = P' + 1}$$
   where $P'$ is the number of predicate nodes (nodes with out-degree $\ge 2$, e.g. `if`, `while`, `for`).  
   *(For compound conditions like `if (A && B)`, expand into two separate predicate nodes or count each simple Boolean condition).*

3. **Method 3 (Enclosed Planar Regions):**
   $$\mathbf{V(G) = R}$$
   where $R$ is the total number of bounded planar regions plus the one unbounded exterior region.

*Properties:* $V(G)$ defines the exact maximum number of **linearly independent basis paths** required to achieve 100% statement and branch coverage.

---

## 2. Module V: Sizing & Function Point (FP) Metrics

### Albrecht's Function Point Model
$$FP = UFC \times VAF$$

#### Step 1: Unadjusted Function Count ($UFC$)
$$UFC = \sum_{i=1}^5 \sum_{j=1}^3 \left(\text{Count}_{i, j} \times w_{i, j}\right)$$

| Information Domain Element | Simple Weight | Average Weight | Complex Weight |
| :--- | :---: | :---: | :---: |
| **External Inputs ($EI$)** | 3 | 4 | 6 |
| **External Outputs ($EO$)** | 4 | 5 | 7 |
| **External Inquiries ($EQ$)** | 3 | 4 | 6 |
| **Internal Logical Files ($ILF$)** | 7 | 10 | 15 |
| **External Interface Files ($EIF$)** | 5 | 7 | 10 |

#### Step 2: Value Adjustment Factor ($VAF$)
Based on 14 General System Characteristics ($F_1$ to $F_{14}$), each rated from $0$ (no influence) to $5$ (essential):
$$\mathbf{VAF = 0.65 + 0.01 \sum_{i=1}^{14} F_i}$$
*(Permissible range: $0.65 \le VAF \le 1.35$. If all $F_i = 3 \implies \sum F_i = 42 \implies VAF = 1.07$).*

#### Step 3: Final Function Points ($FP$)
$$\mathbf{FP = UFC \times \left(0.65 + 0.01 \sum_{i=1}^{14} F_i\right)}$$

#### Step 4: Sizing in Lines of Code (LOC)
$$\mathbf{\text{LOC} = FP \times \text{Average Language Expansion Factor}}$$
*(Standard averages: C = 128, C++ = 53, Java = 53, C# = 54, Python = 25, SQL = 13).*

---

## 3. Module V: COCOMO (Constructive Cost Model)

### Basic COCOMO I (Boehm)
Equations for Effort ($E$ in Person-Months), Development Time ($D$ in Months), and Staff Size ($P$ in Persons):
$$E = a \cdot (KLOC)^b$$
$$D = c \cdot (E)^d$$
$$P = \frac{E}{D}$$

| Development Mode | Project Characteristics | $a$ | $b$ | $c$ | $d$ |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Organic** | Small, familiar domain, in-house team ($< 50$ KLOC) | **2.4** | **1.05** | **2.5** | **0.38** |
| **Semidetached** | Medium size, mixed experience ($50 - 300$ KLOC) | **3.0** | **1.12** | **2.5** | **0.35** |
| **Embedded** | Tight hardware/regulatory constraints, real-time | **3.6** | **1.20** | **2.5** | **0.32** |

### Intermediate COCOMO I
Incorporates Effort Adjustment Factor ($EAF$) derived from 15 Cost Drivers ($CD_1$ to $CD_{15}$ across Product, Hardware, Personnel, and Project attributes):
$$\mathbf{E = a \cdot (KLOC)^b \times EAF}, \qquad \text{where } \mathbf{EAF = \prod_{i=1}^{15} CD_i}$$

---

## 4. Module V: Halstead's Software Science Metrics

Given a program with:
- $\eta_1$ = number of distinct operators, $\eta_2$ = number of distinct operands
- $N_1$ = total number of operator occurrences, $N_2$ = total number of operand occurrences

1. **Program Vocabulary:** $\eta = \eta_1 + \eta_2$
2. **Program Length:** $N = N_1 + N_2$
3. **Estimated Program Length ($\hat{N}$):** $\hat{N} = \eta_1 \log_2 \eta_1 + \eta_2 \log_2 \eta_2$
4. **Program Volume ($V$ in bits):** $V = N \log_2 \eta$
5. **Program Difficulty ($D$):** $D = \left(\frac{\eta_1}{2}\right) \times \left(\frac{N_2}{\eta_2}\right)$
6. **Mental Effort ($E$ in elementary mental discriminations):** $E = D \times V$
7. **Estimated Time ($T$ in seconds):** $T = \frac{E}{18}$ (Stroud number $S = 18$).

---

## 5. Module V: Earned Value Analysis (EVA)

Let:
- $BAC$ = Budget at Completion (Total planned project budget)
- $PV$ = Planned Value (Budgeted Cost of Work Scheduled - $BCWS$)
- $EV$ = Earned Value (Budgeted Cost of Work Performed - $BCWP$)
- $AC$ = Actual Cost (Actual Cost of Work Performed - $ACWP$)

| Metric | Formula | Interpretation |
| :--- | :--- | :--- |
| **Cost Variance ($CV$)** | $\mathbf{CV = EV - AC}$ | $CV > 0 \implies$ Under Budget (Good)<br>$CV < 0 \implies$ Over Budget (Bad) |
| **Schedule Variance ($SV$)** | $\mathbf{SV = EV - PV}$ | $SV > 0 \implies$ Ahead of Schedule (Good)<br>$SV < 0 \implies$ Behind Schedule (Bad) |
| **Cost Performance Index ($CPI$)** | $\mathbf{CPI = \frac{EV}{AC}}$ | $CPI > 1.0 \implies$ Cost Efficient<br>$CPI < 1.0 \implies$ Cost Inefficient |
| **Schedule Performance Index ($SPI$)** | $\mathbf{SPI = \frac{EV}{PV}}$ | $SPI > 1.0 \implies$ Fast Progress<br>$SPI < 1.0 \implies$ Slow Progress |
| **Estimate at Completion ($EAC$)** | $\mathbf{EAC = \frac{BAC}{CPI}}$ | Projected final cost based on current performance |
| **Estimate to Complete ($ETC$)** | $ETC = EAC - AC$ | Additional funds required to finish project |

---

## 6. Module VI: Software Risk Metrics

### Risk Exposure ($RE$)
Also termed Risk Impact or Risk Severity:
$$\mathbf{RE = P \times C}$$
where $P$ is the estimated probability of risk occurrence ($0.0 \le P \le 1.0$), and $C$ is the cost / impact to the project if the risk occurs (in monetary units or schedule delay).

### Risk Reduction Leverage ($RRL$)
Used to evaluate whether a proposed mitigation action is cost-effective:
$$\mathbf{RRL = \frac{RE_{\text{before}} - RE_{\text{after}}}{\text{Cost of Mitigation Action}}}$$
*Rule:* If $RRL > 1.0$, the mitigation action is financially justified.
