__author__ = 'joel'
import os
import collections
import xlsxwriter
import openpyxl
import Read_xlsx_Scoresheet
import Solve_For_X
import get_all_xlsx_filepaths
import math

###############################################################################################
#########################Initial Global Variables###############################################
###############################################################################################
###############################################################################################


#Strings holds the filepath of the excel spreadsheets with the collected data
#imac file path
filepath = "/Volumes/JoelsStuff/JoelsStuff/OneDrive - GE Appliances/GEA Usability Team Documents/Exploratory Research/Proximity/Prox Python Code/Data"
#filepath2 = "/Volumes/JoelsStuff/JoelsStuff/OneDrive - GE Appliances/GEA Usability Team Documents/Exploratory Research/Proximity/Data collection/Proxmity score sheet/"

#search filepath directory for xlsx files. returns the complete file paths for xlsx files
allxlsxfilepaths = get_all_xlsx_filepaths.builddirectorylist(filepath)


#This all the data from the excel spreadsheet. ie. raw data
imported_xls_data = {}

#get data from excel spreadsheet and dump it into imported_xls_data array. Just pass the file path to the function and it returns an array with all data from the array
imported_xls_data = Read_xlsx_Scoresheet.importfromxls(allxlsxfilepaths)
#imported_xls_data[x][0] = gender of participant (i.e. male or female
gender = 0
#imported_xls_data[x][1] = age of participant (i.e.adult or child)
age = 1
#imported_xls_data[x][2] = event (i.e. hit or miss)
event = 2
#imported_xls_data[x][3] = the target (i.e. Dispense, dispensor Controls, Fridge door (dispensor side), Fridge door (no dispensor), Freezer Door)
target =3

#imported_xls_data[x][4] = foot distance of the 1st step onto the MAT with LEFT foot (in inches)
Y_1st_LEFT_step = 4
#imported_xls_data[x][5] = angle of the 1st step onto the MAT with LEFT foot (in degrees)
Angle_1st_LEFT_step = 5
#imported_xls_data[x][6] = timestamp of the 1st step onto the MAT with LEFT foot (in 00:00:000 hours, mins, milliseconds)
Timestamp_1st_LEFT_step = 6

#imported_xls_data[x][7] = foot distance of the 1st  step onto the MAT with RIGHT foot (in inches)
Y_1st_RIGHT_step = 7
#imported_xls_data[x][8] = angle of the 1st  step onto the MAT with RIGHT foot (in degrees)
Angle_1st_RIGHT_step = 8
#imported_xls_data[x][9] = timestamp of the 1st  step onto the MAT with RIGHT foot (in 00:00:000 hours, mins, milliseconds)
Timestamp_1st_RIGHT_step = 9

#imported_xls_data[x][10] = foot distance of the LEFT foot at fridge (if a hit) (in inches)
Y_at_fridge_LEFT_step = 10
#imported_xls_data[x][11] = angle of the LEFT foot at fridge (if a hit) (in degrees)
Angle_at_fridge_LEFT_step = 11
#imported_xls_data[x][12] = timestamp of the LEFT foot at fridge (if a hit) (in 00:00:000 hours, mins, milliseconds)
Timestamp_at_fridge_LEFT_step = 12

#imported_xls_data[x][13] = foot distance of the RIGHT foot at fridge (if a hit) (in inches)
#imported_xls_data[x][14] = angle of the RIGHT foot at fridge (if a hit) (in degrees)
#imported_xls_data[x][15] = timestamp of the RIGHT foot at fridge (if a hit) (in 00:00:000 hours, mins, milliseconds)

#imported_xls_data[x][16] = foot distance of the Last LEFT foot step before leaving mat (in inches)
#imported_xls_data[x][17] = angle of the Last LEFT foot step before leaving mat (in degrees)
#imported_xls_data[x][18] = timestamp of the Last LEFT foot step before leaving mat (in 00:00:000 hours, mins, milliseconds)

#imported_xls_data[x][19] = foot distance of the Last RIGHT foot step before leaving mat: (in inches)
#imported_xls_data[x][20] = angle of the Last RIGHT foot step before leaving mat: (in degrees)
#imported_xls_data[x][21] = timestamp of the Last RIGHT foot step before leaving mat: (in 00:00:000 hours, mins, milliseconds)



print imported_xls_data

#rint imported_xls_data
#print distance
#print speed