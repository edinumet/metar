#! /usr/bin/env python

# egphstab.py
# 1. Draws all variables in a METAR file
 
# Version 0.1
# Date 02 March 2020
# Author: jbm
# Latest: 10:51 03/03/2020

import pandas as pd
import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt
import datetime as dt
from datetime import timedelta

from numpy import float32
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
inpath = ''

# set the name of the input file with airport observations from the METAR archive
infilename = inpath+'EGPH.csv'
headers = ['station', 'valid', 'tmpc', 'dwpc', 'relh', 'drct',
         'sped', 'mslp', 'gust_mph', 'skyc1', 'skyc2', 'skyc3', 'skyl1', 'skyl2', 'skyl3',
         'peak_wind_gust_mph', 'peak_wind_drct']
# types = {'station': 'str', 'valid': 'str', 'tmpc': 'float', 'dwpc': 'float', 'relh' : 'float', 'drct' : 'float',
#          'sped': 'float', 'mslp': 'float', 'gust_mph': 'float', 'skyc1': 'str', 'skyc2': 'str', 'skyc3': 'str',
#          'skyl1': 'str', 'skyl2': 'float', 'skyl3': 'float', 'wxcodes': 'str',
#          'peak_wind_gust_mph': 'float', 'peak_wind_drct': 'float'}
# arse_dates = ['valid']
# Have to clean up the original data file since thee's a mixture of numbers and strings in some columns
# So - replaced the metcodes and skycn information as follows:
# few = 0, skt = 1, bkn = 2, ovc = 3, ncd = 4, nsc = 5, VV = 6
# HZ = 7, BR = 8, VCFG = 9, FG = 10, IFG = 11, BCFG = 12, RA = 13, TSRA = 14, VCSH = 15,
# #NAME? = 99, SNRA = 98, RA BR = 97, -4 VCFG = 97, SHRA = 96, TS - SHRA = 95

df = pd.read_csv(infilename, sep=',', skiprows=6, header=None, names=headers)  # dtype=types)
print(df.head())

# Make the timestamp the index for the file
df['valid'] = pd.to_datetime(df['valid'], format='%d/%m/%Y %H:%M')
df = df.set_index(['valid'])

# Take the mean over 60 minutes ie 60T
df=df.resample('60T').mean()

# Put all the data into ONE big plot

df.plot(subplots=True, figsize=(10, 10))
plt.show()

# or you might just want to plot a subset of the data
#df1 = df[['gust_mph','peak_wind_gust_mph']]
df1 = df[['gust_mph', 'skyc1', 'peak_wind_gust_mph']]
df1.plot(subplots=True, figsize=(10, 10))
plt.show()

# Code below is just about playing with different plot formats

# fig = plt.figure(figsize=(14,8))
# ax1 = fig.add_subplot(4,1,1)
# ax1.set_xlabel("Date")
# ax1.set_ylabel("mm")
# ax1.set_title('JCMB Rainfall')
# ax1.grid(True)
# ax1.plot(df.index, df['rain'])
# 
# ax2 = fig.add_subplot(4,1,2)
# ax2.set_xlabel("Date")
# ax2.set_ylabel("kW m-2")
# ax2.set_title('JCMB Irradiance')
# ax2.grid(True)
# ax2.plot(df.index, df['solar'])
# 
# ax3 = fig.add_subplot(4,1,3)
# ax3.set_xlabel("Date")
# ax3.set_ylabel("m s-1")
# ax3.set_title('JCMB Wind speed')
# ax3.grid(True)
# ax3.plot(df.index, df['windsp'])
# 
# ax4 = fig.add_subplot(4,1,4)
# ax4.set_xlabel("Date")
# ax4.set_ylabel("oC")
# ax4.set_title('JCMB Air temperature')
# ax4.grid(True)
# ax4.plot(df.index, df['airT'])

#df.plt.savefig('JCMB_Weather_Data.png', dpi=300, bbox_inches='tight', pad_inches=0.5)


# have a look at the first 10 lines just to check all is as is expected
# print(df.head(10))

# Set up some plots
# ax1=df[['airT']].plot()
# ax1.set_xlabel("Date")
# ax1.set_ylabel("oC")
# ax1.set_title('JCMB Air temperature')
# plt.savefig('JCMB_T.png', dpi=300, bbox_inches='tight', pad_inches=0.5)
# 
# ax2=df[['rain','windsp','solar']].plot()
# ax2.set_xlabel("Date")
# ax2.set_ylabel("mm")
# ax2.set_title('JCMB Rain etc')
# plt.savefig('JCMB_rain.png', dpi=300, bbox_inches='tight', pad_inches=0.5)

