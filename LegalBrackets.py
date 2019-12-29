openBracketsSet = set()
openBracketsSet.add('[')
openBracketsSet.add('{')
openBracketsSet.add('(')

closeBracketsSet = set()
closeBracketsSet.add(']')
closeBracketsSet.add('}')
closeBracketsSet.add(')')

def ClosingBrackets(b):
    if b == '[': return ']'
    if b == '{': return '}'
    if b == '(': return ')'
    return -1

def LegalBrackets(bracketsString):
    bracketStack = []
    for elem in bracketsString:
        if elem in openBracketsSet:
            bracketStack.append(ClosingBrackets(elem))
        elif elem in closeBracketsSet:
            closingBracket = bracketStack.pop()
            if (closingBracket != elem):
                return False

    if len(bracketStack) > 0:
        return False
        
    return True

########### MAIN ###########

bracketsString = '{summer (is) a great {[time]} of t[he ye]ar}'
result = LegalBrackets(bracketsString)
print(result)

########### STDOUT ###########

#True
