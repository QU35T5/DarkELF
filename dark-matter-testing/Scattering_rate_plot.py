#This is the code for the next plot which will be of gamma(the scattering rate)
# on page 6 in the Dm- sum rules paper
from darkelf import darkelf
import sys, os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker
from matplotlib import rc, rcParams
import matplotlib.cm as cm
from mpl_toolkits.axes_grid1 import make_axes_locatable

rc('text',usetex=True)
work_dir = os.getcwd()
sys.path.append(work_dir+'/..')
plotdir=work_dir+'/plots/'
Si = darkelf(target='Si',filename='Si_gpaw_withLFE.dat',phonon_filename="Si_epsphonon_data6K.dat")


targets.files("Ge")
Si = darkelf(target='Si',filename='Si_gpaw_withLFE.dat',phonon_filename="Si_epsphonon_data6K.dat")
