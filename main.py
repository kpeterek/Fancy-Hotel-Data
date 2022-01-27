import streamlit as st

# Add pages -- see those files for deatils within
from page_explore import page_explore
from page_fit import page_fit
from page_introduction import page_introduction

# Use random seed
import numpy as np
np.random.seed(1)


# Set the default elements on the sidebar
st.set_page_config(page_title='HotelAnalyzer')

logo, name = st.sidebar.columns(2)
with logo:
    image = "moniker_white.png"
    st.image(image, use_column_width=True)
with name:
    st.markdown("<h1 style='text-align: left; color: grey;'> \
                Hotel Data Site </h1>", unsafe_allow_html=True)

st.sidebar.write(" ")


def main():
    """
    Register pages to Explore and Fit:
        page_introduction - contains page with images and brief explanations
        page_explore - contains various functions that allows exploration of
                        continuous distribution; plotting class and export
        page_fit - contains various functions that allows user to upload
                    their data as a .csv file and fit a distribution to data.
    """

    pages = {
        "Introduction": page_introduction,
        "Find Hotels": page_lookup,
        "Import Star Data": page_str,
        "New Supply": page_ns
    }

    st.sidebar.title("Main options")

    # Radio buttons to select desired option
    page = st.sidebar.radio("Select:", tuple(pages.keys()))
                                
    # Display the selected page with the session state
    pages[page]()

    # Write About
    st.sidebar.header("About")
    st.sidebar.warning(
            """
            Hotel Analyser app is created and maintained by 
            **Kyle P.**. 
            """
    )


if __name__ == "__main__":
    main()
