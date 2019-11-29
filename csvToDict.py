import csv
import pandas as pd
import xlrd
import os

def csvToDict(fileName):
    dict = {}
    listX = []
    listY = []
    lx1=[]
    lx2=[]
    header_x = ""
    header_y = ""
    row = 0
    col = 0
    listDict = []
    
    read_file = pd.read_csv (fileName)
    path = fileName + "_conv.xlsx"
    read_file.to_excel (path, index = None, header=True)    
    loc = (path)
    wb = xlrd.open_workbook(loc) 
    sheet = wb.sheet_by_index(0) 
    row = sheet.nrows
    col = sheet.ncols
    os.remove(path)


    with open(fileName, 'r', encoding='UTF-8', newline='') as csvfile: 
        csvreader = csv.reader(csvfile)   
        
        i=0
        for row in csvreader: 
            i = i+1
            if(i>1 and col == 2):
                listX.append(float(row[0]))
                listY.append(float(row[1]))
            elif(i == 1):
                if(col == 2):
                    header_x = row[0]
                    header_y = row[1]
                elif(col == 3):
                    header_y = row[0]
                    header_x = row[1],row[2]
                else:
                    header_x = row[0]
                    
            elif(i>1 and col==3):
                listY.append(float(row[0]))
                lx1.append(float(row[1]))
                lx2.append(float(row[2]))
                    
                
            else:
                dict.update({i-1:float(row[0])})
                listY.append(float(row[0]))
        
    if(col == 3):
        listDict.append(listY)
        listDict.append(lx1)
        listDict.append(lx2)
    elif(col == 2):
        listDict.append(listY)
        listDict.append(listX)
    else:
        pass
    
    return listDict,header_x,header_y,col

#listDict,header_x,header_y,var = csvToDict("C:\\Users\\212546222\\Documents\\DA\\AnalyticsCal-Online\\Dataset\\DataSet3-ClassNotes5_7Sept2019_3Var.csv")
#print(listDict)




