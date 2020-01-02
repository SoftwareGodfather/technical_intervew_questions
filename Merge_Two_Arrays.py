def MergeTwoArrays(arrA, arrB):
    indA = 0
    indB = 0
    res = []
    while(indA < len(arrA) and indB < len(arrB)):
        if(arrA[indA] < arrB[indB]):
            res.append(arrA[indA])
            indA += 1
        elif(arrA[indA] > arrB[indB]):
            res.append(arrB[indB])
            indB += 1
        else:
            res.append(arrA[indA])
            res.append(arrB[indB])
            indA += 1
            indB += 1
        
    for i in range(indA, len(arrA)):
        res.append(arrA[i])
    for i in range(indB, len(arrB)):
        res.append(arrB[i])

    return res


arrA = [2,5,7,9,12]
arrB = [1,3,6,7,8,11,14,20]

res = MergeTwoArrays(arrA, arrB)
print(res)

#STDOUT

#[1, 2, 3, 5, 6, 7, 7, 8, 9, 11, 12, 14, 20]
