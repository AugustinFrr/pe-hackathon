# pe-hackathon
Hackathon info 31/10/2023
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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

classement_pays([40,3,7,50,0,0,0,0,0],2022)
