# 🎬 Netflix Data Analysis using Exploratory Data Analysis (EDA)

## 📌 Overview
Netflix hosts a vast library of movies and TV shows across multiple genres and countries.  
This project focuses on **exploratory data analysis (EDA)** to understand **content trends, genre distribution, release patterns, and regional availability** in the Netflix catalog.

The objective is to **extract insights from data**, not to build recommendation or prediction systems.

---

## 🎯 Objective
- Analyze Netflix content data to identify trends in movies and TV shows  
- Explore genre popularity and content distribution  
- Understand release year patterns and country-wise availability  
- Perform data cleaning and visualization for insight generation  

---

## 📂 Dataset Information
- **Type:** Netflix Movies and TV Shows dataset  
- **Format:** CSV  
- **Source:** Public Netflix dataset  
- **Records:** ~8,000 titles  

### Key Features
- show_id  
- type (Movie / TV Show)  
- title  
- director  
- cast  
- country  
- date_added  
- release_year  
- rating  
- duration  
- listed_in (genres)  

---

## 🧹 Data Cleaning & Preparation
- Handled missing values in director, cast, and country columns  
- Converted `date_added` to datetime format  
- Extracted year and month from date fields  
- Split and normalized multi-value categorical fields (genres, countries)  
- Removed duplicates and irrelevant columns where required  

---

## 🔍 Exploratory Data Analysis
The following analyses were conducted:

### Content Distribution Analysis
- Movies vs TV Shows count  
- Rating-wise content distribution  

### Time-Based Analysis
- Content added over the years  
- Release year trends  

### Genre Analysis
- Most popular genres on Netflix  
- Genre distribution across movies and TV shows  

### Country-Wise Analysis
- Top content-producing countries  
- Regional content availability patterns  

Visualizations were created using **Matplotlib** and **Seaborn**.

---

## 💡 Key Insights
- Netflix has a higher number of movies compared to TV shows  
- Content additions increased significantly after 2015  
- Drama and International Movies are among the most common genres  
- The United States and India contribute the highest number of titles  
- Recent years show a strong focus on global and regional content  

---

## 📊 Business Implications
- Understanding genre popularity can guide content acquisition strategies  
- Regional trends highlight the importance of localized content  
- Release year trends reflect Netflix’s expansion and content investment strategy  

---

## ⚠️ Limitations
- This analysis is descriptive and does not include viewer engagement data  
- No recommendation or prediction models are built  
- Dataset represents available titles, not user preferences  
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

netflix-data-analysis/
│
├── data/
│ └── netflix_titles.csv
│
├── notebook/
│ └── netflix_eda.ipynb
│
├── images/
│ └── plots.png
│
└── README.md


---

## 📌 Conclusion
This project demonstrates how exploratory data analysis can be used to uncover meaningful trends in streaming content catalogs and support data-driven decision-making.

---

## 👤 Author
**Rohit Ranvir**  
(Data Analysis & Python Enthusiast)

