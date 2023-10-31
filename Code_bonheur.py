import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def load_data(filename):
    df = pd.read_excel(filename)
    df = df.dropna()
    return df


##partie Agathe: faire une araignée pour un pays sur les x dernières années

df_annees=load_data('Data.xls')
by_pays=df_annees.groupby(by='Country name')
def mini():
    return min(by_pays.size()) ##1 pays n'est référencé que sur une seule année
def mini_année():
    return min(df_annees['year']) #la plus petite année est 2005



from matplotlib.patches import Circle, RegularPolygon
from matplotlib.path import Path
from matplotlib.projections import register_projection
from matplotlib.projections.polar import PolarAxes
from matplotlib.spines import Spine
from matplotlib.transforms import Affine2D

pays='France'

def radar_factory(pays,frame='circle'):
    for group, subdf in by_pays:
        if group==pays:
            nb_graph=min(3,subdf.shape[0])
            df_pays=subdf.tail(nb_graph)

   
    # calculate evenly-spaced axis angles
    theta = np.linspace(0, 2*np.pi, 9, endpoint=False)

    class RadarTransform(PolarAxes.PolarTransform):

        def transform_path_non_affine(self, path):
            # Paths with non-unit interpolation steps correspond to gridlines,
            # in which case we force interpolation (to defeat PolarTransform's
            # autoconversion to circular arcs).
            if path._interpolation_steps > 1:
                path = path.interpolated(9)
            return Path(self.transform(path.vertices), path.codes)

    class RadarAxes(PolarAxes):

        name = 'radar'
        PolarTransform = RadarTransform

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # rotate plot such that the first axis is at the top
            self.set_theta_zero_location('N')

        def fill(self, *args, closed=True, **kwargs):
            """Override fill so that line is closed by default"""
            return super().fill(closed=closed, *args, **kwargs)

        def plot(self, *args, **kwargs):
            """Override plot so that line is closed by default"""
            lines = super().plot(*args, **kwargs)
            for line in lines:
                self._close_line(line)

        def _close_line(self, line):
            x, y = line.get_data()
            # FIXME: markers at x[0], y[0] get doubled-up
            if x[0] != x[-1]:
                x = np.append(x, x[0])
                y = np.append(y, y[0])
                line.set_data(x, y)

        def set_varlabels(self, labels):
            self.set_thetagrids(np.degrees(theta), labels)

        def _gen_axes_patch(self):
            # The Axes patch must be centered at (0.5, 0.5) and of radius 0.5
            # in axes coordinates.
            if frame == 'circle':
                return Circle((0.5, 0.5), 0.5)
            elif frame == 'polygon':
                return RegularPolygon((0.5, 0.5), 9,
                                      radius=.5, edgecolor="k")
            else:
                raise ValueError("Unknown value for 'frame': %s" % frame)

        def _gen_axes_spines(self):
            if frame == 'circle':
                return super()._gen_axes_spines()
            elif frame == 'polygon':
                # spine_type must be 'left'/'right'/'top'/'bottom'/'circle'.
                spine = Spine(axes=self,
                              spine_type='circle',
                              path=Path.unit_regular_polygon(9))
                # unit_regular_polygon gives a polygon of radius 1 centered at
                # (0, 0) but we want a polygon of radius 0.5 centered at (0.5,
                # 0.5) in axes coordinates.
                spine.set_transform(Affine2D().scale(.5).translate(.5, .5)
                                    + self.transAxes)
                return {'polar': spine}
            else:
                raise ValueError("Unknown value for 'frame': %s" % frame)

    register_projection(RadarAxes)
    return theta,nb_graph,df_pays



theta,nb_graph,df_pays = radar_factory(pays, frame='polygon')

    
spoke_labels = ['Life Ladder','Log GDP','Social Support',
                    'Healthy life expectancy','Freedom life choices','Generosity',
                    'Corruption','Positive affect','Negative affect']

fig, axs = plt.subplots(figsize=(9, 9), nrows=1, ncols=nb_graph,
                            subplot_kw=dict(projection='radar'))
fig.subplots_adjust(wspace=0.25, hspace=0.20, top=0.85, bottom=0.05)

colors = ['b', 'r', 'g']
    # Plot the four cases from the example data on separate axes
for ax, (title, case_data) in zip(axs.flat, df_pays):
    ax.set_rgrids([0.2, 0.4, 0.6, 0.8])
    ax.set_title(title, weight='bold', size='medium', position=(0.5, 1.1),
                     horizontalalignment='center', verticalalignment='center')
    for d, color in zip(case_data, colors[:nb_graph]):
        ax.plot(theta, d, color=color)
        ax.fill(theta, d, facecolor=color, alpha=0.25, label='_nolegend_')
        ax.set_varlabels(spoke_labels)

    # add legend relative to top-left plot
labels = ('pays')
legend = axs[0, 0].legend(labels, loc=(0.9, .95),
                              labelspacing=0.1, fontsize='small')

fig.text(0.5, 0.965, 'différents critères pour les dernières années recensées',
             horizontalalignment='center', color='black', weight='bold',
             size='large')

plt.show()

### nouvel objectif: histogramme des 3 dernières années des différents critères
plt.style.use('_mpl-gallery')
def dernières_années(pays):
    for group, subdf in by_pays:
            if group==pays:
                nb_graph=min(3,subdf.shape[0])
                df_pays=subdf.tail(nb_graph)
    return nb_graph,df_pays

def trace(pays):
     nb_graph,df_pays=dernières_années(pays)
     if nb_graph==1:
          y=[df.iloc[[0],[12,13,14,15,16,17,18,19,20]]]
          x=['Life Ladder','Log GDP','Social Support',
                    'Healthy life expectancy','Freedom life choices','Generosity',
                    'Corruption','Positive affect','Negative affect']
          fig, axes = plt.subplots(1,1,figsize=(10, 5))
          axes.shape
          axes.bar(x, y1, width=1, edgecolor="white", linewidth=0.7)
          axes.set_ylabel('score')
          
    elif nb_graph==2:
# importation des modules
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('Data.xls')



# 1ere partie

# normalisation des données, création d'un index

#pour rajouter la colonne Id et en faire un index :
df['Id'] = df['Country name'] + df['year'].map(str)
df.set_index('Id', inplace=True)

# Renormalisation des colonnes:
maxLl = df['Life Ladder'].max(skipna = True)
minLl = df['Life Ladder'].min(skipna = True)
df['Life Ladder Normalized'] = (df['Life Ladder'] - minLl)/(maxLl -minLl)

maxLogGDP = df['Log GDP per capita'].max(skipna = True)
minLogGDP = df['Log GDP per capita'].min(skipna = True)
df['Log GDP per capita Normalized'] = (df['Life Ladder'] - minLogGDP)/(maxLogGDP -minLogGDP)

maxSs = df['Social support'].max(skipna = True)
minSs = df['Social support'].min(skipna = True)
df['Social support Normalized'] = (df['Social support'] - minSs)/(maxSs -minSs)

maxHea = df['Healthy life expectancy at birth'].max( skipna = True)
minHea = df['Healthy life expectancy at birth'].min(skipna = True)
df['Healthy life expectancy at birth Normalized'] = (df['Healthy life expectancy at birth'] - minHea)/(maxHea -minHea)

maxFree = df['Freedom to make life choices'].max( skipna = True)
minFree = df['Freedom to make life choices'].min( skipna = True)
df['Freedom to make life choices Normalized'] = (df['Freedom to make life choices'] - minFree)/(maxFree -minFree)

maxPC = df['Perceptions of corruption'].max( skipna = True)
minPC = df['Perceptions of corruption'].min( skipna = True)
df['Perceptions of corruption Normalized'] = 1 - (df['Perceptions of corruption'] - minPC)/(maxPC -minPC)

maxPA = df['Positive affect'].max(skipna = True)
minPA = df['Positive affect'].min(skipna = True)
df['Positive affect Normalized'] = (df['Positive affect'] - minPA)/(maxPA -minPA)

maxPA = df['Generosity'].max(skipna = True)
minPA = df['Generosity'].min(skipna = True)
df['Generosity Normalized'] = (df['Generosity'] - minPA)/(maxPA -minPA)

maxNA = df['Negative affect'].max( skipna = True)
minNA = df['Negative affect'].min( skipna = True)
df['Negative affect Normalized'] = 1 - (df['Negative affect'] - minNA)/(maxNA -minNA)




# Partie 2
# pour produire un classement des pays selon une pondération des critèes

Colonnes = ['Life Ladder  Normalized', 'Log GDP per capita Normalized', 'Social support Normalized', 'Healthy life expectancy at birth Normalized', 'Freedom to make life choices Normalized', 'Generosity Normalized', 'Perceptions of corruption Normalized', 'Positive affect Normalized', 'Negative affect Normalized']

def classement_pays (LIC,annee) :
    #ListeImportanceCritère est sous la forme de pourcentage ex : (40,3,7,50,0,0,0,0)
    df = pd.read_excel('Data.xls')
    df_annee = df[(df['year']==annee)]
    df_annee['nouveau_taux']=df['Life Ladder']*(LIC[0]/100)+df['Log GDP per capita']*(LIC[1]/100)+df['Social support Normalized']*(LIC[2]/100)+df['Healthy life expectancy at birth Normalized']*(LIC[3]/100)+df['Freedom to make life choices Normalized']*(LIC[4]/100)+df['Generosity Normalized']*(LIC[5]/100)+df['Perceptions of corruption Normalized']*(LIC[6]/100)+df['Positive affect Normalized']*(LIC[7]/100)+df['Negative affect Normalized']*(LIC[8]/100)
    df_annee=df_annee.sort_values(by=['nouveau_taux'], ascending=False)
    max = df_annee['nouveau_taux'].max()
    df_annee['nouveau_taux']=(df_annee['nouveau_taux']/max)*20
    plt.bar(x=df_annee['Country name'], height=df_annee['nouveau_taux'],linewidth=0.7,width=1)
    plt.title("Classement de l'année demandée des pays selon vos critères")
    plt.xlabel('Pays')
    plt.ylabel('Note sur 20')
   # plt.bar_label(rotation=90, padding=3)
    plt.tight_layout()
    plt.show()

# Test classement_pays 
classement_pays([40,3,7,50,0,0,0,0,0],2022)



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


