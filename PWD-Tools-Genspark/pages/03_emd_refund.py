import streamlit as st
import streamlit.components.v1 as components
from utils.branding import apply_custom_css, show_header
# Remove the import of create_breadcrumb to avoid duplication
from utils.navigation import create_back_button

# Page configuration
st.set_page_config(
    page_title="EMD Refund | PWD Tools Hub",
    page_icon="💳",
    layout="wide"
)

# Apply branding
apply_custom_css()
show_header()
# Remove breadcrumb to avoid duplication
# create_breadcrumb("EMD Refund")

def main():
    # Read and display the HTML content at full width
    try:
        with open("static/html/EmdRefund.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        
        # Display the HTML content centered with wide width
        components.html(html_content, height=1000, scrolling=True)
        
    except FileNotFoundError:
        st.error("EMD Refund tool not available")
    except Exception as e:
        st.error(f"Error loading EMD Refund: {str(e)}")

# Navigation
st.markdown("---")
create_back_button()

if __name__ == "__main__":
    main()