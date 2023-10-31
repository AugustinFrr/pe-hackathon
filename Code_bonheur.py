# 





Colonnes = ['Life Ladder  Normalized', 'Log GDP per capita Normalized', 'Social support Normalized', 'Healthy life expectancy at birth Normalized', 'Freedom to make life choices Normalized', 'Generosity Normalized', 'Perceptions of corruption Normalized', 'Positive affect Normalized', 'Negative affect Normalized']

# importation des modules
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('Data.xls')

# 1ere partie 
# normalisation des données, création d'un index

#pour rajouter la colonne Id et en faire un index :
df['Id'] = df['Country name'] + df['year'].map(str)
df.set_index('Id', inplace=True)

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

# colonne Generosity
maxPA = df['Generosity'].max(skipna = True)
minPA = df['Generosity'].min(skipna = True)
df['Generosity Normalized'] = (df['Generosity'] - minPA)/(maxPA -minPA)

# colonne Negative affect
maxNA = df['Negative affect'].max( skipna = True)
minNA = df['Negative affect'].min( skipna = True)
df['Negative affect Normalized'] = 1 - (df['Negative affect'] - minNA)/(maxNA -minNA)



#fonction du bonheur



# 3e partie
# Comparaison de 2 pays à partir de l'excel 'Data.xls'
# Création d'une fonction qui prend pour argument 2 pays et éventuellement une liste de critères et renvoie un graphique comparatif
# On peut choisir les critères à comparer parmi les colonnes du fichier excel 'Data.xls' ou la liste Colonnes initialisée au début du code

def comparateur(Id1, Id2, annee, liste_critères = None):
    '''
    Fonction qui prend en argument 2 pays, une année et éventuellement une liste de critères et renvoie un histogramme comparatif des 2 pays
    '''

    if liste_critères == None:
        liste_critères = Colonnes
    Id1 = Id1 + str(annee)
    Id2 = Id2 + str(annee)
    
    valeurs_Id1 = [df.loc[Id1, critère] for critère in liste_critères]
    valeurs_Id2 = [df.loc[Id2, critère] for critère in liste_critères]
    
    x = range(len(liste_critères))
    
    plt.figure(figsize=(10,5))
    plt.bar([i-0.2 for i in x], valeurs_Id1, label=Id1, width=0.4)
    plt.bar([i+0.2 for i in x], valeurs_Id2, label=Id2, width=0.4)
    plt.xticks(x, liste_critères, rotation='vertical')
    plt.ylabel('Valeur')
    plt.legend()
    plt.show()

comparateur('Afghanistan', 'Albania', 2018, ['Life Ladder Normalized', 'Healthy life expectancy at birth Normalized', 'Generosity Normalized', 'Perceptions of corruption Normalized', 'Negative affect Normalized'])