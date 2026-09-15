# apollo-sponsorship-audit-case-study
Causal OLS regression and graph centrality pipeline for sports sponsorship valuation and offline inventory auditing by Apollo Sports Business Group.
⚽ Apollo Sports Business Group: Commercial Sponsorship Audit Pipeline

This repository contains the data science pipeline, dataset, and executive report for **Apollo Sports Business Group's** commercial sponsorship audit framework.

The case study evaluates a **$6.5M USD (118M MXP)** multi-sponsor portfolio for a **Tier-2 Top Flight Premier Division Franchise in North America** (anonymized as *Club Alpha*).

---

## 📌 Executive Summary

Traditional sponsorship measurement tools focus solely on digital impressions and screen time. **Apollo Sports Business Group** bridges the gap between raw measurement data and CFO-ready financial decision-making by:
1. **Isolating Cause from Coincidence**: Applying **Causal OLS Regression** to decouple marquee rival attendance spikes from standalone sponsor exposure.
2. **Valuing Offline Inventory**: Using **Eigenvector Graph Centrality** to model physical matchday foot traffic across stadium concourses and entry corridors.
3. **Reconciling the Portfolio**: Categorizing assets into Apollo's 4 Quantified Outcomes (*Protected Value*, *Justified Incremental Investment*, *Potential Cost Reduction*, and *Investment Pending*).

---

## 🛠️ Technology Stack & Environment

* **Language**: Python 3.14 (Compatible with Python 3.12+)
* **Data Processing**: `pandas`, `numpy`
* **Causal Regression**: `statsmodels` (OLS Multivariable Regression)
* **Graph Network Analysis**: `networkx` (Eigenvector Centrality)
* **Visualization**: `matplotlib`, `seaborn`
* **IDE / Execution**: VS Code, Google Colab

---

## 📂 Repository Layout

├── club_alpha_sponsorship.csv               # Anonymized 89-matchday telemetry dataset ├── apollo_case_study_club_alpha.ipynb       # Executable Jupyter Notebook (Google Colab / VS Code) ├── apollo_case_study_club_alpha.py          # Standalone Python analytics script ├── apollo_case_study_club_alpha_report.pdf  # Publication-grade PDF Executive Case Study Report └── README.md                                # Repository documentation
---

## 🚀 How to Run the Notebook

### Option 1: Open in Google Colab
1. Upload `club_alpha_sponsorship.csv` and `apollo_case_study_club_alpha.ipynb` to your Google Drive or GitHub.
2. Click **Open in Colab** and run all cells sequentially.

### Option 2: Local VS Code Setup
```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/apollo-sponsorship-audit.git
cd apollo-sponsorship-audit

# Install dependencies
pip install pandas numpy statsmodels networkx matplotlib seaborn

# Run the analytics script
python3 apollo_case_study_club_alpha.py
⚖️ Disclaimers & Methodology NotesEducational & Demonstration Purposes: This repository, code, and case study are prepared strictly for educational, research, and portfolio demonstration purposes.Model Limitations:Omitted Variable Bias: OLS regression models 89 matchday observations; exogenous factors such as kickoff time slots, weather, and injuries are noted in model documentation.Spatial Weights: Adjacency matrices represent expert modeling assumptions based on physical stadium sightlines.Currency Standard: Primary monetary figures are presented in **USD ($)** with **MXP (Pesos)** in parenthesis ($1 USD = 18.0 MXP).🏢 About Apollo Sports Business GroupApollo Sports Business Group brings financial accountability and commercial intelligence to sports sponsorships, media rights, and hospitality experiences.🌐 Website: apollosbg.com💼 LinkedIn: Apollo Sports Business Group
---
