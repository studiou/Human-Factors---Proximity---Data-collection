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
#filepath = "/Volumes/JoelsStuff/JoelsStuff/OneDrive - GE Appliances/GEA Usability Team Documents/Exploratory Research/Proximity/Prox Python Code/Data"
filepath = "/Users/joel/Misc/JoelsStuff/OneDrive - GE Appliances/GEA Usability Team Documents/Exploratory Research/Proximity/Prox Python Code/"

#search filepath directory for xlsx files. returns the complete file paths for xlsx files
allxlsxfilepaths = get_all_xlsx_filepaths.builddirectorylist(filepath)


#This all the data from the excel spreadsheet. ie. raw data
imported_xls_data = {}

#get data from excel spreadsheet and dump it into imported_xls_data array. Just pass the file path to the function and it returns an array with all data from the array
imported_xls_data = Read_xlsx_Scoresheet.importfromxls(allxlsxfilepaths)

print imported_xls_data

