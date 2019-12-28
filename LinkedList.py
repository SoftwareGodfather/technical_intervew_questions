class node:
  def __init__(self,data):
      self.data = data
      self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def pushFront(self, elem):
        newNode = node(elem)
        newNode.next = self.head
        self.head = newNode
  
    def pushBack(self, elem):
        newNode = node(elem)
        if(self.head is None):
            self.head = newNode
            return
        temp =  self.head 
        prev = None
        while(temp):
            prev = temp
            temp = temp.next
    
        prev.next = newNode
       
    def printList(self):
        cur = self.head
        while(cur):
            print(cur.data)
            cur = cur.next

    def reverse(self):
        print('Reversing...')
        prev = None
        cur = self.head
        nextP = None
        while(cur):
            nextP = cur.next
            cur.next = prev
            prev = cur
            cur = nextP
        self.head = prev

########### MAIN ###########

newList = LinkedList()
newList.pushFront(0)
newList.pushFront(1)
newList.pushFront(2)
newList.pushFront(3)
newList.pushFront(4)
newList.pushBack(7)

newList.printList()
newList.reverse()
newList.printList()

########### STDOUT ###########

#4
#3
#2
#1
#0
#7
#Reversing...
#7
#0
#1
#2
#3
#4
