def MapLocations(myStr):
    loc = dict()
    for ind, elem in enumerate(myStr):
        if elem not in loc.keys():
            loc[elem] = [ind]
        else:
            loc[elem].append(ind)
    return loc
        
def FindCharInStringUsingMap(myChar, mapLocations, pos):
    if(myChar not in mapLocations.keys()):
        return -1
    locList = mapLocations[myChar]
    for singleLocation in locList:
        if singleLocation >= pos:
            return singleLocation
    return -1
    
def GetLongestString(myStr):
    maxStr = ''
    for elem in myStr:
        if(len(elem) > len(maxStr)):
            maxStr =  elem
    return maxStr

def FindSubstringFromPosition(strA, strB, pointA, pointB, mapLocB):
    result = strA[pointA]
    i = pointA + 1
    j = pointB + 1
    while(j < len(strB)) and (i < len(strA)):
        currentlyLookingFor = strA[i]
        #foundInStrB = strB[j:].find(currentlyLookingFor)
        foundInStrB = FindCharInStringUsingMap(currentlyLookingFor, mapLocB, j)
        if(foundInStrB != -1):
            result += currentlyLookingFor
            j = foundInStrB + 1
        i += 1
    return result

def LongestSubSequence(strA, strB, mapLocB):
    allResults = []
    for pointA, charA in enumerate(strA):
        #pointB = strB.find(charA)
        pointB = FindCharInStringUsingMap(charA, mapLocB, 0)
        if(pointB != -1):
            res = FindSubstringFromPosition(strA, strB, pointA, pointB, mapLocB)
            allResults.append(res)
    return allResults

########### MAIN ###########

strA = 'ABAZDC'
strB = 'BACBAD'

mapLocB = MapLocations(strB)

res = LongestSubSequence(strA, strB, mapLocB)
res = GetLongestString(res)
print(res)

########### STDOUT ###########

#ABAD
