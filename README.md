# 🚢 Titanic Survival Analysis — Industry-Level EDA Project

## 📌 Overview

This project performs **Advanced Exploratory Data Analysis (EDA)** on the famous Titanic dataset using Python and Seaborn.

The analysis uncovers the major factors influencing passenger survival through:

* Data Cleaning
* Feature Engineering
* KPI Analysis
* Statistical Insights
* Data Visualization
* Business Intelligence Reporting

The goal is to extract meaningful insights and understand survival patterns during the Titanic disaster.

---

# 🎯 Business Problem Statement

The Titanic disaster resulted in massive loss of life, but survival was not random.

This project analyzes key factors such as:

* Gender impact on survival
* Passenger class influence
* Age distribution patterns
* Fare-based survival trends
* Embarkation port analysis
* Family size impact

to identify the major drivers behind passenger survival probability.

---

# 🛠️ Technologies Used

| Technology       | Purpose                           |
| ---------------- | --------------------------------- |
| Python           | Core Programming                  |
| Pandas           | Data Manipulation                 |
| NumPy            | Numerical Operations              |
| Matplotlib       | Data Visualization                |
| Seaborn          | Statistical Visualization         |
| Scikit-learn     | Data Preprocessing & ML Utilities |
| Jupyter Notebook | Interactive Analysis              |

---

# 📂 Dataset Source

The dataset is directly loaded using Seaborn:

```python
import seaborn as sns

df = sns.load_dataset("titanic")
```

✅ No external dataset download required.

---

# 📊 Key Performance Indicators (KPIs)

The project evaluates the following KPIs:

* Total Passengers
* Total Survivors
* Total Non-Survivors
* Overall Survival Rate
* Survival by Gender
* Survival by Passenger Class
* Fare Distribution Analysis
* Embarkation Port Analysis
* Family Size Impact

---

# 📈 Visualizations Generated

This project generates multiple insightful visualizations including:

| Visualization              | Description                  |
| -------------------------- | ---------------------------- |
| Survival Distribution      | Pie Chart                    |
| Gender Survival Comparison | Bar Plot                     |
| Passenger Class Analysis   | Count Plot                   |
| Age Distribution           | Histogram + KDE              |
| Fare vs Survival           | Box Plot                     |
| Embarkation Analysis       | Bar Plot                     |
| Family Size Impact         | Line Plot                    |
| Correlation Heatmap        | Feature Correlation Analysis |

All generated images are saved inside:

```bash
images/
```

---

# 🔍 Key Insights

## 1️⃣ Gender Plays a Major Role in Survival

Female passengers had significantly higher survival rates compared to males.

---

## 2️⃣ Socioeconomic Status Matters

First-class passengers had the highest survival probability.

---

## 3️⃣ Fare Correlates with Survival

Passengers who paid higher fares had better survival outcomes.

---

## 4️⃣ Children Had Priority

Younger passengers showed higher chances of survival.

---

## 5️⃣ Family Size Impacts Survival

Small to medium-sized family groups had better survival rates than solo travelers or very large families.

---

# 📁 Project Structure

```bash
Titanic-Survival-EDA/
│
├── src/
│   └── eda.py
│
├── notebooks/
│   └── Titanic_EDA.ipynb
│
├── images/
│   └── (Generated Visualizations)
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ How to Run This Project

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Gayathri-Reddy874/Titanic-Survival-EDA.git
cd Titanic-Survival-EDA
```

---

## 2️⃣ Create Virtual Environment (Recommended)

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

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

## 4️⃣ Run the EDA Script

```bash
python src/eda.py
```

---

# 📦 requirements.txt

```txt
pandas==2.0.3
numpy==1.24.3
matplotlib==3.7.2
seaborn==0.13.2
scikit-learn==1.3.0
```

---

# 🚀 Future Improvements

* Build Streamlit Interactive Dashboard
* Add Machine Learning Classification Models
* Deploy Web Application using Flask/Streamlit
* Perform Statistical Hypothesis Testing
* Integrate Power BI Dashboard
* Add Feature Engineering Pipeline
* Implement Automated Reporting

---

# 💡 Learning Outcomes

Through this project, the following concepts were practiced:

* Exploratory Data Analysis (EDA)
* Data Cleaning & Preprocessing
* Data Visualization
* Statistical Analysis
* Feature Correlation Analysis
* Business Insight Generation
* Python Data Analytics Workflow

---

# 👩‍💻 Author

## Mallareddygari Gayathri

**AI/ML Engineer | Data Science Enthusiast**

---

# ⭐ If You Like This Project

If you found this project useful, consider giving it a ⭐ on GitHub!
