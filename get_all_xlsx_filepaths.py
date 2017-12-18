__author__ = 'joel'
def builddirectorylist(path,depth =0):
    """get all the files under a directory and its subdirectories"""
    import os
    allxlsxfilepaths = []
    if(os.path.isdir(path)):
        for item in os.listdir(path):
            #only grab the file paths that end in .xlsx
            if item[-5:] == '.xlsx':
                allxlsxfilepaths.extend(builddirectorylist(path+os.sep+item,depth+1))
    else:
        #only grab the file paths that end in .xlsx
        if path[-5:] == '.xlsx':
            allxlsxfilepaths.append(path)
    return allxlsxfilepaths