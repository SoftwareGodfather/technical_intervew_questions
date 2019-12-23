import random
import math

def rand():
  return random.uniform(0,1)

def SwapPositions(arr, pos1, pos2):
  arr[pos1], arr[pos2] = arr[pos2], arr[pos1]

def RandomReorderList(arr):
  for i in reversed(range(1,len(arr))):
    randIndex = math.floor(i * rand())
    SwapPositions(arr, i, randIndex)

########### MAIN ###########

arr = [1,2,3,4,5,6,7,8,9]
print('Random reorder list in place')
print(f'Before {arr}')
RandomReorderList(arr)
print(f'After  {arr}')

########### STDOUT ###########

#Random reorder list in place
#Before [1, 2, 3, 4, 5, 6, 7, 8, 9]
#After  [9, 4, 1, 2, 7, 5, 3, 6, 8]
