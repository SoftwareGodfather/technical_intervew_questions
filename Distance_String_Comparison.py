def StringCompareNoCaseSensitive(str1, str2, allowedViolation):
    if abs(len(str1) - len(str2)) > allowedViolation:
        return False
    currentViolation = 0
    for i in range(0,len(str1)):
        if(str1[i].upper() != str2[i].upper()):
            currentViolation += 1
        if(currentViolation > allowedViolation):
            return False
    return True

########### MAIN ###########

str1 = 'abc'
str2 = 'ABdC'

res = StringCompareNoCaseSensitive(str1, str2, 1)
print(res)

########### STDOUT ###########

#True
