# Agile vs Waterfall: Visual Comparison & Architectural Contrast

This document contains publication-grade Mermaid diagrams contrasting the **Classical Waterfall Model** (Predictive / Plan-Driven) with **Agile Methodologies** (Adaptive / Empirical).

---

## 1. Process Lifecycle Comparison: Linear vs Cyclic Sprints

```mermaid
flowchart TD
    classDef waterfall fill:#e0f2fe,stroke:#0284c7,stroke-width:2px,color:#0369a1;
    classDef agile fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#15803d;
    classDef output fill:#fef3c7,stroke:#d97706,stroke-width:2px,color:#78350f;

    subgraph WF["CLASSICAL WATERFALL MODEL: Plan-Driven & Sequential (Single Monolithic Pass)"]
        direction LR
        W1["Requirements<br/>(Frozen Upfront)"] --> W2["Design<br/>(Architectural SDD)"]
        W2 --> W3["Implementation<br/>(Coding All Units)"]
        W3 --> W4["Verification<br/>(Late Testing)"]
        W4 --> W5["Deployment<br/>(100% System)"]
        W5 --> WOut["Single Big-Bang Release<br/>(Delivered Month 12–18)"]
    end

    subgraph AG["AGILE METHODOLOGY: Adaptive & Empirical (Repeating 2–4 Week Sprints)"]
        direction TB
        Backlog["Product Backlog<br/>(Prioritized User Stories)"] --> SprintPlan["Sprint Planning<br/>(Select top stories)"]
        
        subgraph SprintBox["2 to 4 Week Sprint Cycle"]
            direction LR
            S1["Daily Standup"] --> S2["Design & Code"]
            S2 --> S3["TDD & Automated Test"]
            S3 --> S4["Continuous Integration"]
        end

        SprintPlan --> SprintBox
        SprintBox --> Demo["Sprint Review & Demo<br/>(Working Software)"]
        Demo --> Retro["Sprint Retrospective<br/>(Process Improvement)"]
        Retro --> Deliverable["Potentially Shippable Product Increment<br/>(Delivered Every 2–4 Weeks)"]
        Deliverable -.->|"Feedback loop updates backlog"| Backlog
    end

    class W1,W2,W3,W4,W5 waterfall;
    class WOut output;
    class Backlog,SprintPlan,S1,S2,S3,S4,Demo,Retro,Deliverable agile;
```

---

## 2. Working Software Availability Timeline

```mermaid
gantt
    title Working Software Delivery: Waterfall vs Agile
    dateFormat  X
    axisFormat Month %m

    section Waterfall (Monolithic)
    Requirements Analysis & Frozen Spec :w1, 0, 3
    System & Detailed Architecture      :w2, 3, 6
    Full System Coding & Construction   :w3, 6, 10
    Integrated System Testing & UAT     :w4, 10, 12
    First Working Software to Customer  :milestone, m_wf, 12, 12

    section Agile (Incremental Sprints)
    Sprint 1 (Basic MVP Features)       :done, s1, 0, 1
    Increment 1 in Customer Hands       :milestone, ms1, 1, 1
    Sprint 2 (Secondary Enhancements)   :done, s2, 1, 2
    Increment 2 in Customer Hands       :milestone, ms2, 2, 2
    Sprint 3 (Integrations & Reporting) :active, s3, 2, 3
    Increment 3 in Customer Hands       :milestone, ms3, 3, 3
    Sprint 4 (Advanced Features)        :crit, s4, 3, 4
    Increment 4 in Customer Hands       :milestone, ms4, 4, 4
```

### Explanation of Diagram:
- In **Waterfall**, customer visibility is zero for 10–12 months. Any mismatch between original requirements and real business needs is discovered only at the very end.
- In **Agile**, the customer receives a working, tested slice of software at the end of **Month 1**, continuing to receive validated software increments every month.
