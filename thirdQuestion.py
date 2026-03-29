inputData = input("Input Data : ")
print(inputData)
print(type(inputData))
convertToArrayofString = inputData.split(" ")
print(convertToArrayofString)
# print(type(convertToArrayofString))

def countList (convertToArrayofString):
    result = []
    appendToArray = []

    for j in convertToArrayofString:
        appendToArray.append(int(j))
        print(f"ini j : {j}")
        print(type(j))
        print(f"Ini appendToArray : {appendToArray}")
        #print(type(appendToArray))
        result = appendToArray
        print(f"ini result : {result}")
        print(type(result))

    gradeComparator = result[0]
    count = 0
    max = 0
    min = 0
    for index in result:
        count = count + index

    for x in result:
        if x < gradeComparator or x == gradeComparator:
            min = x

    for i in result:
        if i > max:
            max = i
    
    print(f"Data : {result}\nTotal : {count}\nMax : {max}\nMin : {min}")
    return f"Data : {result}\nTotal : {count}\nMax : {max}\nMin : {min}"

countList(convertToArrayofString)

#READ.ME#
#Goals : 
#Implementation User Input
#Convert Data Type
#Implementation Function
#Implementation Local & Global Scope
#Implementation Looping & Conditional
#Implementation Operator Logic Comparison
