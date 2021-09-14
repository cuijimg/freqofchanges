# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 12:28:20 2021

@author: F-CUI
"""
import pandas as pd
from pathlib import Path
import dateutil
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np

sdate = dt.date(2012,1,1)
edate = dt.date(2020,12,31)
bowlist =pd.date_range(sdate,edate,freq='qs')
bowlist = bowlist.strftime('%Y-%m-%d')
dict1 = {bowlist[i]: 0 for i in range(len(bowlist))}

file = Path(r'I:\!Hiwis\f-kraeme\Internship\readability_sample_withoutnas_with_score.csv')
df = pd.read_csv(file,encoding='utf-8')
print(len(df))


for i in range(len(df)):
    print(i)
    if i==0:
        continue
    if (df.loc[i,'nWS score'] != df.loc[i-1,'nWS score']) & (df.loc[i,'firm identifier'] == df.loc[i-1,'firm identifier']):
        dict1[df.loc[i,'date']] += 1


print(dict1)
print(len(df['firm identifier'].unique()))




