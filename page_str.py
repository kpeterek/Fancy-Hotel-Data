
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 13:23:16 2020

@author: KyleP
"""

import time
import pandas as pd
import os
import numpy as np
import geopandas as gpd
from geopy.distance import geodesic
import re
import more_itertools
from itertools import permutations
import math
import streamlit as st


def page_str():
    """ 
    The first page in this app made with Streamlit is for an interactive 
    exploration of the continuous distributions that are available in SciPy.
    """
    
    name_docstring_dict, name_eq_dict, name_proper_dict, \
        all_dist_params_dict, name_url_dict = creating_dictionaries()
    
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
