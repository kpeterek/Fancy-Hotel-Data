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
    with make_expanders("Select distribution"):
    

        # Distribution names
        display = distr_selectbox_names()
        
        # Create select box widget containing all SciPy function
        select_distribution = st.selectbox(
             'Click below (or type) to choose a distribution',
             display)
        
        st.markdown("**Parameters**")
