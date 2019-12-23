def FindLongestConsequtiveCaharcters(arr):
  previous = None
  currentNum = 0
  longestNum = 0
  longestChar = None

  for c in arr:
    if(c == previous):
      currentNum += 1
    else:
      currentNum = 0

    if(currentNum > longestNum):
      longestNum = currentNum
      longestChar = c

    previous = c
  
  print(f'Longest Consequtive Char: {longestChar}')

########### MAIN ###########

arr = 'gaabsdftreeertte'
print('Longest Consequtive Caharcters')
print(arr)
FindLongestConsequtiveCaharcters(arr)

########### STDOUT ###########

#Longest Consequtive Caharcters
#gaabsdftreeertte
#Longest Consequtive Char: e
