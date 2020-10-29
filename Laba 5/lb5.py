import csv
import os

print(os.getcwd())
os.chdir("d:/Student/ICS_18.09.2020/laba 4-5/lb5.py")

def isFileExisting(filename):
    return os.path.isfile(filename)

def outputFileByName(filename):
    print("File " + filename)
    fd = open(filename, "r")
    reader = csv.reader(fd, delimiter="\t")
    for row in reader:
        print(row)
    fd.close()

file1="group_one.py"
file2="group_two.py"           

def readFiles():
     
   
    fd1=open(file1,"r")
    reader = csv.reader(fd1, delimiter="\t")
    for row in reader:
        print(row)
    fd1.close()
    print("\ngroup1:")


    fd2=open(file2,"r")
    reader = csv.reader(fd2, delimiter="\t")
    for row in reader:
        print(row)
    fd2.close()
    print("\ngroup2:")

def writeToFiles():
    fd1=open(file1, "w")
    fd1.write("Stas, 79\nDima, 82\nAlica, 66")
    fd1.close()

    fd2=open(file2,"w")
    fd2.write("Karina, 82\nMaks, 52\nDanya, 47")
    fd2.close()
  


def addToFiles():
    fd1=open(file1,"a")
    fd1.write("\nVlad, 72\nBogdan, 63\nVova, 54")
    fd1.close

    fd2=open(file2,"a")
    fd2.write("\nStepan, 82\nIllya, 60\nGrisha 57")
    fd2.close

def serchFilesInDirectory(query):
    if(not isFileExisting(query)):
        print("File with name" + query + "does not exist")
    else:
        outputFileByName(query)

def searchTextInFiles(filename,query):

    fd = open(filename,"r")
    reader = fd.readlines()

    for row in reader:
        if query.lower() in row.lower():
            print(f"found:{row}")

    fd.close()

def sortMarksInFile(filename):
    dict = {}

    fd = open(filename,"r+")
    reader = fd.readlines()
    for row in reader:
        split_row_by_coma = row.split(",")
        dict[int(split_row_by_coma[1])] = split_row_by_coma[0]
    sorted_dict_by_items = sorted(dict.items())
    fd = open(filename,"r+")
    reader = fd.readline()
    for row in reader:
        split_row_by_coma = row.split(",")
        dict[int(split_row_by_coma[1])] = split_row_by_coma[0]
    sorted_dict_by_items = sorted(dict.items())
    print(sorted_dict_by_items)

    fd.close

#readFiles()
#writeToFiles()
#addToFiles()
#searchFilesInDirectory(file2)
#searchTextInFiles(file2, 'ous')
sortMarksInFile(file1)  

