def GetLongestString(myStr):
    maxStr = ''
    for elem in myStr:
        if(len(elem) > len(maxStr)):
            maxStr =  elem
    return maxStr

def FindSubstringFromPosition(strA, strB, pointA, pointB):
    result = strA[pointA]
    i = pointA + 1
    j = pointB + 1
    while(j < len(strB)) and (i < len(strA)):
        currentlyLookingFor = strA[i]
        foundInStrB = strB[j:].find(currentlyLookingFor)
        if(foundInStrB != -1):
            result += currentlyLookingFor
            j += foundInStrB + 1
        i += 1
    return result

def LongestSubSequence(strA, strB):
    allResults = []
    for indA, charA in enumerate(strA):
        pointA = indA
        pointB = strB.find(charA)
        if(pointB != -1):
            res = FindSubstringFromPosition(strA, strB, pointA, pointB)
            allResults.append(res)
    return allResults

########### MAIN ###########

strA = 'ABAZDC'
strB = 'BACBAD'

res = LongestSubSequence(strA, strB)
res = GetLongestString(res)
print(res)

########### STDOUT ###########

#ABAD
