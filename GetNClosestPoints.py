import math
from collections import namedtuple
import queue
point = namedtuple('Point', ['x', 'y'])

def GetDistance(a, b):
  return math.sqrt((a.x-b.x)**2 + (a.y-b.y)**2)

########### MAIN ###########

points = [point(1,2), point(3,-1), point(2,1), point(2,3)]
center = point(2,2)
closestsPoints = 2

distArr = queue.PriorityQueue()
for i in range(0,len(points)):
  distArr.put((GetDistance(points[i], center), points[i]))

while not distArr.empty():
    print(distArr.get())
