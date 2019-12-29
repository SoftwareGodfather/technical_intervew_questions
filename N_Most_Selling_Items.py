from heapq import nlargest

class Item:
    def __init__(self, itemId, name, quantity):
        self.itemId = itemId
        self.name = name
        self.quantity = quantity
        self.sold = 0
    
    def __str__(self):
        return f'itemId:{self.itemId} name:{self.name} quantity:{self.quantity} sold: {self.sold}'

class Werehouse:
    def __init__(self):
        self.items = dict()

    def AddItem(self, itemId, itemName, quantity):
        if itemId in self.items.keys():
            self.items[itemId].quantity += quantity
        else:
            self.items[itemId] = Item(itemId, itemName, quantity)

    def ItemSold(self, itemID):
        if itemID in self.items.keys():
            if self.items[itemID].quantity > 0:
                self.items[itemID].quantity -= 1
                self.items[itemID].sold += 1

    def GetTopSelling(self, N):
        print('\nGetTopSelling...')
        return nlargest(3, self.items, key=lambda s: self.items[s].sold)

    def PrintAll(self):
        for val in self.items.values():
            print(val)

########### MAIN ###########

wh = Werehouse()
wh.AddItem(12, 'book', 10)
wh.AddItem(12, 'book', 2)
wh.AddItem(7, 'table', 5)
wh.AddItem(3, 'computer', 30)
wh.AddItem(2, 'monitor', 7)
wh.AddItem(1, 'keyboard', 40)

wh.ItemSold(12)
wh.ItemSold(3)
wh.ItemSold(1)
wh.ItemSold(12)
wh.ItemSold(3)
wh.ItemSold(12)
wh.PrintAll()

top = wh.GetTopSelling(3)
for elem in top:
    print(elem)

########### STDOUT ###########

#itemId:12 name:book quantity:9 sold: 3
#itemId:7 name:table quantity:5 sold: 0
#itemId:3 name:computer quantity:28 sold: 2
#itemId:2 name:monitor quantity:7 sold: 0
#itemId:1 name:keyboard quantity:39 sold: 1

#GetTopSelling...
#12
#3
#1
