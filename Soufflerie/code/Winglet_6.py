import numpy as np
from matplotlib import pyplot as plt
plt.rcParams.update({'font.size': 22})
from data_processing import file_reading

"""
Compare flap and no flap 0°
"""
"""
Modify here the file path and name
"""
document_path = "C:/Users/robbe/Documents/github/NACA0012/Soufflerie/13_04/Winglet/"


file_name = "13.5ms_Winglet_Decrochage_corr.res"
file_name2 = "13.5ms_ref.res"


rst,incidence,cla,cxa,cma,speed,za,xa,ma  = file_reading(document_path,file_name)
rst2,incidence2,cla2,cxa2,cma2,speed2,za2,xa2,ma2  = file_reading(document_path,file_name2)#data avec la mauvaise corde et envergure (allongement 6)
"""
Data
"""
#PAS besoin de correction

#Il y  a 2 remarques, la premiere est que le file 20mscor.res a été mesuré avec le mauvaise surface et longueur de corde ==> il faut ajuster la mesure prise
# deuxio : en mettant un volet, on allnge la corde et la surface ==> Il faut corriger par le rapport S_ini/S_fin
"""
Plotting
"""

#Fig 1 : cla vs incidence

cla = cla#*S_ini/S_final
cla2 = cla2#*S_ini/S_final
fig,ax = plt.subplots()
ax.plot(incidence,cla,'-b',label = "Winglet")
ax.plot(incidence2,cla2,'-r',label = "Sans winglet")

ax.set_xlabel('$Incidence$')
ax.set_ylabel('$Cla$')
ax.grid(True)
ax.legend()


#Fig 2 : cxa vs incidence
cxa = cxa#*S_ini/S_final
cxa2 = cxa2#*S_ini/S_final
fig,ax = plt.subplots()
ax.plot(incidence,cxa,label ="Winglet")
ax.plot(incidence2,cxa2,'-r',label = "Sans winglet")
ax.set_xlabel('$Incidence$')
ax.set_ylabel('$Cxa$')
ax.grid(True)
ax.legend()

#Fig 3 : cma vs incidence
cma = cma#*S_ini*lref/S_final/(lref+l_volet)
cma2 = cma2#*S_ini*lref/S_final/(lref+l_volet)
fig,ax = plt.subplots()
ax.plot(incidence,cma,label ="Winglet")
ax.plot(incidence2,cma2,'-r',label = "Sans winglet")
ax.set_xlabel('$Incidence$')
ax.set_ylabel('$Cma$')
ax.grid(True)
ax.legend()

#Fig 4 : cla vs cma polaire

fig,ax = plt.subplots()
ax.plot(cxa,cla,label ="Winglet")
ax.plot(cxa2,cla2,'-r',label = "Sans winglet")
ax.set_xlabel('$Cxa$')
ax.set_ylabel('$Cla$')
ax.grid(True)
ax.legend()

#Fig 5 : Vitesse vs incidence (sensé etre constante)

fig,ax = plt.subplots()
ax.plot(incidence,speed,label ="Winglet")
ax.plot(incidence2,speed2,'-r',label = "Sans winglet")
ax.set_xlabel('$Incidence$')
ax.set_ylabel('$Vitesse$')
ax.grid(True)
ax.legend()



"""
Finesse max :
"""
print("finesse max avec Winglet : " , max(cla/cxa))
print("finesse max sans winglet ", max(cla2/cxa2))

plt.show()
