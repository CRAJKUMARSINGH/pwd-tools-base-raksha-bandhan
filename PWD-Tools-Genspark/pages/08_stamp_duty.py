import streamlit as st
import streamlit.components.v1 as components
from utils.branding import apply_custom_css, show_header
from utils.navigation import create_back_button

# Page configuration
st.set_page_config(
    page_title="Stamp Duty Calculator | PWD Tools Hub",
    page_icon="⚖️",
    layout="wide"
)

# Apply branding
apply_custom_css()
show_header()

def main():
    st.title("Stamp Duty Calculator")
    
    # Read and display the HTML content at full width
    try:
        with open("static/html/StampDuty.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        
        # Display the HTML content centered with wide width
        components.html(html_content, height=600, scrolling=True)
        
    except FileNotFoundError:
        st.error("Stamp Duty tool not available")
    except Exception as e:
        st.error(f"Error loading Stamp Duty: {str(e)}")

# Navigation
st.markdown("---")
create_back_button()

if __name__ == "__main__":
    main()