#  Fair Fares NYC: Expanding Access to Affordable Transportation
 MHC × MTA Inaugural Datathon Project 2024

This comprehensive analysis explores Fair Fares ridership data in NYC to understand how expanding eligibility can improve access to affordable public transportation. Using advanced data analysis techniques and visualization approaches, we identify key insights to inform policy recommendations that could make public transit more equitable for all New Yorkers.

---
##  Overview
The Fair Fares NYC program provides discounted metro cards for eligible residents, currently serving those at 120% of the Federal Poverty Level (FPL). Our analysis evaluates the potential impact of expanding eligibility to 200% FPL, with a focused examination of six key neighborhoods:
- Elmhurst/Jackson Heights  
- Flushing  
- Sunset Park  
- Brownsville  
- Morrisania  
- Highbridge  

###  Research Question  
How can expanding Fair Fares eligibility criteria to 200% of the FPL improve access to affordable public transportation in underserved NYC neighborhoods? Which subway lines, bus routes, and stations should be prioritized for expansion to maximize equity and usage?

---
##  Project Goals and Achievements 
1.  **Usage Pattern Analysis**  
   - Identified peak usage times (8:00 AM and 6:00 PM)
   - Discovered 1.77x higher weekday vs weekend usage
   - Mapped network effects between connected stations

2.  **Neighborhood Accessibility Analysis**  
   - Found highest adoption in Morrisania (9.57%) and Highbridge (8.50%)
   - Identified critical transfer points in each focus area
   - Mapped geographic spread of program adoption

3.  **CUNY Campus Impact**  
   - Analyzed ridership patterns around 2-year and 4-year institutions
   - Identified peak academic hours usage
   - Evaluated bus-subway integration near campuses

4.  **Policy Insights**  
   - Developed data-driven expansion recommendations
   - Identified high-impact transfer points
   - Created temporal usage profiles

---
##  Technical Framework  
- **Python**: Advanced data processing with memory optimization
- **SQL**: Complex queries for pattern analysis
- **Visualization**: Interactive maps and statistical charts
- **Jupyter**: Documented analysis workflow
- **Version Control**: Git-based collaboration

---

##  Repository Structure  

```
mhcXmta_datathon_project/
├── data/                     
│   ├── raw/                                          # Original MTA datasets                 
│   │   ├── readme.md                                 # Access to large datasets from Dropbox
│   ├── processed/                                    # Cleaned and optimized data           
│       ├── readme.md                                 # Access to large datasets from Dropbox
│   ├── additional_reports/                           # Supporting documentation   
│       ├── Fair-Fares-Expansion-Full-Report.pdf
│       ├── Public-Transportation-Subsidies-and-Racial-Equity.pdf
│
├── notebooks/               
│   ├── 01_exploratory_analysis.ipynb                 # Initial data exploration
│   ├── 02_neighborhood_analysis.ipynb                # Geographic patterns
│   ├── 03_cuny_analysis.ipynb                        # Campus impact
│   ├── 04_visualizations.ipynb                       # Complex pattern analysis
│
├── sql/                      
│   ├── subway_ridership_queries.sql                  # Subway analysis queries
│   ├── bus_ridership_queries.sql                     # Bus pattern queries
│
├── tableau/                 
│   ├── Comparison of Geographics.twb                 # Tableau work
│   ├── subway_chart.png
│   ├── subway_map_1.png
│   ├── subway_map_2.png
│   ├── bus_treemap.png
│   ├── NYC Aging Service Providers.cpg               # All these files for practice 
│   ├── NYC Aging Service Providers.dbf
│   ├── NYC Aging Service Providers.prj
│   ├── NYC Aging Service Providers.qmd
│   ├── NYC Aging Service Providers.shp
│   ├── NYC Aging Service Providers.shx
│
├── results/                  
│   ├── charts/                                       # Statistical visualizations
│   │   ├── eda_viz1s.png                             # EDA visualization for Subway (s)
│   │   ├── eda_viz1b.png                             # EDA visualization for Bus (b)
│   │   ├── eda_viz2s.png
│   │   ├── eda_viz2b.png
│   │   ├── eda_viz3s.png
│   │   ├── eda_viz3s.png
│   │   ├── eda_viz4s.png
│   │   ├── eda_viz4b.png
│   │   ├── eda_viz5.png
│   │   ├── bus&subway_viz.png
│   │   ├── bus&subway_neighborhood_viz.png
│   │   ├── bus&subway_peak_k/share_viz.png
│   │   ├── bus&subway_cuny_viz.png
│   │   ├── cuny_stations_viz.png
│   │   ├── 4_year_transfer_times_viz.png
│   │   ├── 2_year_transfer_times_viz.png
│   │   ├── network_analysis_viz.png
│   │   ├── time_series_viz.png
│   │   ├── cross-system_transfers_viz.png
│   ├── maps/                                        # Interactive geographic analysis
│       ├── fair_fares_heatmap.html
│
├── colab/
│   ├── main.ipynb                                   # Coding performed during Datathon Day 1
│   ├── refined_incomplete_work.ipynb                # Personal practice
│
├── config/                                          # Analysis parameters              
│   ├── settings.json
│
├── docs/                                            # Technical documentation                 
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

##  Methodology  


### 1⃣ Data Processing and Optimization
- Implemented chunked processing for 10GB+ datasets
- Developed memory-efficient analysis pipelines
- Created optimized data structures

### 2⃣ Network Analysis
- Mapped station connectivity patterns
- Analyzed transfer behaviors
- Identified usage correlation clusters

### 3⃣ Temporal Pattern Analysis
- Discovered peak usage periods
- Mapped seasonal variations
- Analyzed weekday/weekend differences

### 4⃣ Cross-System Integration
- Evaluated bus-subway coordination
- Analyzed transfer efficiencies
- Mapped system synchronization

---

##  Key Findings  

### Network Patterns
- Strong correlation in Fair Fares usage between connected stations
- Higher adoption rates in areas with efficient transfers
- Clear geographic spread patterns

### Temporal Insights
- Morning peak: 8:00 AM (2x average ridership)
- Evening peak: 6:00 PM (1.8x average)
- October shows highest monthly usage

### System Integration
- 98% correlation between bus and subway patterns
- 3-hour offset between mode peaks
- Higher transfer rates on bus routes

---
##  Conclusion  
Our analysis demonstrates that expanding Fair Fares eligibility to 200% FPL could significantly improve transit accessibility for working New Yorkers. Key opportunities include optimizing transfer points, adjusting service timing, and enhancing cross-mode integration. Strategic implementation focusing on high-impact areas could maximize the program's effectiveness while maintaining operational efficiency.

---

##  How to Run the Project  

1. Clone the repository:  
   ```bash
   git clone https://github.com/BasirS/mhcXmta_datathon_project.git 
   cd mhcXmta_datathon_project

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Run Jupyter Notebooks:
- Open Jupyter Notebooks (`.ipynb` files) in your preferred environment (Google Colab, Jupyter Lab, etc.) in sequential order.
- Run SQL scripts using your SQL client and use all the provided SQL queries for detailed analysis.

4. Open Tableau workbooks:
Use Tableau Desktop to load `.twbx` files and explore dashboards and/or other visualizations.

5. Explore interactive visualizations in results/maps!

---

##  References
- ["Making Fair Fares More Fair for More People"](https://pcac.org/report/fairfares/)
- ["Public Transportation Subsidies and Racial Equity"](https://static1.squarespace.com/static/53ee4f0be4b015b9c3690d84/t/666caf05ec78896060ea6814/1718398727325/Public-Transportation-Subsidies-and-Racial-Equity_A-Case-Study_NYC-Ferry-and-Fair-Fares-2024_Final-061424.pdf)
- [NYC Open Data portal](https://data.ny.gov/browse?q=&sortBy=relevance)

---

## Presentation

To share my findings and insights, I created a presentation, which summarizes my findings and includes all visualizations:

- **[Presentation PDF](https://drive.google.com/file/d/1iYncTgAVjepl0k6ZlnvNAORzEr3IkDY7/view?usp=sharing![image](https://github.com/user-attachments/assets/bcbb9e33-4946-4e20-9646-fb296e67d6a0))**  

---

**Together, we're making public transportation more equitable for all New Yorkers!**
