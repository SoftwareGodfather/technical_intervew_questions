import math
from collections import namedtuple
import heapq
point = namedtuple('Point', ['x', 'y'])

def GetDistance(a, b):
  return math.sqrt((a.x-b.x)**2 + (a.y-b.y)**2)

########### MAIN ###########

points = [point(1,2), point(3,-1), point(2,1), point(2,5)]
center = point(2,2)
closestsPoints = 2

#Heap - Using negative dist weights for Max Heap property
distArr = []
for i in range(0,len(points)): #O(nlogk)
  currentDist = GetDistance(points[i], center) * -1
  if(len(distArr) < closestsPoints):
    heapq.heappush(distArr, (currentDist, points[i])) #O(1)
  elif(currentDist > distArr[0][0]):
    heapq.heappushpop(distArr, (currentDist, points[i])) #O(logk)

#O(klogk)
while(len(distArr)):
  print(heapq.heappop(distArr)[1])

########### STDOUT ###########

#Point(x=1, y=2)
#Point(x=2, y=1)
