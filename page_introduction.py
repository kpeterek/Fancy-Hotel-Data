import streamlit as st

def page_introduction():
    
    # Space so that 'About' box-text is lower
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    
    st.markdown("<h2 style='text-align: center;'> Welcome To </h2>", 
                unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;'> Hotel Analyser</h1>", 
                unsafe_allow_html=True)
     

    st.info("""
            There are three main features: \n
            - Retrieving Comp Sets
            - Pulling a geolocated New Supply
            - Importing STR Data  
            $←$ To start playing with the app, select an option on the 
            left sidebar.
            """)


   
    def make_line():
        """ Line divider between images. """
            
        line = st.markdown('<hr style="border:1px solid gray"> </hr>',
                unsafe_allow_html=True)

        return line    

    return


'''

    # Images and brief explanations.
    st.error('Explore distributions')
    feature1, feature2 = st.columns([0.5,0.4])
    with feature1:
        #st.image(image1, use_column_width=True)
    with feature2:
        st.warning('Search for Hotel')
        st.info("""
                - Select distribution from Dropdown Menu (or type its name)
                - Change distribution parameters on sliders and see the change. 
                - Check created hyperlink to **SciPy** official documentation at the bottom of the sidebar.
                """)
    
    make_line()
    
    feature3, feature4 = st.columns([0.6,0.4])
    with feature3:        
        st.image(image2, use_column_width=True)
    with feature4:
        st.warning('Tweak Display')
        st.info("""
                - Pick *Dark/Light Theme*
                - Select **on/off** each option: Histogram, PDF, CDF, SF,
                boxplot, quantiles, or shade 1/2/3 $\sigma$.
                - Get Table with descriptive statistics.
                """)
    make_line()
    
    feature5, feature6 = st.columns([0.6,0.4])
    with feature5:
        st.image(image3, use_column_width=True)
    with feature6:
        st.warning('Export')
        st.info("""
                - Generate a Python code with selected distribution and 
                parameters
                - Save .py file or copy to clipboard to take it home.
                """)
    
    make_line()
    
    st.error('Fit distributions')
    feature7, feature8 = st.columns([0.4,0.6])
    with feature7:
        st.warning('Import')
        st.info("""
                - Import a **.csv** file with your own data (or get a sample).
                - Plot your data with or without basic statistical information.
                """)
    with feature8:
        st.image(image4, use_column_width=True)
    
    make_line()
    
    feature9, feature10 = st.columns([0.4,0.6])
    with feature9:
        st.warning('Fit')
        st.info("""
                - Multiselectbox: pick any number of distributions
                - **'All_distributions'** - select all
                - Fit distribution(s) to your data
                """)
    with feature10:
        st.image(image5, use_column_width=True)        
    
    make_line()
    
    feature10, feature11 = st.columns([0.4,0.6])
    with feature10:
        st.warning('Results & Export')
        st.info("""
                - Interactive **Figures**
                - **Table** with all fitted distribution(s) 
                - Generate **Python code** with best fit distribution 
                """)
    with feature11:
        st.image(image6, use_column_width=True)      
    
    make_line()
    
    st.info('There are 100 continuous distribution functions  \
                from **SciPy v1.6.1** available to play with.')
                '''
