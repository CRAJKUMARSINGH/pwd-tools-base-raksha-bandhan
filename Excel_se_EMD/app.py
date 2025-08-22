from flask import Flask, render_template, request, send_file, jsonify
import io
import pandas as pd
from jinja2 import Template
import pdfkit
import os
from num2words import num2words
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors

app = Flask(__name__)

# Configure wkhtmltopdf path (OS-aware)
import os

wkhtmltopdf_path = None
config = None
try:
    if os.name == 'nt':
        candidate = 'C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'
        if os.path.exists(candidate):
            wkhtmltopdf_path = candidate
    else:
        candidate = '/usr/bin/wkhtmltopdf'
        if os.path.exists(candidate):
            wkhtmltopdf_path = candidate
    if wkhtmltopdf_path:
        config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)
except Exception:
    config = None

# Improved HTML template for the receipt
receipt_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=210mm, height: 297mm">
    <title>Hand Receipt (RPWA 28)</title>
    <style>
        body { font-family: sans-serif; margin: 0; }
        @page {
            margin: 10mm;  /* Page margins */
        }
        .container {
            width: 210mm !important; /* Added !important */
            min-height: 297mm;
            margin: 10mm 20mm !important; /* Added !important */
            border: 2px solid #ccc !important;
            padding: 0mm; /* Changed to 0mm */
            box-sizing: border-box;
            position: relative;
            page-break-before: always;
        }
        .container:first-child {
            page-break-before: auto;
        }
        .header { text-align: center; margin-bottom: 2px; }
        .details { margin-bottom: 1px; }
        .amount-words { font-style: italic; }
        .signature-area { width: 100%; border-collapse: collapse; margin-top: 20px; }
        .signature-area td, .signature-area th {
            border: 1px solid #ccc !important;
            padding: 5px;
            text-align: left;
        }
        .offices { width: 100%; border-collapse: collapse; margin-top: 20px; }
        .offices td, .offices th {
            border: 1px solid black !important;
            padding: 5px;
            text-align: left;
            word-wrap: break-word;
        }
        .input-field { border-bottom: 1px dotted #ccc; padding: 3px; width: calc(100% - 10px); display: inline-block; }
        .seal-container { position: absolute; left: 10mm; bottom: 10mm; width: 40mm; height: 25mm; z-index: 10; }
        .seal { max-width: 100%; max-height: 100%; text-align: center; line-height: 40mm; color: blue; display: flex; justify-content: space-around; align-items: center; }
        .bottom-left-box { 
            position: absolute; bottom: 40mm; left: 40mm; 
            border: 2px solid blue; padding: 10px; 
            width: 450px; text-align: left; height: 55mm; 
            color: blue; 
        }
        .bottom-left-box p { margin: 3px 0; }
         @media print {
            .container {
                border: none;
                width: 210mm;
                min-height: 297mm;
                margin: 0;
                padding: 0;
            }
        }
    </style>
</head>
<body>
    {% for receipt in receipts %}
    <div class="container">
        <div class="header">
            <h2>Payable to: - {{ receipt.payee }} ( Electric Contractor)</h2>
            <h2>HAND RECEIPT (RPWA 28)</h2>
            <p>(Referred to in PWF&A Rules 418,424,436 & 438)</p>
            <p>Division - PWD Electric Division, Udaipur</p>
        </div>
        <div class="details">
            <p>(1)Cash Book Voucher No. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Date &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>
            <p>(2)Cheque No. and Date &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>
            <p>(3) Pay for ECS Rs.{{ receipt.amount }}/- (Rupees <span class="amount-words">{{ receipt.amount_words }} Only</span>)</p>
            <p>(4) Paid by me</p>
            <p>(5) Received from The Executive Engineer PWD Electric Division, Udaipur the sum of Rs. {{ receipt.amount }}/- (Rupees <span class="amount-words">{{ receipt.amount_words }} Only</span>)</p>
            <p> Name of work for which payment is made: <span id="work-name" class="input-field">{{ receipt.work }}</span></p>
            <p> Chargeable to Head:- 8443 [EMD- Refund] </p>
            <table class="signature-area">
                <tr>
                    <td>Witness</td>
                    <td>Stamp</td>
                    <td>Signature of payee</td>
                </tr>
                <tr>
                    <td>Cash Book No. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Page No. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
                    <td></td>
                    <td></td>
                </tr>
            </table>
            <table class="offices">
                <tr>
                    <td>For use in the Divisional Office</td>
                    <td>For use in the Accountant General's office</td>
                </tr>
                <tr>
                    <td>Checked</td>
                    <td>Audited/Reviewed</td>
                </tr>
                <tr>
                    <td>Accounts Clerk</td>
                    <td>DA &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Auditor &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Supdt. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; G.O.</td>
                </tr>
            </table>
        </div>
        <div class="seal-container">
            <div class="seal">
                <p></p>
                <p></p>
                <p></p>
            </div>
        </div>
        <div class="bottom-left-box">
                <p></p>
                <p></p>
                <p></p>
            <p> Passed for Rs. {{ receipt.amount }}</p>
            <p> In Words Rupees: {{ receipt.amount_words }} Only</p>
            <p> Chargeable to Head:- 8443 [EMD- Refund]</p>
            <div class="seal">
                <p>Ar.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;D.A.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;E.E.</p>
            </div>
        </div>
    </div>
    {% endfor %}
</body>
</html>
"""

def _validate_columns(df: pd.DataFrame) -> None:
    required = ["Payee Name", "Amount", "Work"]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(missing)}")


def _rows_to_receipts(df: pd.DataFrame, limit: int = 10):
    receipts = []
    for _, row in df.head(limit).iterrows():
        amount_value = row["Amount"]
        amount_number = float(amount_value) if pd.notna(amount_value) else 0.0
        receipts.append({
            "payee": str(row["Payee Name"]).strip(),
            "amount": f"{amount_number:,.2f}",
            "amount_words": num2words(amount_number, lang='en').title(),
            "work": str(row["Work"]).strip()
        })
    return receipts


def _build_pdf_reportlab(receipts):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        leftMargin=10 * mm,
        rightMargin=10 * mm,
        topMargin=10 * mm,
        bottomMargin=10 * mm,
    )
    styles = getSampleStyleSheet()
    story = []
    for idx, receipt in enumerate(receipts):
        story.append(Paragraph("HAND RECEIPT (RPWA 28)", styles["Title"]))
        story.append(Paragraph(f"Payable to: - {receipt['payee']} (Electric Contractor)", styles["Heading4"]))
        story.append(Paragraph("Division - PWD Electric Division, Udaipur", styles["Normal"]))
        story.append(Spacer(1, 6 * mm))

        lines = [
            "(1) Cash Book Voucher No. _____    Date _____",
            "(2) Cheque No. and Date _____",
            f"(3) Pay for ECS Rs. {receipt['amount']}/- (Rupees {receipt['amount_words']} Only)",
            "(4) Paid by me",
            (
                f"(5) Received from The Executive Engineer PWD Electric Division, Udaipur the sum of Rs."
                f" {receipt['amount']}/- (Rupees {receipt['amount_words']} Only)"
            ),
            f"Name of work for which payment is made: {receipt['work']}",
            "Chargeable to Head:- 8443 [EMD- Refund]",
        ]
        for t in lines:
            story.append(Paragraph(t, styles["Normal"]))

        story.append(Spacer(1, 6 * mm))
        signature_table = Table([
            ["Witness", "Stamp", "Signature of payee"],
            ["Cash Book No. _____ Page No. _____", "", ""],
        ], colWidths=[60 * mm, 30 * mm, 70 * mm])
        signature_table.setStyle(TableStyle([["GRID", (0, 0), (-1, -1), 0.5, colors.grey], ["ALIGN", (0, 0), (-1, -1), "LEFT"]]))
        story.append(signature_table)

        story.append(Spacer(1, 6 * mm))
        offices_table = Table([
            ["For use in the Divisional Office", "For use in the Accountant General's office"],
            ["Checked", "Audited/Reviewed"],
            ["Accounts Clerk", "DA      Auditor      Supdt.      G.O."],
        ], colWidths=[80 * mm, 80 * mm])
        offices_table.setStyle(TableStyle([["GRID", (0, 0), (-1, -1), 0.5, colors.black], ["ALIGN", (0, 0), (-1, -1), "LEFT"]]))
        story.append(offices_table)

        story.append(Spacer(1, 8 * mm))
        for t in [
            f"Passed for Rs. {receipt['amount']}",
            f"In Words Rupees: {receipt['amount_words']} Only",
            "Chargeable to Head:- 8443 [EMD- Refund]",
            "Ar.                    D.A.                    E.E.",
        ]:
            story.append(Paragraph(t, styles["Normal"]))
        if idx < len(receipts) - 1:
            story.append(Spacer(1, 12 * mm))

    doc.build(story)
    buffer.seek(0)
    return buffer.read()


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file" not in request.files or request.files["file"].filename == "":
            return jsonify({"error": "No file uploaded"}), 400
        file = request.files["file"]
        try:
            df = pd.read_excel(file)
            _validate_columns(df)
            receipts = _rows_to_receipts(df)

            rendered_html = Template(receipt_template).render(receipts=receipts)
            script_dir = os.path.dirname(__file__)
            pdf_file = os.path.join(script_dir, "receipts.pdf")

            if config is not None and wkhtmltopdf_path is not None:
                pdfkit.from_string(rendered_html, pdf_file, options={"page-size": "A4"}, configuration=config)
                return send_file(pdf_file, as_attachment=True)
            else:
                pdf_bytes = _build_pdf_reportlab(receipts)
                return send_file(io.BytesIO(pdf_bytes), as_attachment=True, download_name="receipts.pdf", mimetype="application/pdf")
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)