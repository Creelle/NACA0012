import numpy as np
from matplotlib import pyplot as plt
plt.rcParams.update({'font.size': 22})
from data_processing import file_reading

"""
Modify here the file path and name
"""
document_path = "C:/Users/robbe/Documents/github/NACA0012/11_04/"
file_name = "10ms.res"
file_name2 = "10mscor.res"

rst,incidence,cla,cxa,cma,speed,za,xa,ma  = file_reading(document_path,file_name2)
#rst_cor,incidence_cor,cla_cor,cxa_cor,cma_cor,speed_cor  = file_reading(document_path,file_name2)

"""
Plotting
"""
S_ref6  = 0.03424
l_ref6 = 0.107
T_ref = 295
#Fig 1 : cla vs incidence
cla_autre_moyen = -2*za/(101325/(295*287.1)*speed**2*0.03424)
fig,ax = plt.subplots()
ax.plot(incidence,cla,'-b')
ax.plot(incidence,cla_autre_moyen,'-r',label = "autre moyen")
#ax.plot(incidence_cor,cla_cor,'-r',label = 'corrected')
ax.set_xlabel('$Incidence$')
ax.set_ylabel('$Cla$')
ax.grid(True)
ax.legend()

#Fig 2 : cxa vs incidence
cxa_autre_moyen = -2*xa/(101325/(295*287.1)*speed**2*0.03424)
fig,ax = plt.subplots()
ax.plot(incidence,cxa)
ax.plot(incidence,cxa_autre_moyen,'-r',label = "autre moyen")
#ax.plot(incidence_cor,cxa_cor,'-r',label = 'corrected')
ax.set_xlabel('$Incidence$')
ax.set_ylabel('$Cxa$')
ax.grid(True)
ax.legend()

#Fig 3 : cma vs incidence
cma_autre_moyen = 2*ma/(101325/(295*287.1)*speed**2*0.03424*0.107)
fig,ax = plt.subplots()
ax.plot(incidence,cma)
ax.plot(incidence,cma_autre_moyen,'-r',label = "autre moyen")
#ax.plot(incidence_cor,cma_cor,'-r',label = 'corrected')
ax.set_xlabel('$Incidence$')
ax.set_ylabel('$Cma$')
ax.grid(True)
#ax.legend()

#Fig 4 : cla vs cma polaire

fig,ax = plt.subplots()
ax.plot(cxa,cla)
#ax.plot(cxa_cor,cla_cor,'-r',label = 'corrected')
ax.set_xlabel('$Cma$')
ax.set_ylabel('$Cla$')
ax.grid(True)
#ax.legend()

#Fig 5 : Vitesse vs incidence (sensé etre constante)

fig,ax = plt.subplots()
ax.plot(incidence,speed)
#ax.plot(incidence_cor,speed_cor,'-r',label = 'corrected')
ax.set_xlabel('$Incidence$')
ax.set_ylabel('$Vitesse$')
ax.grid(True)
#ax.legend()

plt.show()

"""
Finesse max :
"""
print("finesse max : " , max(cla/cxa))
#print("finesse max  corr", max(cla_cor/cxa_cor))
