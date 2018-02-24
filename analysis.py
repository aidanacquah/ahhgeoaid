# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 11:23:47 2018

@author: acqa
"""

import numpy as np
import pandas as pd

def get_temporal_weights(n_points):
    weights = np.zeros(n_points)
    for i in range(n_points):
        weights[i] = (1.0/(i+1))

    weights = weights/np.sum(weights)
    
    return weights

df = pd.read_csv('Outbreak.csv',sep=',')

for j in range(len(df)):
    df.set_value(j,'Cases',np.float(df['Cases'][j].replace(',','')))

mapping = {"Amran": (16.15,43.92),
           "Al Mahwit":(15.38,43.57),
           "Al Dhale'e":(13.83,44.74),
           "Hajjah":(16.09,43.25),
           "Sana'a":(15.35,44.32),
           "Dhamar":(14.60,44.17),
           "Abyan":(13.68,46.09),
           "Al Hudaydah":(14.79,43.19),
           "Al Bayda":(14.28,45.34),
           "Amanat Al Asimah":(15.40,44.21),
           "Al Jawf":(16.59,45.77),
           "Raymah":(14.63,43.67),
           "Lahj":(13.08,44.48),
           "Aden":(12.83,44.83),
           "Ibb":(14.06,44.14),
           "Taizz":(13.43,43.83),
           "Marib":(15.41,45.46),
           "Sa'ada":(17.02,43.96),
           "Al Maharah":(16.6,51.57),
           "Shabwah":(14.6,45.94),
           "Moklla":(14.54,49.13),
           "Say'on":(15.94,48.80)
           }

areas = ['Amran', 'Al Mahwit', "Al Dhale'e", 'Hajjah', "Sana'a", 'Dhamar', 'Abyan', 'Al Hudaydah', 'Al Bayda', 'Amanat Al Asimah', 'Al Jawf', 'Raymah', 'Lahj', 'Aden', 'Ibb', 'Taizz', 'Marib', "Sa'ada", 'Al Maharah', 'Shabwah', 'Moklla', "Say'on"]

weighted_data = np.empty(len(areas),dtype=np.float64)

for i,area in enumerate (areas):
    data = df[df['Governorate']==area]['CFR (%)']

    weights = get_temporal_weights(len(data))

    weighted_data[i] = np.dot(data,weights)


    # = np.dot(data,weights)