import streamlit as st
from pages.About_Us import about_us_page
from pages.Biology import biology_page
from pages.Chemistry import chemistry_page

st.set_page_config(
    page_title="Kulliyatul Banat",
    page_icon="🧬",
    layout="wide"
)

# Custom CSS to reduce sidebar width
st.markdown("""
    <style>
    [data-testid="stSidebar"][class="css-1aumxhk e1fqkh3o3"] {
        width: 50% !important;
        max-width: 300px !important;
    }
    [data-testid="stSidebar"][class="css-1aumxhk e1fqkh3o3"] > div {
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# Automatically choose the correct page function based on Streamlit's page navigation
def main():
    page = st.query_params.get("page", "About_Us")
    
    if page == "About_Us":
        about_us_page()
    elif page == "Biology":
        biology_page()
    elif page == "Chemistry":
        chemistry_page()

if __name__ == "__main__":
    main()