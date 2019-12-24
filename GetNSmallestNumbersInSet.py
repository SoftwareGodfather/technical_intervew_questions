import heapq

def GetSmallestIndexUsingSet(myNumberSet, smallestSet):
  smallestValue = max(myNumberSet)
  for elem in myNumberSet:
    if(elem < smallestValue) and (elem not in smallestSet):
      smallestValue = elem
  smallestSet.add(smallestValue)

def NSmallestInSet(myNumberSet, nIndex): #O(nk)
  smallestSet = set()
  for i in range(nIndex):
    GetSmallestIndexUsingSet(myNumberSet, smallestSet)
  
  return max(smallestSet)

###########

def NSmallestInSetWithHeap(myNumberSet, smallestSet):
  myHeap = []
  for elem in myNumberSet:
    if(len(myHeap) < smallestSet):
      heapq.heappush(myHeap, elem*-1)
    elif(elem < myHeap[0]):
      heapq.heappushpop(myHeap, elem*-1)
  
  return heapq.heappop(myHeap)*-1

########### MAIN ###########

myNumberSet = {9, 4, 1, 5, 7, 2, 3, 6, 8}
print(NSmallestInSet(myNumberSet, 3))
print(NSmallestInSetWithHeap(myNumberSet, 3))

########### STDOUT ###########

#3
#3
