# Module IV: Testing & Maintenance — Master Question Bank
### Course: 24ITPC302 – Software Engineering (Regulations 2024)

---

## PART A: 2-MARK CONCEPTUAL QUESTIONS (K1 / K2)

1. **Question 4.1:** Distinguish between Verification and Validation using Barry Boehm's questions.  
   *(Answer: Verification: "Are we building the product right?" (reviews, inspections of artifacts); Validation: "Are we building the right product?" (dynamic execution against client needs)).*
2. **Question 4.2:** Explain the lifecycle difference between an Error, a Fault, and a Failure.  
   *(Answer: Error is human mistake $\to$ leads to a Fault/Bug in code $\to$ causes a Failure during runtime execution when the faulty code runs).*
3. **Question 4.3:** State the three formulas for calculating Cyclomatic Complexity $V(G)$ of a Control Flow Graph.  
   *(Answer: (1) $V(G) = E - N + 2P$, (2) $V(G) = P' + 1$ [predicates], (3) $V(G) = R$ [regions]).*
4. **Question 4.4:** What is an "Independent Basis Path" in testing?  
   *(Answer: Any path through the program control flow graph that introduces at least one new set of processing statements or a new condition not traversed by any previous path).*
5. **Question 4.5:** For an input integer variable $X$ constrained to $10 \le X \le 50$, write the test cases derived using Boundary Value Analysis (BVA).  
   *(Answer: Standard BVA values: $10, 11, 30 \text{ (nominal)}, 49, 50$. Robust BVA adds $9$ and $51$).*
6. **Question 4.6:** Differentiate between Stubs and Drivers used in integration testing.  
   *(Answer: A **Driver** is a dummy program that calls the module under test (used in Bottom-Up testing); a **Stub** is a dummy routine that replaces a subordinate module called by the module under test (used in Top-Down testing)).*
7. **Question 4.7:** Contrast Alpha Testing with Beta Testing.  
   *(Answer: Alpha testing is performed by end-users at the developer's site in a controlled environment; Beta testing is performed by end-users at their own sites under live operating conditions without developers).*
8. **Question 4.8:** What is Regression Testing? When must it be executed?  
   *(Answer: Re-running existing test suites after bug fixes or feature additions to verify that modifications have not broken previously functioning capabilities).*
9. **Question 4.9:** What are the 4 categories of Software Maintenance according to Lientz and Swanson? Which accounts for the largest effort?  
   *(Answer: Corrective (21%), Adaptive (25%), Perfective (50%), Preventive (4%). Perfective maintenance accounts for the largest effort).*
10. **Question 4.10:** Define Reverse Engineering and Forward Engineering in the context of legacy software.  
    *(Answer: Reverse Engineering extracts high-level architectural models and design specifications from legacy source code; Forward Engineering rebuilds the system using modern technologies from those extracted models).*

---

## PART B: 13-MARK & 14-MARK UNIVERSITY MODEL QUESTIONS

### Model 1: White-Box Basis Path Testing (Numerical)
- **Problem 1.1:** Consider the following pseudocode function to find the maximum of three numbers:
  ```c
  int findMax(int a, int b, int c) {
      int max = a;
      if (b > max) {
          max = b;
      }
      if (c > max) {
          max = c;
      }
      return max;
  }
  ```
  (i) Draw the Control Flow Graph (CFG) identifying all nodes and edges.  
  (ii) Calculate Cyclomatic Complexity $V(G)$ using all three methods (Edges/Nodes, Predicate nodes, Regions).  
  (iii) Enumerate all linearly independent basis paths.  
  (iv) Formulate specific test input cases $(a, b, c)$ and expected outputs to execute each basis path.

### Model 2: Black-Box Testing & Integration Strategies
- **Problem 2.1:** A software module accepts an applicant's age ($18 \le \text{Age} \le 60$) and credit score ($300 \le \text{Score} \le 900$). Using Equivalence Class Partitioning and Boundary Value Analysis (BVA), derive complete tables of test cases including valid and invalid inputs.
- **Problem 2.2:** Explain the progressive integration testing strategies: Big-Bang, Top-Down Integration, Bottom-Up Integration, and Sandwich Integration. Detail the roles of stubs and drivers, comparing each strategy across debugging ease and early architectural verification.
- **Problem 2.3:** Describe the Software Reengineering Process Model with a comprehensive flow diagram. Detail the steps from Inventory Analysis to Forward Engineering, explaining the importance of code and data restructuring.
