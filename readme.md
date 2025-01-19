# 🚇 Fair Fares NYC: Expanding Access to Affordable Transportation - \*Work In-Progress\*

🏆 MHC × MTA Inaugural Datathon Project

I'm analyzing Fair Fares ridership data in NYC to understand how expanding eligibility can improve access to affordable public transportation. I'm using data analysis and visualization techniques to identify key insights and inform policy recommendations. This project will allow me to develop my data analytics skills while contributing to a valuable cause.

---

## 🌟 Overview
This project explores the **Fair Fares NYC** program, which provides discounted metro cards for eligible residents. My goal is to analyze the impact of expanding eligibility criteria to include individuals earning up to **200% of the Federal Poverty Level (FPL)**, focusing on affordable transportation access in six key neighborhoods:  
- Elmhurst/Jackson Heights  
- Flushing  
- Sunset Park  
- Brownsville  
- Morrisania  
- Highbridge  

### 💡 Research Question  
**How can expanding Fair Fares eligibility criteria to 200% of the FPL improve access to affordable public transportation in underserved NYC neighborhoods? Which subway lines, bus routes, and stations should be prioritized for expansion to maximize equity and usage?**  

---

## 🎯 Project Goals  
1. 🛤️ **Identify Usage Patterns**  
   - Analyze how Fair Fares riders use subway and bus systems.  
2. 🗺️ **Neighborhood Accessibility Analysis**  
   - Evaluate ridership trends in Elmhurst, Flushing, Sunset Park, and other focus areas to determine transit equity gaps.  
3. 🎓 **Impact on CUNY Campuses**  
   - Understand ridership trends around commuter-heavy CUNY colleges, like Baruch, BMCC, and Hunter College.  
4. 📊 **Inform Policy Recommendations**  
   - Provide actionable insights for program expansion and public education campaigns. 

---

## 🛠️ Tools and Technologies  
- **Python**: Data processing, cleaning, and statistical analysis 📊  
- **SQL**: Querying MTA ridership datasets for granular insights 🗄️  
- **Tableau**: Creating compelling data visualizations 📈  
- **Jupyter Notebooks**: Documenting workflows and presenting data narratives 📒  

---

## 📂 Repository Structure  

```
mhcXmta_datathon_project/
├── data/                     
│   ├── raw/                  
│   │   ├── subway_hourly_ridership.csv
│   │   ├── bus_hourly_ridership.csv
│   ├── processed/           
│       ├── subway_cleaned.csv
│       ├── bus_cleaned.csv
│   ├── additional_reports/   
│       ├── Fair-Fares-Expansion-Full-Report.pdf
│       ├── Public-Transportation-Subsidies-and-Racial-Equity.pdf
│
├── notebooks/               
│   ├── 01_exploratory_analysis.ipynb
│   ├── 02_neighborhood_analysis.ipynb
│   ├── 03_cuny_analysis.ipynb
│   ├── 04_visualizations.ipynb
│
├── sql/                      
│   ├── subway_ridership_queries.sql
│   ├── bus_ridership_queries.sql
│
├── tableau/                 
│   ├── visualizations.twbx
│
├── results/                  
│   ├── charts/
│   │   ├── ridership_heatmap.png
│   │   ├── neighborhood_trends.png
│   ├── dashboards/
│       ├── expansion_impact_dashboard.twbx
│
├── config/                  
│   ├── settings.json
│
├── docs/                    
│   ├── methodology.md
│   ├── references.md
│
├── readme.md
├── .gitignore
├── code.py                 
├── requirements.txt        
├── environment.yml           
└── LICENSE                  
```


---

## 📊 Methodology  

### 1️⃣ **Data Collection and Cleaning**  
- Extract hourly ridership datasets for buses and subways from NYC Open Data.
- Use Python scripts to preprocess datasets (e.g., handle missing data, detect outliers, and prepare datasets) for analysis.  

### 2️⃣ **SQL Querying**  
- Extract and aggregate ridership data by time of day, subway line, bus route, borough, and neighborhood to identify patterns.  

### 3️⃣ **Exploratory Data Analysis (EDA)**  
- Investigate ridership trends and identify the most-used subway lines and bus routes for Fair Fares riders.
- Create visualizations to compare subway and bus usage across boroughs and stations.
- Map the ridership heat in underserved neighborhoods.  

### 4️⃣ **Granular Neighborhood Focus**  
- Deep dive into the six target neighborhoods, correlating ridership data with demographics, income, and proximity to CUNY campuses.
- Compare scenarios before and after eligibility expansion.  

### 5️⃣ **CUNY Campus Ridership**  
- Evaluate subway and bus usage near high-density commuter schools, focusing on differences between 2-year and 4-year institutions.  

### 6️⃣ **Visualizations**  
- Use Tableau to create:  
  - Ridership distribution charts by subway lines and bus routes.  
  - Geographic heatmaps for Fair Fares riders.  
  - Dashboard simulations of pre- and post-eligibility expansion ridership.  

---

## 🚀 Results  
_To Be Completed_  

### 📈 Visualizations  
_To Be Completed_  

### 🔍 Interpretation of Findings  
_To Be Completed_  

---

## 📜 Conclusion  
As my project aimed to illustrate how expanding Fair Fares eligibility criteria can address transit inequities and improve access to opportunities for NYC residents living paycheck-to-paycheck...

---

## 🛠️ How to Run the Project  

1. Clone the repository:  
   ```bash
   git clone https://github.com/BasirS/mhcXmta_datathon_project.git 
   cd mhcXmta_datathon_project

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Run Jupyter Notebooks:
- Open Jupyter Notebooks (`.ipynb` files) in your preferred environment (Google Colab, Jupyter Lab, etc.).
- Run SQL scripts using your SQL client.

4. Open Tableau workbooks:
Use Tableau Desktop to load `.twbx` files and explore dashboards and/or other visualizations.

---

## 📚 References
- ["Making Fair Fares More Fair for More People"](https://pcac.org/report/fairfares/)
- ["Public Transportation Subsidies and Racial Equity"](https://static1.squarespace.com/static/53ee4f0be4b015b9c3690d84/t/666caf05ec78896060ea6814/1718398727325/Public-Transportation-Subsidies-and-Racial-Equity_A-Case-Study_NYC-Ferry-and-Fair-Fares-2024_Final-061424.pdf)
- [NYC Open Data portal](https://data.ny.gov/browse?q=&sortBy=relevance)

---

**🎉 Let’s make public transportation more equitable for all New Yorkers!**
