import pandas as pd
import numpy as np

# Generate synthetic dataset
np.random.seed(0)
data = {
    'Project_ID': np.arange(1, 31),
    'Project_Type': np.random.choice(['Residential', 'Commercial', 'Industrial'], size=30),
    'Initial_Budget': np.random.randint(100000, 500000, size=30),
    'Final_Cost': np.random.randint(100000, 600000, size=30),
    'Labor_Hours': np.random.randint(2000, 10000, size=30),
    'Material_Cost': np.random.randint(10000, 100000, size=30),
    'Equipment_Cost': np.random.randint(5000, 50000, size=30),
    'Project_Duration': np.random.randint(30, 365, size=30),
}

df = pd.DataFrame(data)
df['Budget_Overrun'] = (df['Final_Cost'] > df['Initial_Budget']).astype(int)
df.to_csv('construction_budget_data.csv', index=False)
