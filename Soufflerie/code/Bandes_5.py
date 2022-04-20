import numpy as np
from matplotlib import pyplot as plt
plt.rcParams.update({'font.size': 22})
from data_processing import file_reading

"""
Compare the number of bandes on the extrados of the airfoil
"""
"""
Modify here the file path and name
"""
document_path = "C:/Users/robbe/Documents/github/NACA0012/Soufflerie/13_04/Bandes/"
document_path2 = "C:/Users/robbe/Documents/github/NACA0012/Soufflerie/20_04/"

file_name = "20ms_ref.res"
file_name2 = "20ms_2Bandes_corr.res"
file_name3 = "20ms_3Bandes_sep-corr.res"
file_name4 = "20ms_4Bandes_corr.res"

rst,incidence,cla,cxa,cma,speed,za,xa,ma  = file_reading(document_path2,file_name)
rst2,incidence2,cla2,cxa2,cma2,speed2,za2,xa2,ma2  = file_reading(document_path,file_name2)
rst3,incidence3,cla3,cxa3,cma3,speed3,za3,xa3,ma3  = file_reading(document_path,file_name3)
rst4,incidence4,cla4,cxa4,cma4,speed4,za4,xa4,ma4  = file_reading(document_path,file_name4)

"""
Data
"""


#Il y  a 2 remarques, la premiere est que le file 20mscor.res a été mesuré avec le mauvaise surface et longueur de corde ==> il faut ajuster la mesure prise
# deuxio : en mettant un volet, on allnge la corde et la surface ==> Il faut corriger par le rapport S_ini/S_fin
"""
Plotting
"""

#Fig 1 : cla vs incidence
#No need for correction since there is no flap and it was the correct file
fig,ax = plt.subplots()
ax.plot(incidence,cla,'-b',label = "0 Bandes")
ax.plot(incidence2,cla2,'-r',label = "2 Bandes")
ax.plot(incidence3,cla3,'-g',label = "3 Bandes")
ax.plot(incidence4,cla4,'-k',label = "4 Bandes")
ax.set_xlabel('$Incidence$')
ax.set_ylabel('$Cla$')
ax.grid(True)
ax.legend()


#Fig 2 : cxa vs incidence

fig,ax = plt.subplots()
ax.plot(incidence,cxa,'-b',label = "0 Bandes")
ax.plot(incidence2,cxa2,'-r',label = "2 Bandes")
ax.plot(incidence3,cxa3,'-g',label = "3 Bandes")
ax.plot(incidence4,cxa4,'-k',label = "4 Bandes")
ax.set_xlabel('$Incidence$')
ax.set_ylabel('$Cxa$')
ax.grid(True)
ax.legend()

#Fig 3 : cma vs incidence
cma = cma#*S_ini*lref/S_final/(lref+l_volet)
cma2 = cma2#*S_ini*lref/S_final/(lref+l_volet)
fig,ax = plt.subplots()
ax.plot(incidence,cma,'-b',label = "0 Bandes")
ax.plot(incidence2,cma2,'-r',label = "2 Bandes")
ax.plot(incidence3,cma3,'-g',label = "3 Bandes")
ax.plot(incidence4,cma4,'-k',label = "4 Bandes")
ax.set_xlabel('$Incidence$')
ax.set_ylabel('$Cma$')
ax.grid(True)
ax.legend()

#Fig 4 : cla vs cma polaire

fig,ax = plt.subplots()
ax.plot(cla,cxa,'-b',label = "0 Bandes")
ax.plot(cla2,cxa2,'-r',label = "2 Bandes")
ax.plot(cla3,cxa3,'-g',label = "3 Bandes")
ax.plot(cla4,cxa4,'-k',label = "4 Bandes")
ax.set_xlabel('$Cma$')
ax.set_ylabel('$Cla$')
ax.grid(True)
ax.legend()

#Fig 5 : incidence vs speed (sensé etre constante)

fig,ax = plt.subplots()
ax.plot(incidence,speed,'-b',label = "0 Bandes")
ax.plot(incidence2,speed2,'-r',label = "2 Bandes")
ax.plot(incidence3,speed3,'-g',label = "3 Bandes")
ax.plot(incidence4,speed4,'-k',label = "4 Bandes")
ax.set_xlabel('$Incidence$')
ax.set_ylabel('$Vitesse$')
ax.grid(True)
#ax.legend()



"""
Finesse max :
"""
print("finesse max avec 0 bandes : " , max(cla/cxa))
print("finesse max avec 2 bandes : " , max(cla2/cxa2))
print("finesse max avec 3 bandes : " , max(cla3/cxa3))
print("finesse max avec 4 bandes : " , max(cla4/cxa4))


plt.show()
