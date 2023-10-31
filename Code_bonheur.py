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

maxNA = df['Generosity'].max( skipna = True)
minNA = df['Generosity'].min( skipna = True)
df['Generosity Normalized'] = 1 - (df['Generosity'] - minNA)/(maxNA -minNA)

#fonction du bonheur
def valeur_bonheur(pays, année, a,b,c,d,e,f,g,h,i):
    index = pays + année
    bonheur =  a*df.loc[index, 'Life Ladder Normalized'] + b*df.loc[index, 'Log GDP per capita Normalized'] +c*df.loc[index, 'Social support Normalized']+d*df.loc[index, 'Healthy life expectancy at birth Normalized']+e*df.loc[index, 'Freedom to make life choices Normalized']+f*df.loc[index, 'Generosity Normalized']+g*df.loc[index, 'Perceptions of corruption Normalized']+h*df.loc[index, 'Positive affect Normalized']+i*df.loc[index, 'Negative affect Normalized']
    return bonheur
    

#test fonction bonheur
#valeur_bonheur(df, 'Albanie' , '2018', 1/9 , 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9)



# Partie 2
def classement_pays (LIC,annee) :
    #ListeImportanceCritère est sous la forme de pourcentage ex : (40,3,7,50,0,0,0,0)
    df = pd.read_excel('Data.xls')
    df_annee = df[(df['year']==annee)]
    df_annee['nouveau_taux']=df['Life Ladder']*(LIC[0]/100)+df['Log GDP per capita']*(LIC[1]/100)+df['Social support']*(LIC[2]/100)+df['Healthy life expectancy at birth']*(LIC[3]/100)+df['Freedom to make life choices']*(LIC[4]/100)+df['Generosity']*(LIC[5]/100)+df['Perceptions of corruption']*(LIC[6]/100)+df['Positive affect']*(LIC[7]/100)+df['Negative affect']*(LIC[8]/100)
    df_annee=df_annee.sort_values(by=['nouveau_taux'], ascending=False)
    max = df_annee['nouveau_taux'].max()
    df_annee['nouveau_taux']=(df_annee['nouveau_taux']/max)*20
    plt.bar(x=df_annee['Country name'], height=df_annee['nouveau_taux'],linewidth=0.7,width=1)
    plt.title("Classement de l'année demandée des pays selon vos critères")
    plt.xlabel('Pays')
    plt.ylabel('Note sur 20')
    plt.tight_layout()
    plt.show()

# Test classement_pays 
# classement_pays([40,3,7,50,0,0,0,0,0],2022)



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

# test fonction comparateur
# comparateur('Afghanistan', 'Albania', 2018, ['Life Ladder Normalized', 'Healthy life expectancy at birth Normalized', 'Generosity Normalized', 'Perceptions of corruption Normalized', 'Negative affect Normalized'])
