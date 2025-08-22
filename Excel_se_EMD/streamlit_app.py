import io
from typing import List, Dict

import pandas as pd
import streamlit as st
from num2words import num2words
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors


def _validate_dataframe_has_required_columns(dataframe: pd.DataFrame) -> None:
    required_columns: List[str] = ["Payee Name", "Amount", "Work"]
    missing_columns: List[str] = [column for column in required_columns if column not in dataframe.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")


def _dataframe_to_receipts(dataframe: pd.DataFrame, limit: int = 10) -> List[Dict[str, str]]:
    limited_df: pd.DataFrame = dataframe.head(limit)
    receipts: List[Dict[str, str]] = []
    for _, row in limited_df.iterrows():
        amount_value = row["Amount"]
        amount_number = float(amount_value) if pd.notna(amount_value) else 0.0
        receipts.append(
            {
                "payee": str(row["Payee Name"]).strip(),
                "amount": f"{amount_number:,.2f}",
                "amount_words": num2words(amount_number, lang="en").title(),
                "work": str(row["Work"]).strip(),
            }
        )
    return receipts


def _build_pdf(receipts: List[Dict[str, str]]) -> bytes:
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

    for index, receipt in enumerate(receipts):
        title = Paragraph("HAND RECEIPT (RPWA 28)", styles["Title"])
        subtitle = Paragraph(
            f"Payable to: - {receipt['payee']} (Electric Contractor)", styles["Heading4"]
        )
        division = Paragraph("Division - PWD Electric Division, Udaipur", styles["Normal"])

        story.extend([title, subtitle, division, Spacer(1, 6 * mm)])

        lines = [
            f"(1) Cash Book Voucher No. _____    Date _____",
            f"(2) Cheque No. and Date _____",
            f"(3) Pay for ECS Rs. {receipt['amount']}/- (Rupees {receipt['amount_words']} Only)",
            f"(4) Paid by me",
            (
                f"(5) Received from The Executive Engineer PWD Electric Division, Udaipur the sum of Rs."
                f" {receipt['amount']}/- (Rupees {receipt['amount_words']} Only)"
            ),
            f"Name of work for which payment is made: {receipt['work']}",
            "Chargeable to Head:- 8443 [EMD- Refund]",
        ]

        for text in lines:
            story.append(Paragraph(text, styles["Normal"]))

        story.append(Spacer(1, 6 * mm))

        signature_table_data = [
            ["Witness", "Stamp", "Signature of payee"],
            ["Cash Book No. _____ Page No. _____", "", ""],
        ]
        signature_table = Table(signature_table_data, colWidths=[60 * mm, 30 * mm, 70 * mm])
        signature_table.setStyle(
            TableStyle(
                [
                    ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                    ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                ]
            )
        )
        story.append(signature_table)

        story.append(Spacer(1, 6 * mm))

        offices_table_data = [
            ["For use in the Divisional Office", "For use in the Accountant General's office"],
            ["Checked", "Audited/Reviewed"],
            ["Accounts Clerk", "DA      Auditor      Supdt.      G.O."],
        ]
        offices_table = Table(offices_table_data, colWidths=[80 * mm, 80 * mm])
        offices_table.setStyle(
            TableStyle(
                [
                    ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
                    ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                ]
            )
        )
        story.append(offices_table)

        story.append(Spacer(1, 8 * mm))

        passed_lines = [
            f"Passed for Rs. {receipt['amount']}",
            f"In Words Rupees: {receipt['amount_words']} Only",
            "Chargeable to Head:- 8443 [EMD- Refund]",
            "Ar.                    D.A.                    E.E.",
        ]
        for text in passed_lines:
            story.append(Paragraph(text, styles["Normal"]))

        if index < len(receipts) - 1:
            story.append(Spacer(1, 12 * mm))

    doc.build(story)
    buffer.seek(0)
    return buffer.read()


def main() -> None:
    st.set_page_config(page_title="Hand Receipt Generator (RPWA 28)")
    st.title("Hand Receipt Generator (RPWA 28)")
    st.caption("Upload Excel with columns: Payee Name, Amount, Work. Generates a PDF (A4).")

    uploaded_file = st.file_uploader("Upload .xlsx file", type=["xlsx"]) 
    max_rows = st.number_input("Limit number of rows", min_value=1, max_value=1000, value=10, step=1)

    if uploaded_file is not None:
        try:
            df = pd.read_excel(uploaded_file)
            _validate_dataframe_has_required_columns(df)
            receipts = _dataframe_to_receipts(df, limit=int(max_rows))
            pdf_bytes = _build_pdf(receipts)
            st.download_button(
                label="Download PDF",
                data=pdf_bytes,
                file_name="receipts.pdf",
                mime="application/pdf",
            )
            st.success(f"Generated {len(receipts)} receipts.")
        except Exception as error:
            st.error(f"Error: {error}")


if __name__ == "__main__":
    main()


