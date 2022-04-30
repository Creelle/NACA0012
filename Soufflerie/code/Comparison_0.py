import numpy as np
from matplotlib import pyplot as plt

from data_processing import file_reading

"""
Compare the fact that 1) we didn't take the good excel for 11/04 and 2) we added a flap
"""
"""
Modify here the file path and name
"""
document_path = "C:/Users/robbe/Documents/github/NACA0012/Soufflerie/20_04/"
document_path2 = "C:/Users/robbe/Documents/github/NACA0012/Soufflerie/13_04/"
document_path3 = "C:/Users/robbe/Documents/github/NACA0012/Soufflerie/13_04/Volets/"

file_name = "20ms_ref.res"
file_name2 = "20ms_corr_ancienne.res"
file_name3 = "20ms_Volet_0°_corr.res"

rst,incidence,cla,cxa,cma,speed,za,xa,ma  = file_reading(document_path,file_name)#data correct
rst2,incidence2,cla2,cxa2,cma2,speed2,za2,xa2,ma2  = file_reading(document_path2,file_name2)#data avec la mauvaise corde et envergure (allongement 6)
rst3,incidence3,cla3,cxa3,cma3,speed3,za3,xa3,ma3  = file_reading(document_path3,file_name3)#data avec un flap en plus

"""
Data
"""
lref = 0.159
lref6 = 0.107
S_ini = 0.0508
S_final =  6.4*10**-3 + 0.0508
Sref6 = 0.03424
l_volet = 0.02
b = 0.32

#Il y  a 2 remarques, la premiere est que le file 20mscor.res a été mesuré avec le mauvaise surface et longueur de corde ==> il faut ajuster la mesure prise
# deuxio : en mettant un volet, on allnge la corde et la surface ==> Il faut corriger par le rapport S_ini/S_fin
"""
Plotting
"""

#Fig 1 : cla vs incidence

cla = cla
cla2 = cla2*Sref6/S_ini
cla3 = cla3*S_ini/S_final

fig,ax = plt.subplots()
ax.plot(incidence,cla,'-b',label = "20 ms- ref")
ax.plot(incidence2,cla2,'-r',label = "20 ms- ancienne")
ax.plot(incidence3,cla3,'-g',label = "20 ms- avec volet 0°")
ax.set_xlabel('$Incidence$')
ax.set_ylabel('$Cla$')
ax.grid(True)
ax.legend()


#Fig 2 : cxa vs incidence
cxa = cxa
cxa2 = cxa2*Sref6/S_ini
cxa3 = cxa3*S_ini/S_final

fig,ax = plt.subplots()
ax.plot(incidence,cxa,'-b',label = "20 ms- ref")
ax.plot(incidence2,cxa2,'-r',label = "20 ms- ancienne")
ax.plot(incidence3,cxa3,'-g',label = "20 ms- avec volet 0°")
ax.set_xlabel('$Incidence$')
ax.set_ylabel('$Cxa$')
ax.grid(True)
ax.legend()

#Fig 3 : cma vs incidence
cma = cma
cma2 = cma2*Sref6*lref6/S_ini/(lref)
cma3 = cma3*S_ini*lref/S_final/(lref+l_volet)

fig,ax = plt.subplots()
ax.plot(incidence,cma,'-b',label = "20 ms- ref")
ax.plot(incidence2,cma2,'-r',label = "20 ms- ancienne")
ax.plot(incidence3,cma3,'-g',label = "20 ms- avec volet 0°")
ax.set_xlabel('$Incidence$')
ax.set_ylabel('$Cma$')
ax.grid(True)
ax.legend()

#Fig 4 : cla vs cma polaire

fig,ax = plt.subplots()
ax.plot(cla,cxa,'-b',label = "20 ms- ref")
ax.plot(cla2,cxa2,'-r',label = "20 ms- ancienne")
ax.plot(cla3,cxa3,'-g',label = "20 ms- avec volet 0°")
ax.set_xlabel('$Cla$')
ax.set_ylabel('$Cxa$')
ax.grid(True)
ax.legend()


fig,ax = plt.subplots()
ax.plot(incidence,speed,'-b',label = "20 ms- ref")
ax.plot(incidence2,speed2,'-r',label = "20 ms- ancienne")
ax.plot(incidence3,speed3,'-g',label = "20 ms- avec volet 0°")
ax.set_xlabel('$Incidence$')
ax.set_ylabel('$Vitesse$')
ax.grid(True)
ax.legend()



"""
Finesse max :
"""
print("finesse max 20 ms- ref : " , max(cla/cxa))
print("finesse max 20 ms- ancienne", max(cla2/cxa2))
print("finesse max 20 ms- avec volet 0° ", max(cla3/cxa3))

print("Allongement correct ref :",4*b**2/S_ini )
print("Allongement avec volet", 4*b**2/S_final)
plt.show()
#mike chlela
