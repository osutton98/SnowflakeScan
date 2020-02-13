def fileReader():
    with open('snowflakeExample.txt','r') as file:
        data = file.read().replace(' ', '')# removes spaces
    stringToList(data)

def stringToList(filestream): #converts string of data into a list by charachter
    datalist=[]
    for i in filestream:
        datalist.append(i)
    stripComments(datalist)

def stripComments(inList): # removes multi and single line comments from list
    strippedList = []
    i = 0
    while True:
        if i == len(inList):
            break
        if inList[i] == "#" and not inList[i+1] == "!":
            while inList[i] != "\n":
                i += 1

            i += 1
            print()

        if inList[i] == "#" and i < len(inList) and inList[i+1] == "!":
            i += 1

            while not (inList[i] == '!' and i < len(inList) and inList[i+1] == "#"):
                i += 1

            i += 2
            continue
        else:
            strippedList.append(inList[i])

        i += 1

    print(strippedList)

    newLineRemover(strippedList)


def newLineRemover(rawList): #removes tab and new line charachters from list

    for i in range(len(rawList)):
        if i == len(rawList):
            break
        if i<len(rawList) and rawList[i]=="\n":
            rawList.remove(rawList[i])
        if i<len(rawList) and rawList[i]=="\t":
            rawList.remove(rawList[i])
    for i in range(len(rawList)):
        if i == len(rawList):
            break
        if i<len(rawList) and rawList[i]=="\t":
            rawList.remove(rawList[i])
        if i<len(rawList) and rawList[i]=="\n":
            rawList.remove(rawList[i])

    cleanList=rawList;
    print(cleanList)
    syntaxCheck(cleanList)

def syntaxCheck(filee): # Checks for Syntax error and returns their location in the program
    datastring= filee

    for i in range(len(datastring)-1):
        if datastring[i] not in "=;{}|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'":
            errors = i
            print("Error, Invalid Charachter "+ datastring[errors]+" "+ "At this location charachter location", errors)

    quoteCollect(datastring)

    return datastring

def quoteCollect(searchList): # creates indexes of quote strings
    iList=[]
    jList=[]
    startList=[]
    j=0
    for i in range(len(searchList)):
        if searchList[i]=="'":
            #print(i)
            iList.append(i)
    for i in range(0, len(iList), 2):
        startList.append(iList[i])
        #print(startList)
    for i in range(1, len(iList), 2):
        jList.append(iList[i])
    #print(jList)
    joinList(startList,jList,searchList)

def joinList(min , max, elementList): # Joins quote strings into simple list object
    finalList=elementList
    for i in range(len(min)):
        finalList[min[i]:max[i]]=[''.join(finalList[min[i]:max[i]])]
        #print(elementList)

    print(elementList)
    return elementList


fileReader()







