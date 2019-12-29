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
        self.mostSellingItems = []

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
wh.PrintAll()
