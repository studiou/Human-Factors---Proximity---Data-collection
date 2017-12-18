__author__ = 'joel'
import os
import collections
import xlsxwriter
import openpyxl
import Read_xlsx_Scoresheet
import get_all_xlsx_filepaths
import math

###############################################################################################
#########################Initial Variables#####################################################
###############################################################################################
###############################################################################################


#Strings holds the filepath of the excel spreadsheet with the data
#Macbook Pro
#filepath = "/Users/joel/Misc/JoelsStuff/OneDrive - GE Appliances/GEA Usability Team Documents/Exploratory Research/Proximity/Data collection/Proxmity score sheet/Test1.xlsx"

#filepath = "/Users/joel/Misc/Joel's Stuff/OneDrive - GE Appliances/GEA Usability Team Documents/Exploratory Research/Proximity/Data collection/Proxmity score sheet/Test1.xlsx"

#imac
filepath = "/Volumes/JoelsStuff/JoelsStuff/OneDrive - GE Appliances/GEA Usability Team Documents/Exploratory Research/Proximity/Data collection/Proxmity score sheet/Test1.xlsx"

filepath2 = "/Volumes/JoelsStuff/JoelsStuff/OneDrive - GE Appliances/GEA Usability Team Documents/Exploratory Research/Proximity/Data collection/Proxmity score sheet/"

#search file path directory and obtain all file paths for xlsx files
allxlsxfilepaths = get_all_xlsx_filepaths.builddirectorylist(filepath2)
print allxlsxfilepaths

#This all the data from the excel spreadsheet. ie. raw data
imported_xls_data = {}

#get data from excel spreadsheet and dump it into imported_xls_data array. Just pass the file path to the function and it returns an array with all data from the array
imported_xls_data = Read_xlsx_Scoresheet.importfromxls(filepath)



#rint imported_xls_data
#print distance
#print speed