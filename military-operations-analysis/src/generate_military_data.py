import pandas as pd
import numpy as np
import random

# Simulate data
np.random.seed(42)
random.seed(42)

# Troop Deployment Data
deployment_data = {
    'Date': pd.date_range(start='2020-01-01', periods=100, freq='M'),
    'Region': np.random.choice(['North', 'South', 'East', 'West'], size=100),
    'Troops_Deployed': np.random.randint(100, 1000, size=100),
    'Mission_Type': np.random.choice(['Reconnaissance', 'Combat', 'Training', 'Support'], size=100)
}

df_deployment = pd.DataFrame(deployment_data)

# Resource Allocation Data
resource_data = {
    'Date': pd.date_range(start='2020-01-01', periods=100, freq='M'),
    'Region': df_deployment['Region'],
    'Budget_Allocated': np.random.randint(10000, 100000, size=100),
    'Equipment_Allocated': np.random.randint(50, 500, size=100),
    'Supplies_Allocated': np.random.randint(500, 5000, size=100),
}

df_resource = pd.DataFrame(resource_data)

# Mission Outcome Data
mission_outcome_data = {
    'Date': pd.date_range(start='2020-01-01', periods=100, freq='M'),
    'Region': df_deployment['Region'],
    'Mission_Type': df_deployment['Mission_Type'],
    'Mission_Success': np.random.choice([0, 1], size=100, p=[0.3, 0.7]),  # 0 = Fail, 1 = Success
}

df_mission = pd.DataFrame(mission_outcome_data)

# Merge DataFrames for Analysis
df_merged = pd.merge(df_deployment, df_resource, on=['Date', 'Region'])
df_merged = pd.merge(df_merged, df_mission, on=['Date', 'Region', 'Mission_Type'])

# Save to CSV
df_merged.to_csv('military_data.csv', index=False)

print("Data simulation complete. Data saved to 'military_data.csv'.")
