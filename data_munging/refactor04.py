import math
def makeList(fromIndex, toIndex, content):
    valueList = []
    for i in range(fromIndex, toIndex):
        values = (content[i].split(' '))
        valueList.append([val for val in values if val != ''])
    return valueList
def weatherCondition(val1, val2):
    return (len(val1) == 2 and len(val2) == 2)
def footballCondition(val):
    return len(val) > 1


def findSmallest(smallest, valueList, searchIndex1, searchIndex2, ansIndex, typeData):
    for val in valueList:    
        for j in range(len(val)):
            if typeData == "weather":
                checkPass = weatherCondition(val[searchIndex1], val[searchIndex2])
            else:
                checkPass = footballCondition(val)
                
                
                
            if checkPass:
                diff = abs(int(val[searchIndex1])- int(val[searchIndex2]))
                if (diff < smallest):
                    ans =  val[ansIndex]
                    #print("Date = " + str(date))
                    smallest = diff                
    return ans