class Item():
    def __init__(self, itemName, itemCategory, buyLimit, buyPrice, time):
        self.itemName = itemName
        self.itemCategory = itemCategory

        self.buyLimit = buyLimit
        self.buyPrice = buyPrice

        self.time = time


    def percentChange(self):
        '''calculate change of buy/sell price since most recent data'''
        return percentChange

    def avgTimeToUpdate(self):
        '''calculate the avg time it takes to update this item price'''
        return avgTimeToUpdate

    def percentConfidence(self):
        '''calculate the confidence we have in the value based on time and change'''
        return percentConfidence
