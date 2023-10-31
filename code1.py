#fichier de programme
# test de changement

##partie Agathe: faire une araignée pour un pays
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from matplotlib.patches import Circle, RegularPolygon
from matplotlib.path import Path
from matplotlib.projections import register_projection
from matplotlib.projections.polar import PolarAxes
from matplotlib.spines import Spine
from matplotlib.transforms import Affine2D

def ouvrir_table(fichier):