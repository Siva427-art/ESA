import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
df = pd.read_csv('titanic_sample.csv')
questions = [
    'What is the survival rate overall and by class/gender?',
    'Are there any patterns in age, fare, or family size related to survival?',
    'Are there missing values or anomalies in the data?',
    'Does class, gender, or age have a statistically significant effect on survival?'
]
print('Questions to explore:')
for q in questions:
    print('-', q)
print('\nDataFrame Info:')
df.info()
print('\nDataFrame Head:')
print(df.head()) 
print('\nSurvival Rate by Class:')
print(df.groupby('Pclass')['Survived'].mean())
print('\nSurvival Rate by Gender:')
print(df.groupby('Sex')['Survived'].mean())
sns.barplot(x='Pclass', y='Survived', hue='Sex', data=df)
plt.title('Survival Rate by Class and Gender')
plt.show()
sns.histplot(df['Age'].dropna(), kde=True)
plt.title('Age Distribution')
plt.show()
contingency = pd.crosstab(df['Sex'], df['Survived'])
chi2, p, dof, expected = stats.chi2_contingency(contingency)
print(f'\nChi-square test for gender vs survival: p-value={p:.4f}')
print('\nMissing values:')
print(df.isnull().sum())
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
print('\nSurvival Rate by Family Size:')
print(df.groupby('FamilySize')['Survived'].mean())
sns.barplot(x='FamilySize', y='Survived', data=df)
plt.title('Survival Rate by Family Size')
plt.show()


z_scores = np.abs(stats.zscore(df['Fare'].fillna(0)))
outliers = df[z_scores > 3]
print(f'\nNumber of Fare outliers: {len(outliers)}')
if not outliers.empty:
    print(outliers[["PassengerId", "Fare"]])


corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()


df.to_csv('titanic_sample_enhanced.csv', index=False)
print('\nEnhanced dataset saved as titanic_sample_enhanced.csv')
