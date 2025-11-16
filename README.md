# Restaurant-Data-Analysis-Project
A Python-based restaurant data analysis project using Pandas. Includes data cleaning, preprocessing, handling missing values, and generating insights on customer behaviour by gender, meal time, day, smoking status, and tipping patterns. Provides clear, organised results for real-world analysis.

# Tips Data Analysis & Visualization Project

This project performs advanced data analysis, visualization, and automated reporting using the famous Seaborn Tips dataset.
It includes:

•	14 detailed statistical analyses
•	Automatic generation of high-quality charts (PNG, PDF, SVG)
•	A professionally formatted PDF report
•	A PDF exporter for Python source files
•	Clean, modular Python scripts
________________________________________
Project Structure

project/
│
├── tips.csv
├── tips.py                # Main analysis + PDF report generator
├── tips_charts.py         # Chart generator (PNG/PDF/SVG)
├── py_to_pdf.py           # Python-to-PDF converter
├── tips_script.pdf
├── tips_charts.pdf
├── tips_advanced_report.pdf
│
└── charts/
    ├── png/
    ├── pdf/
    └── svg/
________________________________________
 Features
 
1. Complete Dataset Analysis (14 Analyses)
Includes:

•	Gender distribution by time of day
•	Gender distribution by day of week
•	Smoker vs. non-smoker breakdown
•	Total tip amount by gender
•	Average tips and tip percentages
•	Tip percentages by day and time
•	Group-size analyses
•	Correlation matrix
•	Revenue per day
•	Top 10 highest tip percentages
All analyses are printed in the terminal and included in a structured PDF.
________________________________________
2. High-Quality Chart Generation
   
The script generates multiple charts, including:

•	Scatter plots
•	Histograms
•	Bar charts
•	Clustered bar charts
•	Correlation heatmap
Charts are automatically saved in:
charts/png/
charts/pdf/
charts/svg/
________________________________________
 3. Professional PDF Reporting
    
The script generates:

•	tips_advanced_report.pdf – statistical tables in color
•	tips_script.pdf – Python script exported as a styled PDF
•	tips_charts.pdf – chart script exported as PDF
All PDF creation uses ReportLab.
________________________________________
How to Run

Install dependencies
pip install pandas matplotlib seaborn reportlab
Run the analysis + PDF generator
python tips.py
Generate charts
python tips_charts.py
Convert Python scripts to PDF
python py_to_pdf_converter.py
________________________________________
Generated Outputs

•	Terminal Output:
Cleanly formatted printout of all analyses.
•	PDF Report:
  o	Colored tables
  o	14 analysis sections
  o	High-resolution charts (via charts script)
•	Charts: 
Available in PNG, PDF, and SVG formats.
________________________________________
Dependencies

•	Python 3.8+
•	pandas
•	matplotlib
•	seaborn
•	reportlab
________________________________________
Contributions

Pull requests are welcome!
Feel free to contribute:

•	More visualizations
•	New statistical models
•	Machine learning predictions
•	Dashboard (Streamlit / Flask)

