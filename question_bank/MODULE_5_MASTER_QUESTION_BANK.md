# Module V: Project Management — Master Question Bank
### Course: 24ITPC302 – Software Engineering (Regulations 2024)

---

## PART A: 2-MARK CONCEPTUAL QUESTIONS (K1 / K2)

1. **Question 5.1:** State the "4 P's" of Software Project Management in order of priority.  
   *(Answer: People, Product, Process, Project. People are the most important determinant of project success).*
2. **Question 5.2:** State one major advantage and one limitation of Lines of Code (LOC) as a software metric.  
   *(Answer: Advantage: Easily automated and counted post-implementation; Limitation: Highly language-dependent and penalizes clean, concise coding).*
3. **Question 5.3:** What are the 5 Information Domain characteristics evaluated in Function Point (FP) analysis?  
   *(Answer: External Inputs [EI], External Outputs [EO], External Inquiries [EQ], Internal Logical Files [ILF], External Interface Files [EIF]).*
4. **Question 5.4:** Write the formula for the Value Adjustment Factor ($VAF$) in Function Point analysis. What is its permissible range?  
   *(Answer: $VAF = 0.65 + 0.01 \sum_{i=1}^{14} F_i$. Permissible range: $0.65 \le VAF \le 1.35$).*
5. **Question 5.5:** Distinguish between Organic, Semidetached, and Embedded modes in Basic COCOMO I.  
   *(Answer: Organic: Small teams, familiar domain, flexible requirements [$E = 2.4(KLOC)^{1.05}$]; Semidetached: Medium teams, mixed experience [$E = 3.0(KLOC)^{1.12}$]; Embedded: Tight constraints, embedded systems, inflexible [$E = 3.6(KLOC)^{1.20}$]).*
6. **Question 5.6:** In Intermediate COCOMO, how is the Effort Adjustment Factor ($EAF$) calculated?  
   *(Answer: By multiplying all 15 Cost Driver ratings: $EAF = \prod_{i=1}^{15} CD_i$).*
7. **Question 5.7:** Define "Critical Path" in PERT/CPM project scheduling. What is the float/slack of tasks on the critical path?  
   *(Answer: The longest continuous path of dependent activities from project start to finish. The slack of every task on the critical path is strictly zero).*
8. **Question 5.8:** In Earned Value Analysis, what do $CV < 0$ and $SV < 0$ signify?  
   *(Answer: $CV < 0$ indicates the project is **Over Budget** ($AC > EV$); $SV < 0$ indicates the project is **Behind Schedule** ($EV < PV$)).*
9. **Question 5.9:** Write the formulas for Cost Performance Index ($CPI$) and Schedule Performance Index ($SPI$).  
   *(Answer: $CPI = \frac{EV}{AC}$ and $SPI = \frac{EV}{PV}$).*
10. **Question 5.10:** What is an RFP (Request for Proposal) in software acquisition?  
    *(Answer: A formal procurement document issued by a client detailing software specifications, inviting competitive bids from vendors, and establishing evaluation criteria).*

---

## PART B: 13-MARK & 14-MARK UNIVERSITY MODEL QUESTIONS

### Model 1: Function Points & Cost Estimation (Numerical)
- **Problem 1.1:** A software project for a modern hospital management system has the following requirements:
  - External Inputs: 30 (Simple, weight 3) and 10 (Complex, weight 6)
  - External Outputs: 25 (Average, weight 5)
  - External Inquiries: 20 (Simple, weight 3)
  - Internal Logical Files: 6 (Average, weight 10)
  - External Interface Files: 4 (Complex, weight 10)
  All 14 General System Characteristics ($F_i$) are assessed at an average rating of 3.
  (i) Calculate the Unadjusted Function Count ($UFC$).  
  (ii) Calculate the Value Adjustment Factor ($VAF$).  
  (iii) Determine the final Function Points ($FP$).  
  (iv) If the system is to be implemented in Java (average productivity = 53 LOC/FP), compute total estimated KLOC.  
  (v) Using Basic COCOMO I, estimate total Effort (Person-Months) and Development Time (Months) under Organic mode.

- **Problem 1.2:** A software system is estimated at 60 KLOC. Compute the development Effort, Duration, Staff Size, and Productivity under: (i) Organic Mode, (ii) Semidetached Mode, and (iii) Embedded Mode using the Basic COCOMO I formulas. Compare and interpret the results.

### Model 2: Project Scheduling & Earned Value Analysis (Numerical)
- **Problem 2.1:** A software project consists of 6 activities with dependencies and estimated durations:
  - $A$ (None, 4 days), $B$ ($A$, 6 days), $C$ ($A$, 3 days), $D$ ($B$, 8 days), $E$ ($C$, 5 days), $F$ ($D$ and $E$, 4 days).
  (i) Draw the CPM project network diagram.  
  (ii) Compute Earliest Start ($ES$), Earliest Finish ($EF$), Latest Start ($LS$), and Latest Finish ($LF$) for each task.  
  (iii) Determine the Slack for each activity.  
  (iv) Identify the Critical Path and total project completion time.

- **Problem 2.2:** A software company signs a contract to build an e-commerce platform with a planned Budget at Completion $BAC = \$250,000$ and a planned duration of 10 months. At the end of Month 5, a project audit reveals:
  - Planned Value ($PV$) = $\$125,000$
  - Earned Value ($EV$) = $\$100,000$
  - Actual Cost ($AC$) = $\$130,000$
  (i) Calculate Cost Variance ($CV$) and Schedule Variance ($SV$).  
  (ii) Compute Cost Performance Index ($CPI$) and Schedule Performance Index ($SPI$).  
  (iii) Determine the Estimate at Completion ($EAC$) and Estimate to Complete ($ETC$).  
  (iv) Provide a professional assessment of the project's health and suggest corrective actions.
