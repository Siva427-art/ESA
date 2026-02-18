

# 🚢 Titanic EDA & ML Suite

A next-generation, production-grade **Python data science & machine learning suite** for advanced exploratory data analysis (EDA), visualization, and predictive modeling of the Titanic dataset — designed and engineered by **Siva**.

![Python](https://img.shields.io/badge/Python-3.7%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen?style=for-the-badge)
![Data](https://img.shields.io/badge/Datasets-2-blue?style=for-the-badge)
![Visualizations](https://img.shields.io/badge/Visualizations-15%2B-orange?style=for-the-badge)
![ML Models](https://img.shields.io/badge/ML%20Models-5%2B-9cf?style=for-the-badge)
![UI](https://img.shields.io/badge/UI-Streamlit%20%7C%20Jupyter%20Lab-green?style=for-the-badge)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-blue?style=for-the-badge)
![Tests](https://img.shields.io/badge/Tests-Unit%20%7C%20Integration-red?style=for-the-badge)
![Author](https://img.shields.io/badge/Author-Siva-blueviolet?style=for-the-badge)

---

## 📋 Table of Contents

- [Features](#-features)
- [Tech Stack](#️-tech-stack)
- [Data Schema](#-data-schema)
- [Project Structure](#-project-structure)
- [How to Run](#-how-to-run)
- [Demo Commands](#-demo-commands)
- [Visualizations](#-visualizations)
- [Machine Learning](#-machine-learning)
- [Automation & CI/CD](#-automation--cicd)
- [What Makes This Extra Advanced](#-what-makes-this-project-extra-advanced)
- [Author](#-author)

---

## ✨ Features

| Category | Feature | Details |
|----------|---------|---------|
| 📊 **EDA** | Data Cleaning | Missing value handling, type conversion, imputation, outlier removal |
| 🏷️ **Feature Engineering** | Family size, title extraction, fare bins, age groups, one-hot encoding |
| 📈 **Analysis** | Survival Analysis | By class, gender, age, fare, family size, feature importance |
| 🔥 **ML Modeling** | Logistic Regression, Random Forest, XGBoost, SVM, Voting Ensemble |
| 📉 **Outlier Detection** | Boxplots, z-score filtering, IQR, robust scaling |
| 📊 **Visualization** | Bar, pie, violin, swarm, heatmap, pairplot, SHAP plots |
| 🧪 **Hypothesis Testing** | Chi-square, t-test, ANOVA, permutation tests |
| 🧩 **Custom UI** | Streamlit dashboard, Jupyter Lab notebooks, interactive widgets |
| 🛡️ **Validation** | Cross-validation, ROC-AUC, confusion matrix, classification report |
| 📦 **Export** | Enhanced CSV, model pickle, prediction CSV |

---

## 🛠️ Tech Stack

| Component       | Details                                      |
|-----------------|----------------------------------------------|
| **Language**    | Python 3.7+                                  |
| **Libraries**   | pandas, matplotlib, seaborn, scikit-learn, xgboost, streamlit, jupyterlab |
| **Data**        | titanic_sample.csv, titanic_sample_enhanced.csv |
| **UI**          | Streamlit (optional)                         |

---

## 🗃️ Data Schema

| Column         | Description                |
|----------------|---------------------------|
| PassengerId    | Unique ID                 |
| Survived       | Survival (0 = No, 1 = Yes)|
| Pclass         | Ticket class (1/2/3)      |
| Name           | Name (with title)         |
| Sex            | Gender                    |
| Age            | Age in years              |
| SibSp          | # Siblings/Spouses aboard |
| Parch          | # Parents/Children aboard |
| Ticket         | Ticket number             |
| Fare           | Passenger fare            |
| Cabin          | Cabin number              |
| Embarked       | Port of Embarkation       |
| Title          | Extracted from Name       |
| FamilySize     | SibSp + Parch + 1         |
| AgeGroup       | Binned age feature        |
| FareBin        | Binned fare feature       |

---

## 📁 Project Structure

```
eda_analysis.py              # Main EDA & ML script
eda_app.py                  # Streamlit UI (optional)
notebooks/                  # Jupyter notebooks (advanced EDA/ML)
titanic_sample.csv           # Sample Titanic data
titanic_sample_enhanced.csv  # Enhanced Titanic data
models/                      # Saved ML models (pickle)
outputs/                     # Predictions, plots, reports
readme                       # Project documentation
.github/workflows/           # CI/CD pipelines
__pycache__/
```

---

## 🚀 How to Run

### Prerequisites
- Python 3.7 or higher
- Recommended: pip install pandas matplotlib seaborn streamlit

### Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/siva/titanic-eda-visualization.git
cd titanic-eda-visualization

# 2. Install dependencies
pip install pandas matplotlib seaborn streamlit

# 3. Run the EDA & ML script
python eda_analysis.py

# 4. (Optional) Run the Streamlit UI
streamlit run eda_app.py

# 5. (Optional) Explore in Jupyter Lab
jupyter lab
```

---

## 🖥️ Demo Commands

```bash
# Run EDA & ML script
python eda_analysis.py

# Run Streamlit dashboard
streamlit run eda_app.py

# Open advanced EDA/ML notebook
jupyter lab notebooks/eda_ml.ipynb
```

---


## 📊 Visualizations

- Survival by class, gender, age, fare, family size
- Correlation heatmap (Pearson, Cramér’s V)
- Fare & age distribution (hist, KDE, violin)
- Family size impact (bar, swarm)
- Outlier boxplots (z-score, IQR)
- Pairplot of key features
- SHAP/feature importance plots (ML)
- ROC, confusion matrix, learning curves
- Custom interactive charts (Streamlit)

---


## 🤖 Machine Learning

- Data preprocessing & feature selection
- Model training: Logistic Regression, Random Forest, XGBoost, SVM, Voting Ensemble
- Hyperparameter tuning (GridSearchCV)
- Cross-validation, ROC-AUC, classification report
- Model explainability: SHAP, permutation importance
- Export: Pickle models, prediction CSV

---

## 🔄 Automation & CI/CD

- Automated testing (pytest, unittest)
- Linting & formatting (black, flake8)
- GitHub Actions for CI/CD: test, build, deploy
- Notebook execution checks
- Model versioning & artifact storage

---

## 🚀 What Makes This Project Extra Advanced

| Concept | Implementation |
|---------|---------------|
| **Full ML Pipeline** | EDA → Feature Eng → Modeling → Explainability → Export |
| **Production Ready** | CI/CD, tests, code quality, modular design |
| **Interactive UI** | Streamlit dashboard, Jupyter Lab notebooks |
| **Model Explainability** | SHAP, permutation importance, feature ranking |
| **Automation** | GitHub Actions, auto-reporting, artifact storage |
| **Advanced Visualization** | 15+ plot types, interactive widgets |
| **Reproducibility** | Seeded splits, notebook pipelines |
| **Documentation** | Rich markdown, badges, code comments |

---

## 👤 Author

**Siva**

---

## 📄 License

This project is open source and available under the MIT License.

---

<p align="center">
  ⭐ If you found this project useful, consider giving it a star!
</p>
