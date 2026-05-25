# 🚢 Titanic Survival Analysis — End-to-End EDA + Streamlit Dashboard

## 📌 Overview

This project is an **End-to-End Data Science EDA Solution** combining:

* 📓 **Jupyter Notebook** for Exploratory Data Analysis
* 🚀 **Streamlit Dashboard** for Interactive Data Visualization

The project analyzes Titanic passenger data to uncover survival patterns based on:

* Gender
* Passenger Class
* Age
* Fare
* Family Size

The goal is to derive meaningful insights through data analysis and visualization.

---

# 🎯 Objective

To explore and visualize the key factors that influenced passenger survival on the Titanic using:

* Exploratory Data Analysis (EDA)
* Data Cleaning
* Feature Engineering
* Statistical Analysis
* Interactive Dashboard Visualization

---

# 🧠 Business Problem Statement

The Titanic disaster demonstrated that survival was influenced by multiple socio-economic and demographic factors.

This project answers critical questions such as:

* Who survived and why?
* Did gender influence survival?
* Did passenger class impact survival chances?
* Were children prioritized during rescue?
* How did fare affect survival probability?
* Does family size influence survival outcomes?

---

# 📊 Project Components

## 📓 1. Jupyter Notebook — EDA Analysis

Located in:

```bash
notebooks/Titanic_EDA.ipynb
```

### Includes:

* Data Loading using Seaborn
* Data Cleaning & Missing Value Handling
* Feature Engineering
* Statistical Summaries
* Exploratory Data Analysis
* Correlation Analysis
* Data Visualization

---

## 🚀 2. Streamlit Dashboard — Interactive Analytics App

Main application file:

```bash
app.py
```

### Dashboard Features:

* Interactive Filters

  * Gender Filter
  * Passenger Class Filter

* KPI Metrics Dashboard

  * Total Passengers
  * Survival Rate
  * Total Survivors
  * Total Non-Survivors

* Interactive Visualizations

  * Survival Distribution
  * Gender Analysis
  * Passenger Class Analysis
  * Age Distribution
  * Fare Analysis

---

# 🛠️ Technologies Used

| Technology       | Purpose                   |
| ---------------- | ------------------------- |
| Python           | Core Programming          |
| Pandas           | Data Manipulation         |
| NumPy            | Numerical Computing       |
| Matplotlib       | Data Visualization        |
| Seaborn          | Statistical Visualization |
| Streamlit        | Interactive Dashboard     |
| Jupyter Notebook | Exploratory Analysis      |

---

# 📊 Dataset

The dataset is directly loaded using Seaborn:

```python
import seaborn as sns

df = sns.load_dataset("titanic")
```

### ✅ Dataset Advantages

* No API required
* No external CSV download needed
* Fully reproducible workflow

---

# 📁 Project Structure

```
Titanic-Survival-EDA/
│
├── app.py                       # Streamlit Dashboard
│
├── notebooks/
│   └── Titanic_EDA.ipynb        # Full EDA Notebook
│
├── src/
│   └── eda.py                   # Script Version
│
├── images/                      # Saved Visualizations
│
├── requirements.txt             # Project Dependencies
├── README.md                    # Documentation
└── .gitignore
```

---

# ▶️ How to Run the Project

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Gayathri-Reddy874/Titanic-Survival-EDA.git
cd Titanic-Survival-EDA
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash 
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash 
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Run Jupyter Notebook (EDA)

```bash
jupyter notebook
```

Open:

```bash
notebooks/Titanic_EDA.ipynb
```

---

## 5️⃣ Run Streamlit Dashboard

```bash
streamlit run app.py
```

---

# 🌐 Deployment

This project is deployed using **Streamlit Cloud**.

### Live Application

```
Titanic_Survival(https://titanic-survival-eda-fgdw7zpuxucb6qrtbvqucw.streamlit.app/)
```

---

# 📊 Key Insights

## 👩 Gender Impact

Female passengers had significantly higher survival rates compared to males.

---

## 🏛 Passenger Class Influence

First-class passengers had the highest probability of survival.

---

## 👶 Age Factor

Children were prioritized during rescue operations and showed higher survival rates.

---

## 💰 Fare Influence

Passengers who paid higher fares generally had better survival chances.

---

## 👨‍👩‍👧 Family Size Impact

Small to medium-sized family groups had higher survival rates compared to solo travelers or very large families.

---

# 📈 Visualizations Included

The project generates several analytical visualizations:

* Survival Distribution Pie Chart
* Gender-Based Survival Bar Plot
* Passenger Class Count Plot
* Age Distribution Histogram + KDE
* Fare vs Survival Box Plot
* Embarkation Port Analysis
* Family Size Analysis
* Correlation Heatmap

---

# 🚀 Future Enhancements

* Add Machine Learning Survival Prediction Model
* Deploy with GitHub + Streamlit Cloud CI/CD
* Add Power BI Dashboard Integration
* Build SQL-Based Data Pipeline
* Add Authentication System
* Improve UI with Multi-Page Navigation
* Add Real-Time Analytics Features

---

# 📚 Learning Outcomes

This project demonstrates practical understanding of:

* Exploratory Data Analysis (EDA)
* Data Cleaning & Preprocessing
* Feature Engineering
* Statistical Analysis
* Data Visualization
* Dashboard Development
* Streamlit Application Development
* Business Insight Generation

---

# 👩‍💻 Author

## Mallareddygari Gayathri

**AI/ML Engineer | Data Science Enthusiast**

---

# ⭐ Support

If you found this project useful:

* ⭐ Star the Repository

---
