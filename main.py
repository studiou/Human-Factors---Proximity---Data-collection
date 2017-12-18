__author__ = 'joel'
import Functions
import os
import collections
import xlsxwriter
import openpyxl
import math

###############################################################################################
#########################Initial Variables#####################################################
###############################################################################################
###############################################################################################
#this variable holds the placement of my data files
#Macbook Pro
filepath = "/Users/joel/Misc/JoelsStuff/OneDrive - GE Appliances/GEA Usability Team Documents/Exploratory Research/Proximity/Data collection/Proxmity score sheet/Test1.xlsx"

#filepath = "/Users/joel/Misc/Joel's Stuff/OneDrive - GE Appliances/GEA Usability Team Documents/Exploratory Research/Proximity/Data collection/Proxmity score sheet/Test1.xlsx"

#big mac
#filepath = "/Volumes/JoelsStuff/JoelsStuff/OneDrive - GE Appliances/GEA Usability Team Documents/Exploratory Research/Proximity/Data collection/Proxmity score sheet/Test1.xlsx"


#This all the data from the excel spreadsheet
exportdata = {}



###############################################################################################
###############################################################################################
#################################Get data into a dictionary array#############################
###############################################################################################
###############################################################################################
from openpyxl import load_workbook
wb = load_workbook(filepath)
ws = wb['Data Sheet']

#a database of all the videos
index = []
#temporarly store data from spreadsheet
temp = []
flag2 = 1

for row in ws.iter_rows(row_offset=2):

    for cell in row:
        if cell.value == "Subject#.Video.Filename":#break loop if you are at the end of the list
            break
        if cell.value == "|":#break loop if you are at the end of the list

            break
        if cell.value <> None:#get rid of the empty cells
             flag = str(cell.value)#convert to string
             if flag[-1] <> ':':#test to see if it is a label, if so don't record
                 temp.append(cell.value)

    if cell.value == "Subject#.Video.Filename":#break loop if you are at the end of the list
            break

    if flag2 >= 6:
           exportdata[temp[0]]=temp[1:]
           index.append(temp[0])
           temp = []
           flag2 = 0
    flag2= flag2 + 1

###############################################################################################
###############################################################################################
###############################################################################################
###############################################################################################
###############################################################################################

###############################################################################################
###############################################################################################
#####################Move data to 2 distributions (hits and false alarms)######################
#########################convert angle to X coordinates########################################
###############################################################################################

#dictionary for the hits and false alarms distance
distance = {}

#dictionary for the hits and false alarms distance
speed = {}
linger = []

hit_sex_offset = 0

#break the data points extracted from the xlsx file into two arrays
for i in index:
    if exportdata[i][2] == 'Hit':
       #first grab the hits and convert the angle into x coordinates
        distance [i] = exportdata[i][0],exportdata[i][1],exportdata[i][2],exportdata[i][3],\
                       exportdata[i][4],(exportdata[i][4]* (math.cos(math.radians(exportdata[i][5])))),\
                       exportdata[i][7],(exportdata[i][7]* (math.cos(math.radians(exportdata[i][8])))),\
                       exportdata[i][10],(exportdata[i][10]* (math.cos(math.radians(exportdata[i][11])))),\
                       exportdata[i][13],(exportdata[i][13]* (math.cos(math.radians(exportdata[i][14])))),\
                       exportdata[i][16],(exportdata[i][16]* (math.cos(math.radians(exportdata[i][17])))),\
                       exportdata[i][19],(exportdata[i][19]* (math.cos(math.radians(exportdata[i][20]))))

                            # exportdata[i][4],(exportdata[i][4]* (math.cos(math.radians(exportdata[i][5])))),\ '''this converts first step of the left foot to x and y coordinates'''
                            # exportdata[i][6],(exportdata[i][6]* (math.cos(math.radians(exportdata[i][7])))),\ '''this converts first step of the right foot to x and y coordinates'''
                            # exportdata[i][8],(exportdata[i][8]* (math.cos(math.radians(exportdata[i][9])))),\ '''this converts last left step at the dispensor to x and y coordinates'''
                            # exportdata[i][10],(exportdata[i][10]* (math.cos(math.radians(exportdata[i][11])))),\ '''this converts last right at the dispensor to x and y coordinates'''
                            # exportdata[i][12],(exportdata[i][12]* (math.cos(math.radians(exportdata[i][13])))),\ '''this converts last left step at off the mat to x and y coordinates'''
                            # exportdata[i][14],(exportdata[i][14]* (math.cos(math.radians(exportdata[i][15]))))\ '''this converts last right step at off the mat to x and y coordinates'''


        #Next calculate speed for hits
        speed[i] =  exportdata[i][0],exportdata[i][1],exportdata[i][2],exportdata[i][3],\
                    abs(exportdata[i][4] - exportdata[i][7])/ abs(exportdata[i][6] - exportdata[i][9]),\
                    abs(exportdata[i][7] - exportdata[i][10])/ abs(exportdata[i][9] - exportdata[i][12]),\
                    abs(exportdata[i][10] - exportdata[i][13])/ abs(exportdata[i][12] - exportdata[i][15]),\
                    abs(exportdata[i][16] - exportdata[i][19])/ abs(exportdata[i][18] - exportdata[i][21])

    else:
        distance [i] =   exportdata[i][0],exportdata[i][1],exportdata[i][2],\
                         exportdata[i][4],(exportdata[i][4]* (math.cos(math.radians(exportdata[i][5])))),\
                         exportdata[i][7],(exportdata[i][7]* (math.cos(math.radians(exportdata[i][8])))),\
                         exportdata[i][16],(exportdata[i][16]* (math.cos(math.radians(exportdata[i][17])))),\
                         exportdata[i][19],(exportdata[i][19]* (math.cos(math.radians(exportdata[i][20]))))

                #Next calculate speed for hits
        speed[i] =  exportdata[i][0],exportdata[i][1],exportdata[i][2],\
                    abs(exportdata[i][4] - exportdata[i][7])/ abs(exportdata[i][6] - exportdata[i][9]),\
                    abs(exportdata[i][7] - exportdata[i][16])/ abs(exportdata[i][18] - exportdata[i][12]),\
                    abs(exportdata[i][16] - exportdata[i][19])/ abs(exportdata[i][18] - exportdata[i][21])

print exportdata
print distance
print speed