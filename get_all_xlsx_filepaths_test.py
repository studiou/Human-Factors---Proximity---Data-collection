__author__ = 'joel'
import os

path = '/Users/joel/Misc/JoelsStuff/OneDrive - GE Appliances/GEA Usability Team Documents/Exploratory Research/Proximity/Prox Python Code/testie'
depth =0
"""get all the files under a directory and its subdirectories"""

allxlsxfilepaths = []
if(os.path.isdir(path)):
    for item in os.listdir(path):
        #only grab the file paths that end in .xlsx
        if item[len(path)+1:len(path)+2] != "~":
            if item[-5:] == '.xlsx':
                allxlsxfilepaths.extend(path+os.sep+item,depth+1)
else:
    #only grab the file paths that end in .xlsx
   print "WTF"

print allxlsxfilepaths

