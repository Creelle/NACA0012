import numpy as np
import re
from matplotlib import pyplot as plt


"""
File reading

In : "file_path" : local file path example "C:/Users/robbe/Documents/NACA0012/11_04/"
     "file_name" : nae of the file example 10ms.res
Out: rst : all the results
     incidence,cla,cxa,cma,speed :  the arrays that are of the most interest
"""

def file_reading(file_path,file_name):
    file_string = file_path+file_name
    with open(file_string,'r') as f:
        lines = f.readlines()
    f.close()

    titles = lines[3]
    titles = re.sub("\s+",",",titles.strip()).split(",")
    lines = lines[4:] #remove the above strings from the lines

    #remove the \t and replace by commas
    for i in range(len(lines)):
         lines[i]= re.sub("\s+",",",lines[i].strip()).split(",")

    #remove the lines that are incorrect
    line_length = len(lines[0])
    new_lines = []
    for i in range(len(lines)):
        if(len(lines[i])==line_length):
            new_lines.append(lines[i])
        else:
            continue

    #format the results
    rst = np.asarray(new_lines, dtype=float).T
    incidence = rst[titles.index("Incidence")]
    cla = rst[titles.index("Cza")]
    cxa = rst[titles.index("Cxa")]
    cma = rst[titles.index("Cma")]
    speed = rst[titles.index("Vitesse")]
    Za = rst[titles.index("Za")]
    Xa = rst[titles.index("Xa")]
    Ma = rst[titles.index("Ma")]

    return rst,incidence,cla,cxa,cma,speed,Za,Xa,Ma
#rst_cor,incidence_cor,cla_cor,cxa_cor,cma_cor,speed_cor  = file_reading("C:/Users/robbe/Documents/NACA0012/11_04/","10mscor.res")
def file_reading_sillage(file_path,file_name):
    file_string = file_path+file_name

    with open(file_string,'r') as f:
        lines = f.readlines()
    f.close()

    titles = lines[10]


    titles = re.sub("\s+",",",titles.strip()).split(",")

    lines = lines[12:] #remove the above strings from the lines

    #remove the \t and replace by commas
    for i in range(len(lines)):
         lines[i]= re.sub("\s+",",",lines[i].strip()).split(",")

    #remove the lines that are incorrect
    line_length = len(lines[0])
    new_lines = []
    for i in range(len(lines)):
        if(len(lines[i])==line_length):
            new_lines.append(lines[i])
        else:
            continue

    #format the results
    rst = np.asarray(new_lines, dtype=float).T
    speed = rst[2]

    return speed,np.mean(speed),np.std(speed)
