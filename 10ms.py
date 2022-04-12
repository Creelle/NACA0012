import numpy as np

from matplotlib import pyplot as plt
plt.rcParams.update({'font.size': 22})
from data_processing import file_reading


rst,incidence,cla,cxa,cma,speed  = file_reading("C:/Users/robbe/Documents/NACA0012/11_04/","10ms.res")
rst_cor,incidence_cor,cla_cor,cxa_cor,cma_cor,speed_cor  = file_reading("C:/Users/robbe/Documents/NACA0012/11_04/","10mscor.res")

"""
Plotting
"""

#Fig 1 : cla vs incidence

fig,ax = plt.subplots()
ax.plot(incidence,cla,'-b')
ax.plot(incidence_cor,cla_cor,'-r',label = 'corrected')
ax.set_xlabel('$Incidence$')
ax.set_ylabel('$Cla$')
ax.grid(True)
ax.legend()

#Fig 2 : cxa vs incidence

fig,ax = plt.subplots()
ax.plot(incidence,cxa)
ax.plot(incidence_cor,cxa_cor,'-r',label = 'corrected')
ax.set_xlabel('$Incidence$')
ax.set_ylabel('$Cxa$')
ax.grid(True)
ax.legend()

#Fig 3 : cma vs incidence

fig,ax = plt.subplots()
ax.plot(incidence,cma)
ax.plot(incidence_cor,cma_cor,'-r',label = 'corrected')
ax.set_xlabel('$Incidence$')
ax.set_ylabel('$Cma$')
ax.grid(True)
#ax.legend()

#Fig 4 : cla vs cma polaire

fig,ax = plt.subplots()
ax.plot(cxa,cla)
ax.plot(cxa_cor,cla_cor,'-r',label = 'corrected')
ax.set_xlabel('$Cma$')
ax.set_ylabel('$Cla$')
ax.grid(True)
#ax.legend()

#Fig 5 : Vitesse vs incidence (sensé etre constante)

fig,ax = plt.subplots()
ax.plot(incidence,speed)
ax.plot(incidence_cor,speed_cor,'-r',label = 'corrected')
ax.set_xlabel('$Incidence$')
ax.set_ylabel('$Vitesse$')
ax.grid(True)
#ax.legend()

plt.show()

"""
Finesse max :
"""
print("finesse max : " , max(cla/cxa))
print("finesse max  corr", max(cla_cor/cxa_cor))
