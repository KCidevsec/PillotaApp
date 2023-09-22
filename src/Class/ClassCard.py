class Card:
    def __init__(self,suit,rank,points,image,image_r,key):
        self.suit=suit
        self.rank=rank
        self.points=points
        self.image=image#horizontal image
        self.image_r=image_r #vertical image
        self.key=key
    def getSuit(self):
        return self.suit
    def getRank(self):
        return self.rank
    def getCard(self):
        return "%s of %s"%(self.getRank(),self.getSuit())