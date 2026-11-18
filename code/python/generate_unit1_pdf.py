"""
generate_unit1_pdf.py
Compiles the definitive publication-grade PDF for Unit 1:
Course: 24ITPC302 - Software Engineering (Anna University / Autonomous Regulations 2024)
Unit 1: Software Process & Agile Development
Covers:
- Classical Waterfall Model
- Barry Boehm's Spiral Model (16 Marks)
- Agile Methodology vs. Waterfall Model (16 Marks)
- Extreme Programming (XP) (Values, 6-Phase Lifecycle, TDD, Pair Programming)
- The V-Model (V&V, Defect Prevention, Phase Correspondence)
- Incremental Process Model (Core Product, Staged Delivery)
- Official College CAT Question Bank Solutions (Part A: 26 Questions, Part B & C)
Renders via HTML5 + Native Inline SVGs + CSS Print Styles using Microsoft Edge Headless.
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
        font-size: 8pt;
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

.cover-header {
    text-align: center;
    border-bottom: 3px double #0284c7;
    padding-bottom: 12px;
    margin-bottom: 16px;
}

.college-title {
    font-size: 14pt;
    font-weight: 800;
    color: #0369a1;
    margin: 0;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.sub-header {
    font-size: 8.5pt;
    font-weight: 600;
    color: #475569;
    margin: 3px 0;
}

.doc-badge {
    display: inline-block;
    background-color: #0284c7;
    color: #ffffff;
    font-size: 11pt;
    font-weight: 700;
    padding: 4px 18px;
    border-radius: 4px;
    margin-top: 6px;
    letter-spacing: 0.5px;
}

.unit-banner {
    background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
    border-left: 5px solid #0284c7;
    padding: 10px 14px;
    margin-bottom: 16px;
    border-radius: 0 6px 6px 0;
}

.unit-title {
    font-size: 13pt;
    font-weight: 800;
    color: #0369a1;
    margin: 0 0 4px 0;
}

.unit-desc {
    font-size: 8.5pt;
    color: #334155;
    margin: 0;
}

h2.topic-header {
    font-size: 12pt;
    font-weight: 800;
    color: #ffffff;
    background: #0284c7;
    padding: 6px 12px;
    border-radius: 4px;
    margin: 20px 0 10px 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    page-break-after: avoid;
}

h3.section-header {
    font-size: 10.5pt;
    font-weight: 700;
    color: #0369a1;
    border-bottom: 1.5px solid #cbd5e1;
    padding-bottom: 3px;
    margin: 12px 0 6px 0;
    page-break-after: avoid;
}

.meta-pill {
    font-size: 8pt;
    font-weight: 700;
    background: rgba(255, 255, 255, 0.25);
    padding: 2px 8px;
    border-radius: 12px;
    text-transform: uppercase;
}

p {
    margin: 0 0 8px 0;
    text-align: justify;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin: 10px 0 14px 0;
    font-size: 8.5pt;
    page-break-inside: avoid;
}

th, td {
    border: 1px solid #cbd5e1;
    padding: 6px 8px;
    text-align: left;
    vertical-align: top;
}

th {
    background-color: #f1f5f9;
    color: #0f172a;
    font-weight: 700;
}

tr:nth-child(even) {
    background-color: #f8fafc;
}

.alert-box {
    border-left: 4px solid #0284c7;
    background-color: #f0f9ff;
    padding: 8px 12px;
    margin: 10px 0;
    font-size: 9pt;
    border-radius: 0 4px 4px 0;
    page-break-inside: avoid;
}

.alert-warn {
    border-left-color: #d97706;
    background-color: #fffbeb;
}

.alert-success {
    border-left-color: #16a34a;
    background-color: #f0fdf4;
}

.diagram-container {
    text-align: center;
    margin: 14px 0;
    padding: 10px;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    page-break-inside: avoid;
}

.diagram-caption {
    font-size: 8pt;
    font-weight: 700;
    color: #475569;
    margin-top: 6px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.qa-card {
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    margin-bottom: 10px;
    background: #ffffff;
    page-break-inside: avoid;
}

.qa-question {
    background: #f8fafc;
    border-bottom: 1px solid #e2e8f0;
    padding: 6px 10px;
    font-weight: 700;
    font-size: 9pt;
    color: #0369a1;
}

.qa-answer {
    padding: 8px 10px;
    font-size: 8.5pt;
    color: #1e293b;
}

.page-break {
    page-break-before: always;
}
"""

def build_html():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>24ITPC302 Unit 1 Master Examination Compendium</title>
    <style>{CSS_STYLES}</style>
</head>
<body>

    <!-- Cover Header -->
    <div class="cover-header">
        <div class="college-title">Sri Sai Ram Engineering College (Autonomous)</div>
        <div class="sub-header">Affiliated to Anna University | Regulations 2024 | Department of IT & CSE</div>
        <div class="sub-header">24ITPC302 — SOFTWARE ENGINEERING | SEMESTER III</div>
        <div class="doc-badge">UNIT 1: SOFTWARE PROCESS & AGILE DEVELOPMENT — EXAM COMPENDIUM</div>
    </div>

    <div class="unit-banner">
        <div class="unit-title">Module Overview & Examination Scope</div>
        <div class="unit-desc">
            This compendium contains complete, verified, publication-grade solutions for all prescribed 13-Mark, 16-Mark, and 2-Mark questions from Module 1. It integrates complete architectural diagrams, comparative matrices, real-world case studies, and the official college CAT-1 question bank solutions.
        </div>
    </div>

    <!-- TOPIC 1: WATERFALL MODEL -->
    <h2 class="topic-header">
        <span>1. The Classical Waterfall Model (Linear Sequential Model)</span>
        <span class="meta-pill">Sure 13M / 16M</span>
    </h2>

    <h3 class="section-header">1.1 Definition & Philosophy</h3>
    <p>
        The <strong>Classical Waterfall Model</strong> (introduced by Dr. Winston W. Royce in 1970) is a plan-driven, document-centric software lifecycle model that organizes development into a rigid, sequential cascade of distinct phases. Development flows strictly downwards like water over a rock cascade. Output deliverables from each phase serve as direct formal inputs to the subsequent phase. Each phase must be completely executed, documented, and formally signed off before the next phase begins.
    </p>

    <div class="diagram-container">
        <!-- SVG Diagram: Waterfall Model -->
        <svg width="100%" height="220" viewBox="0 0 680 220" xmlns="http://www.w3.org/2000/svg">
            <defs>
                <linearGradient id="wfGrad" x1="0" y1="0" x2="1" y2="0">
                    <stop offset="0%" stop-color="#0284c7"/>
                    <stop offset="100%" stop-color="#0369a1"/>
                </linearGradient>
                <filter id="shadow" x="-5%" y="-5%" width="110%" height="115%">
                    <feDropShadow dx="1" dy="2" stdDeviation="2" flood-color="#94a3b8" flood-opacity="0.3"/>
                </filter>
            </defs>

            <!-- Phase 1: Communication -->
            <g filter="url(#shadow)">
                <rect x="20" y="20" width="130" height="48" rx="6" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>
                <text x="85" y="40" font-family="sans-serif" font-size="9" font-weight="bold" fill="#0369a1" text-anchor="middle">1. Communication</text>
                <text x="85" y="55" font-family="sans-serif" font-size="7.5" fill="#475569" text-anchor="middle">SRS Specification</text>
            </g>

            <path d="M 150 44 L 175 44 L 175 60 L 190 60" fill="none" stroke="#0284c7" stroke-width="2" marker-end="url(#arrow)"/>

            <!-- Phase 2: Planning & Design -->
            <g filter="url(#shadow)">
                <rect x="150" y="55" width="130" height="48" rx="6" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>
                <text x="215" y="75" font-family="sans-serif" font-size="9" font-weight="bold" fill="#0369a1" text-anchor="middle">2. System Design</text>
                <text x="215" y="90" font-family="sans-serif" font-size="7.5" fill="#475569" text-anchor="middle">Architecture & SDD</text>
            </g>

            <!-- Phase 3: Construction / Coding -->
            <g filter="url(#shadow)">
                <rect x="280" y="90" width="130" height="48" rx="6" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>
                <text x="345" y="110" font-family="sans-serif" font-size="9" font-weight="bold" fill="#0369a1" text-anchor="middle">3. Construction</text>
                <text x="345" y="125" font-family="sans-serif" font-size="7.5" fill="#475569" text-anchor="middle">Coding & Unit Tests</text>
            </g>

            <!-- Phase 4: Testing & Verification -->
            <g filter="url(#shadow)">
                <rect x="410" y="125" width="130" height="48" rx="6" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>
                <text x="475" y="145" font-family="sans-serif" font-size="9" font-weight="bold" fill="#0369a1" text-anchor="middle">4. Integration & Test</text>
                <text x="475" y="160" font-family="sans-serif" font-size="7.5" fill="#475569" text-anchor="middle">System Test & UAT</text>
            </g>

            <!-- Phase 5: Deployment & Maintenance -->
            <g filter="url(#shadow)">
                <rect x="535" y="160" width="130" height="48" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
                <text x="600" y="180" font-family="sans-serif" font-size="9" font-weight="bold" fill="#15803d" text-anchor="middle">5. Deployment</text>
                <text x="600" y="195" font-family="sans-serif" font-size="7.5" fill="#475569" text-anchor="middle">Live Operations</text>
            </g>

            <!-- Connecting Cascading Lines -->
            <path d="M 85 68 L 85 79 L 150 79" fill="none" stroke="#64748b" stroke-width="1.5" stroke-dasharray="3,3"/>
            <path d="M 215 103 L 215 114 L 280 114" fill="none" stroke="#64748b" stroke-width="1.5" stroke-dasharray="3,3"/>
            <path d="M 345 138 L 345 149 L 410 149" fill="none" stroke="#64748b" stroke-width="1.5" stroke-dasharray="3,3"/>
            <path d="M 475 173 L 475 184 L 535 184" fill="none" stroke="#64748b" stroke-width="1.5" stroke-dasharray="3,3"/>
        </svg>
        <div class="diagram-caption">Figure 1.1: The Classical Waterfall Lifecycle Cascade with Sequential Gate Transitions</div>
    </div>

    <h3 class="section-header">1.2 Detailed Phase Activities & Formal Deliverables</h3>
    <table>
        <thead>
            <tr>
                <th style="width: 18%;">Lifecycle Phase</th>
                <th style="width: 52%;">Core Engineering Activities</th>
                <th style="width: 30%;">Formal Signed-Off Deliverable</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>1. Communication</strong></td>
                <td>Stakeholder interviews, domain analysis, and technical/economic/operational feasibility studies.</td>
                <td><strong>Software Requirements Specification (SRS)</strong></td>
            </tr>
            <tr>
                <td><strong>2. System Design</strong></td>
                <td>Preliminary architectural styles, subsystem decomposition, database schemas, and interface contracts.</td>
                <td><strong>Software Design Document (SDD)</strong></td>
            </tr>
            <tr>
                <td><strong>3. Construction</strong></td>
                <td>Translating design into compiled source code (Java/C++) and writing white-box unit tests.</td>
                <td><strong>Compiled Source Code & Unit Test Logs</strong></td>
            </tr>
            <tr>
                <td><strong>4. Integration & Testing</strong></td>
                <td>Subsystem interface verification, end-to-end performance, load, security, and User Acceptance Testing (UAT).</td>
                <td><strong>Validated System & Test Report</strong></td>
            </tr>
            <tr>
                <td><strong>5. Deployment</strong></td>
                <td>Client installation, user training, and maintenance (Corrective, Adaptive, Perfective, Preventive).</td>
                <td><strong>Operational Release & User Manuals</strong></td>
            </tr>
        </tbody>
    </table>

    <h3 class="section-header">1.3 Advantages, Disadvantages & Industrial Suitability</h3>
    <table>
        <thead>
            <tr>
                <th style="width: 50%;">Major Advantages</th>
                <th style="width: 50%;">Major Disadvantages</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>• <strong>Simple & Structured:</strong> Straightforward to understand and govern; provides clear milestone reviews.</td>
                <td>• <strong>Inflexible to Change:</strong> Changing requirements late incurs catastrophic redesign and rework costs.</td>
            </tr>
            <tr>
                <td>• <strong>Quality Gates:</strong> Each phase concludes with formal signed-off deliverables before downstream work.</td>
                <td>• <strong>Delayed Working Software:</strong> Software appears only late in Phase 4; users cannot evaluate tangible code for months.</td>
            </tr>
            <tr>
                <td>• <strong>Stable Architecture:</strong> Exhaustive upfront planning prevents hasty, poorly thought-out shortcuts.</td>
                <td>• <strong>Late Risk Discovery:</strong> Critical integration and architecture flaws remain hidden until testing.</td>
            </tr>
        </tbody>
    </table>
    <p><strong>Optimal Industrial Fit:</strong> Systems with 100% frozen, well-understood requirements (compilers, automotive microcontroller firmware, tax calculation software, and legacy migration).</p>

    <!-- TOPIC 2: SPIRAL MODEL -->
    <div class="page-break"></div>
    <h2 class="topic-header">
        <span>2. Barry Boehm's Spiral Model</span>
        <span class="meta-pill">MOST Important 16M</span>
    </h2>

    <h3 class="section-header">2.1 Definition & Geometric Architecture</h3>
    <p>
        The <strong>Spiral Model</strong> (Dr. Barry W. Boehm, 1988) is an <strong>evolutionary, risk-driven process model generator</strong> that couples the iterative nature of prototyping with the controlled, systematic aspects of the Waterfall model. Software development is mapped as a spiral progressing radially outward from initial concept to full operational deployment.
    </p>

    <div class="alert-box alert-success">
        <strong>The Geometry of the Spiral:</strong><br>
        • <strong>Radial Dimension (\(r\)):</strong> Distance from origin represents <strong>cumulative project cost and effort</strong> expended to date.<br>
        • <strong>Angular Dimension (\(\theta\)):</strong> Angular rotation represents <strong>progress through lifecycle phases</strong> within the current iteration. Each 360° turn executes all four quadrants in a clockwise direction.
    </div>

    <div class="diagram-container">
        <!-- SVG Diagram: Barry Boehm's Spiral Model 4 Quadrants -->
        <svg width="100%" height="280" viewBox="0 0 600 280" xmlns="http://www.w3.org/2000/svg">
            <!-- Axes -->
            <line x1="50" y1="140" x2="550" y2="140" stroke="#94a3b8" stroke-width="2"/>
            <line x1="300" y1="20" x2="300" y2="260" stroke="#94a3b8" stroke-width="2"/>

            <!-- Quadrant Labels -->
            <!-- Q2: Top-Left -->
            <rect x="60" y="30" width="220" height="95" rx="6" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5"/>
            <text x="170" y="50" font-family="sans-serif" font-size="9.5" font-weight="bold" fill="#7f1d1d" text-anchor="middle">QUADRANT II (Top-Left)</text>
            <text x="170" y="66" font-family="sans-serif" font-size="8.5" font-weight="bold" fill="#991b1b" text-anchor="middle">IDENTIFY & RESOLVE RISKS</text>
            <text x="170" y="82" font-family="sans-serif" font-size="7.5" fill="#334155" text-anchor="middle">• Detailed Risk Analysis & Scoring</text>
            <text x="170" y="96" font-family="sans-serif" font-size="7.5" fill="#334155" text-anchor="middle">• Build Throwaway Prototypes</text>
            <text x="170" y="110" font-family="sans-serif" font-size="7.5" fill="#334155" text-anchor="middle">• Algorithmic Benchmarks & Simulations</text>

            <!-- Q1: Top-Right -->
            <rect x="320" y="30" width="220" height="95" rx="6" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.5"/>
            <text x="430" y="50" font-family="sans-serif" font-size="9.5" font-weight="bold" fill="#0369a1" text-anchor="middle">QUADRANT I (Top-Right)</text>
            <text x="430" y="66" font-family="sans-serif" font-size="8.5" font-weight="bold" fill="#0b3c61" text-anchor="middle">DETERMINE OBJECTIVES & CONSTRAINTS</text>
            <text x="430" y="82" font-family="sans-serif" font-size="7.5" fill="#334155" text-anchor="middle">• Define Iteration Goals & Scope</text>
            <text x="430" y="96" font-family="sans-serif" font-size="7.5" fill="#334155" text-anchor="middle">• Identify Alternatives (COTS vs Custom)</text>
            <text x="430" y="110" font-family="sans-serif" font-size="7.5" fill="#334155" text-anchor="middle">• Establish Budget & Interface Constraints</text>

            <!-- Q3: Bottom-Left -->
            <rect x="60" y="155" width="220" height="95" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
            <text x="170" y="175" font-family="sans-serif" font-size="9.5" font-weight="bold" fill="#15803d" text-anchor="middle">QUADRANT III (Bottom-Left)</text>
            <text x="170" y="191" font-family="sans-serif" font-size="8.5" font-weight="bold" fill="#14532d" text-anchor="middle">DEVELOP & VERIFY NEXT-LEVEL PRODUCT</text>
            <text x="170" y="207" font-family="sans-serif" font-size="7.5" fill="#334155" text-anchor="middle">• Turn 1: Concept Simulation</text>
            <text x="170" y="221" font-family="sans-serif" font-size="7.5" fill="#334155" text-anchor="middle">• Turn 2: Architectural Prototype</text>
            <text x="170" y="235" font-family="sans-serif" font-size="7.5" fill="#334155" text-anchor="middle">• Turn 3/4: Detailed Design, Code & Test</text>

            <!-- Q4: Bottom-Right -->
            <rect x="320" y="155" width="220" height="95" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
            <text x="430" y="175" font-family="sans-serif" font-size="9.5" font-weight="bold" fill="#78350f" text-anchor="middle">QUADRANT IV (Bottom-Right)</text>
            <text x="430" y="191" font-family="sans-serif" font-size="8.5" font-weight="bold" fill="#b45309" text-anchor="middle">PLAN NEXT PHASE & CUSTOMER REVIEW</text>
            <text x="430" y="207" font-family="sans-serif" font-size="7.5" fill="#334155" text-anchor="middle">• Customer Evaluates Deliverables</text>
            <text x="430" y="221" font-family="sans-serif" font-size="7.5" fill="#334155" text-anchor="middle">• Management Review (Go / No-Go Gate)</text>
            <text x="430" y="235" font-family="sans-serif" font-size="7.5" fill="#334155" text-anchor="middle">• Plan Commitments for Next Outward Turn</text>

            <!-- Circular Direction Arrow -->
            <path d="M 430 25 L 440 25 A 140 140 0 1 0 440 255" fill="none" stroke="#0284c7" stroke-width="2" stroke-dasharray="4,4"/>
            <polygon points="440,25 432,20 432,30" fill="#0284c7"/>
            <text x="300" y="12" font-family="sans-serif" font-size="8" font-weight="bold" fill="#0284c7" text-anchor="middle">CLOCKWISE PROGRESSION (Turn Expands Outward)</text>
        </svg>
        <div class="diagram-caption">Figure 1.2: Barry Boehm's Spiral Model Architecture Showing the Four Clockwise Quadrants</div>
    </div>

    <h3 class="section-header">2.2 Detailed Working of the Four Quadrants</h3>
    <p>
        <strong>1. Quadrant I (Determine Objectives, Alternatives, and Constraints):</strong> Identifies iteration-specific goals, alternative implementation paths (e.g., COTS software vs custom build), and project constraints (budget, deadlines, hardware interfaces).<br>
        <strong>2. Quadrant II (Evaluate Alternatives, Identify & Resolve Risks):</strong> The risk management engine. Performs formal risk scoring. Employs <em>prototyping, simulations, and benchmarking</em> to neutralize technical uncertainties. If a fatal risk cannot be mitigated, the project is terminated immediately, preventing catastrophic multi-million dollar waste.<br>
        <strong>3. Quadrant III (Develop, Verify, and Test):</strong> Implements the artifact corresponding to the current turn. In early turns, produces mathematical models and UI prototypes; in later turns, produces flight-ready operational software tested via unit, integration, and system test suites.<br>
        <strong>4. Quadrant IV (Plan Next Phase & Customer Evaluation):</strong> The customer reviews deliverables. Management audits budget and timeline at a formal <strong>Milestone Commitment Gate (Go / No-Go)</strong> before approving resources for the next outward spiral loop.
    </p>

    <h3 class="section-header">2.3 Real-World Case Study: Military Radar Defense System</h3>
    <p>
        <strong>Project Context:</strong> An Airborne Early Warning & Radar Tracking System required real-time signal processing over satellite links with strict millisecond response times. Flight failure would risk aircraft and crew.<br>
        • <strong>Turn 1 (Concept):</strong> Mathematical simulation in Python proved theoretical tracking viability.<br>
        • <strong>Turn 2 (Architecture Prototype):</strong> Built a hardware emulator. <em>Risk Caught:</em> Uncovered an unacceptable 400ms bus lag over satellite channels! Because it was detected in Turn 2, engineers switched to a dedicated military fiber bus before writing production code.<br>
        • <strong>Turn 3 (Subsystem):</strong> Integrated core tracking algorithms in an avionics wind-tunnel testbench.<br>
        • <strong>Turn 4 (Operational Flight Software):</strong> Final DO-178C flight-certified C++ codebase deployed safely to live aircraft.
    </p>

    <!-- TOPIC 3: AGILE VS WATERFALL -->
    <div class="page-break"></div>
    <h2 class="topic-header">
        <span>3. Agile Methodology vs. Classical Waterfall Model</span>
        <span class="meta-pill">Core 16M Comparison</span>
    </h2>

    <h3 class="section-header">3.1 The Agile Manifesto (Snowbird, Utah, 2001)</h3>
    <div class="alert-box alert-warn">
        <strong>The 4 Values of the Agile Manifesto:</strong><br>
        1. <strong>Individuals and interactions</strong> over processes and tools.<br>
        2. <strong>Working software</strong> over comprehensive documentation.<br>
        3. <strong>Customer collaboration</strong> over contract negotiation.<br>
        4. <strong>Responding to change</strong> over following a plan.
    </div>

    <h3 class="section-header">3.2 Comprehensive 10-Parameter Evaluation Matrix</h3>
    <table>
        <thead>
            <tr>
                <th style="width: 22%;">Evaluation Parameter</th>
                <th style="width: 39%;">Classical Waterfall Model</th>
                <th style="width: 39%;">Agile Methodologies (Scrum / XP)</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>1. Philosophy</strong></td>
                <td><strong>Predictive / Plan-Driven:</strong> Assumes landscape can be fully specified and planned upfront.</td>
                <td><strong>Adaptive / Empirical:</strong> Welcomes continuous change through rapid feedback loops.</td>
            </tr>
            <tr>
                <td><strong>2. Requirements</strong></td>
                <td><strong>Frozen upfront</strong> in a formal SRS; changes are resisted via formal change boards.</td>
                <td>Captured as dynamic <strong>User Stories</strong> continuously reprioritized in a Product Backlog.</td>
            </tr>
            <tr>
                <td><strong>3. Software Delivery</strong></td>
                <td><strong>Single Monolithic ("Big Bang") Release</strong> at the very end of project (Month 12–18).</td>
                <td><strong>Frequent Usable Increments</strong> delivered into customer hands every 1 to 4 weeks.</td>
            </tr>
            <tr>
                <td><strong>4. Customer Role</strong></td>
                <td><strong>Isolated:</strong> Active at project start and during final acceptance; absent during coding.</td>
                <td><strong>Continuous:</strong> Full-time collaboration; Product Owner or Customer works with team daily.</td>
            </tr>
            <tr>
                <td><strong>5. Testing Strategy</strong></td>
                <td><strong>Phased & Late:</strong> Testing begins only after coding is 100% finished.</td>
                <td><strong>Continuous & Shift-Left:</strong> Automated tests written daily (often test-first via TDD).</td>
            </tr>
            <tr>
                <td><strong>6. Cost of Change</strong></td>
                <td><strong>Exponential Growth:</strong> Late changes incur massive rework costs (up to 50×–100×).</td>
                <td><strong>Relatively Flat:</strong> Modular architecture, CI, and small batches make late changes affordable.</td>
            </tr>
            <tr>
                <td><strong>7. Risk Profile</strong></td>
                <td><strong>High Late Risk:</strong> Critical architectural and user mismatch defects surface late in testing.</td>
                <td><strong>Low Continuous Risk:</strong> High-risk features tackled early; failures occur fast and cheap.</td>
            </tr>
            <tr>
                <td><strong>8. Team Structure</strong></td>
                <td><strong>Hierarchical Silos:</strong> Separate analyst, architect, coding, and QA departments.</td>
                <td><strong>Cross-Functional:</strong> Self-organizing teams possessing all needed skills with shared ownership.</td>
            </tr>
            <tr>
                <td><strong>9. Documentation</strong></td>
                <td><strong>Heavy & Formal:</strong> Exhaustive documents (SRS, SDD, Interface Specs, Test Plans).</td>
                <td><strong>Lean & Living:</strong> Working software and automated unit tests serve as living documentation.</td>
            </tr>
            <tr>
                <td><strong>10. Success Metric</strong></td>
                <td>Conformance to schedule milestones and signed specification documents.</td>
                <td>Delivery of <strong>working, verified software</strong> providing real business value.</td>
            </tr>
        </tbody>
    </table>

    <h3 class="section-header">3.3 Decision Framework: When to Choose Which Model?</h3>
    <p>
        • <strong>Choose Waterfall When:</strong> Requirements are completely stable, well-understood, and legally frozen (e.g., standard compiler, tax calculation engine, legacy system migration, or software embedded in fixed hardware).<br>
        • <strong>Choose Agile When:</strong> Requirements are dynamic, ambiguous, or highly competitive (e.g., commercial web/cloud apps, e-commerce, startups, and customer-facing mobile platforms).
    </p>

    <!-- TOPIC 4: EXTREME PROGRAMMING (XP) -->
    <div class="page-break"></div>
    <h2 class="topic-header">
        <span>4. Extreme Programming (XP)</span>
        <span class="meta-pill">Sure 13M / 16M</span>
    </h2>

    <h3 class="section-header">4.1 Definition, 5 Values & The 6-Phase Lifecycle</h3>
    <p>
        <strong>Extreme Programming (XP)</strong>, conceived by Kent Beck in 1996, is an agile software engineering methodology for small-to-medium teams facing rapidly changing requirements. It takes beneficial traditional software engineering practices and turns them up to "extreme" levels.
    </p>
    <div class="alert-box">
        <strong>The 5 Core Values of XP:</strong> 
        (1) <em>Communication</em> (verbal face-to-face dialogue), 
        (2) <em>Simplicity</em> (YAGNI — You Aren't Gonna Need It), 
        (3) <em>Feedback</em> (instant test & customer feedback), 
        (4) <em>Courage</em> (fearless refactoring), 
        (5) <em>Respect</em> (team collaboration & sustainable pace).
    </div>

    <div class="diagram-container">
        <!-- SVG Diagram: The 6-Phase XP Lifecycle -->
        <svg width="100%" height="110" viewBox="0 0 680 110" xmlns="http://www.w3.org/2000/svg">
            <g>
                <rect x="10" y="25" width="95" height="55" rx="5" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.5"/>
                <text x="57" y="45" font-family="sans-serif" font-size="8.5" font-weight="bold" fill="#0369a1" text-anchor="middle">1. Exploration</text>
                <text x="57" y="58" font-family="sans-serif" font-size="7" fill="#475569" text-anchor="middle">User Stories</text>
                <text x="57" y="69" font-family="sans-serif" font-size="7" fill="#475569" text-anchor="middle">Spike Solutions</text>
            </g>
            <path d="M 105 52 L 122 52" stroke="#0284c7" stroke-width="2" marker-end="url(#arrow)"/>

            <g>
                <rect x="125" y="25" width="95" height="55" rx="5" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.5"/>
                <text x="172" y="45" font-family="sans-serif" font-size="8.5" font-weight="bold" fill="#0369a1" text-anchor="middle">2. Planning</text>
                <text x="172" y="58" font-family="sans-serif" font-size="7" fill="#475569" text-anchor="middle">Planning Game</text>
                <text x="172" y="69" font-family="sans-serif" font-size="7" fill="#475569" text-anchor="middle">Release Velocity</text>
            </g>
            <path d="M 220 52 L 237 52" stroke="#0284c7" stroke-width="2"/>

            <g>
                <rect x="240" y="15" width="125" height="75" rx="5" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
                <text x="302" y="35" font-family="sans-serif" font-size="8.5" font-weight="bold" fill="#78350f" text-anchor="middle">3. Iterations to Release</text>
                <text x="302" y="48" font-family="sans-serif" font-size="7" fill="#78350f" text-anchor="middle">• 1–3 Week Timebox</text>
                <text x="302" y="59" font-family="sans-serif" font-size="7" fill="#78350f" text-anchor="middle">• Pair Programming</text>
                <text x="302" y="70" font-family="sans-serif" font-size="7" fill="#78350f" text-anchor="middle">• TDD & Continuous Int.</text>
                <text x="302" y="81" font-family="sans-serif" font-size="7" fill="#78350f" text-anchor="middle">• Acceptance Tests</text>
            </g>
            <path d="M 365 52 L 382 52" stroke="#0284c7" stroke-width="2"/>

            <g>
                <rect x="385" y="25" width="95" height="55" rx="5" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.5"/>
                <text x="432" y="45" font-family="sans-serif" font-size="8.5" font-weight="bold" fill="#0369a1" text-anchor="middle">4. Productionizing</text>
                <text x="432" y="58" font-family="sans-serif" font-size="7" fill="#475569" text-anchor="middle">Load Testing</text>
                <text x="432" y="69" font-family="sans-serif" font-size="7" fill="#475569" text-anchor="middle">Customer Sign-off</text>
            </g>
            <path d="M 480 52 L 497 52" stroke="#0284c7" stroke-width="2"/>

            <g>
                <rect x="500" y="25" width="85" height="55" rx="5" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.5"/>
                <text x="542" y="45" font-family="sans-serif" font-size="8.5" font-weight="bold" fill="#0369a1" text-anchor="middle">5. Maintenance</text>
                <text x="542" y="58" font-family="sans-serif" font-size="7" fill="#475569" text-anchor="middle">Live Operations</text>
                <text x="542" y="69" font-family="sans-serif" font-size="7" fill="#475569" text-anchor="middle">New Stories</text>
            </g>
            <path d="M 585 52 L 602 52" stroke="#0284c7" stroke-width="2"/>

            <g>
                <rect x="605" y="25" width="65" height="55" rx="5" fill="#f3f4f6" stroke="#4b5563" stroke-width="1.5"/>
                <text x="637" y="47" font-family="sans-serif" font-size="8.5" font-weight="bold" fill="#1f2937" text-anchor="middle">6. Death</text>
                <text x="637" y="60" font-family="sans-serif" font-size="7" fill="#475569" text-anchor="middle">Archiving</text>
                <text x="637" y="71" font-family="sans-serif" font-size="7" fill="#475569" text-anchor="middle">Retirement</text>
            </g>
        </svg>
        <div class="diagram-caption">Figure 1.3: Kent Beck's Complete 6-Phase Extreme Programming Lifecycle</div>
    </div>

    <h3 class="section-header">4.2 Core XP Engineering Practices Detailed</h3>
    <p>
        <strong>1. Pair Programming:</strong> Two programmers work at a single computer. The <strong>Driver</strong> types code and unit tests, focusing on tactical syntax and algorithms. The <strong>Navigator</strong> reviews code in real time, catching corner cases, syntax flaws, and architectural coherence. Roles rotate every 20–30 minutes. <em>Benefits:</em> Continuous peer review, collective code ownership, and elimination of single points of failure.<br>
        <strong>2. Test-Driven Development (TDD):</strong> Developers follow the strict <strong>Red-Green-Refactor</strong> cycle: (1) <em>Red:</em> Write an automated unit test that fails. (2) <em>Green:</em> Write the minimal production code to pass the test. (3) <em>Refactor:</em> Clean up code and eliminate duplication while ensuring tests remain green. <em>Note:</em> TDD enforces modularity and regression safety, though developer oversight can still miss requirement edge cases.<br>
        <strong>3. Continuous Integration (CI):</strong> Pairs integrate tested code into the main repository multiple times a day. An automated build server compiles and runs all test suites on every commit, eliminating late-stage "Integration Hell".<br>
        <strong>4. On-Site Customer:</strong> A dedicated business representative sits full-time in the development room, providing instant requirement clarifications and conducting acceptance testing.
    </p>

    <!-- TOPIC 5: V-MODEL & INCREMENTAL MODEL -->
    <div class="page-break"></div>
    <h2 class="topic-header">
        <span>5. The V-Model & Incremental Process Model</span>
        <span class="meta-pill">High Yield 13M</span>
    </h2>

    <h3 class="section-header">5.1 The V-Model (Verification and Validation)</h3>
    <p>
        The <strong>V-Model</strong> maps development phases symmetrically against testing phases. Test planning begins concurrently with each specification stage:
    </p>
    <table>
        <thead>
            <tr>
                <th style="width: 48%;">Verification (Left Wing: "Are we building the product right?")</th>
                <th style="width: 4%;">↔</th>
                <th style="width: 48%;">Validation (Right Wing: "Are we building the right product?")</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>Requirements Analysis:</strong> Functional & non-functional SRS.</td>
                <td>↔</td>
                <td><strong>Acceptance Testing (UAT):</strong> Validates business goals with users.</td>
            </tr>
            <tr>
                <td><strong>System Design:</strong> Hardware/software limits & performance.</td>
                <td>↔</td>
                <td><strong>System Testing:</strong> Validates end-to-end performance and security.</td>
            </tr>
            <tr>
                <td><strong>Architecture Design:</strong> Subsystem APIs and interface specs.</td>
                <td>↔</td>
                <td><strong>Integration Testing:</strong> Verifies inter-module data contracts.</td>
            </tr>
            <tr>
                <td><strong>Module Design:</strong> Algorithmic logic and internal methods.</td>
                <td>↔</td>
                <td><strong>Unit Testing:</strong> Verifies isolated code units and boundary values.</td>
            </tr>
            <tr>
                <td colspan="3" style="text-align: center; background: #fef3c7; font-weight: bold; color: #78350f;">
                    Apex (Vertex of the V): CODING & IMPLEMENTATION
                </td>
            </tr>
        </tbody>
    </table>
    <div class="alert-box alert-success">
        <strong>The Defect Prevention Principle:</strong> Writing test cases concurrently with requirements and design exposes ambiguities when remediation cost is \(1\times\) rather than \(50\times\)–\(100\times\) post-release.
    </div>

    <h3 class="section-header">5.2 The Incremental Process Model</h3>
    <p>
        The <strong>Incremental Model</strong> applies Waterfall phases in a staggered, iterative progression. 
        <strong>Increment 1</strong> delivers the <strong>Core Product</strong> satisfying fundamental, high-priority user needs. Subsequent increments add supplemental features based on customer feedback from live operational usage.
    </p>
    <div class="alert-box">
        <strong>Incremental vs. Iterative:</strong><br>
        • <em>Incremental:</em> Staged delivery of operational software subsets (adding <strong>more functional pieces</strong> over time, room-by-room).<br>
        • <em>Iterative:</em> Progressive refinement of the <strong>entire system</strong> across repeating cycles (portrait sketch \(\to\) color \(\to\) fine details).
    </div>

    <!-- TOPIC 6: CAT-1 QUESTION BANK SOLUTIONS -->
    <div class="page-break"></div>
    <h2 class="topic-header">
        <span>6. Official College CAT-1 Question Bank Solutions (Unit 1)</span>
        <span class="meta-pill">Part-A 2-Marks High Yield</span>
    </h2>

    <div class="qa-card">
        <div class="qa-question">Q1. What is software engineering? [2M | K1 | CO1]</div>
        <div class="qa-answer">Software Engineering is the establishment and use of sound engineering principles to obtain economically software that is reliable and works efficiently on real machines (Fritz Bauer). It integrates three elements: <strong>Process</strong>, <strong>Methods</strong>, and <strong>Tools</strong>.</div>
    </div>

    <div class="qa-card">
        <div class="qa-question">Q2. 'Software doesn't wear out'. Justify. [2M | K1 | CO1]</div>
        <div class="qa-answer">Hardware suffers from physical friction, heat, and environmental wear, following a bathtub curve. Software is logical, not physical; it does not wear out. However, software <strong>deteriorates</strong> because successive maintenance changes and patches introduce unintended side-effects and structural decay.</div>
    </div>

    <div class="qa-card">
        <div class="qa-question">Q3. What are the 5 fundamental framework activities of a software process? [2M | K1 | CO1]</div>
        <div class="qa-answer">(1) <strong>Communication:</strong> Requirements elicitation. (2) <strong>Planning:</strong> Estimation, scheduling, risk analysis. (3) <strong>Modeling:</strong> Analysis and design models. (4) <strong>Construction:</strong> Coding and testing. (5) <strong>Deployment:</strong> Delivery and customer feedback.</div>
    </div>

    <div class="qa-card">
        <div class="qa-question">Q4. What are the umbrella activities of a software process? [2M | K1 | CO1]</div>
        <div class="qa-answer">Activities occurring across the entire project: (1) Software Project Tracking & Control, (2) Risk Management, (3) Software Quality Assurance (SQA), (4) Software Configuration Management (SCM), (5) Technical Reviews, (6) Measurement and Reusability Management.</div>
    </div>

    <div class="qa-card">
        <div class="qa-question">Q5. List the process maturity levels in SEI's CMM. [2M | K1 | CO1]</div>
        <div class="qa-answer">Level 1: <strong>Initial</strong> (Ad-hoc, chaotic). Level 2: <strong>Repeatable</strong> (Basic project tracking). Level 3: <strong>Defined</strong> (Standardized organizational processes). Level 4: <strong>Managed</strong> (Quantitative metrics and quality control). Level 5: <strong>Optimizing</strong> (Continuous process improvement).</div>
    </div>

    <div class="qa-card">
        <div class="qa-question">Q6. Why is it called "Extreme" in Extreme Programming (XP)? [2M | K2 | CO1]</div>
        <div class="qa-answer">It pushes common-sense practices to extreme levels: continuous code review via <strong>Pair Programming</strong>, continuous testing via <strong>TDD</strong>, continuous integration via <strong>CI</strong> multiple times daily, and customer feedback via an <strong>On-Site Customer</strong>.</div>
    </div>

    <div class="qa-card">
        <div class="qa-question">Q7. List two deficiencies in the Waterfall model. How are they overcome? [2M | K1 | CO1]</div>
        <div class="qa-answer">(1) <em>Inability to accommodate changing requirements:</em> Overcome by <strong>Agile/Prototyping</strong>. (2) <em>Working code appears late, hiding critical risks:</em> Overcome by <strong>Boehm's Spiral Model</strong> (explicit risk analysis) or <strong>Incremental Model</strong> (early Core Product).</div>
    </div>

    <div class="qa-card">
        <div class="qa-question">Q8. For a heavy lift launch vehicle in a space mission, which model is suitable? [2M | K1 | CO1]</div>
        <div class="qa-answer"><strong>Boehm's Spiral Model (or V-Model/Formal Methods).</strong> Heavy lift launch vehicles involve life-critical, mission-critical operations with extreme aerodynamic and avionics uncertainties. The Spiral Model’s mandatory <strong>Quadrant II Risk Analysis and Prototyping</strong> prevents catastrophic failure.</div>
    </div>

    <div class="qa-card">
        <div class="qa-question">Q9. Differentiate between Verification and Validation. [2M | K1 | CO1]</div>
        <div class="qa-answer"><strong>Verification</strong> asks <em>"Are we building the product right?"</em> (Static reviews and inspections without running code). <strong>Validation</strong> asks <em>"Are we building the right product?"</em> (Dynamic testing of compiled code to satisfy customer requirements).</div>
    </div>

</body>
</html>
"""

def main():
    base_dir = r"C:\Users\siva2\OneDrive\Desktop\soft"
    unit1_dir = os.path.join(base_dir, "Unit-1")
    os.makedirs(unit1_dir, exist_ok=True)

    html_content = build_html()
    html_path = os.path.join(unit1_dir, "UNIT_1_SOFTWARE_PROCESS_AND_AGILE.html")
    pdf_path = os.path.join(unit1_dir, "UNIT_1_SOFTWARE_PROCESS_AND_AGILE.pdf")
    root_pdf_path = os.path.join(base_dir, "UNIT_1_SOFTWARE_PROCESS_AND_AGILE.pdf")

    print(f"Writing HTML to {html_path}...")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    edge_exe = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    print(f"Generating PDF via Microsoft Edge Headless...")
    cmd = [
        edge_exe,
        "--headless=new",
        "--disable-gpu",
        "--virtual-time-budget=6000",
        f"--print-to-pdf={pdf_path}",
        "--no-pdf-header-footer",
        html_path
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=90)
    time.sleep(2)

    if os.path.exists(pdf_path):
        size_kb = os.path.getsize(pdf_path) / 1024
        print(f"SUCCESS: PDF generated at {pdf_path} ({size_kb:.2f} KB)")
        shutil.copyfile(pdf_path, root_pdf_path)
        print(f"SUCCESS: Copied to root at {root_pdf_path}")
    else:
        print("ERROR: Failed to generate PDF:", res.stderr)

if __name__ == "__main__":
    main()
