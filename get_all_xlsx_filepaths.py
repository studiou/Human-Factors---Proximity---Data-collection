__author__ = 'joel'
def builddirectorylist(path,depth =0):
    """get all the files under a directory and its subdirectories"""
    import os
    allxlsxfilepaths = []
    if(os.path.isdir(path)):
        for item in os.listdir(path):
            allxlsxfilepaths.extend(builddirectorylist(path+os.sep+item,depth+1))
            print allxlsxfilepaths
    else:
        allxlsxfilepaths.append(path)
    return allxlsxfilepaths