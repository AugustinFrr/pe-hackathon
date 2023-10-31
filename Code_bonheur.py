# 





# 3e partie
# Comparaison de 2 pays à partir de l'excel 'Data.xls'
# Création d'une fonction qui prend pour argument 2 pays et éventuellement une liste de critères et renvoie un graphique comparatif
Colonnes = ['Life Ladder', 'Log GDP per capita', 'Social support', 'Healthy life expectancy at birth', 'Freedom to make life choices', 'Generosity', 'Perceptions of corruption', 'Positive affect', 'Negative affect']

import pandas as pd
import matplotlib.pyplot as plt
df_bonheur = pd.read_excel('Data.xls')


def comparateur(Id1, Id2, annee liste_critères = None):
    if liste_critères == None:
        liste_critères = Colonnes
    Id1 = Id1 + str(annee)
    Id2 = Id2 + str(annee)
    i=0
    for critère in liste_critères:
        plt.figure(figsize=(10,5))
        plt.bar(i,df_bonheur.loc[Id1,critère], label=Id1)
        plt.bar(i,df_bonheur.loc[Id2,critère], label=Id2)
        i += 1
        plt.xlabel('Année')
        plt.ylabel(critère)
        plt.legend()
        plt.show()


print(df_bonheur.head(3))

