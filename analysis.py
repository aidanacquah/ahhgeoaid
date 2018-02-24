# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 11:23:47 2018

@author: acqa
"""

import numpy as np
import pandas as pd

df = pd.read_csv('Outbreak.csv',sep=',')

casesdf = df[['Date','Governorate','Cases']]


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

casedf = casesdf.replace({'Governorate': mapping})