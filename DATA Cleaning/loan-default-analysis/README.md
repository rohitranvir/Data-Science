# 📊 Loan Default Risk Analysis using Exploratory Data Analysis (EDA)

## 📌 Overview
Loan defaults pose a significant financial risk to lending institutions.  
This project focuses on **exploratory data analysis (EDA)** to understand **patterns and factors associated with loan default risk** using historical loan applicant data.

The goal is **not prediction**, but **risk understanding and business insight generation**.

---

## 🎯 Objective
- Analyze loan applicant data to identify factors linked to default risk  
- Understand the relationship between income, loan amount, credit history, and loan status  
- Derive actionable **business insights** using data visualization  

---

## 📂 Dataset Information
- **Type:** Loan approval / loan default dataset  
- **Format:** CSV  
- **Records:** ~600  
- **Target Variable:** `Loan_Status` (Default / Non-Default)

### Key Features
- ApplicantIncome  
- CoapplicantIncome  
- LoanAmount  
- Loan_Amount_Term  
- Credit_History  
- Education  
- Self_Employed  
- Loan_Status  

---

## 🧹 Data Cleaning & Preparation
- Handled missing values:
  - **Categorical features:** Mode
  - **Numerical features:** Median
- Converted loan status labels into business-readable categories
- Verified and corrected data types
- Created new feature:
  - **TotalIncome = ApplicantIncome + CoapplicantIncome**

---

## 🔍 Exploratory Data Analysis
The following analyses were performed:

### Univariate Analysis
- Loan status distribution
- Applicant income distribution
- Loan amount distribution

### Bivariate Analysis
- Credit history vs loan status  
- Income vs loan status  
- Loan amount vs loan status  
- Employment type vs loan status  
- Education level vs loan status  

### Correlation Analysis
- Heatmap for numerical features to identify relationships

Visualizations were created using **Matplotlib** and **Seaborn**.

---

## 💡 Key Insights
- Applicants **without credit history** show significantly higher default rates  
- Lower income groups tend to have higher default occurrences, though overlap exists  
- Loan amount alone is not a strong indicator of default risk  
- Employment type and education show minor but noticeable patterns  
- Credit history is the **most influential risk-related feature**  

---

## 🏦 Business Implications
- Credit history should be prioritized during loan evaluation  
- Income-to-loan ratio can help flag high-risk applications  
- Risk assessment should consider **multiple factors together**, not in isolation  

---

## ⚠️ Limitations
- This project is **purely exploratory** and does not include predictive modeling  
- Results are dependent on dataset quality and size  
- Findings may not generalize across regions or financial institutions  
- Correlation does not imply causation  

---

## 🛠️ Tools & Technologies
- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  

---

## 📁 Project Structure
loan-default-risk-analysis/
│
├── data/
│ └── loan_data.csv
│
├── notebook/
│ └── loan_default_eda.ipynb
│
├── images/
│ └── visualizations.png
│
└── README.md


---

## 📌 Conclusion
This project demonstrates how **exploratory data analysis** can uncover meaningful patterns in financial data and support better decision-making before applying predictive models.

---

## 👤 Author
**Rohit Ranvir**  
(Data Analysis & Python Enthusiast)

