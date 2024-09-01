import matplotlib.pyplot as plt
import seaborn as sns

# Plot budget overrun distribution
plt.figure(figsize=(8, 6))
sns.countplot(x='Budget_Overrun', data=df)
plt.title('Budget Overrun Distribution')
plt.show()

# Plot correlation heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix of Construction Costs')
plt.show()

# Plot cost vs. final cost
plt.figure(figsize=(12, 8))
sns.scatterplot(x='Initial_Budget', y='Final_Cost', hue='Budget_Overrun', data=df, palette='coolwarm')
plt.title('Initial Budget vs. Final Cost')
plt.show()
