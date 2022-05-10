import numpy as np
import scipy as sp
from scipy.special import erf
import math 
import matplotlib.pyplot as plt

#Velocities (km/s)
v_0   = 230 #Halo velocity
v_e   = 240 #Earth velocity
v_esc = 600 #Galaxy escape velocity
  
#Probability distribution for DM-velocities
N_0 = np.pi**(3/2)*v_0**2*(v_0*math.erf(v_esc/v_0) - \
      2*v_esc/np.sqrt(np.pi)*np.exp(-v_esc**2/v_0**2))
a = (np.pi**(3/2)*v_0**3)/(4*v_e*N_0)

def p1(v_z):
        return (a*(math.erf((v_e-v_z)/v_0) + math.erf((v_e+v_z)/v_0) - \
                (np.pi*v_0**2/N_0)*np.exp(-v_esc**2/v_0**2)))*(v_z < v_esc - v_e) + \
                (a*(math.erf(v_esc/v_0) + math.erf((v_e-v_z)/v_0)) - \
                (np.pi*v_0**2)/(2*N_0)*(v_e + v_esc - v_z)/v_e*np.exp(-v_esc**2/v_0**2)) * \
                (v_esc - v_e < v_z < v_esc + v_e)

m_chi = 1e4
omega = np.linspace(0,3*m_chi*v_0**2)
k     = np.linspace(0,3*m_chi*v_0)

#Contour graph routine
np.seterr(divide='ignore', invalid='ignore')
[K,W] = np.meshgrid(k,omega)

X = np.zeros((len(K), len(K[0])))
Y = np.zeros((len(K), len(K[0])))
contour_func = np.zeros((len(K), len(K[0])))

for i in range(len(K)):
        for j in range(len(K[0])):
                contour_func[i][j] = W[i][j]/K[i][j]*p1(W[i][j]/K[i][j] + K[i][j]/(2*m_chi))
                X[i][j] =  K[i][j]/(v_0*m_chi)
                Y[i][j] = W[i][j]/(v_0**2*m_chi) 

plt.contourf(X,Y,contour_func,9)
plt.xlabel(r'$k/(m_\chi v_0)$')
plt.ylabel(r'$\omega/(m_\chi v_0^2)$')
cbar = plt.colorbar()
cbar.set_label(r'$\frac{\omega}{k}p_1\left( \frac{\omega}{k} + \frac{k}{wm_\chi} \right) \mathrm{\; [s/km]}$')
plt.show()

#Saves figure as a pdf-file to the 'figures' folder
#plt.savefig('figures/velocitydist.pdf',bbox_inches='tight')