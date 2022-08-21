from lib import *

def db(x):
    return 10*np.log10(x)

def dbm(x):
    return db(x)+30

def idb(x):
    return 10**(x/10)

def idbm(x):
    return 10**(x/10-3)



