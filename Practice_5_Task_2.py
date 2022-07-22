# Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.
def CheckList(inputList):
    inputList.sort()
    resultList=[]
    resultList.append(inputList[0])
    resultList.append(inputList[-1])
    for i in range(len(inputList)-1):
        if (inputList[i+1]-inputList[i])>1:
            resultList.insert(1,inputList[i])
            resultList.pop()
            break
    return resultList

def StrToInt(inputList):
    outputList=[int(x) for x in inputList]   
    return outputList

my_list=(input("Enter your list. Use whitespace to separate elements: ").split())
my_list_original=my_list[:]
print(f"You entered the following sequence of numbers: {my_list_original}")
print(f"The maximum ascending sequence is {CheckList(StrToInt(my_list))}")
