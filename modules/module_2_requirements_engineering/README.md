# Module II: Requirements Analysis and Specification

**Course Code:** 24ITPC302 | **Lecture Periods:** 8  
**Core Reference:** Roger S. Pressman (Ch 5–7), Ian Sommerville (Ch 4), Rajib Mall (Ch 3)

---

## 🎯 Executive Summary & Learning Outcomes
This module details the complete Requirements Engineering (RE) lifecycle, contrasting Functional and Non-Functional requirements, defining the structure of the IEEE 830 Software Requirements Specification (SRS), and modeling system dynamics via Structured System Analysis (DFDs), Petri Nets, and Data Dictionaries.

---

## 📖 Key Syllabus Topics & Deep-Dive Concepts

### 1. Functional vs Non-Functional Requirements
- **Functional Requirements:** Describe the behavioral services and business calculations the system must perform (e.g., "The system shall authenticate the user using biometric verification", "Calculate monthly interest on loan balance").
- **Non-Functional Requirements (NFRs / Quality Attributes):** Constraints placed on the services or functions:
  - *Performance:* Response time ($< 2$ seconds), throughput (10,000 requests/sec).
  - *Security:* 256-bit AES encryption at rest and in transit, Role-Based Access Control (RBAC).
  - *Reliability & Availability:* 99.999% uptime, Mean Time Between Failures ($MTBF$).
  - *Usability:* Maximum 3 clicks to complete checkout.
  - *Portability:* Runs seamlessly across Linux, Windows, macOS, Android, and iOS.
  - *Standard Model:* **FURPS+** (Functionality, Usability, Reliability, Performance, Supportability).

### 2. Software Requirements Document (SRS) — IEEE 830 Standard Structure
An SRS is the official contractual document between client and development team.

```
1. Introduction
   1.1 Purpose
   1.2 Scope of the Software
   1.3 Definitions, Acronyms, and Abbreviations
   1.4 References
   1.5 Overview
2. Overall Description
   2.1 Product Perspective (System interfaces, user interfaces, hardware interfaces)
   2.2 Product Functions (High-level summary)
   2.3 User Characteristics
   2.4 General Constraints (Regulatory, memory, security)
   2.5 Assumptions and Dependencies
3. Specific Requirements (Detailed Functional & Non-Functional Specifications)
   3.1 External Interface Requirements
   3.2 Functional Requirements (Detailed use cases and input-process-output specs)
   3.3 Performance Requirements
   3.4 Design Constraints
   3.5 Software System Attributes (Reliability, Availability, Security, Maintainability)
```

**Characteristics of an Ideal SRS:**
1. *Unambiguous:* Every stated requirement has only one possible interpretation.
2. *Complete:* Encompasses all significant requirements (inputs, outputs, error handling).
3. *Consistent:* No conflicting requirements (e.g., speed vs memory constraints).
4. *Verifiable / Testable:* Can design an objective cost-effective test to confirm compliance.
5. *Modifiable:* Redundancy-free structure allowing easy change propagation.
6. *Traceable:* Forward and backward traceability via Requirement Traceability Matrix (RTM).

### 3. Requirements Engineering Process
1. **Feasibility Studies:**
   - *Technical Feasibility:* Do we possess the technology, hardware, and engineering skills?
   - *Economic Feasibility:* Cost-Benefit Analysis ($CBA$), Return on Investment ($ROI$).
   - *Operational Feasibility:* Will end-users adapt and operate the system efficiently?
   - *Schedule & Legal Feasibility:* Compliant with delivery deadlines, copyright, GDPR?
2. **Requirements Elicitation & Analysis:**
   - Techniques: Stakeholder interviews, surveys/questionnaires, Joint Application Development (JAD), brainstorm sessions, on-site observation, Use Cases, User Stories.
3. **Requirements Validation:**
   - Formal inspections/reviews, Prototyping, Automated consistency checking.
4. **Requirements Management:**
   - Change control board (CCB), version control of SRS, Requirement Traceability Matrix (RTM) linking Business Needs $\to$ SRS ID $\to$ Design Module $\to$ Test Case ID.

### 4. Classical Analysis & Modeling

#### A. Structured System Analysis & Data Flow Diagrams (DFD)
- Symbols: Process (Circle / Rounded rectangle), Data Store (Open rectangle / Parallel bars), External Entity / Source / Sink (Square / Rectangle), Data Flow (Directed arrow).
- **Levels of DFD:**
  - *Level 0 (Context Diagram):* Entire system treated as a single central process interacting with external entities.
  - *Level 1 DFD:* Decomposes the central process into 4–7 primary functional sub-processes with internal data stores.
  - *Level 2 DFD:* Explodes complex Level 1 sub-processes into fine-grained tasks.
- *Balancing Rule:* The inputs and outputs flowing into/out of a parent process at Level $N$ must exactly equal the aggregate inputs and outputs at Level $N+1$.

#### B. Petri Nets (Concurrent & Real-Time System Modeling)
A bipartite directed graph consisting of:
- **Places ($P$):** Represent system states or conditions (drawn as circles).
- **Transitions ($T$):** Represent events or actions (drawn as bars or boxes).
- **Arcs ($A$):** Directed arrows connecting Places to Transitions ($P \to T$) or Transitions to Places ($T \to P$). Arcs *never* connect Place to Place or Transition to Transition directly.
- **Tokens ($\bullet$):** Black dots placed inside Places representing resource availability.
- **Marking ($M$):** Vector distribution of tokens across places: $M = (m_1, m_2, \dots, m_n)$.
- **Firing Rule:** A transition is *enabled* if each of its input places contains at least one token. When fired, it consumes one token from each input place and deposits one token into each output place.

#### C. Data Dictionary
A centralized metadata repository defining the composition of all data flows, data structures, and data stores:
- `=` (is composed of)
- `+` (and / sequence)
- `[ | ]` (selection / either-or)
- `{ }` (iteration / repetition 0 or more times)
- `( )` (optional component)

---

## 🎯 Model University Questions & Combos
- **Combo 2.1 (13M):** Outline the IEEE 830 standard structure for an SRS. Discuss the 5 essential quality attributes of a good requirements document.
- **Combo 2.2 (13M):** Explain the 4 steps of the Requirements Engineering process. Construct a Level 0 Context Diagram and Level 1 DFD for an Online Banking System.
- **Combo 2.3 (13M):** Define Petri Nets. State the firing rules with an example of mutual exclusion in a shared resource environment.
