# 24ITPC302: Software Engineering — Official Syllabus & Curriculum Breakdown

**Institution:** Sri Sai Ram Engineering College (Autonomous), West Tambaram, Chennai – 600 044  
**Affiliated to:** Anna University, Chennai  
**Regulation:** 2024 Autonomous Regulations  
**Department:** Information Technology / Computer Science and Engineering  
**Programme:** B.Tech Information Technology / B.E. Computer Science and Engineering  
**Semester:** Semester III  
**Course Code:** 24ITPC302  
**Course Title:** SOFTWARE ENGINEERING  
**NPTEL Course Code:** 106105182 (Prof. Rajib Mall, IIT Kharagpur)  
**SDG Goals:** SDG No. 4 (Quality Education) & SDG No. 9 (Industry, Innovation, and Infrastructure)  
**Credits:** L: 3 | T: 0 | P: 0 | C: 3 (Total Periods: 45)  
**Official PDF:** [SYLLABUS - 24ITPC302.pdf](file:///C:/Users/siva2/OneDrive/Desktop/soft/syllabus/SYLLABUS%20-%2024ITPC302.pdf)

---

## 🎯 Course Educational Objectives

1. To address real-time complex engineering problems using innovative approaches with strong core computing skills.
2. To apply core-analytical knowledge and appropriate techniques to provide solutions to real-time challenges of national and global society.
3. Apply ethical knowledge for professional excellence & leadership for the betterment of society.
4. Use software design principles and tools to create modular, maintainable, and scalable software architectures.
5. Develop life-long learning skills needed for better employment and entrepreneurship.

---

## 📚 Detailed 6-Module Syllabus Structure

### MODULE I: SOFTWARE PROCESS AND AGILE DEVELOPMENT (7 Periods)
- **Introduction to Software Engineering:** The Nature of Software, Software Crisis, Software Myths, Engineering Discipline vs Ad-hoc Programming.
- **Software Process Models (Prescriptive Models):**
  - Linear Sequential / Classic Waterfall Model (Strengths, Weaknesses, Applications)
  - V-Model (Verification and Validation Model, Dual-pathway mapping)
  - Incremental Model (Iterative Staged Delivery)
  - RAD Model (Rapid Application Development, 60–90 day delivery cycle)
  - Iterative Model (Successive refinement)
  - Spiral Model (Boehm's 4-Quadrant Risk-Driven Evolutionary Lifecycle)
  - Prototyping Model (Throwaway vs Evolutionary)
- **Specialized Process Models:** Component-Based Development, Formal Methods Model, Aspect-Oriented Software Development.
- **Introduction to Agility:** The Agile Manifesto, 4 Core Values, 12 Agile Principles, Agile Process Framework.
- **Extreme Programming (XP):** XP Values, XP Process Lifecycle (Planning, Design, Coding, Testing), Pair Programming, Test-Driven Development (TDD), Refactoring, Continuous Integration.

---

### MODULE II: REQUIREMENTS ANALYSIS AND SPECIFICATION (8 Periods)
- **Software Requirements:**
  - Functional Requirements (Services, Calculations, Data Handling, Business Rules)
  - Non-Functional Requirements (Performance, Security, Reliability, Usability, Portability, FURPS+ Model)
  - User Requirements vs System Requirements
- **Software Requirements Document (SRS):** IEEE 830-1998 Standard Structure, Characteristics of Good SRS (Unambiguous, Complete, Consistent, Verifiable, Modifiable, Traceable).
- **Requirement Engineering Process:**
  1. Feasibility Studies (Technical, Operational, Economic/Financial, Legal/Schedule)
  2. Requirements Elicitation and Analysis (Interviews, Surveys, JAD, Scenarios, Use Cases)
  3. Requirements Validation (Reviews, Inspections, Prototyping, Model Validation)
  4. Requirements Management (Traceability Matrix, Change Control, Baseline Management)
- **Classical Analysis & Modeling:**
  - Structured System Analysis (Data Flow Diagrams - DFD Level 0/1/2, Process Specifications)
  - Petri Nets (Places, Transitions, Tokens, Marking, Firing Rules for Concurrent/Asynchronous Systems)
  - Data Dictionary (Meta-data repository, EBNF notation for data elements)

---

### MODULE III: SOFTWARE DESIGN (8 Periods)
- **Design Process & Concepts:**
  - Abstraction (Data, Procedural, Control)
  - Modularity (Functional decomposition)
  - Information Hiding (Parnas Principle)
  - Functional Independence: **Cohesion** (Coincidental, Logical, Temporal, Procedural, Communicational, Sequential, Functional) & **Coupling** (Content, Common, Control, Stamp, Data, Uncoupled)
  - Refinement, Refactoring, Design Classes
- **Design Model & Design Heuristics:** Analysis-to-Design Mapping, Fan-In vs Fan-Out heuristics, Scope of Effect vs Scope of Control.
- **Architectural Design & Styles:**
  - Data-Centered Architecture (Repository, Blackboard)
  - Data-Flow Architecture (Pipe-and-Filter, Batch Sequential)
  - Call-and-Return Architecture (Main program and Subroutine, Remote Procedure Call, Layered Systems)
  - Object-Oriented Architecture
  - Event-Driven / Publish-Subscribe Architecture
- **Architectural Mapping using Data Flow:** Transform Mapping vs Transaction Mapping (Deriving Structure Charts from DFDs).
- **User Interface Design:**
  - Golden Rules (Place user in control, Reduce user memory load, Make interface consistent)
  - Interface Analysis (User analysis, Task analysis, Work environment analysis)
  - Interface Design Steps, Navigation Design, Usability Evaluation.
- **Component-Level Design:** Designing Class-Based Components (OCP, LSP, DIP, ISP), Traditional Component Design (Structured Programming constructs, PDL, Flowcharts, Decision Tables).

---

### MODULE IV: TESTING AND MAINTENANCE (8 Periods)
- **Software Testing Fundamentals:** Verification vs Validation, Error, Fault, Bug, Failure lifecycle, Internal and External Views of Testing.
- **White-Box Testing (Structural Testing):**
  - **Basis Path Testing:** Control Flow Graph (CFG), Cyclomatic Complexity $V(G) = E - N + 2P$, Independent Basis Paths, Graph Matrices.
  - **Control Structure Testing:** Condition Testing, Data Flow Testing, Loop Testing (Simple, Nested, Concatenated, Unstructured loops).
- **Black-Box Testing (Functional Testing):**
  - Equivalence Class Partitioning (Valid vs Invalid equivalence classes)
  - Boundary Value Analysis (BVA: min, min+, nom, max-, max, robust testing)
  - Cause-Effect Graphing & Decision Table Testing
  - Orthogonal Array Testing
- **Levels of Testing & Strategies:**
  - Unit Testing (Drivers and Stubs)
  - Integration Testing (Non-incremental / Big-Bang vs Incremental: Top-Down with Stubs, Bottom-Up with Drivers, Sandwich / Hybrid Testing)
  - Validation Testing (Alpha Testing at developer's site, Beta Testing at end-user site, Acceptance Testing)
  - System Testing (Recovery, Security, Stress, Performance Testing)
  - Regression Testing & Debugging Strategies (Brute force, Backtracking, Cause elimination)
- **Software Implementation Techniques:** Clean Code Practices, Code Smell Detection, Refactoring Patterns.
- **Maintenance and Reengineering:**
  - Software Maintenance Types (Corrective, Adaptive, Perfective, Preventive)
  - Business Process Reengineering (BPR) Model
  - Software Reengineering Process Model (Inventory analysis, Document restructuring, Reverse engineering, Code restructuring, Data restructuring, Forward engineering)
  - Reverse Engineering vs Forward Engineering

---

### MODULE V: PROJECT MANAGEMENT (7 Periods)
- **Software Project Management & The 4 P's:** People, Product, Process, Project.
- **Software Sizing & Effort Estimation:**
  - Lines of Code (LOC) Metrics: Advantages, Disadvantages, Productivity calculation.
  - **Function Point (FP) Metric (Albrecht Model):**
    - 5 Information Domain Characteristics: External Inputs ($EI$), External Outputs ($EO$), External Inquiries ($EQ$), Internal Logical Files ($ILF$), External Interface Files ($EIF$).
    - Unadjusted Function Count ($UFC = \sum w_i \times \text{Count}_i$).
    - Value Adjustment Factor ($VAF = 0.65 + 0.01 \sum_{i=1}^{14} F_i$, 14 General System Characteristics).
    - Function Point: $\mathbf{FP = UFC \times VAF}$.
  - Make / Buy Decision (Decision Tree Analysis, Cost-Benefit Comparison).
  - Uncertainties in Effort Estimation, Building Estimation Models, Bottom-Up Estimation.
- **COCOMO Models (Constructive Cost Model by Barry Boehm):**
  - **COCOMO I (Basic):** 3 Development Modes:
    - *Organic Mode:* Small teams, familiar domain ($E = 2.4(KLOC)^{1.05}$, $D = 2.5(E)^{0.38}$)
    - *Semidetached Mode:* Medium teams, mixed experience ($E = 3.0(KLOC)^{1.12}$, $D = 2.5(E)^{0.35}$)
    - *Embedded Mode:* Tight hardware/software constraints ($E = 3.6(KLOC)^{1.20}$, $D = 2.5(E)^{0.32}$)
  - **Intermediate COCOMO:** Effort Adjustment Factor ($EAF = \prod Cost Drivers$).
  - **COCOMO II:** Application Composition, Early Design, and Post-Architecture Models (Scale factors, Sizing by Unadjusted Function Points).
- **Project Scheduling & Timeline Planning:**
  - Work Breakdown Structure (WBS), Gantt Charts, Milestone Charts.
  - PERT / CPM Network Analysis, Float / Slack calculation, Critical Path Identification.
- **Earned Value Analysis (EVA):**
  - Planned Value ($PV$ / $BCWS$), Earned Value ($EV$ / $BCWP$), Actual Cost ($AC$ / $ACWP$).
  - Cost Variance: $CV = EV - AC$; Schedule Variance: $SV = EV - PV$.
  - Cost Performance Index: $CPI = \frac{EV}{AC}$; Schedule Performance Index: $SPI = \frac{EV}{PV}$.
- **Project Planning Process & RFP:** Project Plan Structure, Request for Proposal (RFP) Lifecycle.

---

### MODULE VI: RISK MANAGEMENT & CASE TOOLS (7 Periods)
- **Software Risk Management:**
  - Reactive vs Proactive Risk Strategies.
  - Software Risk Types: Project Risks, Technical Risks, Business Risks, Known vs Predictable vs Unpredictable Risks.
  - **Risk Identification:** Risk Item Checklist, Product size, Business impact, Customer characteristics, Process definition, Development environment, Technology to be built, Staff size and experience.
  - **Risk Projection / Assessment:** Developing a Risk Table, Probability assessment ($P$), Impact assessment ($C$), **Risk Exposure ($RE$):** $\mathbf{RE = P \times C}$.
  - **RMMM Plan:**
    1. *Risk Mitigation:* Proactive avoidance strategies.
    2. *Risk Monitoring:* Tracking risk indicators and triggers.
    3. *Risk Management:* Contingency plans and emergency recovery.
- **Computer-Aided Software Engineering (CASE) TOOLS:**
  - Definition, Scope, and Evolution of CASE Tools.
  - Tangible and Intangible Benefits of CASE Tools across the Software Life Cycle.
  - CASE Environment Architecture: User Interface, Tool Integration Services, Object Management System (OMS) / Central Repository.
  - **Classification / Types of CASE Tools:**
    - Upper CASE Tools (Analysis, Planning, Design, DFD/ER modeling, Requirements tracing)
    - Lower CASE Tools (Code generators, Compilers, Debuggers, Static code analyzers, Test automation)
    - Integrated CASE (I-CASE) Tools (Full lifecycle environments, configuration management, project management)

---

## 📖 Recommended Textbooks & Reference Literature

### Primary Textbooks:
1. **Roger S. Pressman**, *Software Engineering: A Practitioner's Approach*, 6th / 7th / 8th Edition, McGraw Hill International Edition.
2. **Ian Sommerville**, *Software Engineering*, 7th / 8th / 9th Edition, Pearson Education.
3. **Gene Kim, Jez Humble, Patrick Debois, and John Willis**, *The DevOps Handbook: How to Create World-Class Agility, Reliability, & Security in Technology Organizations*, IT Revolution Press, 2nd Edition, 2016.

### Reference Books:
1. **Rajib Mall**, *Fundamentals of Software Engineering*, 3rd / 4th / 5th Edition, PHI Learning Private Limited.
2. **Pankaj Jalote**, *Software Engineering: A Precise Approach*, Wiley India, 2010.
3. **S. A. Kelkar**, *Software Engineering*, Prentice Hall of India Pvt Ltd, 2007.
4. **Stephen R. Schach**, *Software Engineering*, Tata McGraw-Hill Publishing Company Limited, 2007.

### Official NPTEL & Web Learning Resources:
1. **NPTEL Web & Video Course:** `https://nptel.ac.in/courses/106/105/106105182/` (Prof. Rajib Mall, IIT Kharagpur, 60 Lectures).
2. **Swayam Course:** `https://swayam.gov.in/nd1_noc19_cs69/preview`
3. **VSSUT Comprehensive Lecture Notes:** `http://www.vssut.ac.in/lecture_notes/lecture1428551142.pdf`
4. **Rutgers University SE Course Slides:** `https://www.ece.rutgers.edu/~marsic/books/SE/instructor/slides/`
5. **University of Washington SE Course Materials:** `https://courses.cs.washington.edu/courses/cse403/01au/lectures/`
