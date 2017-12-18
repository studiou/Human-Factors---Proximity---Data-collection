__author__ = 'joel'
def importfromxls(filepath):
    """get all the files under a directory and its subdirectories"""
    import os
    import openpyxl
    imported_xls_data = {}

    ###############################################################################################
    ###############################################################################################
    #################################Get data into a dictionary array#############################
    ###############################################################################################
    ###############################################################################################
    from openpyxl import load_workbook
    workbook = load_workbook(filepath)
    ws = workbook['Data Sheet']

    #a database of all the videos
    index = []
    #temporarly store data from spreadsheet
    temp = []
    flag2 = 1

    for row in ws.iter_rows(row_offset=2):

        for cell in row:
            if cell.value == "Subject#.Video.Filename":#break loop once you hit the end of data entry within the spreadsheet.
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
               imported_xls_data[temp[0]]=temp[1:]
               index.append(temp[0])
               temp = []
               flag2 = 0
        flag2= flag2 + 1

    ###############################################################################################
    ###############################################################################################
    ###############################################################################################
    ###############################################################################################
    ###############################################################################################
    return imported_xls_data