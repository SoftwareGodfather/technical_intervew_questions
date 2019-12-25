def FindLongestConsecutiveCharacters(arr):
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
  
  print(f'Longest Consecutive Char: {longestChar}')

########### MAIN ###########

arr = 'gaabsdftreeertte'
print('Longest Consecutive Characters')
print(arr)
FindLongestConsecutiveCharacters(arr)

########### STDOUT ###########

#Longest Consecutive Characters
#gaabsdftreeertte
#Longest Consequtive Char: e
