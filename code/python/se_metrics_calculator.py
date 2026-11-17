"""
se_metrics_calculator.py
Quantitative Software Engineering Metrics & Estimation Engine for 24ITPC302.
Supports:
1. Function Point (FP) Calculation (UFC, VAF, FP, LOC)
2. Basic & Intermediate COCOMO I Models (Organic, Semidetached, Embedded)
3. Cyclomatic Complexity V(G) via 3 methods
4. Earned Value Analysis (EVA: CV, SV, CPI, SPI, EAC)
5. Risk Exposure (RE) & Risk Reduction Leverage (RRL)
"""

import math

# ----------------------------------------------------
# 1. FUNCTION POINT CALCULATION
# ----------------------------------------------------
UFC_WEIGHTS = {
    "EI":  {"simple": 3, "average": 4, "complex": 6},
    "EO":  {"simple": 4, "average": 5, "complex": 7},
    "EQ":  {"simple": 3, "average": 4, "complex": 6},
    "ILF": {"simple": 7, "average": 10, "complex": 15},
    "EIF": {"simple": 5, "average": 7, "complex": 10}
}

LOC_PER_FP = {
    "C": 128,
    "C++": 53,
    "Java": 53,
    "C#": 54,
    "Python": 25,
    "JavaScript": 47,
    "SQL": 13
}

def calculate_function_points(counts_dict, complexity="average", fi_list=None):
    """
    counts_dict: {'EI': count, 'EO': count, 'EQ': count, 'ILF': count, 'EIF': count}
    complexity: 'simple', 'average', or 'complex'
    fi_list: list of 14 integers (0 to 5)
    """
    ufc = 0
    breakdown = {}
    for comp, count in counts_dict.items():
        w = UFC_WEIGHTS[comp][complexity]
        contrib = count * w
        ufc += contrib
        breakdown[comp] = {"count": count, "weight": w, "subtotal": contrib}
    
    if fi_list is None:
        fi_list = [3] * 14  # Default average rating
    
    sum_fi = sum(fi_list)
    vaf = 0.65 + 0.01 * sum_fi
    fp = ufc * vaf
    
    return {
        "UFC": ufc,
        "Sum_Fi": sum_fi,
        "VAF": round(vaf, 4),
        "FP": round(fp, 2),
        "Breakdown": breakdown
    }

# ----------------------------------------------------
# 2. COCOMO I ESTIMATION ENGINE
# ----------------------------------------------------
COCOMO_CONSTANTS = {
    "organic":      {"a": 2.4, "b": 1.05, "c": 2.5, "d": 0.38},
    "semidetached": {"a": 3.0, "b": 1.12, "c": 2.5, "d": 0.35},
    "embedded":     {"a": 3.6, "b": 1.20, "c": 2.5, "d": 0.32}
}

def calculate_cocomo_basic(kloc, mode="organic"):
    mode = mode.lower()
    if mode not in COCOMO_CONSTANTS:
        raise ValueError(f"Unknown mode '{mode}'. Choose organic, semidetached, or embedded.")
    
    consts = COCOMO_CONSTANTS[mode]
    a, b, c, d = consts["a"], consts["b"], consts["c"], consts["d"]
    
    effort = a * (kloc ** b)  # Person-Months
    time_dev = c * (effort ** d)  # Months
    staff = effort / time_dev if time_dev > 0 else 0
    productivity = (kloc * 1000) / effort if effort > 0 else 0
    
    return {
        "Mode": mode.capitalize(),
        "KLOC": kloc,
        "Effort_PM": round(effort, 2),
        "Time_Months": round(time_dev, 2),
        "Staff_Persons": round(staff, 2),
        "Productivity_LOC_per_PM": round(productivity, 2)
    }

def calculate_cocomo_intermediate(kloc, mode="organic", cost_drivers=None):
    base = calculate_cocomo_basic(kloc, mode)
    eaf = 1.0
    if cost_drivers:
        for cd in cost_drivers:
            eaf *= cd
    
    adjusted_effort = base["Effort_PM"] * eaf
    consts = COCOMO_CONSTANTS[mode.lower()]
    c, d = consts["c"], consts["d"]
    time_dev = c * (adjusted_effort ** d)
    staff = adjusted_effort / time_dev if time_dev > 0 else 0
    
    return {
        "Mode": mode.capitalize(),
        "KLOC": kloc,
        "EAF": round(eaf, 4),
        "Nominal_Effort_PM": base["Effort_PM"],
        "Adjusted_Effort_PM": round(adjusted_effort, 2),
        "Time_Months": round(time_dev, 2),
        "Staff_Persons": round(staff, 2)
    }

# ----------------------------------------------------
# 3. CYCLOMATIC COMPLEXITY V(G)
# ----------------------------------------------------
def calculate_cyclomatic_complexity(edges=None, nodes=None, predicates=None, regions=None, p=1):
    results = {}
    if edges is not None and nodes is not None:
        vg_en = edges - nodes + 2 * p
        results["Method_Edges_Nodes"] = {"E": edges, "N": nodes, "P": p, "V(G)": vg_en}
    if predicates is not None:
        vg_pred = predicates + 1
        results["Method_Predicates"] = {"P_prime": predicates, "V(G)": vg_pred}
    if regions is not None:
        results["Method_Regions"] = {"R": regions, "V(G)": regions}
    return results

# ----------------------------------------------------
# 4. EARNED VALUE ANALYSIS (EVA)
# ----------------------------------------------------
def calculate_earned_value(bac, pv, ev, ac):
    cv = ev - ac
    sv = ev - pv
    cpi = ev / ac if ac > 0 else 0
    spi = ev / pv if pv > 0 else 0
    eac = bac / cpi if cpi > 0 else 0
    etc = eac - ac
    
    cost_status = "Under Budget (Good)" if cv >= 0 else "Over Budget (Critical)"
    sched_status = "Ahead of Schedule (Good)" if sv >= 0 else "Behind Schedule (Critical)"
    
    return {
        "BAC": bac,
        "PV": pv,
        "EV": ev,
        "AC": ac,
        "Cost_Variance_CV": round(cv, 2),
        "Schedule_Variance_SV": round(sv, 2),
        "CPI": round(cpi, 3),
        "SPI": round(spi, 3),
        "EAC": round(eac, 2),
        "ETC": round(etc, 2),
        "Cost_Status": cost_status,
        "Schedule_Status": sched_status
    }

# ----------------------------------------------------
# 5. RISK EXPOSURE (RE)
# ----------------------------------------------------
def calculate_risk_exposure(prob, cost_impact, before_re=None, after_re=None, mitigation_cost=None):
    re = prob * cost_impact
    res = {
        "Probability": prob,
        "Impact_Cost": cost_impact,
        "Risk_Exposure_RE": round(re, 2)
    }
    if before_re is not None and after_re is not None and mitigation_cost:
        rrl = (before_re - after_re) / mitigation_cost
        res["RRL"] = round(rrl, 3)
        res["Justified"] = rrl > 1.0
    return res

if __name__ == "__main__":
    print("==================================================")
    print("24ITPC302: SOFTWARE ENGINEERING METRICS ENGINE")
    print("==================================================")
    
    # 1. Function Point Test
    counts = {"EI": 10, "EO": 8, "EQ": 6, "ILF": 4, "EIF": 2}
    fp_res = calculate_function_points(counts, complexity="average")
    print("\n1. Function Point Calculation:")
    print(f"   UFC: {fp_res['UFC']} | VAF: {fp_res['VAF']} | FP: {fp_res['FP']}")
    print(f"   Estimated Java LOC (53 LOC/FP): {round(fp_res['FP'] * 53)}")

    # 2. COCOMO Test (33 KLOC Organic)
    cocomo_res = calculate_cocomo_basic(33, "organic")
    print("\n2. Basic COCOMO Estimation (33 KLOC Organic):")
    print(f"   Effort: {cocomo_res['Effort_PM']} PM | Time: {cocomo_res['Time_Months']} Months | Staff: {cocomo_res['Staff_Persons']} Persons")

    # 3. Cyclomatic Complexity Test (E=16, N=14)
    vg_res = calculate_cyclomatic_complexity(edges=16, nodes=14, predicates=3, regions=4)
    print("\n3. Cyclomatic Complexity:")
    print(f"   V(G) = E - N + 2 = {vg_res['Method_Edges_Nodes']['V(G)']}")

    # 4. Earned Value Analysis Test
    eva_res = calculate_earned_value(bac=100000, pv=45000, ev=40000, ac=48000)
    print("\n4. Earned Value Analysis:")
    print(f"   CV: ${eva_res['Cost_Variance_CV']} ({eva_res['Cost_Status']})")
    print(f"   SV: ${eva_res['Schedule_Variance_SV']} ({eva_res['Schedule_Status']})")
    print(f"   CPI: {eva_res['CPI']} | SPI: {eva_res['SPI']} | EAC: ${eva_res['EAC']}")
    print("==================================================")
