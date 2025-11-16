Restaurant Data Analysis Project

A complete restaurant data analysis project built using Python, Pandas, Matplotlib, Seaborn, and ReportLab. 
 
This project performs data cleaning, statistical analysis, visualization, and automated PDF report generation based on the classic Tips dataset.

---

Project Structure

Restaurant-Data-Analysis-Project/

___data/               # Contains tips.csv dataset
___ src/               # Python scripts (analysis, charts, pdf converter)
___ charts/            # Auto-generated PNG, PDF, and SVG charts
___ reports/           # Auto-generated PDF reports
___ README.md
________________________________________
Features

1. Data Analysis (src/tips.py)
   
•	Gender-based tipping comparison
•	Tip percentage distribution
•	Total revenue per day
•	Smoking vs. tipping behaviour
•	Correlation matrix
•	Top 10 highest tip-percentage customers
•	Generates a formatted PDF report in reports/
________________________________________

2. Data Visualisation (src/tips_charts.py)

Automatically generates:
•	Scatter plot: Total Bill vs Tip
•	Histogram: Tip Percentage Distribution
•	Bar charts:
    o	Average tip percentage by day
    o	Customer count per day
    o	Average tip by group size
    o	Total revenue per day
    o	Gender count by time and by day
    o	Tip percentage by smoker status
•	Correlation heatmap

Charts are saved to:
•	charts/png/
•	charts/pdf/
•	charts/svg/
________________________________________

3. Python to PDF Conversion (src/py_to_pdf_converter.py)
Converts Python scripts into formatted, readable PDF files using ReportLab:

•	tips.py → reports/tips_script.pdf
•	tips_charts.py → reports/tips_charts.pdf
________________________________________

Installation

1. Clone the repository

git clone https://github.com/YOUR_USERNAME/Restaurant-Data-Analysis-Project.git
cd Restaurant-Data-Analysis-Project

Replace YOUR_USERNAME with your GitHub username.

2. (Optional) Create a virtual environment

python -m venv venv

# Windows:
venv\Scripts\activate

# macOS / Linux:

source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt
________________________________________

How to Run

Run the main analysis and generate the PDF report
python src/tips.py

This will:
•	Print all 14 analyses in the terminal
•	Generate reports/tips_advanced_report.pdf
________________________________________

Generate all charts
python src/tips_charts.py

This will create charts inside:
•	charts/png/
•	charts/pdf/
•	charts/svg/
________________________________________

Convert Python scripts to PDF
python src/py_to_pdf_converter.py

This will create:
•	reports/tips_script.pdf
•	reports/tips_charts.pdf
________________________________________

Dependencies

Main libraries:
•	pandas
•	numpy
•	matplotlib
•	seaborn
•	reportlab

See requirements.txt for the full list.
________________________________________
License

This project is licensed under the MIT License.
See the LICENSE file for details.
________________________________________

Contributing

Pull requests are welcome.

You can improve:
•	Visualisations
•	Statistical analyses
•	Report formatting
•	Code structure
________________________________________
Support

If you find this project useful, please consider giving the repository a star ⭐
