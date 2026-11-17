"""
generate_se_cat_pdfs.py
Generates publication-quality CAT-I and CAT-II examination question papers and complete step-by-step model solutions for:
Course: 24ITPC302 - Software Engineering (Anna University / Autonomous Regulations 2024)
Covers all faculty-prescribed priority exam topics:
- CAT-I: Units 1, 2, 3 (Agile, Waterfall, XP, Spiral, V-Model, Incremental, IEEE 830 SRS, RE Process, Petri Nets, Functional/NFR, Design Pyramid, Architectural Styles, 12 Design Concepts)
- CAT-II: Units 4, 5, 6 (Basis Path Testing V(G), Black-Box BVA, Integration Testing, COCOMO I & II, Function Points, Earned Value Analysis EVA, Risk Exposure, RMMM Plan, CASE Tools Architecture & OMS Repository)
Renders via HTML5 + MathJax + CSS print styles to Microsoft Edge headless.
"""

import os
import subprocess
import time
import shutil

CSS_STYLES = """
@page {
    size: A4;
    margin: 14mm 12mm 14mm 12mm;
    @bottom-right {
        content: "Page " counter(page) " of " counter(pages);
        font-size: 8.5pt;
        color: #64748b;
    }
}

body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: #0f172a;
    line-height: 1.5;
    font-size: 9.5pt;
    margin: 0;
    padding: 0;
}

.header-container {
    text-align: center;
    border-bottom: 2.5px solid #0369a1;
    padding-bottom: 10px;
    margin-bottom: 14px;
}

.college-name {
    font-size: 14pt;
    font-weight: 800;
    color: #0369a1;
    letter-spacing: 0.5px;
    margin: 0;
    text-transform: uppercase;
}

.college-sub {
    font-size: 8.5pt;
    font-weight: 600;
    color: #475569;
    margin: 2px 0 4px 0;
}

.exam-title {
    font-size: 12pt;
    font-weight: 800;
    color: #0f172a;
    margin: 4px 0;
    background-color: #f0f9ff;
    display: inline-block;
    padding: 3px 16px;
    border-radius: 4px;
    border: 1px solid #bae6fd;
}

.meta-table {
    width: 100%;
    margin-top: 6px;
    font-size: 8.5pt;
    border-collapse: collapse;
}

.meta-table td {
    padding: 2px 6px;
    border: none;
}

.part-header {
    background: linear-gradient(90deg, #0369a1, #0284c7);
    color: white;
    font-size: 10.5pt;
    font-weight: 700;
    padding: 5px 12px;
    border-radius: 4px;
    margin-top: 18px;
    margin-bottom: 10px;
    page-break-after: avoid;
}

.question-card {
    border: 1px solid #cbd5e1;
    border-left: 4px solid #0284c7;
    border-radius: 4px;
    padding: 10px 12px;
    margin-bottom: 12px;
    background-color: #ffffff;
    page-break-inside: avoid;
}

.question-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px dashed #cbd5e1;
    padding-bottom: 4px;
    margin-bottom: 6px;
}

.q-title {
    font-weight: 700;
    font-size: 10pt;
    color: #0369a1;
}

.q-badge {
    background-color: #e0f2fe;
    color: #0369a1;
    font-size: 8pt;
    font-weight: 700;
    padding: 2px 6px;
    border-radius: 10px;
}

.q-text {
    font-style: italic;
    color: #334155;
    background-color: #f8fafc;
    border-left: 3px solid #94a3b8;
    padding: 5px 8px;
    margin: 4px 0 8px 0;
    font-size: 9pt;
}

.solution-heading {
    color: #047857;
    font-weight: 700;
    font-size: 9pt;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-top: 6px;
    margin-bottom: 3px;
}

.step-title {
    font-weight: 700;
    color: #0f172a;
    margin-top: 6px;
    margin-bottom: 2px;
    font-size: 9pt;
    text-decoration: underline;
    text-underline-offset: 2px;
}

.data-table {
    width: 100%;
    border-collapse: collapse;
    margin: 6px 0;
    font-size: 8pt;
}

.data-table th, .data-table td {
    border: 1px solid #cbd5e1;
    padding: 3px 5px;
    text-align: left;
}

.data-table th {
    background-color: #f1f5f9;
    font-weight: 700;
    color: #0369a1;
}

.answer-box {
    background-color: #f0fdf4;
    border: 1.5px solid #22c55e;
    border-radius: 4px;
    padding: 5px 8px;
    margin-top: 6px;
    font-weight: 700;
    color: #15803d;
    font-size: 9pt;
}

.or-divider {
    text-align: center;
    font-weight: 800;
    color: #dc2626;
    margin: 10px 0;
    font-size: 10.5pt;
    letter-spacing: 1.5px;
}

.code-box {
    background-color: #f8fafc;
    border: 1px solid #cbd5e1;
    border-radius: 4px;
    padding: 6px 10px;
    font-family: Consolas, monospace;
    font-size: 8pt;
    margin: 5px 0;
    line-height: 1.35;
    white-space: pre-wrap;
}

.page-break {
    page-break-before: always;
}
"""

def wrap_html(title, body):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<style>
{CSS_STYLES}
</style>
</head>
<body>
{body}
</body>
</html>
"""

# ========================================================
# CAT-I HTML CONTENT (Units 1, 2, 3)
# ========================================================
CAT1_BODY = r"""
<div class="header-container">
    <div class="college-name">Sri Sai Ram Engineering College (Autonomous)</div>
    <div class="college-sub">West Tambaram, Chennai – 600 044 | Affiliated to Anna University, Chennai</div>
    <div class="college-sub">DEPARTMENT OF INFORMATION TECHNOLOGY & COMPUTER SCIENCE — REGULATIONS 2024</div>
    <div class="exam-title">CONTINUOUS ASSESSMENT TEST – I (CAT-I) — MODEL EXAM QUESTION PAPER & SOLUTIONS</div>
    <table class="meta-table">
        <tr>
            <td><strong>Course Code & Title:</strong> 24ITPC302 – Software Engineering</td>
            <td><strong>Max Marks:</strong> 50 Marks</td>
            <td><strong>Duration:</strong> 1 ½ Hours</td>
        </tr>
        <tr>
            <td><strong>Degree & Branch:</strong> B.Tech IT / B.E. CSE (Semester III)</td>
            <td><strong>Scope:</strong> Units I, II, III (Prescribed Faculty Priority Topics)</td>
            <td><strong>Academic Year:</strong> 2026</td>
        </tr>
    </table>
</div>

<div class="part-header">PART – A (5 × 2 = 10 Marks) — Answer ALL Questions</div>

<!-- Q1 -->
<div class="question-card">
    <div class="question-header">
        <span class="q-title">Question 1</span>
        <span class="q-badge">2 Marks | K2 | Unit 1</span>
    </div>
    <div class="q-text">State the four core values of the Agile Manifesto.</div>
    <div class="solution-heading">Model Answer:</div>
    <p>The Agile Manifesto declares that we value:<br>
    1. <strong>Individuals and interactions</strong> over processes and tools.<br>
    2. <strong>Working software</strong> over comprehensive documentation.<br>
    3. <strong>Customer collaboration</strong> over contract negotiation.<br>
    4. <strong>Responding to change</strong> over following a plan.</p>
</div>

<!-- Q2 -->
<div class="question-card">
    <div class="question-header">
        <span class="q-title">Question 2</span>
        <span class="q-badge">2 Marks | K2 | Unit 1</span>
    </div>
    <div class="q-text">Differentiate between Verification and Validation in the V-Model.</div>
    <div class="solution-heading">Model Answer:</div>
    <p>• <strong>Verification (Left Wing):</strong> Static evaluation of work products (reviews, inspections) <em>without</em> code execution to answer: <em>"Are we building the product right?"</em><br>
    • <strong>Validation (Right Wing):</strong> Dynamic execution of compiled software (Unit, Integration, System, Acceptance testing) to answer: <em>"Are we building the right product?"</em></p>
</div>

<!-- Q3 -->
<div class="question-card">
    <div class="question-header">
        <span class="q-title">Question 3</span>
        <span class="q-badge">2 Marks | K2 | Unit 2</span>
    </div>
    <div class="q-text">List four essential quality characteristics of a good Software Requirements Specification (SRS) under IEEE 830.</div>
    <div class="solution-heading">Model Answer:</div>
    <p>1. <strong>Unambiguous:</strong> Exactly one interpretation exists for every requirement statement.<br>
    2. <strong>Complete:</strong> Covers all functional, performance, design constraints, and responses to invalid inputs.<br>
    3. <strong>Consistent:</strong> No internal contradictions between requirements.<br>
    4. <strong>Verifiable:</strong> A cost-effective, objective testing procedure can prove compliance.</p>
</div>

<!-- Q4 -->
<div class="question-card">
    <div class="question-header">
        <span class="q-title">Question 4</span>
        <span class="q-badge">2 Marks | K2 | Unit 2</span>
    </div>
    <div class="q-text">Define a Petri Net formally and state the transition firing rule.</div>
    <div class="solution-heading">Model Answer:</div>
    <p>A Petri Net is a 5-tuple \(\mathbf{PN = (P, T, F, W, M_0)}\) where \(P\) is Places, \(T\) is Transitions, \(F\) is Flow arcs, \(W\) is Arc weights, and \(M_0\) is Initial marking.<br>
    <strong>Firing Rule:</strong> Transition \(t\) is enabled iff \(\forall p \in I(t), M(p) \ge W(p, t)\). Upon firing, it consumes \(W(p, t)\) tokens from each input place and deposits \(W(t, p')\) tokens into each output place.</p>
</div>

<!-- Q5 -->
<div class="question-card">
    <div class="question-header">
        <span class="q-title">Question 5</span>
        <span class="q-badge">2 Marks | K2 | Unit 3</span>
    </div>
    <div class="q-text">Distinguish between Cohesion and Coupling. State the most desirable level for each.</div>
    <div class="solution-heading">Model Answer:</div>
    <p>• <strong>Cohesion:</strong> Measure of internal functional strength of elements within a module. <em>Most Desirable:</em> <strong>Functional Cohesion (Highest)</strong>.<br>
    • <strong>Coupling:</strong> Measure of interdependence between software modules. <em>Most Desirable:</em> <strong>Data Coupling / Uncoupled (Lowest)</strong>.<br>
    <em>Golden Rule:</em> <strong>Maximize Cohesion, Minimize Coupling!</strong></p>
</div>

<div class="part-header">PART – B (3 × 13 or 14 = 40 Marks) — Answer Either (a) OR (b) from each Question</div>

<!-- Q6 (Unit 1) -->
<div class="question-card">
    <div class="question-header">
        <span class="q-title">Question 6 (a)</span>
        <span class="q-badge">13 Marks | K3 | Unit 1</span>
    </div>
    <div class="q-text">
        (i) Explain Barry Boehm's Spiral Model of software development with a neat diagram. Describe activities in each of the four quadrants and explain why it is referred to as "risk-driven". [8M]<br>
        (ii) Compare and contrast the Waterfall Model with the Spiral Model across 5 project parameters. [5M]
    </div>
    <div class="solution-heading">Detailed Model Answer:</div>
    <div class="step-title">Part (i): Boehm's Spiral Model & The 4 Quadrants [8 Marks]</div>
    <p>Barry Boehm (1988) designed the Spiral Model as an evolutionary, risk-driven lifecycle model coupling prototyping with Waterfall controls.</p>
    <div class="code-box">
             QUADRANT II (Risk Assessment)     |    QUADRANT I (Objectives & Constraints)
  - Perform thorough risk analysis            |  - Identify iteration objectives
  - Build simulations, prototypes, benchmarks  |  - Establish alternative design approaches
  ---------------------------------------------+---------------------------------------------
            QUADRANT III (Development)         |    QUADRANT IV (Planning & Review)
  - Code and verify software artifacts         |  - Client evaluates deliverables
  - Unit, integration, and system tests       |  - Plan next phase / spiral turn
    </div>
    <p>• <strong>Why Risk-Driven:</strong> At every spiral cycle, effort is guided by the risk associated with that step. If Quadrant II reveals an insurmountable technical risk, development stops immediately, preventing massive financial waste.</p>
    <div class="step-title">Part (ii): Waterfall vs Spiral Comparison Matrix [5 Marks]</div>
    <table class="data-table">
        <thead><tr><th>Parameter</th><th>Classical Waterfall</th><th>Boehm's Spiral Model</th></tr></thead>
        <tbody>
            <tr><td><strong>Lifecycle Model</strong></td><td>Linear sequential, rigid forward stages.</td><td>Evolutionary, iterative spiral cycles.</td></tr>
            <tr><td><strong>Risk Management</strong></td><td>Implicit; no formal risk assessment phase.</td><td>Explicit, mandatory risk analysis in Quadrant II.</td></tr>
            <tr><td><strong>Requirement Changes</strong></td><td>Inflexible; demands frozen specs upfront.</td><td>Highly adaptive; accommodates evolving user needs.</td></tr>
            <tr><td><strong>Working Software</strong></td><td>Available very late (Construction phase).</td><td>Early prototypes delivered in early spiral turns.</td></tr>
            <tr><td><strong>Best Suited For</strong></td><td>Stable, well-understood systems (compilers).</td><td>High-risk, mission-critical enterprise systems.</td></tr>
        </tbody>
    </table>
</div>

<div class="or-divider">--- OR ---</div>

<div class="question-card">
    <div class="question-header">
        <span class="q-title">Question 6 (b)</span>
        <span class="q-badge">13 Marks | K3 | Unit 1</span>
    </div>
    <div class="q-text">
        (i) What is Extreme Programming (XP)? Describe the 4 core values and illustrate the XP development lifecycle. [7M]<br>
        (ii) Detail the mechanisms, working principles, and engineering advantages of: (1) Pair Programming, and (2) Test-Driven Development (TDD). [6M]
    </div>
    <div class="solution-heading">Detailed Model Answer:</div>
    <div class="step-title">Part (i): XP Values & Development Lifecycle [7 Marks]</div>
    <p>• <strong>4 Values:</strong> Communication (open verbal dialogue), Simplicity (build only for today's needs), Feedback (continuous testing and client reviews), Courage (fearless refactoring).<br>
    • <strong>Lifecycle:</strong> User Stories (written on index cards) \(\to\) Release Planning (commitments) \(\to\) Spike Solutions (risk prototypes) \(\to\) Iteration Planning \(\to\) TDD Unit Test \(\to\) Pair Programming \(\to\) Continuous Integration (daily builds) \(\to\) Customer Acceptance Test \(\to\) Production Release.</p>
    <div class="step-title">Part (ii): Pair Programming & Test-Driven Development [6 Marks]</div>
    <p>• <strong>Pair Programming:</strong> Two engineers work on a single workstation. The <strong>Driver</strong> controls the keyboard and implements code; the <strong>Navigator</strong> reviews logic, checks corner cases, and plans ahead. Roles switch frequently. <em>Benefits:</em> 15–20% defect reduction, continuous peer review, knowledge dissemination, zero single points of failure.<br>
    • <strong>Test-Driven Development (TDD):</strong> Developers write automated unit tests <em>before</em> writing production code (<strong>Red-Green-Refactor</strong> cycle). Code is written solely to make failing tests pass. <em>Benefits:</em> Guarantees 100% test coverage, modular decoupled code, complete confidence during refactoring.</p>
</div>

<!-- Q7 (Unit 2) -->
<div class="question-card">
    <div class="question-header">
        <span class="q-title">Question 7 (a)</span>
        <span class="q-badge">13 Marks | K3 | Unit 2</span>
    </div>
    <div class="q-text">
        (i) Outline the standard IEEE 830-1998 format for an SRS document. Detail Section 3 (Specific Requirements). [7M]<br>
        (ii) Describe the four phases of the Requirements Engineering Process and explain how the Requirements Traceability Matrix (RTM) is constructed. [6M]
    </div>
    <div class="solution-heading">Detailed Model Answer:</div>
    <div class="step-title">Part (i): IEEE 830 Standard Architecture [7 Marks]</div>
    <div class="code-box">
1. INTRODUCTION (1.1 Purpose, 1.2 Scope, 1.3 Definitions, 1.4 References, 1.5 Overview)
2. OVERALL DESCRIPTION (2.1 Product Perspective, 2.2 Functions, 2.3 User Classes, 2.4 Constraints, 2.5 Dependencies)
3. SPECIFIC REQUIREMENTS (Core Technical Section):
   3.1 External Interface Requirements: User UI, Hardware, Software OS/DB, Communications TLS/HTTP
   3.2 Functional Requirements: Inputs, Transformations, Logic, Outputs for each service
   3.3 Performance Requirements: Latency < 200ms, Throughput 5000 TPS, Concurrency
   3.4 Design Constraints: Tech stack constraints, coding standards, memory caps
   3.5 Software System Attributes: Reliability, Availability (99.99%), Security, Portability
    </div>
    <div class="step-title">Part (ii): RE Process Phases & Requirements Traceability Matrix [6 Marks]</div>
    <p>• <strong>Phases:</strong> (1) Feasibility Study (Technical, Economic CBA, Operational); (2) Requirements Elicitation & Analysis (Interviews, JAD workshops, Use cases); (3) Specification (IEEE 830 SRS); (4) Validation (Formal inspections, reviews, test generation).<br>
    • <strong>RTM:</strong> A bidirectional table linking each requirement ID to its architectural design module, code source file, and test case ID. Guarantees 100% test coverage and prevents scope creep.</p>
</div>

<div class="or-divider">--- OR ---</div>

<div class="question-card">
    <div class="question-header">
        <span class="q-title">Question 7 (b)</span>
        <span class="q-badge">13 Marks | K3 | Unit 2</span>
    </div>
    <div class="q-text">
        (i) Define a Petri Net formally as a 5-tuple. Explain the transition firing rule and how concurrency and mutual exclusion are modeled. [7M]<br>
        (ii) Construct a Petri Net for a Producer-Consumer system with a bounded buffer of size 1. Trace markings across two transitions. [6M]
    </div>
    <div class="solution-heading">Detailed Model Answer:</div>
    <div class="step-title">Part (i): Formal 5-Tuple & Concurrency Modeling [7 Marks]</div>
    <p>$$\mathbf{PN = (P, T, F, W, M_0)}$$</p>
    <p>• \(P\): Places (circles); \(T\): Transitions (bars); \(F\): Flow arcs; \(W\): Arc weights; \(M_0\): Initial marking.<br>
    • <strong>Enabling Condition:</strong> Transition \(t\) is enabled iff \(\forall p \in I(t), M(p) \ge W(p, t)\).<br>
    • <strong>Firing Rule:</strong> Consumes \(W(p, t)\) tokens from each input place; deposits \(W(t, p')\) tokens into each output place.<br>
    • <strong>Concurrency:</strong> Two transitions sharing no input places can fire independently in any order or simultaneously.</p>
    <div class="step-title">Part (ii): Producer-Consumer Synchronization Model [6 Marks]</div>
    <p>• Places: \(P_1\) (Producer Ready), \(P_2\) (Buffer Empty), \(P_3\) (Buffer Full), \(P_4\) (Consumer Ready).<br>
    • Initial Marking: \(M_0 = [P_1: 1, \ P_2: 1, \ P_3: 0, \ P_4: 1]\).<br>
    • <strong>Step 1 (\(T_1\) fires - Produce & Deposit):</strong> Consumes from \(P_1, P_2\); deposits into \(P_1, P_3 \implies M_1 = [1, 0, 1, 1]\).<br>
    • <strong>Step 2 (\(T_2\) fires - Fetch & Consume):</strong> Consumes from \(P_3, P_4\); deposits into \(P_4, P_2 \implies M_2 = [1, 1, 0, 1] = M_0\).<br>
    <div class="answer-box">✓ Proof: Mutual exclusion holds; buffer overflow and underflow are mathematically prevented.</div></p>
</div>

<!-- Q8 (Unit 3) -->
<div class="question-card">
    <div class="question-header">
        <span class="q-title">Question 8 (a)</span>
        <span class="q-badge">14 Marks | K3 | Unit 3</span>
    </div>
    <div class="q-text">
        (i) Illustrate Pressman's 4-Level Software Design Pyramid and explain how each level transforms analysis models into design artifacts. [8M]<br>
        (ii) Differentiate High-Level Design (HLD) and Low-Level Design (LLD). Explain the Fan-In vs Fan-Out heuristics. [6M]
    </div>
    <div class="solution-heading">Detailed Model Answer:</div>
    <div class="step-title">Part (i): The 4-Level Design Pyramid [8 Marks]</div>
    <div class="code-box">
             / \
            / [4] \   COMPONENT-LEVEL DESIGN (Algorithms, PDL, Decision Tables)
           /-------\
          /   [3]   \ INTERFACE DESIGN (User GUI, Internal/External APIs)
         /-----------\
        /     [2]     \ ARCHITECTURAL DESIGN (Subsystems, Connectors, Arch Styles)
       /---------------\
      /       [1]       \ DATA / CLASS DESIGN (ER Schemas, Data Structures)
    </div>
    <p>1. <strong>Data/Class Design (Base):</strong> Transforms analysis classes into DB schemas and data structures.<br>
    2. <strong>Architectural Design:</strong> Establishes system skeleton, subsystem relations, and architectural styles.<br>
    3. <strong>Interface Design:</strong> Defines interaction flow between components, external systems, and human users.<br>
    4. <strong>Component-Level Design (Apex):</strong> Converts structural elements into detailed procedural algorithms and pseudocode.</p>
    <div class="step-title">Part (ii): HLD vs LLD & Design Heuristics [6 Marks]</div>
    <p>• <strong>HLD:</strong> System architecture, subsystem boundaries, DB design. Audience: Architects, clients.<br>
    • <strong>LLD:</strong> Detailed method logic, flowcharts, pseudocode. Audience: Developers, testers.<br>
    • <strong>Fan-Out:</strong> Number of directly invoked submodules (\(3 \le \text{Fan-Out} \le 7\)). High fan-out indicates control overload.<br>
    • <strong>Fan-In:</strong> Number of calling parent modules. <strong>Maximize Fan-In</strong> for maximum reusability.</p>
</div>

<div class="or-divider">--- OR ---</div>

<div class="question-card">
    <div class="question-header">
        <span class="q-title">Question 8 (b)</span>
        <span class="q-badge">14 Marks | K3 | Unit 3</span>
    </div>
    <div class="q-text">
        (i) Explain four major Software Architectural Styles: Data-Centered, Data-Flow (Pipe-and-Filter), Layered, and Event-Driven. [8M]<br>
        (ii) State and explain any six fundamental software design concepts formulated by Pressman, highlighting Cohesion and Coupling hierarchies. [6M]
    </div>
    <div class="solution-heading">Detailed Model Answer:</div>
    <div class="step-title">Part (i): Four Architectural Styles [8 Marks]</div>
    <p>• <strong>Data-Centered (Repository):</strong> Central data store accessed by independent clients. High modularity, but central store is a bottleneck.<br>
    • <strong>Data-Flow (Pipe-and-Filter):</strong> Unidirectional data streams (Pipes) transformed by filters. Highly parallelizable, but poor for interactive UI.<br>
    • <strong>Layered (Call-and-Return):</strong> Hierarchical tiers (UI \(\to\) Business Logic \(\to\) Data Access \(\to\) Database). Loose coupling; multi-layer overhead.<br>
    • <strong>Event-Driven (Pub-Sub):</strong> Producers emit events to an Event Broker; subscribers react asynchronously. Highly scalable; hard to trace.</p>
    <div class="step-title">Part (ii): Pressman's Design Concepts & Cohesion/Coupling [6 Marks]</div>
    <p>• <strong>Key Concepts:</strong> Abstraction, Modularity, Information Hiding (Parnas), Refinement (Wirth), Refactoring, Functional Independence.<br>
    • <strong>Cohesion Hierarchy (Worst \(\to\) Best):</strong> Coincidental \(\to\) Logical \(\to\) Temporal \(\to\) Procedural \(\to\) Communicational \(\to\) Sequential \(\to\) <strong>Functional (Best)</strong>.<br>
    • <strong>Coupling Hierarchy (Worst \(\to\) Best):</strong> Content (Worst) \(\to\) Common \(\to\) Control \(\to\) Stamp \(\to\) <strong>Data (Best)</strong> \(\to\) Uncoupled.</p>
</div>
"""

# ========================================================
# CAT-II HTML CONTENT (Units 4, 5, 6)
# ========================================================
CAT2_BODY = r"""
<div class="header-container">
    <div class="college-name">Sri Sai Ram Engineering College (Autonomous)</div>
    <div class="college-sub">West Tambaram, Chennai – 600 044 | Affiliated to Anna University, Chennai</div>
    <div class="college-sub">DEPARTMENT OF INFORMATION TECHNOLOGY & COMPUTER SCIENCE — REGULATIONS 2024</div>
    <div class="exam-title">CONTINUOUS ASSESSMENT TEST – II (CAT-II) — MODEL EXAM QUESTION PAPER & SOLUTIONS</div>
    <table class="meta-table">
        <tr>
            <td><strong>Course Code & Title:</strong> 24ITPC302 – Software Engineering</td>
            <td><strong>Max Marks:</strong> 50 Marks</td>
            <td><strong>Duration:</strong> 1 ½ Hours</td>
        </tr>
        <tr>
            <td><strong>Degree & Branch:</strong> B.Tech IT / B.E. CSE (Semester III)</td>
            <td><strong>Scope:</strong> Units IV, V, VI (Prescribed Faculty Priority Topics)</td>
            <td><strong>Academic Year:</strong> 2026</td>
        </tr>
    </table>
</div>

<div class="part-header">PART – A (5 × 2 = 10 Marks) — Answer ALL Questions</div>

<!-- Q1 -->
<div class="question-card">
    <div class="question-header">
        <span class="q-title">Question 1</span>
        <span class="q-badge">2 Marks | K2 | Unit 4</span>
    </div>
    <div class="q-text">Define McCabe's Cyclomatic Complexity V(G) and state its three calculation formulas.</div>
    <div class="solution-heading">Model Answer:</div>
    <p>Cyclomatic Complexity \(V(G)\) defines the upper bound on the number of linearly independent paths through program source code.<br>
    1. <em>Edges and Nodes:</em> \(\mathbf{V(G) = E - N + 2P}\) (where \(P=1\)).<br>
    2. <em>Predicate Nodes:</em> \(\mathbf{V(G) = P' + 1}\) (where \(P'\) = decision nodes).<br>
    3. <em>Enclosed Regions:</em> \(\mathbf{V(G) = \text{Enclosed Regions} + 1}\) (outer region).</p>
</div>

<!-- Q2 -->
<div class="question-card">
    <div class="question-header">
        <span class="q-title">Question 2</span>
        <span class="q-badge">2 Marks | K2 | Unit 4</span>
    </div>
    <div class="q-text">Differentiate between Test Drivers and Test Stubs in Integration Testing.</div>
    <div class="solution-heading">Model Answer:</div>
    <p>• <strong>Test Driver:</strong> A dummy main program that invokes the module under test and passes test data. Used in <strong>Bottom-Up Integration Testing</strong>.<br>
    • <strong>Test Stub:</strong> A dummy called module that simulates the behavior of a subordinate submodule. Used in <strong>Top-Down Integration Testing</strong>.</p>
</div>

<!-- Q3 -->
<div class="question-card">
    <div class="question-header">
        <span class="q-title">Question 3</span>
        <span class="q-badge">2 Marks | K2 | Unit 5</span>
    </div>
    <div class="q-text">State the governing effort and time equations for Basic COCOMO I in Organic and Embedded modes.</div>
    <div class="solution-heading">Model Answer:</div>
    <p>• <strong>Organic Mode:</strong> \(\mathbf{E = 2.4 \cdot (KLOC)^{1.05} \text{ PM}}, \quad \mathbf{D = 2.5 \cdot (E)^{0.38} \text{ Months}}\)<br>
    • <strong>Embedded Mode:</strong> \(\mathbf{E = 3.6 \cdot (KLOC)^{1.20} \text{ PM}}, \quad \mathbf{D = 2.5 \cdot (E)^{0.32} \text{ Months}}\)</p>
</div>

<!-- Q4 -->
<div class="question-card">
    <div class="question-header">
        <span class="q-title">Question 4</span>
        <span class="q-badge">2 Marks | K2 | Unit 5</span>
    </div>
    <div class="q-text">In Earned Value Analysis (EVA), define Cost Variance (CV) and Schedule Variance (SV). How are negative values interpreted?</div>
    <div class="solution-heading">Model Answer:</div>
    <p>• <strong>Cost Variance:</strong> \(CV = EV - AC\). \(CV < 0 \implies\) <strong>Over Budget (Cost Overrun)</strong>.<br>
    • <strong>Schedule Variance:</strong> \(SV = EV - PV\). \(SV < 0 \implies\) <strong>Behind Schedule (Delayed)</strong>.</p>
</div>

<!-- Q5 -->
<div class="question-card">
    <div class="question-header">
        <span class="q-title">Question 5</span>
        <span class="q-badge">2 Marks | K2 | Unit 6</span>
    </div>
    <div class="q-text">Define Risk Exposure (RE) and state the formula for Risk Reduction Leverage (RRL).</div>
    <div class="solution-heading">Model Answer:</div>
    <p>• <strong>Risk Exposure:</strong> \(\mathbf{RE = P \times C}\) (Probability \(\times\) Impact Cost).<br>
    • <strong>Risk Reduction Leverage:</strong> \(\mathbf{RRL = \frac{RE_{\text{before}} - RE_{\text{after}}}{\text{Cost of Action}}}\). Action is justified if \(RRL > 1.0\).</p>
</div>

<div class="part-header">PART – B (3 × 13 or 14 = 40 Marks) — Answer Either (a) OR (b) from each Question</div>

<!-- Q6 (Unit 4) -->
<div class="question-card">
    <div class="question-header">
        <span class="q-title">Question 6 (a)</span>
        <span class="q-badge">13 Marks | K3 | Unit 4</span>
    </div>
    <div class="q-text">
        For the following method:<br>
        <code>int findMax(int a, int b, int c) { int max = a; if (b > max) max = b; if (c > max) max = c; return max; }</code><br>
        (i) Draw the Control Flow Graph (CFG) and determine Cyclomatic Complexity V(G) using three methods. [7M]<br>
        (ii) Derive the set of linearly independent basis paths and construct a complete test suite with input vectors and expected outputs. [6M]
    </div>
    <div class="solution-heading">Detailed Model Answer:</div>
    <div class="step-title">Part (i): CFG & 3 Independent V(G) Calculations [7 Marks]</div>
    <p>• <strong>Nodes:</strong> \(N=6\) (1: entry, 2: \(b>max\), 3: \(max=b\), 4: \(c>max\), 5: \(max=c\), 6: return).<br>
    • <strong>Edges:</strong> \(E=7\) (\(1\to 2, 2\to 3, 2\to 4, 3\to 4, 4\to 5, 4\to 6, 5\to 6\)).<br>
    1. <em>Edges/Nodes:</em> \(V(G) = E - N + 2P = 7 - 6 + 2(1) = \mathbf{3}\).<br>
    2. <em>Predicate Nodes:</em> Nodes 2 and 4 are predicates \(\implies V(G) = P' + 1 = 2 + 1 = \mathbf{3}\).<br>
    3. <em>Enclosed Regions:</em> 2 enclosed regions \(+\) 1 outer region \(= \mathbf{3}\).</p>
    <div class="step-title">Part (ii): Linearly Independent Basis Paths & Test Suite [6 Marks]</div>
    <table class="data-table">
        <thead><tr><th>Path</th><th>Node Traversal Sequence</th><th>Condition Covered</th><th>Test Input (a, b, c)</th><th>Expected Output</th></tr></thead>
        <tbody>
            <tr><td><strong>Path 1</strong></td><td>\(1 \to 2 \to 4 \to 6\)</td><td>Both IFs False</td><td>(10, 5, 2)</td><td>10</td></tr>
            <tr><td><strong>Path 2</strong></td><td>\(1 \to 2 \to 3 \to 4 \to 6\)</td><td>First IF True, Second False</td><td>(5, 10, 2)</td><td>10</td></tr>
            <tr><td><strong>Path 3</strong></td><td>\(1 \to 2 \to 4 \to 5 \to 6\)</td><td>First IF False, Second True</td><td>(5, 2, 10)</td><td>10</td></tr>
        </tbody>
    </table>
    <div class="answer-box">✓ Final Answer: V(G) = 3 | Exactly 3 test cases achieve 100% statement and branch coverage.</div>
</div>

<div class="or-divider">--- OR ---</div>

<div class="question-card">
    <div class="question-header">
        <span class="q-title">Question 6 (b)</span>
        <span class="q-badge">13 Marks | K3 | Unit 4</span>
    </div>
    <div class="q-text">
        (i) Explain Black-Box Boundary Value Analysis (BVA) and Equivalence Class Partitioning for an input range [18, 60]. [7M]<br>
        (ii) Compare Top-Down and Bottom-Up Integration Testing strategies. Explain the role of Stubs and Drivers. [6M]
    </div>
    <div class="solution-heading">Detailed Model Answer:</div>
    <div class="step-title">Part (i): BVA & Equivalence Partitioning [7 Marks]</div>
    <p>• <strong>Equivalence Classes:</strong> Valid class: \(18 \le x \le 60\); Invalid classes: \(x < 18\) and \(x > 60\).<br>
    • <strong>BVA Values:</strong> Test at boundaries \(\{a, a+1, \text{nominal}, b-1, b\}\) \(\implies \{18, 19, 35, 59, 60\}\) plus invalid boundaries \(\{17, 61\}\).</p>
    <div class="step-title">Part (ii): Top-Down vs Bottom-Up Integration [6 Marks]</div>
    <table class="data-table">
        <thead><tr><th>Feature</th><th>Top-Down Integration</th><th>Bottom-Up Integration</th></tr></thead>
        <tbody>
            <tr><td><strong>Direction</strong></td><td>From top-level control module down to leaves.</td><td>From leaf utility modules up to top control.</td></tr>
            <tr><td><strong>Harness Required</strong></td><td>Requires <strong>Test Stubs</strong> to simulate submodules.</td><td>Requires <strong>Test Drivers</strong> to call modules.</td></tr>
            <tr><td><strong>Advantages</strong></td><td>Early prototype demonstration of control logic.</td><td>Early testing of critical utility/data modules.</td></tr>
        </tbody>
    </table>
</div>

<!-- Q7 (Unit 5) -->
<div class="question-card">
    <div class="question-header">
        <span class="q-title">Question 7 (a)</span>
        <span class="q-badge">13 Marks | K3 | Unit 5</span>
    </div>
    <div class="q-text">
        A software project is estimated to be 35 KLOC. Compute Effort, Duration, Staff Size, and Productivity if developed in:<br>
        (i) Organic Mode, and (ii) Embedded Mode under Barry Boehm's Basic COCOMO I model. [13M]
    </div>
    <div class="solution-heading">Detailed Model Answer:</div>
    <div class="step-title">Step 1: Governing Formulas</div>
    <p>\[ \mathbf{E = a \cdot (KLOC)^b \text{ [PM]}}, \qquad \mathbf{D = c \cdot (E)^d \text{ [Months]}}, \qquad \mathbf{P = \frac{E}{D} \text{ [Staff]}} \]</p>
    <div class="step-title">Step 2: Organic Mode Calculations (\(a=2.4, b=1.05, c=2.5, d=0.38\))</div>
    <p>• <strong>Effort:</strong> \(E = 2.4 \times (35)^{1.05} = 2.4 \times 41.761 = \mathbf{100.23 \text{ Person-Months}}\)<br>
    • <strong>Duration:</strong> \(D = 2.5 \times (100.23)^{0.38} = 2.5 \times 5.764 = \mathbf{14.41 \text{ Months}}\)<br>
    • <strong>Staff Size:</strong> \(P = 100.23 / 14.41 = \mathbf{6.96 \approx 7 \text{ Persons}}\)<br>
    • <strong>Productivity:</strong> \(35,000 / 100.23 = \mathbf{349.2 \text{ LOC/PM}}\)</p>
    <div class="step-title">Step 3: Embedded Mode Calculations (\(a=3.6, b=1.20, c=2.5, d=0.32\))</div>
    <p>• <strong>Effort:</strong> \(E = 3.6 \times (35)^{1.20} = 3.6 \times 71.026 = \mathbf{255.69 \text{ Person-Months}}\)<br>
    • <strong>Duration:</strong> \(D = 2.5 \times (255.69)^{0.32} = 2.5 \times 5.922 = \mathbf{14.81 \text{ Months}}\)<br>
    • <strong>Staff Size:</strong> \(P = 255.69 / 14.81 = \mathbf{17.26 \approx 18 \text{ Persons}}\)<br>
    • <strong>Productivity:</strong> \(35,000 / 255.69 = \mathbf{136.9 \text{ LOC/PM}}\)</p>
    <div class="answer-box">✓ Final Answer: Organic: 100.2 PM (7 Persons, 14.4 Mos) | Embedded: 255.7 PM (18 Persons, 14.8 Mos)</div>
</div>

<div class="or-divider">--- OR ---</div>

<div class="question-card">
    <div class="question-header">
        <span class="q-title">Question 7 (b)</span>
        <span class="q-badge">13 Marks | K3 | Unit 5</span>
    </div>
    <div class="q-text">
        (i) Explain Albrecht's Function Point (FP) Model. Detail the 5 information domain characteristics and the 14 complexity adjustment factors. [7M]<br>
        (ii) A system has UFC = 369. All 14 complexity factors are rated 3. Compute VAF, FP, and estimated Java size (53 LOC/FP). [6M]
    </div>
    <div class="solution-heading">Detailed Model Answer:</div>
    <div class="step-title">Part (i): FP Theory & Formula [7 Marks]</div>
    <p>\[ \mathbf{FP = UFC \times VAF = UFC \times \left(0.65 + 0.01 \sum_{i=1}^{14} F_i\right)} \]</p>
    <p>• <strong>5 Domain Characteristics:</strong> External Inputs (EI), External Outputs (EO), External Inquiries (EQ), Internal Logical Files (ILF), External Interface Files (EIF).<br>
    • <strong>14 Factors:</strong> Data communications, distributed processing, performance, transaction rate, online data entry, end-user efficiency, online update, complex processing, reusability, installation ease, operational ease, multiple sites, facilitate change.</p>
    <div class="step-title">Part (ii): Worked Numerical Solution [6 Marks]</div>
    <p>• \(\sum F_i = 14 \times 3 = 42 \implies VAF = 0.65 + 0.01(42) = \mathbf{1.07}\)<br>
    • \(FP = 369 \times 1.07 = \mathbf{394.83 \text{ Function Points}}\)<br>
    • Java Size: \(394.83 \times 53 = \mathbf{20,926 \text{ LOC} \ (20.93 \text{ KLOC})}\).</p>
    <div class="answer-box">✓ Final Answer: VAF = 1.07 | FP = 394.83 | Java Code Size = 20.93 KLOC</div>
</div>

<!-- Q8 (Unit 5 & 6) -->
<div class="question-card">
    <div class="question-header">
        <span class="q-title">Question 8 (a)</span>
        <span class="q-badge">14 Marks | K3 | Unit 5</span>
    </div>
    <div class="q-text">
        A project has BAC = $150,000, 10 months duration. At Month 5, records reveal:<br>
        PV = $75,000, EV = $60,000, AC = $70,000.<br>
        Calculate CV, SV, CPI, SPI, EAC, and ETC. Audit project health and recommend management action. [14M]
    </div>
    <div class="solution-heading">Detailed Model Answer:</div>
    <div class="step-title">Step 1: Variances & Performance Indices</div>
    <p>• <strong>Cost Variance:</strong> \(CV = EV - AC = 60,000 - 70,000 = \mathbf{-\$10,000}\) (\(CV < 0 \implies\) <strong>Over Budget by $10,000</strong>).<br>
    • <strong>Schedule Variance:</strong> \(SV = EV - PV = 60,000 - 75,000 = \mathbf{-\$15,000}\) (\(SV < 0 \implies\) <strong>Behind Schedule by $15,000</strong>).<br>
    • <strong>Cost Performance Index:</strong> \(CPI = \frac{EV}{AC} = \frac{60,000}{70,000} = \mathbf{0.857}\) (Only $0.86 value earned per $1 spent).<br>
    • <strong>Schedule Performance Index:</strong> \(SPI = \frac{EV}{PV} = \frac{60,000}{75,000} = \mathbf{0.800}\) (Progressing at only 80% planned velocity).</p>
    <div class="step-title">Step 2: Forecasting Total Cost & Completion</div>
    <p>• <strong>Estimate at Completion:</strong> \(EAC = \frac{BAC}{CPI} = \frac{150,000}{0.8571} = \mathbf{\$175,000}\) (Projected cost overrun: $25,000).<br>
    • <strong>Estimate to Complete:</strong> \(ETC = EAC - AC = 175,000 - 70,000 = \mathbf{\$105,000}\).</p>
    <div class="step-title">Step 3: Management Health Audit & Action</div>
    <p>Project is in <strong>Critical Condition</strong> (both cost overrun and schedule slippage). Management must: (1) Freeze scope additions; (2) Reassign senior staff to critical path activities; (3) Negotiate revised timeline with client.</p>
    <div class="answer-box">✓ Final Answer: CV = -$10k | SV = -$15k | CPI = 0.857 | SPI = 0.800 | EAC = $175,000 | ETC = $105,000</div>
</div>

<div class="or-divider">--- OR ---</div>

<div class="question-card">
    <div class="question-header">
        <span class="q-title">Question 8 (b)</span>
        <span class="q-badge">14 Marks | K3 | Unit 6</span>
    </div>
    <div class="q-text">
        (i) What is an RMMM Plan? Construct a complete RMMM table for the scenario: "Key Senior Developers Quit during Construction". [7M]<br>
        (ii) Illustrate the architecture of an integrated CASE environment, detailing the central role of the Object Management System (OMS) repository. [7M]
    </div>
    <div class="solution-heading">Detailed Model Answer:</div>
    <div class="step-title">Part (i): RMMM Plan & Operational Table [7 Marks]</div>
    <table class="data-table">
        <thead><tr><th>RMMM Pillar</th><th>Operational Procedures & Action Items</th></tr></thead>
        <tbody>
            <tr><td><strong>Mitigation</strong></td><td>Enforce Pair Programming so knowledge is distributed; mandate detailed documentation; retention bonuses.</td></tr>
            <tr><td><strong>Monitoring</strong></td><td>Track overtime hours (> 50 hrs/wk = burnout trigger); conduct monthly 1-on-1s; monitor commit frequency.</td></tr>
            <tr><td><strong>Management</strong></td><td>Promote junior pair partner immediately; activate contract on-demand staffing; de-scope non-critical features.</td></tr>
        </tbody>
    </table>
    <div class="step-title">Part (ii): CASE Architecture & The OMS Central Repository [7 Marks]</div>
    <div class="code-box">
[ User Interface Layer (GUI / IDE) ]
           |
[ Tool Integration Services: Data, Control, Presentation ]
           |
[ Upper CASE: DFD/UML ]  <--->  [ Lower CASE: Compilers/Tests ]  <--->  [ Management: Jira/Gantt ]
           \                           |                           /
            +--------------------------+--------------------------+
                                       |
          [ OBJECT MANAGEMENT SYSTEM (OMS) CENTRAL REPOSITORY ]
          (Metadata, Version History, RTM Traceability, Shared Schema)
    </div>
    <p>• <strong>OMS Role:</strong> Centralized relational database storing all project artifacts (requirements, models, code, tests). Ensures data consistency, prevents tool conflicts, and powers automated bidirectional traceability.</p>
</div>
"""

def generate_pdf(html_content, output_html_path, output_pdf_path, root_pdf_path):
    print(f"Writing {output_html_path}...")
    with open(output_html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    edge_exe = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    print(f"Generating PDF via Edge headless: {output_pdf_path}...")
    cmd = [
        edge_exe,
        "--headless=new",
        "--disable-gpu",
        "--virtual-time-budget=6000",
        f"--print-to-pdf={output_pdf_path}",
        "--no-pdf-header-footer",
        output_html_path
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=90)
    time.sleep(2)
    if os.path.exists(output_pdf_path):
        size = os.path.getsize(output_pdf_path)
        print(f"PDF created: {output_pdf_path} ({size} bytes)")
        shutil.copyfile(output_pdf_path, root_pdf_path)
        print(f"Copied to root: {root_pdf_path}")
        return True
    else:
        print("PDF generation failed:", res.stderr)
        return False

def main():
    base_dir = r"C:\Users\siva2\OneDrive\Desktop\soft"
    qp_dir = os.path.join(base_dir, "question_papers")
    os.makedirs(qp_dir, exist_ok=True)

    # 1. CAT-I
    cat1_html = wrap_html("24ITPC302 CAT-I Model Exam Solutions", CAT1_BODY)
    cat1_html_path = os.path.join(qp_dir, "CAT_1_2026_SE_SOLUTIONS.html")
    cat1_pdf_path = os.path.join(qp_dir, "CAT_1_2026_SE_SOLUTIONS.pdf")
    cat1_root_pdf = os.path.join(base_dir, "CAT_1_2026_SE_SOLUTIONS.pdf")
    generate_pdf(cat1_html, cat1_html_path, cat1_pdf_path, cat1_root_pdf)

    # 2. CAT-II
    cat2_html = wrap_html("24ITPC302 CAT-II Model Exam Solutions", CAT2_BODY)
    cat2_html_path = os.path.join(qp_dir, "CAT_2_2026_SE_SOLUTIONS.html")
    cat2_pdf_path = os.path.join(qp_dir, "CAT_2_2026_SE_SOLUTIONS.pdf")
    cat2_root_pdf = os.path.join(base_dir, "CAT_2_2026_SE_SOLUTIONS.pdf")
    generate_pdf(cat2_html, cat2_html_path, cat2_pdf_path, cat2_root_pdf)

if __name__ == "__main__":
    main()
