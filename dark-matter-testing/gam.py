from doctest import OutputChecker
import numpy as np
import matplotlib as plt
import scipy as sp
from scipy.integrate import tplquad
from VelocityDist import contour_func
from darkelf.epsilon import elf


t = 1 # temp

g_chi = t # coupling strenght of DM particle to mediator
g_e = t # coupling strenght of mediator to EM charge
g_0 = t # upper bound of 1 - 1/eps_L(0,k) (physical meaning??)
m_chi = t # DM-particle mass (eV)
m =  t # mediator mass (eV)
v_0 = 2.3e5 # (m/s)
e = 1.6022e-19 # (C)

gamma_opt = 0.68 * g_chi**2 * g_e**2 * g_0 / (4 * np.pi * e**2) * m_chi * v_0
            # for massless mediator

# gamma_opt = 9.1 * g_chi**2 * g_e**2 * g_0 / (4 * np.pi * e**2) * m_chi * v_0 *\
#             (m_chi * v_0 /m)**4
#           for heavy mediator of mass m (?)





#gamma_bar = 2 * g_chi**2 * g_e**2 / e**2 * 
    # konstanter * int_k1^k2 1 dk * int_w1^w2 contour_fnc(w,k) /w dw * \
    # int_enhetessfär (1-eps(0,k))/(2pi)^3 * ELF(w,k) dOmega