#adélie

import pandas as pd

df = pd.read_excel('Data.xls')

# colonne Life Ladder
maxLl = df['Life Ladder'].max(skipna = True)
minLl = df['Life Ladder'].min(skipna = True)
df['Life Ladder Normalized'] = (df['Life Ladder'] - minLl)/(maxLl -minLl)

# colonne Log GDP per capita
maxLogGDP = df['Log GDP per capita'].max(skipna = True)
minLogGDP = df['Log GDP per capita'].min(skipna = True)
df['Log GDP per capita Normalized'] = (df['Life Ladder'] - minLogGDP)/(maxLogGDP -minLogGDP)

# colonne Social support
maxSs = df['Social support'].max(skipna = True)
minSs = df['Social support'].min(skipna = True)
df['Social support Normalized'] = (df['Social support'] - minSs)/(maxSs -minSs)

# colonne Healthy life expectancy at birth
maxHea = df['Healthy life expectancy at birth'].max( skipna = True)
minHea = df['Healthy life expectancy at birth'].min(skipna = True)
df['Healthy life expectancy at birth Normalized'] = (df['Healthy life expectancy at birth'] - minHea)/(maxHea -minHea)

# colonne Freedom to make life choices
maxFree = df['Freedom to make life choices'].max( skipna = True)
minFree = df['Freedom to make life choices'].min( skipna = True)
df['Freedom to make life choices Normalized'] = (df['Freedom to make life choices'] - minFree)/(maxFree -minFree)

# colonne Perceptions of corruption
maxPC = df['Perceptions of corruption'].max( skipna = True)
minPC = df['Perceptions of corruption'].min( skipna = True)
df['Perceptions of corruption Normalized'] = 1 - (df['Perceptions of corruption'] - minPC)/(maxPC -minPC)

# colonne Positive affect
maxPA = df['Positive affect'].max(skipna = True)
minPA = df['Positive affect'].min(skipna = True)
df['Positive affect Normalized'] = (df['Positive affect'] - minPA)/(maxPA -minPA)

# colonne Negative affect
maxNA = df['Negative affect'].max( skipna = True)
minNA = df['Negative affect'].min( skipna = True)
df['Negative affect Normalized'] = 1 - (df['Negative affect'] - minNA)/(maxNA -minNA)

#print(df.head(8))

#pour rajouter la colonne Id:

import pandas as pd
df = pd.read_excel('Data.xls')
df['Id'] = df['Country name'] + df['year'].map(str)
print(df.head(8))

#fonction du bonheur