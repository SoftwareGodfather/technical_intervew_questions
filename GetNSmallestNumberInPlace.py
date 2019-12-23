def swap(arr, pos1, pos2):
  arr[pos1], arr[pos2] = arr[pos2], arr[pos1]

def GetSmallestIndex(arr, arrSize):
  minIndex = 0
  for i in range(0, arrSize):
    if(arr[i] < arr[minIndex]):
      minIndex = i
  return minIndex

def GetNSmallestNumberInPlace(arr, n):
  smallestList = []
  for i in range(0, n):
    minIndex = GetSmallestIndex(arr, len(arr)-i)
    smallestList.append(arr[minIndex])
    swap(arr, minIndex, len(arr)-i-1)

  return smallestList

###########

def GetSmallestIndexUsingSet(arr, smallestIndexSet):
  minIndex = 0
  for i in range(0, len(arr)):
    if (arr[i] < arr[minIndex]) and (i not in smallestIndexSet):
      minIndex = i
  smallestIndexSet.add(minIndex)

def GetNSmallestNumberInPlaceNoArrModification(arr, n):
  smallestIndexSet = set()
  for i in range(0, n):
    GetSmallestIndexUsingSet(arr, smallestIndexSet)

  res = [arr[elem] for elem in smallestIndexSet]
  return res

########### MAIN ###########

arr = [9, 4, 1, 5, 7, 2, 3, 6, 8]
print(f'Before 1 algorithm: {arr}')
print( GetNSmallestNumberInPlace(arr, 2))
print(f'After 1 algorithm:  {arr} \n')

arr = [9, 4, 1, 5, 7, 2, 3, 6, 8]
print(f'Before 2 algorithm: {arr}')
print( GetNSmallestNumberInPlaceNoArrModification(arr, 2))
print(f'After 2 algorithm:  {arr}')

########### STDOUT ###########

#Before 1 algorithm: [9, 4, 1, 5, 7, 2, 3, 6, 8]
#[1, 2]
#After 1 algorithm:  [9, 4, 8, 5, 7, 6, 3, 2, 1]

#Before 2 algorithm: [9, 4, 1, 5, 7, 2, 3, 6, 8]
#[1, 2]
#After 2 algorithm:  [9, 4, 1, 5, 7, 2, 3, 6, 8]
