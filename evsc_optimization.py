import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import os

# Read all CSVs
df_dg = pd.read_csv('./data/DG_SC_placement_locationwise.csv')
df_pso = pd.read_csv('./data/evcs_pso_selected_locations.csv')
df_input = pd.read_csv('./data/evcs_best_25_locations.csv')
df_market = pd.read_csv('./data/ev_market_features.csv')

# Merge step by step on 'BusNo' (adjust if needed)
df_merged = df_dg.merge(df_pso, on=['BusNo', 'Location'], how='outer')
df_merged = df_merged.merge(df_input, on=['BusNo', 'Location'], how='outer')
df_merged = df_merged.merge(df_market, on=['BusNo', 'Location'], how='outer')

print("Merged columns:", df_merged.columns.tolist())

# List your columns (update as needed!)
feature_cols = [
    'AnnualElecCost', 'LandCost', 'UserCost', 'Reliability',
    'NearbyEVSeller', 'EVDensity', 'MallsNearby'
]

feature_cols_present = [col for col in feature_cols if col in df_merged.columns]
print("Features used for normalization:", feature_cols_present)

df_merged[feature_cols_present] = df_merged[feature_cols_present].fillna(0)

# Normalize
scaler = MinMaxScaler()
norm_cols = [col + '_norm' for col in feature_cols_present]
df_merged[norm_cols] = scaler.fit_transform(df_merged[feature_cols_present])

# Set your weights (adjust as needed)
weights = {
    'AnnualElecCost_norm': 0.2,
    'LandCost_norm': 0.1,
    'UserCost_norm': 0.2,
    'Reliability_norm': 0.15,
    'NearbyEVSeller_norm': 0.1,
    'EVDensity_norm': 0.15,
    'MallsNearby_norm': 0.1
}

# Only use weights for normalized columns that exist
weighted_sum_cols = [col for col in weights if col in df_merged.columns]
df_merged['WeightedSum'] = sum(df_merged[col] * weights[col] for col in weighted_sum_cols)

df_final = df_merged.sort_values('WeightedSum').head(25)
if os.path.exists('./data/final_best_25_evcs_locations.csv'):
    os.remove('./data/final_best_25_evcs_locations.csv')
df_final.to_csv('./data/final_best_25_evcs_locations.csv', index=False)
print("Saved best 25 locations to 'final_best_25_evcs_locations.csv'")