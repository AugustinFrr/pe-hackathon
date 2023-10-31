#plan
# import file as panda 
# group data per country 
# make the country the index
# normalise

import pandas as pd

df = pd.read_excel('Data.xls')

# colonne Life Ladder
maxLl = df['Life ladder'].max(axis = 1, skipna = True)
minLl = df['Life ladder'].min(axis = 1, skipna = True)
df['Life Ladder Normalized'] = (df['Life Ladder'] - minLl)/(maxLl -minLl)

# colonne Log GDP per capita
maxLogGDP = df['Log GDP per capita'].max(axis = 1, skipna = True)
minLogGDP = df['Log GDP per capita'].min(axis = 1, skipna = True)
df['Log GDP per capita Normalized'] = (df['Life Ladder'] - minLogGDP)/(maxLogGDP -minLogGDP)

# colonne Social support
maxSs = df['Social support'].max(axis = 1, skipna = True)
minSs = df['Social support'].min(axis = 1, skipna = True)
df['Social support Normalized'] = (df['Social support'] - minSs)/(maxSs -minSs)

# colonne Healthy life expectancy at birth
maxHea = df['Healthy life expectancy at birth'].max(axis = 1, skipna = True)
minHea = df['Healthy life expectancy at birth'].min(axis = 1, skipna = True)
df['Healthy life expectancy at birth Normalized'] = (df['Healthy life expectancy at birth'] - minHea)/(maxHea -minHea)

# colonne Freedom to make life choices
maxFree = df['Freedom to make life choices'].max(axis = 1, skipna = True)
minFree = df['Freedom to make life choices'].min(axis = 1, skipna = True)
df['Freedom to make life choices Normalized'] = (df['Freedom to make life choices'] - minFree)/(maxFree -minFree)

# colonne Perceptions of corruption
maxPC = df['Perceptions of corruption'].max(axis = 1, skipna = True)
minPC = df['Perceptions of corruption'].min(axis = 1, skipna = True)
df['Perceptions of corruption Normalized'] = 1 - (df['Perceptions of corruption'] - minPC)/(maxPC -minPC)

# colonne Positive affect
maxPA = df['Positive affect'].max(axis = 1, skipna = True)
minPA = df['Positive affect'].min(axis = 1, skipna = True)
df['Positive affect Normalized'] = (df['Positive affect'] - minPA)/(maxPA -minPA)

# colonne Negative affect
maxNA = df['Negative affect'].max(axis = 1, skipna = True)
minNA = df['Negative affect'].min(axis = 1, skipna = True)
df['Negative affect Normalized'] = 1 - (df['Negative affect'] - minNA)/(maxNA -minNA)
