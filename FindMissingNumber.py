def FindMissingNumber(arr1, arr2):
    numberDict = dict()
    for elem in arr1:
        if(elem not in numberDict.keys()):
            numberDict[elem] = 1
        else:
            numberDict[elem] += 1

    for elem in arr2:
        if(elem not in numberDict.keys()):
            return elem
        else:
            numberDict[elem] -= 1
        
    for key, val in numberDict.items():
        if val>0:
            return key
    return 'None is missing'

########### MAIN ###########

arr1 = [4,12,9,5,6]
arr2 = [4,9,12,6]

mis = FindMissingNumber(arr1, arr2)
print(mis)

########### STDOUT ###########

#5
