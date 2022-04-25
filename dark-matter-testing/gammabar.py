import numpy as np
import scipy as sp
from scipy.integrate import quad,dblquad
from scipy.special import erf
import math 
import matplotlib.pyplot as plt

temp = 1

#Constants and variables
v_0   = 23e4 #m/s
v_e   = 24e4 #m/s
v_esc = 60e4 #m/s
e = 1.6021766e-19 #C
g_chi = temp
g_e = temp
m = temp #fig one uses m = 0, we need a new expression for non-zero m (see eq. 13)

N_0 = np.pi**(3/2)*v_0**2*(v_0*math.erf(v_esc/v_0) - \
      2*v_esc/np.sqrt(np.pi)*np.exp(-v_esc**2/v_0**2))
  
#Truncated Maxwell-Boltzmann Distribution (Appendix B heterostructures)
a = (np.pi**(3/2)*v_0**3)/(4*v_e*N_0)

def p1(v_z):
        return (a*(math.erf((v_e-v_z)/v_0) + math.erf((v_e+v_z)/v_0) - \
                (np.pi*v_0**2/N_0)*np.exp(-v_esc**2/v_0**2)))*(v_z < v_esc - v_e) + \
                (a*(math.erf(v_esc/v_0) + math.erf((v_e-v_z)/v_0)) - \
                (np.pi*v_0**2)/(2*N_0)*(v_e + v_esc - v_z)/v_e*np.exp(-v_esc**2/v_0**2)) *\
                (v_esc - v_e < v_z < v_esc + v_e)

#J: My idea is to evaluate the double integral (wrt k and omega) using scipy's dlbquad,
#   and then multiplying this by the solid angle integral (entire unit sphere, also using dblquad)