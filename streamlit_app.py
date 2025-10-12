"""
Streamlit App for PWD Tools
This app serves the HTML-based tools through Streamlit components.
"""

import streamlit as st
import streamlit.components.v1 as components
import os

# Set page configuration
st.set_page_config(
    page_title="PWD Tools Hub",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        text-align: center;
        padding: 1rem;
        background: linear-gradient(135deg, #0ea5e9 0%, #0284c7 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .tool-card {
        border: 1px solid #e5e7eb;
        border-radius: 10px;
        padding: 1rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        transition: transform 0.2s;
    }
    .tool-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }
    .tool-icon {
        font-size: 2rem;
        margin-bottom: 0.5rem;
    }
    .back-button {
        background-color: #0ea5e9;
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        cursor: pointer;
        text-decoration: none;
        display: inline-block;
        margin-bottom: 1rem;
    }
    .back-button:hover {
        background-color: #0284c7;
    }
    </style>
""", unsafe_allow_html=True)

# Main header
st.markdown("""
    <div class="main-header">
        <h1>🏗️ PWD Tools Hub</h1>
        <p>Infrastructure Management Suite for Public Works Department</p>
    </div>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("🧭 Navigation")
tool_selection = st.sidebar.radio(
    "Select Tool:",
    [
        "🏠 Home",
        "📄 Bill Note Sheet",
        "🧮 Deductions Table",
        "⏱️ Delay Calculator",
        "💰 Liquidity Damages Calculator",
        "🔒 Security Refund",
        "🏛️ Stamp Duty"
    ]
)

# Home page
if tool_selection == "🏠 Home":
    st.header("Welcome to PWD Tools Hub")
    st.markdown("""
    This platform provides a collection of tools designed specifically for Public Works Department operations.
    
    ### Available Tools:
    - **Bill Note Sheet Generator** - Create standardized bill note sheets
    - **Deductions Table** - Calculate all standard deductions for bill amounts
    - **Delay Calculator** - Calculate project delays and associated metrics
    - **Liquidity Damages Calculator** - Calculate liquidity damages and penalties
    - **Security Refund** - Process security deposit refunds
    - **Stamp Duty** - Calculate stamp duty amounts for various documents
    
    ### Features:
    - Modern, responsive interface
    - Bilingual support (English/Hindi)
    - Printable reports
    - Detailed calculation steps
    """)
    
    st.info("Select a tool from the sidebar to get started!")

# Bill Note Sheet
elif tool_selection == "📄 Bill Note Sheet":
    st.header("📄 Bill Note Sheet Generator")
    
    # Read and display the HTML content
    try:
        with open("public/tools/BillNoteSheet.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        components.html(html_content, height=800, scrolling=True)
    except FileNotFoundError:
        st.error("Bill Note Sheet tool not available")
    except Exception as e:
        st.error(f"Error loading Bill Note Sheet: {str(e)}")

# Deductions Table
elif tool_selection == "🧮 Deductions Table":
    st.header("🧮 Deductions Table")
    
    # Read and display the HTML content
    try:
        with open("public/tools/DeductionsTable.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        components.html(html_content, height=800, scrolling=True)
    except FileNotFoundError:
        st.error("Deductions Table tool not available")
    except Exception as e:
        st.error(f"Error loading Deductions Table: {str(e)}")

# Delay Calculator
elif tool_selection == "⏱️ Delay Calculator":
    st.header("⏱️ Delay Calculator")
    
    # Read and display the HTML content
    try:
        with open("public/tools/DelayCalculator.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        components.html(html_content, height=600, scrolling=True)
    except FileNotFoundError:
        st.error("Delay Calculator tool not available")
    except Exception as e:
        st.error(f"Error loading Delay Calculator: {str(e)}")

# Liquidity Damages Calculator
elif tool_selection == "💰 Liquidity Damages Calculator":
    st.header("💰 Liquidity Damages Calculator")
    
    # Read and display the HTML content
    try:
        with open("public/tools/LiquidityDamagesCalculator.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        components.html(html_content, height=1000, scrolling=True)
    except FileNotFoundError:
        st.error("Liquidity Damages Calculator tool not available")
    except Exception as e:
        st.error(f"Error loading Liquidity Damages Calculator: {str(e)}")

# Security Refund
elif tool_selection == "🔒 Security Refund":
    st.header("🔒 Security Refund Calculator")
    
    # Read and display the HTML content
    try:
        with open("public/tools/SecurityRefund.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        components.html(html_content, height=800, scrolling=True)
    except FileNotFoundError:
        st.error("Security Refund tool not available")
    except Exception as e:
        st.error(f"Error loading Security Refund: {str(e)}")

# Stamp Duty
elif tool_selection == "🏛️ Stamp Duty":
    st.header("🏛️ Stamp Duty Calculator")
    
    # Read and display the HTML content
    try:
        with open("public/tools/StampDuty.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        components.html(html_content, height=400, scrolling=True)
    except FileNotFoundError:
        st.error("Stamp Duty tool not available")
    except Exception as e:
        st.error(f"Error loading Stamp Duty: {str(e)}")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center;">
    <p>Prepared for Mrs. Premlata Jain, AAO, PWD Udaipur</p>
    <p>© 2025 PWD Tools Hub | Infrastructure Management Suite</p>
</div>
""", unsafe_allow_html=True)