# 🚇 Fair Fares NYC: Expanding Access to Affordable Transportation  
### 🏆 MHC × MTA Inaugural Datathon Project  

## 🌟 Overview  
This project explores the **Fair Fares NYC** program, which provides discounted metro cards for eligible residents. Our goal is to analyze the impact of expanding eligibility criteria to include individuals earning up to **200% of the federal poverty level**, focusing on transportation access in key neighborhoods:  
- Elmhurst/Jackson Heights  
- Flushing  
- Sunset Park  
- Brownsville  
- Morrisania  
- Highbridge  

### 💡 Research Question  
**How can expanding Fair Fares' eligibility criteria to “200% of the federal poverty level” improve access to affordable public transportation in these neighborhoods, and which subway lines and bus routes should be prioritized for expansion?**  

---

## 🎯 Project Goals  
1. 🛤️ **Analyze Transportation Usage Patterns**  
   - Identify which subway lines and bus routes Fair Fares passengers are using.  
2. 🗺️ **Geographic Analysis of Access Points**  
   - Visualize where Fair Fares passengers are entering the system, by borough and neighborhood.  
3. 🎓 **Impact on CUNY Campuses**  
   - Examine subway and bus ridership around CUNY 4-year and 2-year colleges.  
4. 🌆 **Neighborhood Analysis**  
   - Focus on key neighborhoods to identify priority routes for expanding access.  

---

## 🛠️ Tools and Technologies  
- **Python**: Data processing, cleaning, and analysis 📊  
- **SQL**: Querying ridership databases for actionable insights 🗄️  
- **Tableau**: Creating compelling data visualizations 📈  
- **Jupyter Notebooks**: Documenting code and workflows 📒  

---

## 📂 Repository Structure  

```
Fair-Fares-Project/
├── data/
│   ├── subway_hourly_ridership.csv
│   ├── bus_hourly_ridership.csv
│   ├── additional_reports/
│       ├── Fair-Fares-Expansion-Full-Report.pdf
│       ├── Public-Transportation-Subsidies-and-Racial-Equity.pdf
├── notebooks/
│   ├── data_cleaning.ipynb
│   ├── exploratory_analysis.ipynb
│   ├── neighborhood_analysis.ipynb
│   ├── cuny_analysis.ipynb
├── sql/
│   ├── subway_ridership_queries.sql
│   ├── bus_ridership_queries.sql
├── tableau/
│   ├── visualizations.twbx
├── scripts/
│   ├── data_preprocessing.py
│   ├── analysis_helpers.py
├── readme.md
└── requirements.txt
```


---

## 📊 Methodology  

### 1️⃣ **Data Cleaning and Preparation**  
- Use Python scripts to preprocess datasets (handle missing values, outliers, etc.).  

### 2️⃣ **SQL Querying**  
- Extract and aggregate ridership data by subway line, bus route, borough, and neighborhood.  

### 3️⃣ **Exploratory Data Analysis (EDA)**  
- Investigate ridership trends and identify the most-used subway lines and bus routes for Fair Fares riders.  

### 4️⃣ **Neighborhood Analysis**  
- Evaluate ridership in **Elmhurst/Jackson Heights, Flushing, Sunset Park, Brownsville, Morrisania, and Highbridge**.  
- Compare scenarios before and after eligibility expansion.  

### 5️⃣ **Impact on CUNY Campuses**  
- Analyze ridership near CUNY 4-year and 2-year colleges to uncover patterns.  

### 6️⃣ **Visualizations**  
- Use Tableau to create:  
  - Ridership distribution charts by subway lines and bus routes.  
  - Geographic heatmaps for Fair Fares ridership.  
  - Impact dashboards for eligibility expansion.  

---

## 🚀 Results  
_To Be Completed_  

### 📈 Visualizations  
_To Be Completed_  

### 🔍 Interpretation of Findings  
_To Be Completed_  

---

## 📜 Conclusion  
_To Be Completed_  

---

## 🛠️ How to Run the Project  

1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/FmhcXmta_datathon_project.git 
   cd Fair-Fares-Project  

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Run Jupyter Notebooks:
Open the Jupyter Notebooks (`.ipynb` files) either in Google Colab, Jupyter Notebook (local installation), JupyterLab (local installation), Deepnote, Kaggle Kernels. You should be able to run the cells directly within the editor.

4. Execute SQL scripts:
Use your preferred SQL client to run queries in the `sql/` directory.

5. Open Tableau workbooks:
Load `tableau/visualizations.twbx` to explore dashboards.

## 📚 References
- ["Making Fair Fares More Fair for More People"](https://pcac.org/report/fairfares/)
- ["Public Transportation Subsidies and Racial Equity"](https://static1.squarespace.com/static/53ee4f0be4b015b9c3690d84/t/666caf05ec78896060ea6814/1718398727325/Public-Transportation-Subsidies-and-Racial-Equity_A-Case-Study_NYC-Ferry-and-Fair-Fares-2024_Final-061424.pdf)
- [NYC Open Data portal](https://data.ny.gov/browse?q=&sortBy=relevance)

**🎉 Let’s create meaningful insights and make public transportation more equitable for NYC!**
