# =========================================
# Titanic Survival Analysis - EDA Project
# Using Seaborn Dataset
# =========================================

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import os

warnings.filterwarnings('ignore')

# Plot Styling
plt.style.use('ggplot')
sns.set_theme(style='whitegrid')

# =========================================
# Load Dataset (SEABORN)
# =========================================

print("Loading Titanic Dataset from Seaborn...")

df = sns.load_dataset("titanic")

print("Dataset Loaded Successfully!")

# =========================================
# Create Images Folder
# =========================================

if not os.path.exists('images'):
    os.makedirs('images')

# =========================================
# Basic Dataset Information
# =========================================

print("\n===== DATASET SHAPE =====")
print(df.shape)

print("\n===== DATASET COLUMNS =====")
print(df.columns)

print("\n===== DATASET INFO =====")
print(df.info())

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== STATISTICAL SUMMARY =====")
print(df.describe(include='all'))

# =========================================
# Data Cleaning
# =========================================

print("\n===== DATA CLEANING =====")

df['age'] = df['age'].fillna(df['age'].median())
df['fare'] = df['fare'].fillna(df['fare'].median())
df['embarked'] = df['embarked'].fillna(df['embarked'].mode()[0])

# Drop cabin (too many missing values)
df.drop(columns=['deck'], inplace=True, errors='ignore')

print("Missing Values Handled Successfully!")

# =========================================
# Feature Engineering
# =========================================

print("\n===== FEATURE ENGINEERING =====")

df['FamilySize'] = df['sibsp'] + df['parch'] + 1

bins = [0, 12, 19, 59, 100]
labels = ['Child', 'Teen', 'Adult', 'Senior']

df['AgeGroup'] = pd.cut(df['age'], bins=bins, labels=labels)

print("Feature Engineering Completed!")

# =========================================
# KPI Calculations
# =========================================

print("\n===== BUSINESS KPIs =====")

total_passengers = len(df)
total_survivors = (df['survived'] == 1).sum()
total_non_survivors = (df['survived'] == 0).sum()

survival_rate = round((total_survivors / total_passengers) * 100, 2)

print(f"Total Passengers: {total_passengers}")
print(f"Total Survivors: {total_survivors}")
print(f"Total Non-Survivors: {total_non_survivors}")
print(f"Overall Survival Rate: {survival_rate}%")

# =========================================
# 1. Survival Distribution
# =========================================

plt.figure(figsize=(7, 7))

labels = ['Not Survived', 'Survived']
colors = ['#ff6b6b', '#4ecdc4']

df['survived'].value_counts().plot(
    kind='pie',
    autopct='%1.1f%%',
    labels=labels,
    colors=colors,
    startangle=90
)

plt.title('Survival Distribution')
plt.savefig('images/survival_distribution.png', bbox_inches='tight')
plt.show()

# =========================================
# 2. Survival by Gender
# =========================================

plt.figure(figsize=(8, 5))

gender_survival = df.groupby('sex')['survived'].mean() * 100

sns.barplot(x=gender_survival.index, y=gender_survival.values, palette='viridis')

plt.title('Survival Rate by Gender')
plt.xlabel('Gender')
plt.ylabel('Survival Rate (%)')

for i, v in enumerate(gender_survival.values):
    plt.text(i, v + 1, f"{v:.1f}%", ha='center')

plt.savefig('images/gender_survival.png', bbox_inches='tight')
plt.show()

# =========================================
# 3. Survival by Passenger Class
# =========================================

plt.figure(figsize=(8, 5))

sns.countplot(data=df, x='pclass', hue='survived', palette='Set2')

plt.title('Survival Distribution by Passenger Class')
plt.savefig('images/class_survival.png', bbox_inches='tight')
plt.show()

# =========================================
# 4. Age Distribution by Survival
# =========================================

plt.figure(figsize=(10, 6))

sns.histplot(data=df, x='age', hue='survived', bins=30, kde=True)

plt.title('Age Distribution by Survival')
plt.savefig('images/age_distribution.png', bbox_inches='tight')
plt.show()

# =========================================
# 5. Fare vs Survival
# =========================================

plt.figure(figsize=(8, 5))

sns.boxplot(data=df, x='survived', y='fare')

plt.title('Fare Distribution by Survival')
plt.savefig('images/fare_vs_survival.png', bbox_inches='tight')
plt.show()

# =========================================
# 6. Embarkation Analysis
# =========================================

plt.figure(figsize=(8, 5))

embark_survival = df.groupby('embarked')['survived'].mean() * 100

sns.barplot(x=embark_survival.index, y=embark_survival.values, palette='magma')

plt.title('Survival Rate by Embarkation Port')

for i, v in enumerate(embark_survival.values):
    plt.text(i, v + 1, f"{v:.1f}%", ha='center')

plt.savefig('images/embarkation_survival.png', bbox_inches='tight')
plt.show()

# =========================================
# 7. Family Size Impact
# =========================================

plt.figure(figsize=(10, 5))

family_survival = df.groupby('FamilySize')['survived'].mean() * 100

sns.lineplot(x=family_survival.index, y=family_survival.values, marker='o')

plt.title('Survival Rate by Family Size')
plt.savefig('images/family_size_survival.png', bbox_inches='tight')
plt.show()

# =========================================
# Correlation Heatmap
# =========================================

print("\n===== CORRELATION ANALYSIS =====")

encoded_df = df.copy()

encoded_df['sex'] = encoded_df['sex'].map({'male': 0, 'female': 1})
encoded_df['embarked'] = encoded_df['embarked'].map({'S': 0, 'C': 1, 'Q': 2})

numeric_cols = ['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'fare', 'FamilySize']

plt.figure(figsize=(12, 8))

sns.heatmap(encoded_df[numeric_cols].corr(), annot=True, cmap='coolwarm')

plt.title('Feature Correlation Heatmap')

plt.savefig('images/correlation_heatmap.png', bbox_inches='tight')
plt.show()

# =========================================
# Insights
# =========================================

print("\n===== BUSINESS INSIGHTS =====")

print("Female Survival Rate:",
      df[df['sex'] == 'female']['survived'].mean() * 100)

print("Male Survival Rate:",
      df[df['sex'] == 'male']['survived'].mean() * 100)

print("\nSurvival by Class:")
print(df.groupby('pclass')['survived'].mean() * 100)

print("\nEDA Completed Successfully!")