import streamlit as st
from utils.branding import get_tool_colors

def create_tool_grid():
    """Create the main grid of tool buttons with enhanced styling using a 3-column layout"""
    
    # Tool definitions with categories and external links
    # Updated to match actual available pages
    tools = [
        {
            "name": "Excel se EMD",
            "description": "Excel to EMD Refund Generator",
            "icon": "📊",
            "category": "financial",
            "status": "internal",
            "page": "pages/01_excel_se_emd.py"
        },
        {
            "name": "Bill Note Sheet",
            "description": "Generate Bill Note Sheets",
            "icon": "📝",
            "category": "financial",
            "status": "internal",
            "page": "pages/02_bill_note_sheet.py"
        },
        {
            "name": "EMD Refund",
            "description": "EMD Refund Calculator and Tracker",
            "icon": "💸",
            "category": "financial",
            "status": "internal",
            "page": "pages/03_emd_refund.py"
        },
        {
            "name": "Deductions Table",
            "description": "Manage Deductions in Contracts",
            "icon": "➖",
            "category": "financial",
            "status": "internal",
            "page": "pages/04_deductions_table.py"
        },
        {
            "name": "Delay Calculator",
            "description": "Calculate project delays and penalties",
            "icon": "⏰",
            "category": "calculations",
            "status": "internal",
            "page": "pages/05_delay_calculator.py"
        },
        {
            "name": "Security Refund",
            "description": "Security Deposit Refund Calculator",
            "icon": "🔒",
            "category": "financial",
            "status": "internal",
            "page": "pages/06_security_refund.py"
        },
        {
            "name": "Financial Progress",
            "description": "Track Financial Progress of Projects",
            "icon": "📈",
            "category": "monitoring",
            "status": "internal",
            "page": "pages/07_financial_progress.py"
        },
        {
            "name": "Stamp Duty",
            "description": "Calculate Stamp Duty for Documents",
            "icon": "⚖️",
            "category": "calculations",
            "status": "internal",
            "page": "pages/08_stamp_duty.py"
        }
    ]
    
    # Use existing color scheme from branding
    colors = get_tool_colors()
    
    # Create header with tool count
    st.markdown(f"""
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
        <div class="header-container" style="padding: 10px 20px; border-radius: 50px; font-weight: bold;">
            🏗️ {len(tools)} Essential Tools Available
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Create 3-column grid layout for tools
    col1, col2, col3 = st.columns(3)
    columns = [col1, col2, col3]
    
    for i, tool in enumerate(tools):
        with columns[i % 3]:
            # Apply custom button styling with hover effects matching the CTkButton style
            st.markdown(f"""
            <style>
            .tool-card-ctk-{i} {{
                background: linear-gradient(135deg, #f0f8f5 0%, #e8f5e8 100%);
                border: 2px solid #2E8B57;
                border-radius: 15px;
                padding: 20px;
                margin: 10px 0;
                text-align: center;
                cursor: pointer;
                transition: all 0.3s ease;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                min-height: 180px;
                display: flex;
                flex-direction: column;
                justify-content: space-between;
            }}
            
            .tool-card-ctk-{i}:hover {{
                transform: translateY(-3px);
                box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
                border-color: #228B22;
                background: linear-gradient(135deg, #e8f5e8 0%, #d4f0d4 100%);
            }}
            
            .tool-icon-ctk {{font-size: 2.5rem; margin-bottom: 10px;}}
            .tool-title-ctk {{font-weight: bold; font-size: 1.1rem; margin-bottom: 8px; color: #2E8B57;}}
            .tool-desc-ctk {{font-size: 0.9rem; color: #666; margin-bottom: 10px;}}
            .tool-status-ctk {{font-size: 0.8rem; padding: 3px 8px; border-radius: 10px; display: inline-block;}}
            .tool-status-internal {{background-color: #2E8B57; color: white;}}
            .tool-status-external {{background-color: #4682B4; color: white;}}
            </style>
            
            <div class="tool-card-ctk-{i}">
                <div class="tool-icon-ctk">{tool['icon']}</div>
                <div class="tool-title-ctk">{tool['name']}</div>
                <div class="tool-desc-ctk">{tool['description']}</div>
                <div class="tool-status-ctk tool-status-{tool['status']}">{tool['status'].capitalize()}</div>
            </div>
            """, unsafe_allow_html=True)
            
            # Button for navigation functionality
            if tool['status'] == 'internal':
                if st.button(f"{tool['name']}", key=f"tool-button-{i}", use_container_width=True, type="primary"):
                    st.switch_page(tool['page'])
            else:
                if st.button(f"Open {tool['name']}", key=f"tool-button-{i}", use_container_width=True):
                    if 'url' in tool:
                        st.markdown(f"<meta http-equiv='refresh' content='0; url={tool['url']}'>", unsafe_allow_html=True)
    
    # No JavaScript needed - using Streamlit buttons for navigation


def create_tool_button(tool, colors):
    """Create individual tool button with enhanced styling"""
    
    # Get color for the category or use default
    category_info = colors.get(tool["category"], {"bg": "#f0f8f5", "border": "#2E8B57", "icon": "🛠️"})
    status_indicator = "🔗 External" if tool["status"] == "external" else "🏠 Internal"
    status_color = "#DC143C" if tool["status"] == "external" else "#2E8B57"
    
    # Create enhanced button container with design closer to repo
    button_html = f"""
    <div class="tool-button">
        <div style="font-size: 3rem; margin-bottom: 15px;">{tool['icon']}</div>
        <div style="font-size: 1.2rem; font-weight: bold; color: #2E8B57; margin-bottom: 10px;">
            {tool['name']}
        </div>
        <div style="font-size: 0.9rem; color: #555; min-height: 60px; margin-bottom: 15px;">
            {tool['description']}
        </div>
        <div style="font-size: 0.8rem; color: {status_color}; font-weight: bold; margin-top: auto; padding: 5px 10px; border-radius: 20px; background-color: rgba(46, 139, 87, 0.1);">
            {status_indicator}
        </div>
    </div>
    """
    
    st.markdown(button_html, unsafe_allow_html=True)
    
    # Navigation link with enhanced styling - restoring the cool design
    if tool["status"] == "external" and tool["url"]:
        st.link_button("Open External Tool ↗", tool["url"], use_container_width=True)
    else:
        # Use switch_page for internal tools (more reliable than page_link)
        if st.button("Open Tool", key=f"tool_{tool['name']}", use_container_width=True):
            st.switch_page(tool["page"])

def create_category_filter():
    """Create category filter for tools"""
    st.sidebar.markdown("### 🎯 Filter by Category")
    
    categories = ["All", "Financial", "Processing", "Operations", "Monitoring"]
    selected_category = st.sidebar.selectbox("Select Category:", categories)
    
    return selected_category.lower() if selected_category != "All" else None

def show_tool_stats():
    """Display statistics about available tools"""
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("🔗 External Tools", "2", "Connected")
    with col2:
        st.metric("🏠 Internal Tools", "9", "Available")
    with col3:
        st.metric("📊 Total Categories", "5", "Organized")
