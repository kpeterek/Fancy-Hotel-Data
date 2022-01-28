import streamlit as st
from scipy import stats
from scipy.stats.mstats import mquantiles
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import base64
import geopandas as gpd
from geopy.distance import geodesic
import re
import more_itertools
from itertools import permutations
import math
from streamlit_folium import folium_static
import folium


def page_explore():
	""" 
	The first page in this app made with Streamlit is for an interactive 
	exploration of the continuous distributions that are available in SciPy.
	"""
	cols_needed = ['Title','Address','City','State','PostalCode','Units','Open Date','Phase','Latitude','Longitude','distance','sort']
	cols_exist = ['StarID','Property','Address','City','State','postalcode','Rooms','Latitude','Longitude','distance']
	str_census = pd.read_csv('str_census_small.csv')
	str_pipeline = pd.read_csv('pipeline.csv')
	name_str = str_census[['Hotel Name','STR Number']]
    	
	def make_line():
        	""" Line divider between images. """
            	
        	line = st.markdown('<hr style="border:1px solid gray"> </hr>',
                unsafe_allow_html=True)

        	return line  
	
	def make_expanders(expander_name, sidebar=True):
		""" Set up expanders which contains a set of options. """
		if sidebar:         
			try:
				return st.sidebar.expander(expander_name)
			except:
				return st.sidebar.beta_expander(expander_name)

	st.sidebar.subheader("To explore:")
	#with make_expanders("Select Hotel"):

	
	hotel = st.sidebar.selectbox('Select Hotel',name_str['Hotel Name'])
	st.sidebar.write(hotel, ' has the StarID of ',name_str[name_str['Hotel Name'] == hotel]['STR Number'].item())
	star = st.sidebar.number_input(label='Enter Star ID',value=63037)
	st.markdown("**Subject Property**")	
	submit = st.sidebar.button('Pull Hotel Information')
	data = str_census[str_census['STR Number'] == int(star)]
	st.dataframe(data)
	coords = list(data[['Latitude','Longitude']].values.flatten())
	m = folium.Map(location=coords, zoom_start=16)
	tooltip = data['Hotel Name'].values[0]
	folium.Marker(coords, tooltip=tooltip).add_to(m)
	folium_static(m)
	#st.write(list(data[['Latitude','Longitude']].values.flatten()))
	radius_option = st.sidebar.radio("Options", ('7mile search radius', 'Custom Slider','Manual Input')) 
	

	def nearby_comps_str(STR,radius=7):
		R = 3958.756
		prop_name = str_census['Hotel Name'][str_census['STR Number'] == STR].iloc[:,].item()
		prop_city = str_census['City'][str_census['STR Number'] == STR].iloc[:,].item()
		coords_subj = str(str_census.iloc[:,27][str_census['STR Number'] == STR].iloc[:,].item()),str(str_census.iloc[:,28][str_census['STR Number'] == STR].iloc[:,].item())
		lat_min,lat_max = math.degrees(math.radians(float(coords_subj[0]))-radius/R),math.degrees(math.radians(float(coords_subj[0]))+radius/R)
		lon_min,lon_max = math.degrees(math.radians(float(coords_subj[1]))-math.asin(math.sin(radius/R)/math.cos(math.radians(float(coords_subj[0]))))),math.degrees(math.radians(float(coords_subj[1]))+math.asin(math.sin(radius/R)/math.cos(math.radians(float(coords_subj[0])))))
		distance_census = str_census.dropna(subset=['Latitude','Longitude'])[(str_census.Latitude.between(lat_min,lat_max))&(str_census.Longitude.between(lon_min,lon_max))]
		distance_census["Lat,Lon"] = list(zip(distance_census['Latitude'],distance_census['Longitude']))
		distance_census ['distance'] = [geodesic(coords_subj,distance_census['Lat,Lon'].loc[distance_census.index == x]).miles for x in distance_census.index]
		print(prop_name, prop_city, coords_subj)
		return distance_census

	
		
	def obtain_functional_data():
		def sliders():
			"""
			Function that defines a slider. It's going to be
			initiated with the default value as defined in SciPy.
			Slider min value of 0.01; max value of 10 - are added
			arbitrary.
			"""

			slider_i = st.slider('Default value: '+'{}'.format(param)+' = '+f'{parameter_value}',
				   min_value = min_param_value,
				   value = float("{:.2f}".format(parameter_value)),
				   max_value = 1000.00,
				   step = step_value)

			return slider_i

		    # Doing try and except which will allow slider stepping
		    # interval to be changed in the advanced mode.
			try:
				if radius == 'Custom Slider':
					step_value = 0.10
					slider_i = sliders()
					sliders_params.append(slider_i)

				if radius == 'Manually Input':
					manual = float(st.text_input('Default value: '+'{}'.format(param)+' = '+f'{parameter_value}', float("{:.2f}".format(parameter_value))))
					sliders_params.append(manual)
			except:
				step_value = 0.10
				slider_i = sliders()  
				sliders_params.append(slider_i)
			return sliders_params
	sliders_params = obtain_functional_data()
	if radius_option == '7mile search radius':
		radius = 7.0
	if radius_option == 'Custom Slider':
		radius = st.sidebar.slider('Select radius',0.0,6.0,(0.0,3.0))[1]
	if radius_option == 'Manual Input':
		radius = st.sidebar.number_intput(label='Enter Radius (MI): ',value=15.0)
	rooms = st.sidebar.slider('Select room range',10,1000,(50, 120))
	comps_button = st.sidebar.button('Pull Hotel Comps')
	
	if comps_button:
		make_line()
		st.markdown("**Operating Comps**")
		comp_data = nearby_comps_str(star,radius=radius)
		st.dataframe(comp_data.loc[(comp_data['Rooms'].between(rooms[0],rooms[1]))])
			




