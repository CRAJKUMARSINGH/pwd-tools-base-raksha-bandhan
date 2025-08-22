# PWD Tools – Raksha Bandhan Edition

This repository contains a Flask app and a Streamlit app to generate Hand Receipt (RPWA 28) PDFs from an Excel file with columns: "Payee Name", "Amount", and "Work".

## Quick Start (Windows)

- Double-click `Run-Streamlit-App.bat` for the easiest experience (no wkhtmltopdf required).
- Or double-click `Run-Flask-App.bat` to run the Flask app (uses wkhtmltopdf if available, otherwise auto-falls back to a pure-PDF engine).

Both scripts will install Python packages automatically the first time.

## Excel Format

Required columns (case-sensitive):
- Payee Name
- Amount
- Work

## Flask App

Location: `Excel_se_EMD/app.py`
- Upload an `.xlsx` file and download the generated PDF.
- If `wkhtmltopdf` is detected, it renders the HTML-based template.
- If not detected, it falls back to a pure-Python PDF generator (ReportLab).

Start (Windows): double-click `Run-Flask-App.bat`.

## Streamlit App

Location: `Excel_se_EMD/streamlit_app.py`
- UI includes file uploader and row limit.
- Always uses pure-Python PDF generation (ReportLab).

Start (Windows): double-click `Run-Streamlit-App.bat`.

## Deployment

### Streamlit Cloud
- Ensure `Excel_se_EMD/requirements.txt` is used.
- Set the app entrypoint to `Excel_se_EMD/streamlit_app.py`.

### Vercel (static tools)
The `public/tools` directory contains static HTML tools that can be deployed as-is on any static host including Vercel. The Flask/Streamlit apps are Python-based and are not deployed on Vercel.

## Notes
- wkhtmltopdf optional paths checked:
  - Windows: `C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe`
  - Linux: `/usr/bin/wkhtmltopdf`
- If wkhtmltopdf is not present, the Flask app gracefully falls back.

## Troubleshooting
- If packages fail to install, open a terminal and run:
  ```bash
  python -m pip install --upgrade pip
  python -m pip install -r Excel_se_EMD/requirements.txt
  ```
- Verify your Excel columns exactly match the names listed above.


