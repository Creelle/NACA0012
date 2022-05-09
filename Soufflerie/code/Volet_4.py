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
document_path = "C:/Users/robbe/Documents/github/NACA0012/Soufflerie/13_04/Volets/"
document_path2 = "C:/Users/robbe/Documents/github/NACA0012/Soufflerie/20_04/"
file_name = "20ms_Volet_0°_corr.res"
file_name2 = "20ms_Volet_17°_corr.res"
file_name3 = "20ms_ref.res"

rst,incidence,cla,cxa,cma,speed,za,xa,ma  = file_reading(document_path,file_name)
rst2,incidence2,cla2,cxa2,cma2,speed2,za2,xa2,ma2  = file_reading(document_path,file_name2)#data avec la mauvaise corde et envergure (allongement 6)
rst3,incidence3,cla3,cxa3,cma3,speed3,za3,xa3,ma3  = file_reading(document_path2,file_name3)#data avec la mauvaise corde et envergure (allongement 6)

"""
Data
"""
lref = 0.159
S_ini = 0.0508
S_final =  6.4*10**-3 + 0.0508
l_volet = 0.02

#Il y  a 2 remarques, la premiere est que le file 20mscor.res a été mesuré avec le mauvaise surface et longueur de corde ==> il faut ajuster la mesure prise
# deuxio : en mettant un volet, on allnge la corde et la surface ==> Il faut corriger par le rapport S_ini/S_fin
"""
Plotting
"""

#Fig 1 : cla vs incidence

cla = cla*S_ini/S_final
cla2 = cla2*S_ini/S_final
cla3=cla3
fig,ax = plt.subplots()
ax.plot(incidence3,cla3,'-b',label = "Pas de volet")
ax.plot(incidence,cla,'-r',label = "Volet 0°")
ax.plot(incidence2,cla2,'-g',label = "Volet 17°")

ax.set_xlabel('$Incidence$')
ax.set_ylabel('$Cla$')
ax.grid(True)
ax.legend()


#Fig 2 : cxa vs incidence
cxa = cxa*S_ini/S_final
cxa2 = cxa2*S_ini/S_final
fig,ax = plt.subplots()
ax.plot(incidence,cxa,label = "Volet 0°")
ax.plot(incidence2,cxa2,'-r',label = "Volet 17°")
ax.plot(incidence3,cxa3,'-g',label = "Pas de volet")
ax.set_xlabel('$Incidence$')
ax.set_ylabel('$Cxa$')
ax.grid(True)
ax.legend()

#Fig 3 : cma vs incidence
cma = cma*S_ini*lref/S_final/(lref+l_volet)
cma2 = cma2*S_ini*lref/S_final/(lref+l_volet)
fig,ax = plt.subplots()
ax.plot(incidence,cma,label = "Volet 0°")
ax.plot(incidence2,cma2,'-r',label = "Volet 17°")
ax.plot(incidence3,cma3,'-g',label = "Pas de volet")
ax.set_xlabel('$Incidence$')
ax.set_ylabel('$Cma$')
ax.grid(True)
ax.legend()

#Fig 4 : cla vs cma polaire

fig,ax = plt.subplots()
ax.plot(cxa,cla,label = "Volet 0°")
ax.plot(cxa2,cla2,'-r',label = "Volet 17°")
ax.plot(cxa3,cla3,'-g',label = "Pas de volet")
ax.set_xlabel('$Cxa$')
ax.set_ylabel('$Cla$')
ax.grid(True)
ax.legend()

#Fig 5 : Vitesse vs incidence (sensé etre constante)

fig,ax = plt.subplots()
ax.plot(incidence,speed,label = "Volet 0°")
ax.plot(incidence2,speed2,'-r',label = "Volet 17°")
ax.plot(incidence3,speed3,'-g',label = "Pas de volet")
ax.set_xlabel('$Incidence$')
ax.set_ylabel('$Vitesse$')
ax.grid(True)
#ax.legend()



"""
Finesse max :
"""
print("finesse max avec volet 0° : " , max(cla/cxa))
print("finesse max avec volet 17° ", max(cla2/cxa2))
print("finesse max sans volet ", max(cla3/cxa3))

plt.show()
