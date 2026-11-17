# 24ITPC302: CAT-I Model Examination Question Paper & Detailed Solutions
### Sri Sai Ram Engineering College (Autonomous) — Regulations 2024
### Department of Information Technology & Computer Science and Engineering
**Course:** 24ITPC302 – Software Engineering | **Max Marks:** 50 | **Duration:** 1 ½ Hours  
**Coverage:** Units I, II, III (Syllabus Faculty Priority Questions)

---

## PART – A (5 × 2 = 10 Marks) — Answer ALL Questions

### Q1: State the four core values of the Agile Manifesto. [2 Marks | K2]
**Answer:**
1. **Individuals and interactions** over processes and tools.
2. **Working software** over comprehensive documentation.
3. **Customer collaboration** over contract negotiation.
4. **Responding to change** over following a plan.

---

### Q2: Differentiate between Verification and Validation in the V-Model. [2 Marks | K2]
**Answer:**
- **Verification (Left Wing):** Static reviews, inspections, and desk checking *without* code execution to verify process compliance: *"Are we building the product right?"*
- **Validation (Right Wing):** Dynamic execution of compiled software (Unit, Integration, System, Acceptance testing) to evaluate runtime behavior against customer needs: *"Are we building the right product?"*

---

### Q3: List four essential quality characteristics of a good Software Requirements Specification (SRS) under IEEE 830. [2 Marks | K2]
**Answer:**
1. **Unambiguous:** Exactly one interpretation exists for every requirement statement.
2. **Complete:** Encompasses all functional, performance, security, and interface constraints.
3. **Consistent:** Contains no conflicting or contradictory specifications.
4. **Verifiable:** Can be proved through an objective, cost-effective testing procedure.

---

### Q4: Define a Petri Net formally and state the transition firing rule. [2 Marks | K2]
**Answer:**
A Petri Net is a 5-tuple:
$$\mathbf{PN = (P, T, F, W, M_0)}$$
where $P$ is Places, $T$ is Transitions, $F$ is Directed Flow Arcs, $W$ is Arc Weights, and $M_0$ is Initial Marking.  
**Firing Rule:** Transition $t$ is enabled iff $\forall p \in I(t), M(p) \ge W(p, t)$. Upon firing, it consumes $W(p, t)$ tokens from each input place and deposits $W(t, p')$ tokens into each output place.

---

### Q5: Distinguish between Cohesion and Coupling. State the most desirable level for each. [2 Marks | K2]
**Answer:**
- **Cohesion:** Degree of functional strength of elements within a module. *Desirable:* **Functional Cohesion (Highest)**.
- **Coupling:** Degree of interdependence between software modules. *Desirable:* **Data Coupling / Uncoupled (Lowest)**.  
*Golden Law:* **Maximize Cohesion, Minimize Coupling!**

---

## PART – B (3 × 13 or 14 = 40 Marks) — Answer Either (a) OR (b) from each Question

### Q6 (a): Boehm's Spiral Model & Waterfall Model Comparison [13 Marks | K3 | Unit 1]
**(i) Explain Barry Boehm's Spiral Model of software development with a neat diagram. Describe activities in each of the four quadrants and explain why it is referred to as "risk-driven". [8 Marks]**  
**(ii) Compare and contrast the Waterfall Model with the Spiral Model across 5 project parameters. [5 Marks]**

#### Solution:
**(i) Spiral Model 4 Quadrants:**
```
             QUADRANT II (Risk Assessment)     |    QUADRANT I (Objectives & Constraints)
  - Perform thorough risk analysis            |  - Identify iteration objectives
  - Build simulations, prototypes, benchmarks  |  - Establish alternative design approaches
  ---------------------------------------------+---------------------------------------------
            QUADRANT III (Development)         |    QUADRANT IV (Planning & Review)
  - Code and verify software artifacts         |  - Client evaluates deliverables
  - Unit, integration, and system tests       |  - Plan next phase / spiral turn
```
- **Why Risk-Driven:** At each turn of the spiral, the amount of effort spent is governed by the risk associated with that step. Insurmountable risks uncovered in Quadrant II trigger immediate project termination, preventing financial disaster.

**(ii) Waterfall vs Spiral Comparison Matrix:**
| Parameter | Classical Waterfall | Boehm's Spiral Model |
| :--- | :--- | :--- |
| **Lifecycle Paradigm** | Linear sequential, rigid forward stages. | Evolutionary, iterative spiral cycles. |
| **Risk Management** | Implicit; no formal risk assessment phase. | Explicit, mandatory risk analysis in Quadrant II. |
| **Requirement Changes** | Inflexible; demands frozen specs upfront. | Highly adaptive; accommodates evolving user needs. |
| **Working Software** | Delivered late (Construction phase). | Early operational prototypes in early spirals. |
| **Best Suited For** | Stable, well-understood systems (compilers). | High-risk, mission-critical enterprise systems. |

---

### OR

### Q6 (b): Extreme Programming (XP) Values, Lifecycle & Core Practices [13 Marks | K3 | Unit 1]
**(i) What is Extreme Programming (XP)? Describe the 4 core values and illustrate the XP development lifecycle. [7 Marks]**  
**(ii) Detail the mechanisms, working principles, and engineering advantages of: (1) Pair Programming, and (2) Test-Driven Development (TDD). [6 Marks]**

#### Solution:
**(i) XP Values & Lifecycle:**
- **4 Values:** *Communication, Simplicity, Feedback, Courage*.
- **Lifecycle:** User Stories (index cards) $\to$ Release Planning $\to$ Spike Solutions $\to$ Iteration Planning $\to$ TDD Unit Test $\to$ Pair Programming $\to$ Continuous Integration $\to$ Customer Acceptance Test $\to$ Production Release.

**(ii) Core Practices:**
- **Pair Programming:** Two engineers, one screen. The **Driver** implements code tactical logic; the **Navigator** reviews code in real time, catching corner cases and evaluating architecture. Roles switch regularly. *Benefits:* 15–20% defect reduction, collective code ownership, zero single points of failure.
- **Test-Driven Development (TDD):** Automated unit tests are written *before* production code (**Red-Green-Refactor** cycle). Guarantees 100% test coverage, modularity, and fearless refactoring.

---

### Q7 (a): IEEE 830 SRS Standard Structure & Requirements Engineering Process [13 Marks | K3 | Unit 2]
**(i) Outline the standard IEEE 830-1998 format for an SRS document. Detail Section 3 (Specific Requirements). [7 Marks]**  
**(ii) Describe the four phases of the Requirements Engineering Process and explain how the Requirements Traceability Matrix (RTM) is constructed. [6 Marks]**

#### Solution:
**(i) IEEE 830 Standard Outline:**
```
1. INTRODUCTION (1.1 Purpose, 1.2 Scope, 1.3 Definitions, 1.4 References, 1.5 Overview)
2. OVERALL DESCRIPTION (2.1 Perspective, 2.2 Functions, 2.3 User Classes, 2.4 Constraints, 2.5 Assumptions)
3. SPECIFIC REQUIREMENTS (Core Technical Section):
   3.1 External Interface Requirements: User UI, Hardware, Software OS/DB, Communications TLS/HTTP
   3.2 Functional Requirements: Inputs, Transformations, Logic, Outputs for each service
   3.3 Performance Requirements: Latency < 200ms, Throughput 5000 TPS, Concurrency
   3.4 Design Constraints: Tech stack constraints, coding standards, memory caps
   3.5 Software System Attributes: Reliability, Availability (99.99%), Security, Portability
```
**(ii) RE Process & RTM:**
- **Phases:** 1. Feasibility Study (Technical, Economic CBA, Operational); 2. Requirements Elicitation & Analysis (Interviews, JAD, Use cases); 3. Specification (IEEE 830 SRS); 4. Validation (Inspections, reviews, test generation).
- **RTM:** A matrix linking each Requirement ID $\to$ Design Module $\to$ Source Code File $\to$ Test Case ID. Ensures 100% test coverage, prevents scope creep, and enables instant impact analysis.

---

### OR

### Q7 (b): Petri Nets Concurrency Modeling & Producer-Consumer Problem [13 Marks | K3 | Unit 2]
**(i) Define a Petri Net formally as a 5-tuple. Explain the transition firing rule and how concurrency and mutual exclusion are modeled. [7 Marks]**  
**(ii) Construct a Petri Net for a Producer-Consumer system with a bounded buffer of size 1. Trace markings across two transitions. [6 Marks]**

#### Solution:
**(i) 5-Tuple & Concurrency Modeling:**
$$\mathbf{PN = (P, T, F, W, M_0)}$$
- $P$: Places (circles); $T$: Transitions (bars); $F$: Flow arcs; $W$: Arc weights; $M_0$: Initial marking.
- Enabling: $\forall p \in I(t), M(p) \ge W(p, t)$. Firing consumes tokens from inputs, deposits in outputs.

**(ii) Producer-Consumer Model:**
- Places: $P_1$ (Producer Ready), $P_2$ (Buffer Empty), $P_3$ (Buffer Full), $P_4$ (Consumer Ready).
- Initial Marking: $M_0 = [P_1: 1, \ P_2: 1, \ P_3: 0, \ P_4: 1]$.
- **Step 1 ($T_1$ fires - Produce & Deposit):** Consumes from $P_1, P_2$; deposits into $P_1, P_3 \implies M_1 = [1, 0, 1, 1]$.
- **Step 2 ($T_2$ fires - Fetch & Consume):** Consumes from $P_3, P_4$; deposits into $P_4, P_2 \implies M_2 = [1, 1, 0, 1] = M_0$.
- *Conclusion:* Mutual exclusion holds; buffer overflow and underflow are mathematically prevented.

---

### Q8 (a): Pressman's 4-Level Software Design Pyramid & Heuristics [14 Marks | K3 | Unit 3]
**(i) Illustrate Pressman's 4-Level Software Design Pyramid and explain how each level transforms analysis models into design artifacts. [8 Marks]**  
**(ii) Differentiate High-Level Design (HLD) and Low-Level Design (LLD). Explain the Fan-In vs Fan-Out heuristics. [6 Marks]**

#### Solution:
**(i) The 4-Level Design Pyramid:**
```
             / \
            / [4] \   COMPONENT-LEVEL DESIGN (Algorithms, PDL, Decision Tables)
           /-------\
          /   [3]   \ INTERFACE DESIGN (User GUI, Internal/External APIs)
         /-----------\
        /     [2]     \ ARCHITECTURAL DESIGN (Subsystems, Connectors, Arch Styles)
       /---------------\
      /       [1]       \ DATA / CLASS DESIGN (ER Schemas, Data Structures)
```
1. **Data/Class Design (Base):** Transforms analysis classes into DB schemas and data structures.
2. **Architectural Design:** Establishes system skeleton, subsystem relations, and architectural styles.
3. **Interface Design:** Defines interaction flow between components, external systems, and human users.
4. **Component-Level Design (Apex):** Converts structural elements into detailed procedural algorithms and pseudocode.

**(ii) HLD vs LLD & Design Heuristics:**
- **HLD:** Macroscopic architecture, subsystem boundaries, DB schema. Audience: Architects, clients.
- **LLD:** Microscopic method logic, flowcharts, pseudocode. Audience: Developers, testers.
- **Fan-Out:** Number of directly called submodules ($3 \le \text{Fan-Out} \le 7$). High fan-out indicates control overload.
- **Fan-In:** Number of parent modules calling a submodule. **Maximize Fan-In** for high reusability.

---

### OR

### Q8 (b): Architectural Styles & Pressman's 12 Design Concepts [14 Marks | K3 | Unit 3]
**(i) Explain four major Software Architectural Styles: Data-Centered, Data-Flow (Pipe-and-Filter), Layered, and Event-Driven. [8 Marks]**  
**(ii) State and explain any six fundamental software design concepts formulated by Pressman, highlighting Cohesion and Coupling hierarchies. [6 Marks]**

#### Solution:
**(i) Four Architectural Styles:**
- **Data-Centered (Repository):** Central data store accessed by independent clients. High modularity, but central store is a bottleneck.
- **Data-Flow (Pipe-and-Filter):** Unidirectional data streams (Pipes) transformed by filters. Highly parallelizable, but poor for interactive UI.
- **Layered (Call-and-Return):** Hierarchical tiers (UI $\to$ Business Logic $\to$ Data Access $\to$ Database). Loose coupling; multi-layer overhead.
- **Event-Driven (Pub-Sub):** Producers emit events to an Event Broker; subscribers react asynchronously. Highly scalable; hard to trace.

**(ii) Design Concepts & Cohesion/Coupling:**
- **Concepts:** Abstraction, Modularity, Information Hiding (Parnas), Refinement (Wirth), Refactoring, Functional Independence.
- **Cohesion Hierarchy (Worst $\to$ Best):** *Coincidental $\to$ Logical $\to$ Temporal $\to$ Procedural $\to$ Communicational $\to$ Sequential $\to$* **Functional (Best)**.
- **Coupling Hierarchy (Worst $\to$ Best):** *Content (Worst) $\to$ Common $\to$ Control $\to$ Stamp $\to$* **Data (Best)** $\to$ *Uncoupled*.
