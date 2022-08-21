import numpy as np
from matplotlib.pyplot import *

def db(x):
    return 10*np.log10(x)

def dbm(x):
    return db(x)+30




