def PrintMyList(my_list):
  result = ''
  for elem in my_list:
    result += elem
  print(result)

def FindIndex(my_list, myStr, startP):
  while(startP < len(my_list)):
    if(my_list[startP] == myStr):
      return startP
    else:
      startP += 1
  return -1
  
def ReverseList(my_list, startP, endP):
  while(startP < endP):
    tmp = my_list[startP]
    my_list[startP] = my_list[endP]
    my_list[endP] = tmp
    startP += 1
    endP -= 1

def ReverseEachWordSeparately(my_list):
  startP = 0
  endP = FindIndex(my_list, ' ', startP)

  while(endP != -1):
    ReverseList(my_list, startP, endP-1)
    startP = endP+1
    endP = FindIndex(my_list, ' ', startP)
  #Revesre last word
  ReverseList(my_list, startP, len(my_list)-1)

# MAIN

orig_list = ['p','e','r','f','e','c','t',' ',
            'm','a','k','e','s', ' ',
            'p','r','a','c','t','i','c','e']

print('Before:')
PrintMyList(orig_list)

ReverseList(orig_list, 0, len(orig_list)-1)
ReverseEachWordSeparately(orig_list)

print('After:')
PrintMyList(orig_list)

########### STDOUT ###########
#Before:
#perfect makes practiceAfter:
#practice makes perfect
