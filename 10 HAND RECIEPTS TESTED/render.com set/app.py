from flask import Flask, render_template, request, send_file
import pandas as pd
from jinja2 import Template
import os
from num2words import num2words
from weasyprint import HTML
import logging

app = Flask(__name__)

receipt_template = open('templates/receipts.html').read()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        if file:
            try:
                df = pd.read_excel(file)
                num_rows = len(df)

                receipts = []
                for _, row in df.iterrows():
                    amount = row["Amount"]
                    if pd.isna(amount):
                        amount = 0
                    else:
                        amount = int(amount)
                    receipts.append({
                        "payee": row["Payee Name"],
                        "amount": amount,
                        "amount_words": num2words(amount, lang='en').title(),
                        "work": row["Work"]
                    })

                rendered_html = Template(receipt_template).render(receipts=receipts)

                script_dir = os.path.dirname(__file__)
                pdf_file = os.path.join(script_dir, "receipts.pdf")

                HTML(string=rendered_html).write_pdf(pdf_file)

                return send_file(pdf_file, as_attachment=True)

            except Exception as e:
                logging.error(f"An error occurred: {e}") #Log the error.
                return f"An error occurred: {e}"

    return render_template("index.html")