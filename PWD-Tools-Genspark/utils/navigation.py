import streamlit as st

def create_breadcrumb(current_page):
    """Create breadcrumb navigation"""
    st.markdown(f"""
    <div style="background-color: #f0f8f5; padding: 10px; border-radius: 5px; margin-bottom: 20px;">
        <span style="color: #2E8B57;">🏠 <a href="/" style="color: #2E8B57; text-decoration: none;">Home</a></span>
        <span style="color: #666;"> → </span>
        <span style="color: #333; font-weight: bold;">{current_page}</span>
    </div>
    """, unsafe_allow_html=True)

def create_back_button():
    """Create a back to home button"""
    if st.button("🏠 Back to Home", key="back_home", type="primary"):
        st.switch_page("app.py")

def create_tool_navigation():
    """Create navigation between tools"""
    # Add custom CSS for enhanced sidebar styling
    st.markdown("""
    <style>
    [data-testid=stSidebar] {
        background: linear-gradient(135deg, #f0f8f5 0%, #e8f5e8 100%);
        border-right: 1px solid #d0e8d0;
    }
    
    [data-testid=stSidebar] .stMarkdown {
        padding: 0 10px;
    }
    
    .sidebar-header {
        background: linear-gradient(135deg, #2E8B57 0%, #3CB371 100%);
        color: white;
        padding: 20px 15px;
        border-radius: 15px;
        margin: 15px;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
        border: 2px solid rgba(255,255,255,0.2);
        position: relative;
        overflow: hidden;
    }
    
    .sidebar-header::before {
        content: "";
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.2) 0%, transparent 70%);
        transform: rotate(30deg);
    }
    
    .sidebar-header h3 {
        margin: 0 0 8px 0;
        font-size: 1.4em;
        position: relative;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
    }
    
    .sidebar-header p {
        margin: 0;
        font-size: 1em;
        opacity: 0.95;
        position: relative;
    }
    
    .sidebar-welcome {
        background: rgba(255, 255, 255, 0.7);
        border-radius: 10px;
        padding: 12px;
        margin: 15px;
        text-align: center;
        border: 1px solid #c8e6c8;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    
    .sidebar-tool-category {
        color: #2E8B57;
        font-weight: bold;
        margin: 20px 15px 10px 15px;
        padding: 8px 12px;
        border-radius: 8px;
        background: rgba(46, 139, 87, 0.1);
        border-left: 3px solid #2E8B57;
        font-size: 1.1em;
        display: flex;
        align-items: center;
    }
    
    .sidebar-tool-category::before {
        content: "";
        display: inline-block;
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: #2E8B57;
        margin-right: 10px;
    }
    
    .sidebar-divider {
        border-top: 1px dashed #2E8B57;
        margin: 20px 15px;
        position: relative;
    }
    
    .sidebar-divider::after {
        content: "🔧";
        position: absolute;
        top: -10px;
        left: 50%;
        transform: translateX(-50%);
        background: #f0f8f5;
        padding: 0 10px;
        color: #2E8B57;
    }
    
    /* Enhanced sidebar button styling */
    .sidebar .stButton > button {
        background: linear-gradient(135deg, #2E8B57 0%, #3CB371 100%);
        color: white;
        border-radius: 10px;
        border: none;
        padding: 14px 15px;
        font-weight: 600;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        margin: 6px 15px;
        width: calc(100% - 30px);
        text-align: left;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        position: relative;
        overflow: hidden;
    }
    
    .sidebar .stButton > button:hover {
        background: linear-gradient(135deg, #228B22 0%, #2E8B57 100%);
        transform: translateX(8px);
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    }
    
    .sidebar .stButton > button:active {
        transform: translateX(5px);
    }
    
    .sidebar .stButton > button::after {
        content: "→";
        position: absolute;
        right: 15px;
        top: 50%;
        transform: translateY(-50%);
        opacity: 0;
        transition: all 0.3s ease;
    }
    
    .sidebar .stButton > button:hover::after {
        opacity: 1;
        right: 10px;
    }
    
    .sidebar-footer {
        background: rgba(255, 255, 255, 0.7);
        border-radius: 10px;
        padding: 15px;
        margin: 15px;
        text-align: center;
        border: 1px solid #c8e6c8;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        font-size: 0.9em;
    }
    
    .sidebar-footer p {
        margin: 5px 0;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Add sidebar header with enhanced styling
    st.sidebar.markdown('''
    <div class="sidebar-header">
        <h3>🏗️ PWD Tools Hub</h3>
        <p>Infrastructure Suite</p>
    </div>
    ''', unsafe_allow_html=True)
    
    # Add welcome message
    st.sidebar.markdown('''
    <div class="sidebar-welcome">
        <p>👋 Welcome to PWD Tools Hub</p>
        <p>Select a tool from below to get started</p>
    </div>
    ''', unsafe_allow_html=True)
    
    # Add navigation instructions
    st.sidebar.markdown("### 🧭 Tool Navigation")
    
    # Group tools by category for better organization
    st.sidebar.markdown('<div class="sidebar-tool-category">💰 Financial Tools</div>', unsafe_allow_html=True)
    
    financial_tools = {
        "📊 Excel se EMD": "pages/01_excel_se_emd.py",
        "💰 Bill Note Sheet": "pages/02_bill_note_sheet.py",
        "💳 EMD Refund": "pages/03_emd_refund.py",
        "🛡️ Security Refund": "pages/06_security_refund.py",
        "📈 Financial Progress": "pages/07_financial_progress.py"
    }
    
    for tool_name, tool_page in financial_tools.items():
        if st.sidebar.button(tool_name, key=f"nav_{tool_name}", use_container_width=True):
            st.switch_page(tool_page)
    
    st.sidebar.markdown('<div class="sidebar-tool-category">🧮 Calculation Tools</div>', unsafe_allow_html=True)
    
    calculation_tools = {
        "📋 Deductions Table": "pages/04_deductions_table.py",
        "⏰ Delay Calculator": "pages/05_delay_calculator.py",
        "⚖️ Stamp Duty": "pages/08_stamp_duty.py"
    }
    
    for tool_name, tool_page in calculation_tools.items():
        if st.sidebar.button(tool_name, key=f"nav_{tool_name}", use_container_width=True):
            st.switch_page(tool_page)
    
    # Add divider and enhanced footer
    st.sidebar.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)
    st.sidebar.markdown('''
    <div class="sidebar-footer">
        <p>🛠️ Version 2.0 | Last Updated: Sep 2025</p>
        <p>© PWD Tools Hub | Designed for LDCs</p>
    </div>
    ''', unsafe_allow_html=True)

def show_external_link_warning():
    """Show warning for external links"""
    st.warning("""
    🔗 **External Tool Access**
    
    You are being redirected to an external PWD tool. This tool is hosted separately but integrated into our hub.
    
    - All tools maintain the same security standards
    - Your session data is protected
    - Use the browser back button to return here
    """)