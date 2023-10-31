import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def load_data(filename):
    df = pd.read_csv(filename)
    df = df.dropna()
    df = df.rename(columns={"foo": "bar"})
    return df

##partie Agathe: faire une araignée pour un pays

from matplotlib.patches import Circle, RegularPolygon
from matplotlib.path import Path
from matplotlib.projections import register_projection
from matplotlib.projections.polar import PolarAxes
from matplotlib.spines import Spine
from matplotlib.transforms import Affine2D

