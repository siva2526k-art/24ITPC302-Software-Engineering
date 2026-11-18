# Petri Nets: Visual Modeling & Producer-Consumer State Transitions

This document contains standardized, publication-grade Mermaid diagrams representing **Petri Nets** as a formal mathematical tool for modeling concurrent, asynchronous, and distributed systems.

---

## 1. The Producer-Consumer Synchronization Model (Bounded Buffer)

The classical Producer-Consumer system coordinates two asynchronous processes sharing a finite buffer of capacity $K=2$.

```mermaid
flowchart TD
    classDef place fill:#e0f2fe,stroke:#0284c7,stroke-width:2px,color:#0369a1;
    classDef trans fill:#1e293b,stroke:#0f172a,stroke-width:2px,color:#ffffff;
    classDef buffer fill:#fef3c7,stroke:#d97706,stroke-width:2px,color:#78350f;

    subgraph Producer["PRODUCER PROCESS"]
        P1(("P1: Producer Ready<br/>[Token: ●]"))
        T1["T1: Produce & Deposit Item<br/>(Transition Bar)"]
    end

    subgraph SharedBuffer["SHARED BOUNDED BUFFER (Capacity K = 2)"]
        P2(("P2: Buffer Slots Free<br/>[Tokens: ● ●]"))
        P3(("P3: Buffer Items Ready<br/>[Tokens: Empty]"))
    end

    subgraph Consumer["CONSUMER PROCESS"]
        T2["T2: Fetch & Consume Item<br/>(Transition Bar)"]
        P4(("P4: Consumer Ready<br/>[Token: ●]"))
    end

    %% Firing Connections for T1 (Produce)
    P1 -->|Consumes 1 token| T1
    P2 -->|Consumes 1 empty slot| T1
    T1 -->|Deposits token back| P1
    T1 -->|Deposits 1 produced item| P3

    %% Firing Connections for T2 (Consume)
    P3 -->|Consumes 1 item| T2
    P4 -->|Consumes 1 token| T2
    T2 -->|Deposits token back| P4
    T2 -->|Releases 1 slot back| P2

    class P1,P4 place;
    class T1,T2 trans;
    class P2,P3 buffer;
```

---

## 2. Token Reachability & State Transition Trace

A Petri Net execution is traced via its **Marking Vector** $M = [M(P_1), M(P_2), M(P_3), M(P_4)]$:

```mermaid
stateDiagram-v2
    direction LR

    M0: M0 = [1, 2, 0, 1]<br/>Initial State<br/>(2 slots free, 0 items)
    M1: M1 = [1, 1, 1, 1]<br/>T1 Fires (Produce 1st Item)<br/>(1 slot free, 1 item)
    M2: M2 = [1, 0, 2, 1]<br/>T1 Fires Again (Buffer FULL)<br/>(0 slots free, 2 items)
    M3: M3 = [1, 1, 1, 1]<br/>T2 Fires (Consume 1 Item)<br/>(1 slot free, 1 item)
    M4: M4 = [1, 2, 0, 1]<br/>T2 Fires Again (Buffer EMPTY)<br/>(2 slots free, 0 items)

    [*] --> M0
    M0 --> M1: T1 fires (Produce)
    M1 --> M2: T1 fires (Produce)
    M1 --> M4: T2 fires (Consume)
    M2 --> M3: T2 fires (Consume)
    M3 --> M4: T2 fires (Consume)
    M4 --> [*]
```

### Explanation of Petri Net Dynamics:
1. **Initial Marking ($M_0 = [1, 2, 0, 1]$):**
   - Place $P_1$ has 1 token: Producer is idle and ready.
   - Place $P_2$ has 2 tokens: 2 buffer slots are vacant.
   - Place $P_3$ has 0 tokens: No items are available in the buffer.
   - Place $P_4$ has 1 token: Consumer is idle and ready.
2. **Firing Transition $T_1$ (Produce):**
   - $T_1$ is enabled because its input places ($P_1$ and $P_2$) both contain tokens.
   - When $T_1$ fires, it consumes 1 token from $P_1$ and 1 token from $P_2$, producing 1 item into $P_3$ and returning 1 token to $P_1$.
   - Resulting Marking: $M_1 = [1, 1, 1, 1]$.
3. **Buffer Underflow Prevention:**
   - Transition $T_2$ (Consume) cannot fire from $M_0$ because input place $P_3$ has 0 tokens! This mathematically guarantees that the consumer can never read from an empty buffer.
4. **Buffer Overflow Prevention:**
   - From $M_2 = [1, 0, 2, 1]$, transition $T_1$ cannot fire because $P_2$ has 0 tokens (buffer is full). The producer is safely blocked until the consumer frees a slot via $T_2$.
