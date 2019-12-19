def FindMissingUsingDict(arr1, arr2):
  myDict = dict()

  for elem in arr1:
    if elem not in myDict.keys():
      myDict[elem] = 1
    else:
      myDict[elem] += 1
  
  for elem in arr2:
    if elem not in myDict.keys():
      myDict[elem] = 1
    else:
      myDict[elem] -= 1
  
  for k,v in myDict.items():
    if(v!=0):
      numOfMissings = abs(v)
      for _ in range(numOfMissings):
        print(f'Missing Number {k}')

########### MAIN ###########

arr1 = [3,6,2,1,6,9, 100, 100]
arr2 = [3,6,2,1,6,9, 102, 6, 6]
print('FindMissing')
print(f'arr1 {arr1}')
print(f'arr2 {arr2}\n')

FindMissingUsingDict(arr1, arr2)

########### STDOUT ###########

#FindMissing
#arr1 [3, 6, 2, 1, 6, 9, 100, 100]
#arr2 [3, 6, 2, 1, 6, 9, 102, 6, 6]

#Missing Number 6
#Missing Number 6
#Missing Number 100
#Missing Number 100
#Missing Number 102
