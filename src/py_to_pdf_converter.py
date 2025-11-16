import os
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter


# ===========================
# Base directories
# ===========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))       # .../Tips/src
REPORT_DIR = os.path.join(BASE_DIR, "..", "reports")        # .../Tips/reports

if not os.path.exists(REPORT_DIR):
    os.makedirs(REPORT_DIR)

# ===========================
# Function to convert py → pdf
# ===========================


def py_to_pdf(input_filename, output_filename):

    input_path = os.path.join(BASE_DIR, input_filename)
    output_path = os.path.join(REPORT_DIR, output_filename)

    styles = getSampleStyleSheet()
    doc = SimpleDocTemplate(output_path, pagesize=letter)
    story = []

    # Read python file content
    with open(input_path, 'r', encoding='utf-8') as f:
        code = f.read()

    # Replace line breaks for PDF formatting
    code = code.replace("\n", "<br/>")

    story.append(
        Paragraph(f"Python Script: {input_filename}", styles["Title"]))
    story.append(Spacer(1, 20))
    story.append(
        Paragraph(f"<font face='Courier'>{code}</font>", styles["BodyText"]))

    doc.build(story)
    print(f"Created PDF: {output_path}")


# ===========================
# Convert Python scripts to PDF
# ===========================
py_to_pdf("tips.py", "tips_script.pdf")
py_to_pdf("tips_charts.py", "tips_charts.pdf")
