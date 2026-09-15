# ⚽ Apollo Sports Business Group: Commercial Sponsorship Audit Pipeline

Causal regression and graph centrality pipeline for sports sponsorship valuation and offline inventory auditing by **Apollo Sports Business Group**.

This repository contains the data science pipeline, dataset, and executive report for Apollo's evidence-based commercial audit framework.

The case study evaluates a **$6.56M USD (118.05M MXN)** multi-sponsor portfolio for a **Tier-2 Top Flight Premier Division Franchise in North America** (anonymized as *Club Alpha*).

---

## 📌 Executive Summary

Traditional sponsorship measurement tools focus solely on digital impressions and screen time. **Apollo Sports Business Group** bridges the gap between raw measurement data and CFO-ready financial decision-making by:

1. **Evaluating Association vs. Baseline Noise**: Applying Multivariable OLS Regression to evaluate broadcast reach associated with marquee rival attendance vs. standalone sponsor exposure.
2. **Valuing Offline Inventory**: Using **Eigenvector Graph Centrality** to model physical matchday foot traffic across stadium concourses, entry gates, and fan corridors.
3. **Reconciling the Portfolio**: Categorizing assets into Apollo's 4 Quantified Outcomes (*Protected Value*, *Justified Incremental Investment*, *Potential Cost Reduction*, and *Investment Pending*).

---

## 🛠️ Technology Stack & Environment

* **Language**: Python 3.14 (Compatible with Python 3.12+)
* **Data Processing**: `pandas`, `numpy`
* **Regression Modeling**: `statsmodels` (Multivariable OLS Regression)
* **Graph Network Analysis**: `networkx` (Eigenvector Centrality)
* **Visualization**: `matplotlib`, `seaborn`
* **PDF Engine**: `reportlab` (Publication-grade document layout)
* **IDE / Environment**: VS Code, Google Colab, Gemini Notebook

---

## 📂 Repository Layout

├── club_alpha_sponsorship.csv               # Anonymized 89-matchday telemetry dataset ├── apollo_case_study_club_alpha.ipynb       # Executable Jupyter Notebook (Google Colab / VS Code) ├── apollo_case_study_club_alpha.py          # Standalone Python analytics script ├── apollo_case_study_club_alpha_report.pdf  # Executive PDF Case Study Report └── README.md                                # Repository documentation
---

## 🚀 How to Run the Notebook

### Option 1: Open in Google Colab
1. Upload `club_alpha_sponsorship.csv` and `apollo_case_study_club_alpha.ipynb` to your Google Drive or GitHub repository.
2. Open the `.ipynb` file in Google Colab and run all cells sequentially.

### Option 2: Local VS Code Setup
```bash
# Clone the repository
git clone https://github.com/ApolloSBG/apollo-sponsorship-audit-case-study.git
cd apollo-sponsorship-audit-case-study

# Install dependencies
pip install pandas numpy statsmodels networkx matplotlib seaborn reportlab

# Run the analytics script
python3 apollo_case_study_club_alpha.py
⚖️ Disclaimers & Methodology NotesEducational & Demonstration Purposes: This repository, code, dataset, and report are prepared strictly for educational, research, and portfolio demonstration purposes. Figures represent illustrative model outputs rather than real client or proprietary financial records.Model Limitations:Omitted Variable Bias: OLS regression models 89 matchday observations; exogenous factors such as kickoff time slots, weather, broadcast channel tier, and player availability are noted in model documentation.Spatial Weights: Adjacency matrices represent expert modeling assumptions based on physical stadium sightlines.Currency Standard: Primary monetary figures are presented in **USD ($)** with **MXN (Pesos)** in parenthesis ($1 USD = 18.0 MXN).🏢 About Apollo Sports Business GroupApollo Sports Business Group brings financial accountability and commercial intelligence to sports sponsorships, media rights, and hospitality experiences.🌐 Website: apollosbg.com💼 LinkedIn: Apollo Sports Business Group
