# Spiral Model: Visual Architecture & Barry Boehm's 4 Quadrants

This document contains publication-grade Mermaid diagrams representing **Barry Boehm's Spiral Model (1988)**, showing the four quadrants, the radial and angular dimensions, and the progressive spiral turns.

---

## 1. Boehm's Four-Quadrant Spiral Architecture

The Spiral Model divides software engineering activities into four distinct quadrants traversed in a clockwise direction. Each loop of the spiral represents an evolutionary phase:

```mermaid
flowchart TD
    classDef q1 fill:#e0f2fe,stroke:#0284c7,stroke-width:2px,color:#0369a1;
    classDef q2 fill:#fee2e2,stroke:#dc2626,stroke-width:2px,color:#7f1d1d;
    classDef q3 fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#15803d;
    classDef q4 fill:#fef3c7,stroke:#d97706,stroke-width:2px,color:#78350f;
    classDef turn fill:#f3f4f6,stroke:#6b7280,stroke-width:2px,color:#111827;

    subgraph Top["UPPER HALF: PLANNING & RISK MITIGATION"]
        direction LR
        subgraph Q2["QUADRANT II (Top-Left)<br/>IDENTIFY & RESOLVE RISKS"]
            Q2_Desc["• Exhaustive risk analysis & scoring<br/>• Build rapid throwaway prototypes<br/>• Benchmark simulation & stress tests<br/>• Eliminate high-risk uncertainties"]
        end

        subgraph Q1["QUADRANT I (Top-Right)<br/>DETERMINE OBJECTIVES & CONSTRAINTS"]
            Q1_Desc["• Define iteration objectives & goals<br/>• Identify technical alternatives (COTS vs custom)<br/>• Establish project constraints (cost, schedule)<br/>• Identify interfaces & operational boundaries"]
        end
    end

    subgraph Bottom["LOWER HALF: ENGINEERING & EVALUATION"]
        direction LR
        subgraph Q3["QUADRANT III (Bottom-Left)<br/>ENGINEER, DEVELOP & VERIFY"]
            Q3_Desc["• Construct product increment for current turn<br/>• Low turn: Architecture simulations<br/>• Mid turn: Detailed design & functional prototype<br/>• High turn: Operational code & rigorous testing"]
        end

        subgraph Q4["QUADRANT IV (Bottom-Right)<br/>PLAN NEXT PHASE & CUSTOMER REVIEW"]
            Q4_Desc["• Customer evaluates current deliverables<br/>• Management audits budget, schedule & quality<br/>• Milestone commitment review (Go / No-Go)<br/>• Formulate detailed plan for next spiral cycle"]
        end
    end

    %% Clockwise traversal loop
    Q1 -->|"Step 1: Move clockwise to evaluate risks"| Q2
    Q2 -->|"Step 2: Move clockwise to construct deliverable"| Q3
    Q3 -->|"Step 3: Move clockwise to review & plan"| Q4
    Q4 -->|"Step 4: Expand spiral outward to next turn"| Q1

    class Q1,Q1_Desc q1;
    class Q2,Q2_Desc q2;
    class Q3,Q3_Desc q3;
    class Q4,Q4_Desc q4;
```

---

## 2. Progressive Spiral Turns: From Concept to Operational Software

Each cycle around the four quadrants expands radially outward, representing increasing cumulative cost and progress toward a complete system:

```mermaid
flowchart TD
    classDef turn1 fill:#f0fdf4,stroke:#22c55e,stroke-width:2px,color:#14532d;
    classDef turn2 fill:#eff6ff,stroke:#3b82f6,stroke-width:2px,color:#1e3a8a;
    classDef turn3 fill:#faf5ff,stroke:#a855f7,stroke-width:2px,color:#581c87;
    classDef turn4 fill:#fff7ed,stroke:#f97316,stroke-width:2px,color:#7c2d12;
    classDef decision fill:#fee2e2,stroke:#ef4444,stroke-width:2px,color:#991b1b;

    T1["SPIRAL TURN 1: Concept of Operations<br/>• Objective: Feasibility & business viability<br/>• Risk Action: Technical feasibility study<br/>• Deliverable: Concept document & basic simulation"]
    
    G1{"Review Gate 1:<br/>Concept Viable?"}
    T1 --> G1
    G1 -- "No" --> Abort1([Terminate Project Early - Minimized Loss])
    G1 -- "Yes" --> T2

    T2["SPIRAL TURN 2: Requirements & Architecture<br/>• Objective: Functional scope & structural design<br/>• Risk Action: Architectural prototype & UI mockups<br/>• Deliverable: Validated SRS & Architectural Prototype"]

    G2{"Review Gate 2:<br/>Architecture Sound?"}
    T2 --> G2
    G2 -- "No" --> Abort2([Terminate Project Before Heavy Coding])
    G2 -- "Yes" --> T3

    T3["SPIRAL TURN 3: Detailed Design & Subsystems<br/>• Objective: Algorithmic design & component build<br/>• Risk Action: Interface benchmarking & stress tests<br/>• Deliverable: Operational subsystem prototype"]

    G3{"Review Gate 3:<br/>Subsystems Verified?"}
    T3 --> G3
    G3 -- "No" --> Redo3["Refactor / Re-evaluate Risks"] --> T3
    G3 -- "Yes" --> T4

    T4["SPIRAL TURN 4: Operational System<br/>• Objective: Full-scale system construction<br/>• Risk Action: Deployment risk & security auditing<br/>• Deliverable: Production software, acceptance tests, live release"]

    T4 --> Deployed([System in Production & Maintenance])

    class T1 turn1;
    class T2 turn2;
    class T3 turn3;
    class T4 turn4;
    class G1,G2,G3 decision;
```

### Explanation of Spiral Dimensions:
- **Radial Dimension ($r$):** The distance from the center origin represents **cumulative project cost and effort**. As the spiral moves outward, more capital and engineering resources are expended.
- **Angular Dimension ($\theta$):** The angular position represents **progress completed within the current iteration cycle**. Each $360^\circ$ rotation represents the completion of one entire development turn across all four quadrants.
- **Why It Is "Risk-Driven":** If an unresolvable technical or financial risk is uncovered in Quadrant II of Turn 1 or 2, the project is terminated immediately at a fraction of the total budget, preventing catastrophic multi-million dollar failures.
