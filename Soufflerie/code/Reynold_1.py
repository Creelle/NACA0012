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
document_path = "C:/Users/robbe/Documents/github/NACA0012/Soufflerie/11_04/"

file_name = "20mscor.res"
file_name2 = "15mscor.res"
file_name3 = "10mscor.res"

rst,incidence,cla,cxa,cma,speed,za,xa,ma  = file_reading(document_path,file_name)#data avec la mauvaise corde et envergure (allongement 6)
rst2,incidence2,cla2,cxa2,cma2,speed2,za2,xa2,ma2  = file_reading(document_path,file_name2)#data avec la mauvaise corde et envergure (allongement 6)
rst3,incidence3,cla3,cxa3,cma3,speed3,za3,xa3,ma3  = file_reading(document_path,file_name3)#data avec la mauvaise corde et envergure (allongement 6)
"""
Data
"""
lref = 0.159
lref6 = 0.107
S_ini = 0.0508
S_final =  6.4*10**-3 + 0.0508
Sref6 = 0.03424
l_volet = 0.02

#Il y  a 2 remarques, la premiere est que le file 20mscor.res a été mesuré avec le mauvaise surface et longueur de corde ==> il faut ajuster la mesure prise
# deuxio : en mettant un volet, on allnge la corde et la surface ==> Il faut corriger par le rapport S_ini/S_fin
"""
Plotting
"""

#Fig 1 : cla vs incidence

cla = cla*Sref6/S_ini
cla2 = cla2*Sref6/S_ini
cla3 = cla3*Sref6/S_ini

fig,ax = plt.subplots()
ax.plot(incidence,cla,'-b',label = "20 ms")
ax.plot(incidence2,cla2,'-r',label = "15 ms")
ax.plot(incidence3,cla3,'-g',label = "10 ms")
ax.set_xlabel('$Incidence$')
ax.set_ylabel('$Cla$')
ax.grid(True)
ax.legend()


#Fig 2 : cxa vs incidence
cxa = cxa*Sref6/S_ini
cxa2 = cxa2*Sref6/S_ini
cxa3 = cxa3*Sref6/S_ini

fig,ax = plt.subplots()
ax.plot(incidence,cxa,'-b',label = "20 ms")
ax.plot(incidence2,cxa2,'-r',label = "15 ms")
ax.plot(incidence3,cxa3,'-g',label = "10 ms")
ax.set_xlabel('$Incidence$')
ax.set_ylabel('$Cxa$')
ax.grid(True)
ax.legend()

#Fig 3 : cma vs incidence
cma = cma*Sref6*lref6/S_ini/(lref)
cma2 = cma2*Sref6*lref6/S_ini/(lref)
cma3 = cma3*Sref6*lref6/S_ini/(lref)

fig,ax = plt.subplots()
ax.plot(incidence,cma,'-b',label = "20 ms")
ax.plot(incidence2,cma2,'-r',label = "15 ms")
ax.plot(incidence3,cma3,'-g',label = "10 ms")
ax.set_xlabel('$Incidence$')
ax.set_ylabel('$Cma$')
ax.grid(True)
ax.legend()

#Fig 4 : cla vs cma polaire

fig,ax = plt.subplots()
ax.plot(cxa,cla,'-b',label = "20 ms")
ax.plot(cxa2,cla2,'-r',label = "15 ms")
ax.plot(cxa3,cla3,'-g',label = "10 ms")
ax.set_xlabel('$Cxa$')
ax.set_ylabel('$Cla$')
ax.grid(True)
ax.legend()




"""
Finesse max :
"""
print("finesse max 20 ms : " , max(cla/cxa))
print("finesse max 15 ms ", max(cla2/cxa2))
print("finesse max 10 ms ", max(cla3/cxa3))

plt.show()
