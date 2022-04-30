import numpy as np
from matplotlib import pyplot as plt
plt.rcParams.update({'font.size': 22})
from data_processing import file_reading_sillage

document_path = "C:/Users/robbe/Documents/github/NACA0012/Soufflerie/20_04/"
file_name_x15 = "sillage_1.5cm.txt"

file_name_x10 = "sillage_1cm.txt"
file_name_x10_y10 = "sillage_1cmy=1cm.txt"
file_name_x10_y20 = "sillage_1cmy=2cm.txt"
file_name_x10_ym10 = "sillage_1cmy=-1cm.txt"
file_name_x10_ym20 ="sillage_1cmy=-2cm.txt"



speed0,std0= file_reading_sillage(document_path,file_name_x10)[1:]
speed1,std1=file_reading_sillage(document_path,file_name_x10_y10)[1:]
speed2,std2=file_reading_sillage(document_path,file_name_x10_y20)[1:]
speedm1,stdm1=file_reading_sillage(document_path,file_name_x10_ym10)[1:]
speedm2,stdm2=file_reading_sillage(document_path,file_name_x10_ym20)[1:]

file_name_x20 = "sillage_2cm.txt"
file_name_x20_y10 = "sillage_2cmy=1.txt"
file_name_x20_y20 = "sillage_2cmy=2.txt"
file_name_x20_ym10 = "sillage_2cmy=-1.txt"
file_name_x20_ym20 ="sillage_2cmy=-2.txt"

speed02,std02= file_reading_sillage(document_path,file_name_x20)[1:]
speed12,std12=file_reading_sillage(document_path,file_name_x20_y10)[1:]
speed22,std22=file_reading_sillage(document_path,file_name_x20_y20)[1:]
speedm12,stdm12=file_reading_sillage(document_path,file_name_x20_ym10)[1:]
speedm22,stdm22=file_reading_sillage(document_path,file_name_x20_ym20)[1:]

file_name_x30 = "sillage_3cm.txt"
file_name_x30_y10 = "sillage_3cmy=1cm.txt"
file_name_x30_y20 = "sillage_3cmy=2cm.txt"
file_name_x30_ym10 = "sillage_3cmy=-1cm.txt"
file_name_x30_ym20 ="sillage_3cmy=-2cm.txt"

speed03,std03= file_reading_sillage(document_path,file_name_x30)[1:]
speed13,std13=file_reading_sillage(document_path,file_name_x30_y10)[1:]
speed23,std23=file_reading_sillage(document_path,file_name_x30_y20)[1:]
speedm13,stdm13=file_reading_sillage(document_path,file_name_x30_ym10)[1:]
speedm23,stdm23=file_reading_sillage(document_path,file_name_x30_ym20)[1:]

file_name_x15 = "sillage_1.5cm.txt"
speed15,std15= file_reading_sillage(document_path,file_name_x15)[1:]
file_name_x25 = "sillage_2.5cm.txt"
speed25,std25= file_reading_sillage(document_path,file_name_x25)[1:]
file_name_x40 = "sillage_4cm.txt"
speed40,std40= file_reading_sillage(document_path,file_name_x40)[1:]
file_name_x50 = "sillage_5cm.txt"
speed50,std50= file_reading_sillage(document_path,file_name_x50)[1:]
file_name_x60 = "sillage_6cm.txt"
speed60,std60= file_reading_sillage(document_path,file_name_x60)[1:]
file_name_x70 = "sillage_7cm.txt"
speed70,std70= file_reading_sillage(document_path,file_name_x70)[1:]

y = np.linspace(-2,2,5)
x= np.array([speedm2,speedm1,speed0,speed1,speed2])

x2= np.array([speedm22,speedm12,speed02,speed12,speed22])
x3= np.array([speedm23,speedm13,speed03,speed13,speed23])

error_x = np.array([stdm2,stdm1,std0,std1,std2])
error_x2 = np.array([stdm22,stdm12,std02,std12,std22])
error_x3 = np.array([stdm23,stdm13,std03,std13,std23])


fig,ax = plt.subplots()
ax.errorbar(x,y,xerr = error_x,fmt='-b',capsize=3,label = "$x = 1 cm$")
ax.errorbar(x2,y,xerr = error_x2,fmt='-r',capsize=3,label = "$x = 2 cm$")
ax.errorbar(x3,y,xerr = error_x3,fmt='-g',capsize=3,label = "$x = 3 cm$")
# ax.plot(speed15,0,'o',label= "$x = 1.5 cm$")
# ax.plot(speed25,0,'o',label= "$x = 2.5 cm$")
# ax.plot(speed40,0,'o',label= "$x = 4 cm$")
# ax.plot(speed50,0,'o',label= "$x = 5 cm$")
# ax.plot(speed60,0,'o',label= "$x = 6 cm$")
# ax.plot(speed70,0,'o',label= "$x = 7 cm$")
ax.set_xlabel('$speed$ $[m/s]$')
ax.set_ylabel('y $[cm]$')
ax.grid(True)
ax.legend()

plt.show()
