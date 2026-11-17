# Module III: Software Design — Master Question Bank
### Course: 24ITPC302 – Software Engineering (Regulations 2024)

---

## PART A: 2-MARK CONCEPTUAL QUESTIONS (K1 / K2)

1. **Question 3.1:** What is the fundamental difference between software architecture and detailed design?  
   *(Answer: Architecture defines the high-level structural organization of components, interfaces, and control flow; Detailed design specifies the internal data structures, algorithms, and logic of individual components).*
2. **Question 3.2:** State the Information Hiding principle formulated by David Parnas.  
   *(Answer: Modules should be designed such that their internal algorithms and data structures are hidden behind clean public interfaces, preventing unauthorized external access and localizing change impact).*
3. **Question 3.3:** Define Cohesion and Coupling. State the primary objective of software modularization.  
   *(Answer: Cohesion is the intra-module functional strength; Coupling is the inter-module dependency. Objective: Maximize Cohesion and Minimize Coupling).*
4. **Question 3.4:** Why is Functional Cohesion considered the most desirable form of cohesion?  
   *(Answer: Because every element in the module is focused exclusively on executing a single, unambiguous mathematical or computational function, maximizing reusability and testability).*
5. **Question 3.5:** Why is Content Coupling considered the worst form of coupling?  
   *(Answer: One module directly modifies the code or internal data of another module, completely breaking encapsulation and making debugging nearly impossible).*
6. **Question 3.6:** Differentiate between Fan-In and Fan-Out. Which should be maximized in software architecture?  
   *(Answer: Fan-Out is the number of modules directly called by a module; Fan-In is the number of modules calling it. Fan-In should be maximized as it represents code reuse).*
7. **Question 3.7:** What is the primary characteristic of a Pipe-and-Filter architectural style?  
   *(Answer: Data is processed as continuous streams by independent filter components connected through unidirectional pipes, with no shared global state).*
8. **Question 3.8:** Explain the concept of Layered Architecture. What is its main advantage?  
   *(Answer: Organizes components into horizontal layers where each layer provides services only to the layer immediately above it and consumes services from the layer below. Advantage: Modularity and layer-swapping).*
9. **Question 3.9:** What is the difference between Transform Flow and Transaction Flow in a DFD?  
   *(Answer: Transform flow processes an input data stream sequentially through an afferent branch, transform center, and efferent branch; Transaction flow forks into one of many distinct paths based on an input transaction code).*
10. **Question 3.10:** State the 3 Golden Rules of User Interface Design proposed by Theo Mandel.  
    *(Answer: (1) Place the user in control, (2) Reduce the user's memory load, (3) Make the interface consistent).*

---

## PART B: 13-MARK & 14-MARK UNIVERSITY MODEL QUESTIONS

### Model 1: Modularity, Cohesion & Coupling
- **Problem 1.1:** Define Functional Independence. Explain all 7 levels of Cohesion from lowest (Coincidental) to highest (Functional) and all 6 levels of Coupling from highest (Content) to lowest (Data). Provide code illustrations for each level.
- **Problem 1.2:** Describe design heuristics used in effective modular system design: (i) Scope of Effect vs Scope of Control, (ii) Controlling Fan-In and Fan-Out, and (iii) Architectural Refinement.

### Model 2: Architectural Styles & Data Flow Mapping
- **Problem 2.1:** Compare and contrast the following architectural styles with neat diagrams: (i) Data-Centered / Repository Architecture, (ii) Client-Server / Layered Architecture, and (iii) Pipe-and-Filter Architecture. Outline the pros and cons of each.
- **Problem 2.2:** Explain the complete procedure of Transform Mapping used to convert a Data Flow Diagram (DFD) into a Structure Chart. Walk through the steps of identifying the transform center, designing afferent and efferent branches, and factoring the control structure.
