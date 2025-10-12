import streamlit as st
import time

def apply_custom_css():
    """Apply custom CSS styling with crane branding and green gradient theme"""
    st.markdown("""
    <style>
    /* Main app styling */
    .main > div {
        padding-top: 0rem;
    }
    
    /* Header styling with green gradient */
    .header-container {
        background: linear-gradient(135deg, #2E8B57 0%, #90EE90 100%);
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        color: white;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* Tool button styling */
    .tool-button {
        background: linear-gradient(135deg, #f0f8f5 0%, #e8f5e8 100%);
        border: 2px solid #2E8B57;
        border-radius: 15px;
        padding: 20px;
        margin: 10px;
        text-align: center;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    .tool-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        border-color: #228B22;
    }
    
    /* Metric styling */
    .metric-container {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        padding: 15px;
        border-radius: 10px;
        border-left: 4px solid #2E8B57;
    }
    
    /* Sidebar styling */
    .sidebar .sidebar-content {
        background: linear-gradient(135deg, #f0f8f5 0%, #e8f5e8 100%);
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
        margin: 6px 0;
        width: 100%;
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
    
    /* Sidebar header */
    .sidebar-header {
        background: linear-gradient(135deg, #2E8B57 0%, #3CB371 100%);
        color: white;
        padding: 20px 15px;
        border-radius: 15px;
        margin-bottom: 20px;
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
    
    .sidebar-tool-category {
        color: #2E8B57;
        font-weight: bold;
        margin: 20px 0 10px 0;
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
        margin: 20px 0;
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
    
    /* Success animation */
    .celebration {
        animation: bounce 1s ease-in-out infinite alternate;
    }
    
    @keyframes bounce {
        0% { transform: translateY(0px); }
        100% { transform: translateY(-10px); }
    }
    
    /* Credits styling */
    .credits {
        background: linear-gradient(135deg, #2E8B57 0%, #3CB371 100%);
        color: white;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        margin-top: 20px;
    }
    
    /* Button styling */
    .stButton > button {
        width: 100%;
        background-color: #2E8B57;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 10px 20px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background-color: #228B22;
        transform: translateY(-1px);
    }
    
    /* Custom Tool Card Styles - CTkButton Inspired */
    .tool-card-ctk {
        background: linear-gradient(135deg, #f0f8f5 0%, #e8f5e8 100%);
        border: 2px solid #2E8B57;
        border-radius: 15px;
        padding: 20px;
        margin: 10px;
        text-align: center;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        min-height: 180px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    
    .tool-card-ctk:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        border-color: #228B22;
        background: linear-gradient(135deg, #e8f5e8 0%, #f0f8f5 100%);
    }
    
    .tool-icon-ctk {
        font-size: 2rem;
        margin-bottom: 10px;
    }
    
    .tool-title-ctk {
        font-size: 1.1rem;
        font-weight: bold;
        color: #333333;
        margin-bottom: 8px;
    }
    
    .tool-desc-ctk {
        font-size: 0.9rem;
        color: #666666;
        margin-bottom: 10px;
    }
    
    .tool-status-ctk {
        font-size: 0.8rem;
        padding: 4px 10px;
        border-radius: 20px;
        display: inline-block;
    }
    
    .tool-status-ctk.internal {
        background-color: #2E8B57;
        color: white;
    }
    
    .tool-status-ctk.external {
        background-color: #4682B4;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

def get_tool_colors():
    """Return the color scheme for tool buttons and components"""
    return {
        'primary': '#2E8B57',  # Green
        'secondary': '#90EE90',  # Light green
        'accent': '#228B22',  # Dark green for hover
        'background': '#f0f8f5',  # Light background
        'border': '#2E8B57',  # Border color
        'text': '#333333',  # Text color
        'text_light': '#666666',  # Light text color
        'external': '#4682B4'  # Steel blue for external tools
    }

def show_header():
    """Display the main header with crane logo and branding"""
    st.markdown("""
    <div class="header-container">
        <h1>🏗️ PWD Tools Hub</h1>
        <h3>Infrastructure Management Suite</h3>
    </div>
    """, unsafe_allow_html=True)

def show_credits():
    """Show credits at the bottom of the page"""
    st.markdown("""
    <div class="credits">
        <p>© 2023 PWD Tools Hub | Infrastructure Management Suite</p>
        <p>Built with Streamlit | Designed for Lower Divisional Clerks</p>
        <div style="margin-top: 15px; padding-top: 10px; border-top: 1px solid rgba(255,255,255,0.3);">
            <p><strong>Initiative Credit</strong></p>
            <p>Mrs. Premlata Jain<br>
            Additional Administrative Officer, PWD Udaipur</p>
            <p>Version 2.0 | Last Updated: September 2025</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

def show_success_message(message="Operation completed successfully!"):
    """Show a success message with animation"""
    st.success(f"✅ {message}")
    time.sleep(1)

# Category styles for different tool types
def get_tool_categories():
    return {
        "financial": {"bg": "#E8F5E8", "border": "#2E8B57", "icon": "💰"},
        "processing": {"bg": "#F0F8FF", "border": "#4169E1", "icon": "📋"},
        "calculator": {"bg": "#F0FFF0", "border": "#66CDAA", "icon": "🧮"},
        "tracking": {"bg": "#FFF0F5", "border": "#CD853F", "icon": "📊"},
        "reporting": {"bg": "#F8F8FF", "border": "#DDA0DD", "icon": "📈"},
        "utilities": {"bg": "#F5F5DC", "border": "#DEB887", "icon": "🛠️"}
    }