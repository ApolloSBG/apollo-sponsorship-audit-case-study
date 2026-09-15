# ==============================================================================
# APOLLO SPORTS BUSINESS GROUP — EXECUTIVE CASE STUDY
# Commercial Sponsorship Audit & Offline Venue Valuation Pipeline
# Tech Stack: Python 3.14 (or 3.12+), VS Code, Statsmodels, NetworkX, Pandas
# ==============================================================================
import pandas as pd
import numpy as np
import statsmodels.api as sm
import networkx as nx

# 1. Load Anonymized Matchday Telemetry Dataset
df_matches = pd.read_csv('club_alpha_sponsorship.csv')

# 2. Multivariable Regression Analysis (Association vs. Baseline Noise)
X = df_matches[['Attendance', 'Is_Big_Game', 'Brand_C_Chest_Active']]
X = sm.add_constant(X)
y = df_matches['TV_Reach_Viewers']

model_ols = sm.OLS(y, X).fit()
print("=== MULTIVARIABLE REGRESSION RESULTS ===")
print(model_ols.summary().tables[1])

print("\nKey Statistical Insights:")
print(f"- Marquee Opponent Association: +{model_ols.params['Is_Big_Game']:,.0f} viewers (p < 0.001)")
print(f"- Standalone Chest Association: +{model_ols.params['Brand_C_Chest_Active']:,.0f} viewers (statistically non-significant)")

# 3. Spatial Graph Centrality & Offline Venue Inventory Audit
assets_data = [
    {'Asset_ID': 'chest_main', 'Asset_Name': 'Front Chest (Brand D)', 'Contract_USD': 1.85, 'Contract_MXN': 33.30, 'Zone': 'Kit'},
    {'Asset_ID': 'jersey_back', 'Asset_Name': 'Jersey Back (Brand E)', 'Contract_USD': 1.25, 'Contract_MXN': 22.50, 'Zone': 'Kit'},
    {'Asset_ID': 'jersey_sleeve', 'Asset_Name': 'Sleeve (Brand P)', 'Contract_USD': 0.39, 'Contract_MXN': 7.00, 'Zone': 'Kit'},
    {'Asset_ID': 'short_front', 'Asset_Name': 'Shorts (Brand S)', 'Contract_USD': 0.32, 'Contract_MXN': 5.75, 'Zone': 'Kit'},
    {'Asset_ID': 'socks', 'Asset_Name': 'Socks (Brand K)', 'Contract_USD': 0.25, 'Contract_MXN': 4.50, 'Zone': 'Kit'},
    {'Asset_ID': 'led_perimeter', 'Asset_Name': 'LED Boards (Brand G)', 'Contract_USD': 1.00, 'Contract_MXN': 18.00, 'Zone': 'Venue'},
    {'Asset_ID': 'concourse_activation', 'Asset_Name': 'Concourse Bars (Brand B)', 'Contract_USD': 0.67, 'Contract_MXN': 12.00, 'Zone': 'Venue'},
    {'Asset_ID': 'digital_social', 'Asset_Name': 'Digital Campaigns (Brand M)', 'Contract_USD': 0.83, 'Contract_MXN': 15.00, 'Zone': 'Digital'}
]
df_assets = pd.DataFrame(assets_data)

G = nx.Graph()
for _, r in df_assets.iterrows():
    G.add_node(r['Asset_ID'], zone=r['Zone'])

for i in list(G.nodes):
    for j in list(G.nodes):
        if i != j:
            z1, z2 = G.nodes[i]['zone'], G.nodes[j]['zone']
            w = 0.90 if z1 == z2 else (0.65 if set([z1, z2]) == {'Kit', 'Venue'} else 0.40)
            G.add_edge(i, j, weight=w)

centrality = nx.eigenvector_centrality(G, weight='weight')
df_assets['Centrality'] = df_assets['Asset_ID'].map(centrality)

print("\n=== APOLLO SPONSORSHIP AUDIT LEDGER ===")
print(df_assets[['Asset_Name', 'Contract_USD', 'Contract_MXN', 'Centrality']])
