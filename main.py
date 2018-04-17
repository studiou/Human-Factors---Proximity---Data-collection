__author__ = 'joel'
import os
import collections
import xlsxwriter
import openpyxl
import Read_xlsx_Scoresheet
import Solve_For_X
import get_all_xlsx_filepaths
import math
import Processed_Data_Class
from SpeedAndDistanceCal import *
import csv
from Processed_Data_Class import *

###############################################################################################
#########################Initial Global Variables###############################################
###############################################################################################
###############################################################################################


#Strings holds the filepath of the excel spreadsheets with the collected data
#IDO imac file path
filepath = "/Volumes/JoelsStuff/JoelsStuff/OneDrive - GE Appliances/GEA Usability Team Documents/Exploratory Research/Proximity/Prox Python Code/testie"
#U imac file path
#filepath = "/Users/joel/Misc/Joel's Stuff/OneDrive - GE Appliances/GEA Usability Team Documents/Exploratory Research/Proximity/Data collection/Score sheets from videos/Test"
#filepath = '/Users/joel/Misc/JoelsStuff/OneDrive - GE Appliances/GEA Usability Team Documents/Exploratory Research/Proximity/Prox Python Code/testie'
output = filepath + "/output.csv"

#search filepath directory for xlsx files. returns the complete file paths for xlsx files
allxlsxfilepaths = get_all_xlsx_filepaths.builddirectorylist(filepath)


#This all the data from the excel spreadsheet. ie. raw data
imported_xls_data = {}

#get data from excel spreadsheet and dump it into imported_xls_dta array. Just pass the file path to the function and it returns an array with all data from the array
imported_xls_data = Read_xlsx_Scoresheet.importfromxls(allxlsxfilepaths)

print imported_xls_data

processedlist = []

for key, value in imported_xls_data.iteritems():
    processedlist.append(P_Data(key,value))

#print "\n processed data \n"
#print "Participant number + Video Name,Sex,Age,Event,Target,Time Stamp, Near point radius, Near point angle, Far point radius, Far point angle, Time Stamp, Near point radius, Near point angle, Far point radius, Far point angle \n"

for item in processedlist:
    print item.pnum_video + ", " + item.sex + ", " + item.age  + ", " + item.event  + ", " + item.target  + ", " + str(item.PersonProfile1.time_seconds) + ", " + str(item.PersonProfile1.pointNear.radius) + ", " + str(item.PersonProfile1.pointNear.angle) + ", " + str(item.PersonProfile1.pointFar.radius ) + ", " + str(item.PersonProfile1.pointFar.angle ) + ", " + str(item.PersonProfile2.time_seconds) + ", " + str(item.PersonProfile2.pointNear.radius ) + ", " + str(item.PersonProfile2.pointNear.angle) + ", " + str(item.PersonProfile2.pointFar.radius) + ", " + str(item.PersonProfile2.pointFar.angle)


###Create CSV
filehandler = open(output,'w')
#Print header
print >> filehandler,  "Participant number + Video Name,Sex,Age,Event,Target,Speed,Closest to Dispenser (radius),Time Stamp, Enter Mat Near Point Radius, Enter Mat Near Point Angle, Enter mat far point radius, Enter Mat Far Point Angle, Time Stamp, Final Step Near Point Radius, Final Step Near Point Angle, Final Step Far Point Radius, Final Step Far Point Angle"
#Print Data
for item in processedlist:
    if item.event == "False alarm":
        printline =  item.pnum_video + ", " + item.sex + ", " + item.age  + ", " + item.event  + ", " + "N/A"  + ", " +  str(item.speed)  + ", " +  str(item.nearestDistancePolarPoint.radius) + ", " + str(item.PersonProfile1.time_seconds) + ", " + str(item.PersonProfile1.pointNear.radius) + ", " + str(item.PersonProfile1.pointNear.angle) + ", " + str(item.PersonProfile1.pointFar.radius ) + ", " + str(item.PersonProfile1.pointFar.angle ) + ", " + str(item.PersonProfile2.time_seconds) + ", " + str(item.PersonProfile2.pointNear.radius ) + ", " + str(item.PersonProfile2.pointNear.angle) + ", " + str(item.PersonProfile2.pointFar.radius) + ", " + str(item.PersonProfile2.pointFar.angle)

    else:
        printline = item.pnum_video + ", " + item.sex + ", " + item.age  + ", " + item.event  + ", " + item.target  + ", " + str(item.speed) + ", " +  str(item.nearestDistancePolarPoint.radius) + ", " + str(item.PersonProfile1.time_seconds) + ", " + str(item.PersonProfile1.pointNear.radius) + ", " + str(item.PersonProfile1.pointNear.angle) + ", " + str(item.PersonProfile1.pointFar.radius ) + ", " + str(item.PersonProfile1.pointFar.angle ) + ", " + str(item.PersonProfile2.time_seconds) + ", " + str(item.PersonProfile2.pointNear.radius ) + ", " + str(item.PersonProfile2.pointNear.angle) + ", " + str(item.PersonProfile2.pointFar.radius) + ", " + str(item.PersonProfile2.pointFar.angle)

    print >>filehandler,printline
filehandler.close()
#finished inputting data so close the file and write it to a txt doc
