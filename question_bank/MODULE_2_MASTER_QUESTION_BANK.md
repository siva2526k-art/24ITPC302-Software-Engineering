# Module II: Requirements Analysis & Specification — Master Question Bank
### Course: 24ITPC302 – Software Engineering (Regulations 2024)

---

## PART A: 2-MARK CONCEPTUAL QUESTIONS (K1 / K2)

1. **Question 2.1:** Distinguish between Functional Requirements and Non-Functional Requirements with examples.  
   *(Answer: Functional specifies what the system must compute/do, e.g., "Authenticate user with OTP"; Non-functional specifies quality constraints/how it performs, e.g., "Response time must be under 1.5 seconds").*
2. **Question 2.2:** What is the FURPS+ model of requirements classification?  
   *(Answer: Functionality, Usability, Reliability, Performance, Supportability, plus constraints like design, implementation, interface, and physical constraints).*
3. **Question 2.3:** Why is an SRS considered a legal contract between client and developer?  
   *(Answer: It forms the binding contractual baseline defining agreed-upon scope; acceptance testing is legally judged against conformance to the SRS).*
4. **Question 2.4:** State any four desirable characteristics of a good Software Requirements Specification (SRS) according to IEEE 830.  
   *(Answer: Unambiguous, Complete, Consistent, Verifiable, Modifiable, Traceable).*
5. **Question 2.5:** What are the 4 fundamental phases of the Requirements Engineering process?  
   *(Answer: (1) Feasibility Studies, (2) Requirements Elicitation & Analysis, (3) Requirements Specification, (4) Requirements Validation).*
6. **Question 2.6:** Explain the purpose of a Requirement Traceability Matrix (RTM).  
   *(Answer: A grid table that links each original business requirement forward to its corresponding design module, source code file, and test case ID to ensure no requirements are omitted or orphaned).*
7. **Question 2.7:** What is a Context Diagram (Level 0 DFD)? What is its primary rule?  
   *(Answer: A single high-level process representing the entire software system, interacting only with external entities. Rule: It contains no internal data stores).*
8. **Question 2.8:** State the DFD Balancing Rule between Level 1 and Level 2 diagrams.  
   *(Answer: The data flows entering and leaving a parent process at Level 1 must exactly match the aggregate data flows entering and leaving its decomposed child sub-processes at Level 2).*
9. **Question 2.9:** Define Petri Nets. What are the four structural components?  
   *(Answer: A mathematical modeling tool for concurrent, asynchronous systems consisting of Places (circles), Transitions (bars), Arcs (directed arrows), and Tokens (dots)).*
10. **Question 2.10:** Write the standard Data Dictionary notation symbols for Sequence, Selection, and Iteration.  
    *(Answer: Sequence: `+`; Selection / Choice: `[ | ]`; Iteration / Repetition: `{ }`; Optional: `( )`).*

---

## PART B: 13-MARK & 14-MARK UNIVERSITY MODEL QUESTIONS

### Model 1: SRS & Requirements Engineering Process
- **Problem 1.1:** Present the standard IEEE 830 outline for a Software Requirements Specification (SRS). Discuss in detail the contents of Section 1 (Introduction), Section 2 (Overall Description), and Section 3 (Specific Requirements). Explain why verifiability is critical.
- **Problem 1.2:** Describe the 4 types of Feasibility Studies conducted during the initial phase of software engineering. Explain the techniques used during Requirements Elicitation (Interviews, JAD, Questionnaires, Use Cases).

### Model 2: Structured Analysis, DFDs & Petri Nets
- **Problem 2.1:** Consider an **Online Railway Ticket Reservation System**. Draw the Level 0 Context Diagram and the Level 1 Data Flow Diagram (DFD). Clearly show all external entities, processes, data flows, and data stores. Define the Data Dictionary entries for `Ticket_Request` and `Reservation_Record`.
- **Problem 2.2:** Explain how Petri Nets model concurrency, synchronization, and mutual exclusion in operating and software systems. Show the transition firing rules with a neat diagram illustrating the Producer-Consumer problem with a bounded buffer.
