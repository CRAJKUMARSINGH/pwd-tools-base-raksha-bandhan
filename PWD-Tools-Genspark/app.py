import streamlit as st
import sys
import os

# Ensure the current directory is in the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Import only the functions we actually use
from utils.branding import apply_custom_css, show_header, show_credits
from utils.navigation import create_tool_navigation

# Page configuration
st.set_page_config(
    page_title="PWD Tools Hub | Infrastructure Management Suite",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom styling and branding
apply_custom_css()

# Show header with branding
show_header()

# Main content area
def main():
    # Welcome section
    st.markdown("### 🎯 PWD Tools Hub")
    st.markdown("**Infrastructure Management Tools** - Simple tools for PWD operations")
    
    st.markdown("---")
    
    # Instructions for using sidebar
    st.markdown("### 🔧 Available Tools")
    st.info("Please use the sidebar navigation to access the tools.")
    
    # Create tool navigation in sidebar
    create_tool_navigation()

# Main app execution - only run when this file is executed directly
if __name__ == "__main__":
    main()
    
    # Show credits at bottom
    st.markdown("---")
    show_credits()