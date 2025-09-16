import streamlit as st
import pandas as pd
from num2words import num2words
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
import io
import base64
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Page configuration
st.set_page_config(
    page_title="HR Hand Receipt Generator",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom styles for better formatting
def get_custom_styles():
    styles = getSampleStyleSheet()
    
    # Custom title style
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Title'],
        fontSize=16,
        spaceAfter=12,
        alignment=TA_CENTER,
        textColor=colors.black
    )
    
    # Custom heading style
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading4'],
        fontSize=14,
        spaceAfter=8,
        alignment=TA_LEFT,
        textColor=colors.black
    )
    
    # Custom normal style
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=6,
        alignment=TA_LEFT,
        textColor=colors.black
    )
    
    return {
        'title': title_style,
        'heading': heading_style,
        'normal': normal_style
    }

def build_pdf_with_reportlab(receipts):
    """Build PDF using ReportLab - completely self-contained"""
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        leftMargin=15 * mm,
        rightMargin=15 * mm,
        topMargin=15 * mm,
        bottomMargin=15 * mm,
    )
    
    styles = get_custom_styles()
    story = []
    
    for idx, receipt in enumerate(receipts):
        # Add page break for subsequent receipts
        if idx > 0:
            story.append(Spacer(1, 20 * mm))
        
        # Title
        title = Paragraph("HAND RECEIPT (RPWA 28)", styles['title'])
        story.append(title)
        story.append(Spacer(1, 8 * mm))
        
        # Payee information
        payee_text = f"Payable to: - {receipt['payee']} (Electric Contractor)"
        payee_para = Paragraph(payee_text, styles['heading'])
        story.append(payee_para)
        story.append(Spacer(1, 6 * mm))
        
        # Division
        division_text = "Division - PWD Electric Division, Udaipur"
        division_para = Paragraph(division_text, styles['normal'])
        story.append(division_para)
        story.append(Spacer(1, 8 * mm))
        
        # Rules reference
        rules_text = "(Referred to in PWF&A Rules 418,424,436 & 438)"
        rules_para = Paragraph(rules_text, styles['normal'])
        story.append(rules_para)
        story.append(Spacer(1, 12 * mm))
        
        # Receipt details
        details = [
            f"(1) Cash Book Voucher No. _____    Date _____",
            f"(2) Cheque No. and Date _____",
            f"(3) Pay for ECS Rs. {receipt['amount']}/- (Rupees {receipt['amount_words']} Only)",
            "(4) Paid by me",
            f"(5) Received from The Executive Engineer PWD Electric Division, Udaipur the sum of Rs. {receipt['amount']}/- (Rupees {receipt['amount_words']} Only)",
            f"Name of work for which payment is made: {receipt['work']}",
            "Chargeable to Head:- 8443 [EMD- Refund]"
        ]
        
        for detail in details:
            detail_para = Paragraph(detail, styles['normal'])
            story.append(detail_para)
            story.append(Spacer(1, 4 * mm))
        
        story.append(Spacer(1, 8 * mm))
        
        # Signature area table
        signature_data = [
            ["Witness", "Stamp", "Signature of payee"],
            ["Cash Book No. _____ Page No. _____", "", ""]
        ]
        signature_table = Table(signature_data, colWidths=[60 * mm, 30 * mm, 70 * mm])
        signature_table.setStyle(TableStyle([
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 9),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ('TOPPADDING', (0, 0), (-1, -1), 6),
        ]))
        story.append(signature_table)
        
        story.append(Spacer(1, 8 * mm))
        
        # Offices table
        offices_data = [
            ["For use in the Divisional Office", "For use in the Accountant General's office"],
            ["Checked", "Audited/Reviewed"],
            ["Accounts Clerk", "DA      Auditor      Supdt.      G.O."]
        ]
        offices_table = Table(offices_data, colWidths=[80 * mm, 80 * mm])
        offices_table.setStyle(TableStyle([
            ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 9),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ('TOPPADDING', (0, 0), (-1, -1), 6),
        ]))
        story.append(offices_table)
        
        story.append(Spacer(1, 10 * mm))
        
        # Bottom section
        bottom_details = [
            f"Passed for Rs. {receipt['amount']}",
            f"In Words Rupees: {receipt['amount_words']} Only",
            "Chargeable to Head:- 8443 [EMD- Refund]",
            "Ar.                    D.A.                    E.E."
        ]
        
        for bottom_detail in bottom_details:
            bottom_para = Paragraph(bottom_detail, styles['normal'])
            story.append(bottom_para)
            story.append(Spacer(1, 3 * mm))
    
    # Build the PDF
    doc.build(story)
    buffer.seek(0)
    return buffer

def validate_excel_data(df):
    """Validate Excel data and return any errors"""
    required_columns = ["Payee Name", "Amount", "Work"]
    missing_columns = [col for col in required_columns if col not in df.columns]
    
    if missing_columns:
        return f"Missing required columns: {', '.join(missing_columns)}"
    
    if len(df) == 0:
        return "Excel file is empty"
    
    # Check for missing values in required columns
    for col in required_columns:
        if df[col].isna().any():
            return f"Column '{col}' contains missing values"
    
    return None

def process_excel_data(df, max_receipts=10):
    """Process Excel data and return formatted receipts"""
    receipts = []
    
    # Limit to max_receipts
    df_limited = df.head(max_receipts)
    
    for _, row in df_limited.iterrows():
        try:
            amount = row["Amount"]
            # Handle different data types for amount
            if pd.isna(amount):
                amount = 0
            elif isinstance(amount, str):
                # Try to convert string to float
                amount = float(amount.replace(',', '').replace('₹', '').strip())
            else:
                amount = float(amount)
            
            receipt = {
                "payee": str(row["Payee Name"]).strip(),
                "amount": f"{amount:,.2f}",
                "amount_words": num2words(amount, lang='en').title(),
                "work": str(row["Work"]).strip()
            }
            receipts.append(receipt)
            
        except Exception as e:
            logger.error(f"Error processing row: {row}, Error: {e}")
            continue
    
    return receipts

def create_download_link(pdf_buffer, filename):
    """Create a download link for the PDF"""
    b64 = base64.b64encode(pdf_buffer.getvalue()).decode()
    href = f'<a href="data:application/pdf;base64,{b64}" download="{filename}">Download PDF</a>'
    return href

def main():
    # Header
    st.title("🏢 HR Hand Receipt Generator (RPWA 28)")
    st.markdown("Generate professional hand receipts from Excel data for PWD Electric Division, Udaipur")
    
    # Sidebar
    st.sidebar.header("⚙️ Settings")
    max_receipts = st.sidebar.slider("Maximum Receipts", 1, 20, 10, help="Limit the number of receipts to generate")
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📋 Required Excel Format")
    st.sidebar.markdown("Your Excel file must contain these columns:")
    st.sidebar.markdown("- **Payee Name**: Name of the contractor")
    st.sidebar.markdown("- **Amount**: Payment amount")
    st.sidebar.markdown("- **Work**: Description of the work")
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📖 About")
    st.sidebar.markdown("This application generates Hand Receipts (RPWA 28) as per PWF&A Rules 418, 424, 436 & 438 for the PWD Electric Division, Udaipur.")
    
    # Main content
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("📤 Upload Excel File")
        
        uploaded_file = st.file_uploader(
            "Choose an Excel file (.xlsx or .xls)",
            type=['xlsx', 'xls'],
            help="Upload your Excel file with the required columns"
        )
        
        if uploaded_file is not None:
            try:
                # Read Excel file
                df = pd.read_excel(uploaded_file)
                
                # Display file info
                st.success(f"✅ File uploaded successfully: {uploaded_file.name}")
                st.info(f"📊 File contains {len(df)} rows and {len(df.columns)} columns")
                
                # Show preview
                st.subheader("📋 Data Preview")
                st.dataframe(df.head(), use_container_width=True)
                
                # Validate data
                validation_error = validate_excel_data(df)
                if validation_error:
                    st.error(f"❌ Validation Error: {validation_error}")
                    return
                
                # Process data
                receipts = process_excel_data(df, max_receipts)
                if not receipts:
                    st.error("❌ No valid data found in Excel file")
                    return
                
                st.success(f"✅ Processed {len(receipts)} receipts successfully")
                
                # Show processed data
                st.subheader("🔍 Processed Receipts")
                processed_df = pd.DataFrame(receipts)
                st.dataframe(processed_df, use_container_width=True)
                
                # Generate PDF button
                if st.button("🔄 Generate PDF Receipts", type="primary"):
                    with st.spinner("Generating PDF..."):
                        try:
                            pdf_buffer = build_pdf_with_reportlab(receipts)
                            
                            # Create download link
                            filename = f"hand_receipts_{len(receipts)}_receipts.pdf"
                            download_link = create_download_link(pdf_buffer, filename)
                            
                            st.success("✅ PDF generated successfully!")
                            st.markdown(download_link, unsafe_allow_html=True)
                            
                            # Show PDF preview (optional)
                            st.subheader("📄 PDF Preview")
                            st.info("Click the download link above to get your PDF file.")
                            
                        except Exception as e:
                            st.error(f"❌ Error generating PDF: {str(e)}")
                            logger.error(f"Error generating PDF: {e}")
                
            except Exception as e:
                st.error(f"❌ Error reading Excel file: {str(e)}")
                logger.error(f"Error reading Excel file: {e}")
    
    with col2:
        st.header("📋 Sample Data")
        st.markdown("Here's an example of how your Excel file should look:")
        
        sample_data = {
            "Payee Name": ["John Doe", "Jane Smith", "Bob Johnson"],
            "Amount": [50000, 75000, 25000],
            "Work": ["Electrical Installation", "Transformer Maintenance", "Cable Laying"]
        }
        
        sample_df = pd.DataFrame(sample_data)
        st.dataframe(sample_df, use_container_width=True)
        
        st.markdown("---")
        st.markdown("### 💡 Tips")
        st.markdown("- Ensure amounts are numeric values")
        st.markdown("- Avoid special characters in names")
        st.markdown("- Keep work descriptions concise")
        
        # Download sample template
        st.markdown("### 📥 Download Sample Template")
        sample_df.to_excel("sample_template.xlsx", index=False)
        with open("sample_template.xlsx", "rb") as f:
            st.download_button(
                label="📥 Sample Template",
                data=f.read(),
                file_name="sample_template.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

if __name__ == "__main__":
    main()
