import streamlit as st
from scipy import stats
from scipy.stats.mstats import mquantiles
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import base64


def page_explore():
    """ 
    The first page in this app made with Streamlit is for an interactive 
    exploration of the continuous distributions that are available in SciPy.
    """
    
    
    def make_expanders(expander_name, sidebar=True):
        """ Set up expanders which contains a set of options. """
        if sidebar:         
            try:
                return st.sidebar.expander(expander_name)
            except:
                return st.sidebar.beta_expander(expander_name)
    
    st.sidebar.subheader("To explore:")
    with make_expanders("Select Hotel"):
    

        # Distribution names
        hotel = st.sidebar.selectbox('Select Hotel',name_str['Property'])
		st.sidebar.write(hotel, ' has the StarID of ',name_str[name_str.Property == hotel]['StarID'].item())
		data = dodge_pipeline[['Title','Address','City','State','PostalCode','Units','Open Date','Phase','Latitude','Longitude']]
		star = st.sidebar.text_input('Enter Star ID')
		st_filter = st.sidebar.selectbox('Filter by?', ['radius','tract','city'])
		radius = st.sidebar.text_input('Radius?')
		if radius.isnumeric():
    			pass
		else:
    			radius = 0.0
		submit = st.sidebar.button('run new supply')
		if submit:
			data = dd.newsupply(float(star),float(radius),st_filter)
			st.write(data.dropna())
			data.rename(columns = {'Latitude':'lat','Longitude':'lon'},inplace=True)
			data.dropna(inplace=True)
			st.map(data)
        
        # Create select box widget containing all SciPy function
        select_distribution = st.selectbox(
             'Click below (or type) to choose a distribution',
             display)
        
        st.markdown("**Parameters**")
