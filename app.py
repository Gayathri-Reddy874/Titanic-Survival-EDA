import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# =====================================
# Page Config
# =====================================
st.set_page_config(
    page_title="Titanic Survival Dashboard",
    layout="wide"
)

st.title("🚢 Titanic Survival Analysis Dashboard")

# =====================================
# Load Data
# =====================================
@st.cache_data
def load_data():
    df = sns.load_dataset("titanic")

    df["age"] = df["age"].fillna(df["age"].median())
    df["fare"] = df["fare"].fillna(df["fare"].median())
    df["embarked"] = df["embarked"].fillna(df["embarked"].mode()[0])

    df["FamilySize"] = df["sibsp"] + df["parch"] + 1

    return df

df = load_data()

# =====================================
# Sidebar Filters
# =====================================
st.sidebar.header("🔍 Filters")

pclass = st.sidebar.multiselect(
    "Passenger Class",
    options=sorted(df["pclass"].unique()),
    default=sorted(df["pclass"].unique())
)

sex = st.sidebar.multiselect(
    "Gender",
    options=df["sex"].unique(),
    default=df["sex"].unique()
)

df_filtered = df[(df["pclass"].isin(pclass)) & (df["sex"].isin(sex))]

# =====================================
# KPIs
# =====================================
st.subheader("📊 Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Passengers", len(df_filtered))
col2.metric("Survivors", int(df_filtered["survived"].sum()))
col3.metric("Survival Rate (%)",
            round(df_filtered["survived"].mean() * 100, 2))
col4.metric("Avg Fare", round(df_filtered["fare"].mean(), 2))

# =====================================
# Charts Section
# =====================================

st.subheader("📈 Data Visualizations")

tab1, tab2, tab3, tab4 = st.tabs([
    "Survival", "Gender", "Class", "Age"
])

# -----------------------------
# Survival Distribution
# -----------------------------
with tab1:
    fig, ax = plt.subplots()
    df_filtered["survived"].value_counts().plot(
        kind="pie",
        autopct="%1.1f%%",
        labels=["Not Survived", "Survived"],
        ax=ax
    )
    ax.set_ylabel("")
    st.pyplot(fig)

# -----------------------------
# Gender Analysis
# -----------------------------
with tab2:
    fig, ax = plt.subplots()
    sns.barplot(
        data=df_filtered,
        x="sex",
        y="survived",
        ax=ax
    )
    ax.set_title("Survival Rate by Gender")
    st.pyplot(fig)

# -----------------------------
# Class Analysis
# -----------------------------
with tab3:
    fig, ax = plt.subplots()
    sns.countplot(
        data=df_filtered,
        x="pclass",
        hue="survived",
        ax=ax
    )
    ax.set_title("Survival by Passenger Class")
    st.pyplot(fig)

# -----------------------------
# Age Distribution
# -----------------------------
with tab4:
    fig, ax = plt.subplots()
    sns.histplot(
        data=df_filtered,
        x="age",
        hue="survived",
        kde=True,
        bins=30,
        ax=ax
    )
    ax.set_title("Age Distribution by Survival")
    st.pyplot(fig)

# =====================================
# Insights Section
# =====================================
st.subheader("💡 Insights")

st.markdown("""
- Women had higher survival probability than men.
- First-class passengers had better survival rates.
- Children were prioritized during rescue.
- Higher fare passengers survived more often.
""")