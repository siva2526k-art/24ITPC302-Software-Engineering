# University Exam Model Answer: Functional vs. Non-Functional Requirements

**Course Code:** 24ITPC302 — Software Engineering  
**Unit:** Module II — Requirements Analysis & Specification  
**Target Marks:** 13 Marks / 16 Marks  
**Evaluation Standard:** Anna University / Autonomous Regulations 2024 Model

---

## Question:
> **(a) Differentiate between Functional and Non-Functional Requirements in detail with appropriate examples. Explain the FURPS+ classification model. [7 Marks]**  
> **(b) Why are Non-Functional Requirements often harder to specify and verify than Functional Requirements? State the quantifiable engineering metrics used to specify Performance, Reliability, Availability, and Usability. [6 Marks]**

---

## 1. Definitions
- **Functional Requirements (FR):** Statements describing the specific behavioral services, calculations, data transformations, and input-output functions that a software system must execute. (Defines *"What the system does"*).
- **Non-Functional Requirements (NFR):** Constraints, standards, and quality attributes imposed on the software services, defining operational limits such as latency, throughput, security, availability, and usability. (Defines *"How well the system does it"*).

---

## 2. Comprehensive 10-Parameter Comparison Matrix

| Evaluation Dimension | Functional Requirements (FR) | Non-Functional Requirements (NFR) |
| :--- | :--- | :--- |
| **1. Fundamental Question** | **"What does the system do?"** | **"How well does the system perform?"** |
| **2. Definition** | Precise statements of behavioral features, calculations, and data processing. | Operational constraints on performance, security, reliability, and ergonomics. |
| **3. Scope of Impact** | **Localized:** Confined to a single module, class, or user screen. | **Cross-Cutting:** Pervades the entire software architecture, database, and infrastructure. |
| **4. Origin** | Derived directly from customer business operations and user workflows. | Derived from technical constraints, legal regulations, performance needs, and user experience standards. |
| **5. Verification** | Binary (**Pass / Fail**): Feature either executes correctly or does not. | Continuous / Quantitative: Measured against numeric thresholds (e.g., latency $< 200\text{ ms}$). |
| **6. Architectural Impact** | Influences low-level component logic and algorithm design. | Dictates high-level architectural styles (microservices, caching, redundancy). |
| **7. Specification Format** | Expressed via Use Cases, User Stories, and Input-Process-Output tables. | Expressed as quantifiable constraints using standard engineering metrics. |
| **8. Testing Technique** | Black-box functional testing, unit testing, user acceptance testing. | Stress testing, load profiling, penetration testing, usability lab tests. |
| **9. Failure Consequence** | An isolated feature fails, but the rest of the application remains usable. | System-wide collapse: entire platform crashes, data is breached, or users abandon app. |
| **10. Concrete Example** | *"The system shall calculate 8% sales tax on cart items."* | *"The system shall process 3,000 transactions per second at $< 200\text{ ms}$ latency."* |

---

## 3. The FURPS+ Classification Framework

Developed by Robert Grady at Hewlett-Packard, **FURPS+** is the industry-standard taxonomy for software quality attributes:

1. **Functionality ($F$):** Core business capabilities, mathematical operations, security authentication, and general system services.
2. **Usability ($U$):** Human ergonomics, visual consistency, navigation ease, error feedback, and accessibility (WCAG).
3. **Reliability ($R$):** Precision of outputs, crash recovery, Mean Time Between Failures ($MTBF$), and predictability under exceptional inputs.
4. **Performance ($P$):** Processing speed, response latency, throughput (TPS), memory footprints, and resource consumption.
5. **Supportability ($S$):** Modularity, maintainability, testability, diagnostic logging, and portability across operating environments.
6. **The "+" Constraints:** 
   - *Design constraints:* Mandated architectural patterns (e.g., Microservices).
   - *Implementation constraints:* Required programming languages, tools, or libraries.
   - *Interface constraints:* Required interaction protocols with legacy external systems.
   - *Physical constraints:* Hardware limitations (size, weight, battery power).

---

## 4. Why Are Non-Functional Requirements Harder to Specify & Verify?

1. **Subjective Natural Language Adjectives:** Stakeholders describe NFRs using ambiguous adjectives (*"fast"*, *"secure"*, *"user-friendly"*, *"robust"*). Without numeric thresholds, developers and clients disagree on acceptance.
2. **Conflicting Priorities (Architectural Trade-Offs):** Enhancing one quality attribute frequently damages another:
   - Increasing **Security** (multi-factor authentication, 256-bit AES encryption) increases latency and degrades **Performance** and **Usability**.
   - Enhancing **Performance** (caching, asynchronous writes) can compromise transactional **Consistency**.
3. **Pervasive System Scope:** An NFR like Security or Reliability cannot be implemented in a single module; it requires coordination across front-end UI, backend middleware, network ciphers, and physical database schemas.

---

## 5. Quantifiable Engineering Metrics for NFRs

An NFR must never be left as an informal statement; it must be written using **verifiable, quantifiable engineering metrics**:

| Quality Attribute | Defective / Vague Requirement | Valid, Quantifiable & Testable Requirement | Engineering Metric Used |
| :--- | :--- | :--- | :--- |
| **Performance (Latency)** | *"The system must respond quickly."* | *"Search query results shall be rendered within 500 ms for 95% of queries under a load of 2,000 concurrent users."* | Response Latency (Milliseconds) at specific user concurrency. |
| **Performance (Throughput)** | *"The system must handle large order volumes."* | *"The order ingestion pipeline shall process a minimum of 3,500 orders per second under peak festival traffic."* | Throughput (Transactions per Second - TPS). |
| **Reliability** | *"The software should rarely crash."* | *"The software shall exhibit a Mean Time Between Failures (MTBF) of at least 2,500 hours of continuous operations."* | Mean Time Between Failures ($MTBF$). |
| **Availability** | *"The portal must always be online."* | *"The system shall maintain an operational availability of 99.99% ('Four Nines'), allowing less than 52.6 minutes of downtime per year."* | Availability Formula: $A = \frac{MTBF}{MTBF + MTTR} \times 100\%$ |
| **Usability** | *"The user interface must be easy to learn."* | *"A newly hired clerk shall complete a customer account creation task within 3 minutes with zero errors after 30 minutes of training."* | Task Completion Time & Error Rate on Benchmark Users. |
| **Security** | *"The customer database must be safe from hackers."* | *"All stored patient health records shall be encrypted using AES-256 at rest, and all HTTP transmissions must enforce TLS 1.3 encryption."* | Industry Encryption Standard & Protocol Version. |

---

## 6. Mathematical Availability Calculation (Sample Problem)

$$\text{Availability } (A) = \frac{\text{MTBF}}{\text{MTBF} + \text{MTTR}} \times 100\%$$

- **Problem:** A core banking system has a Mean Time Between Failures ($MTBF$) of 998 hours. When an unexpected outage occurs, the automated failover cluster has a Mean Time to Repair ($MTTR$) of 2 hours. Calculate its availability.
- **Solution:**
  $$A = \frac{998}{998 + 2} \times 100\% = \frac{998}{1000} \times 100\% = \mathbf{99.8\%}$$
  *(This represents 17.5 hours of downtime per year, indicating a need for hot-standby redundancy to reach high-availability standards.)*

---

## 7. Conclusion
Functional requirements establish *what* software features to build, while Non-Functional requirements establish the *architectural quality and boundaries* within which those features operate. Specifying NFRs using objective, quantifiable engineering metrics ensures that the final software is not only functionally correct, but also robust, secure, scalable, and acceptable to users.
