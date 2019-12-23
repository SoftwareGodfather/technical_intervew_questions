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
    
########### MAIN ###########

arr = [9, 4, 1, 5, 7, 2, 3, 6, 8]
print(f'Before algorithm: {arr}')
print( GetNSmallestNumberInPlace(arr, 2))
print(f'After algorithm:  {arr}')

########### STDOUT ###########

#Before algorithm: [9, 4, 1, 5, 7, 2, 3, 6, 8]
#[1, 2]
#After algorithm:  [9, 4, 8, 5, 7, 6, 3, 2, 1]
