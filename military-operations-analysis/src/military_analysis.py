import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Load the data
df = pd.read_csv('military_data.csv')

# Drop non-numeric columns before computing the correlation
numeric_df = df.select_dtypes(include=['float64', 'int64'])

# Exploratory Data Analysis (EDA)
# Correlation Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# Mission Success Rate by Region
sns.barplot(x='Region', y='Mission_Success', data=df, ci=None)
plt.title('Mission Success Rate by Region')
plt.show()

# Predictive Modeling
X = df[['Troops_Deployed', 'Budget_Allocated', 'Equipment_Allocated', 'Supplies_Allocated']]
y = df['Mission_Success']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
