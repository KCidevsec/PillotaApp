from Tkinter import*
import random
import time
import unicodedata

#constants
window_Height=1200
window_Width=800
pop_window_Height=250
pop_window_Width=402
window_Color="dark green"
suit=["Hearts","Clubs","Diamonds","Spades"]
ranks=["7","8","9","10","J","Q","K","A"]

#class cards, constructor, accesors, mutators
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

class Deck:
    def __init__(self):
        global suit
        global ranks
        self.deck=[]
        for i in ranks:
            for j in suit:
                card=self.initializeCard(i,j)
                self.deck.append(card)
    def shuffle(self):
        random.shuffle(self.deck)
    def getDeck(self):
        for i in range(0,32):
            print(self.deck[i].getCard())
        return self.deck
    def initializeCard(self,rank,suit):
        if suit=="Clubs":
            if rank=="7":
                seven_clubs=PhotoImage(file="./Deck_Images/7clubs.gif")
                seven_clubs=seven_clubs.zoom(2,2)
                seven_clubs_R=PhotoImage(file="./Deck_Images_R/7clubs.gif")
                seven_clubs_R=seven_clubs_R.zoom(2,2)
                card=Card(suit,rank,0,seven_clubs,seven_clubs_R,1)
                return card
            if rank=="8":
                eight_clubs=PhotoImage(file="./Deck_Images/8clubs.gif")
                eight_clubs=eight_clubs.zoom(2,2)
                eight_clubs_R=PhotoImage(file="./Deck_Images_R/8clubs.gif")
                eight_clubs_R=eight_clubs_R.zoom(2,2)
                card=Card(suit,rank,0,eight_clubs,eight_clubs_R,2)
                return card
            if rank=="9":
                nine_clubs=PhotoImage(file="./Deck_Images/9clubs.gif")
                nine_clubs=nine_clubs.zoom(2,2)
                nine_clubs_R=PhotoImage(file="./Deck_Images_R/9clubs.gif")
                nine_clubs_R=nine_clubs_R.zoom(2,2)
                card=Card(suit,rank,0,nine_clubs,nine_clubs_R,3)
                return card
            if rank=="10":
                ten_clubs=PhotoImage(file="./Deck_Images/10clubs.gif")
                ten_clubs=ten_clubs.zoom(2,2)
                ten_clubs_R=PhotoImage(file="./Deck_Images_R/10clubs.gif")
                ten_clubs_R=ten_clubs_R.zoom(2,2)   
                card=Card(suit,rank,10,ten_clubs,ten_clubs_R,4)
                return card
            if rank=="J":
                jack_clubs=PhotoImage(file="./Deck_Images/Jclubs.gif")
                jack_clubs=jack_clubs.zoom(2,2)
                jack_clubs_R=PhotoImage(file="./Deck_Images_R/Jclubs.gif")
                jack_clubs_R=jack_clubs_R.zoom(2,2)   
                card=Card(suit,rank,2,jack_clubs,jack_clubs_R,5)
                return card
            if rank=="Q":
                queen_clubs=PhotoImage(file="./Deck_Images/Qclubs.gif")
                queen_clubs=queen_clubs.zoom(2,2)
                queen_clubs_R=PhotoImage(file="./Deck_Images_R/Qclubs.gif")
                queen_clubs_R=queen_clubs_R.zoom(2,2)
                card=Card(suit,rank,3,queen_clubs,queen_clubs_R,6)
                return card
            if rank=="K":
                king_clubs=PhotoImage(file="./Deck_Images/Kclubs.gif")
                king_clubs=king_clubs.zoom(2,2)
                king_clubs_R=PhotoImage(file="./Deck_Images_R/Kclubs.gif")
                king_clubs_R=king_clubs_R.zoom(2,2)
                card=Card(suit,rank,4,king_clubs,king_clubs_R,7)
                return card
            if rank=="A":
                ace_clubs=PhotoImage(file="./Deck_Images/Aclubs.gif")
                ace_clubs=ace_clubs.zoom(2,2)
                ace_clubs_R=PhotoImage(file="./Deck_Images_R/Aclubs.gif")
                ace_clubs_R=ace_clubs_R.zoom(2,2)
                card=Card(suit,rank,11,ace_clubs,ace_clubs_R,8)
                return card
        if suit=="Hearts":
            if rank=="7":
                seven_hearts=PhotoImage(file="./Deck_Images/7hearts.gif")
                seven_hearts=seven_hearts.zoom(2,2)
                seven_hearts_R=PhotoImage(file="./Deck_Images_R/7hearts.gif")
                seven_hearts_R=seven_hearts_R.zoom(2,2)
                card=Card(suit,rank,0,seven_hearts,seven_hearts_R,9)
                return card
            if rank=="8":
                eight_hearts=PhotoImage(file="./Deck_Images/8hearts.gif")
                eight_hearts=eight_hearts.zoom(2,2)
                eight_hearts_R=PhotoImage(file="./Deck_Images_R/8hearts.gif")
                eight_hearts_R=eight_hearts_R.zoom(2,2) 
                card=Card(suit,rank,0,eight_hearts,eight_hearts_R,10)
                return card
            if rank=="9":
                nine_hearts=PhotoImage(file="./Deck_Images/9hearts.gif")
                nine_hearts=nine_hearts.zoom(2,2)
                nine_hearts_R=PhotoImage(file="./Deck_Images_R/9hearts.gif")
                nine_hearts_R=nine_hearts_R.zoom(2,2)
                card=Card(suit,rank,0,nine_hearts,nine_hearts_R,11)
                return card
            if rank=="10":
                ten_hearts=PhotoImage(file="./Deck_Images/10hearts.gif")
                ten_hearts=ten_hearts.zoom(2,2)
                ten_hearts_R=PhotoImage(file="./Deck_Images_R/10hearts.gif")
                ten_hearts_R=ten_hearts_R.zoom(2,2)
                card=Card(suit,rank,10,ten_hearts,ten_hearts_R,12)
                return card
            if rank=="J":
                jack_hearts=PhotoImage(file="./Deck_Images/Jhearts.gif")
                jack_hearts=jack_hearts.zoom(2,2)
                jack_hearts_R=PhotoImage(file="./Deck_Images_R/Jhearts.gif")
                jack_hearts_R=jack_hearts_R.zoom(2,2)   
                card=Card(suit,rank,2,jack_hearts,jack_hearts_R,13)
                return card
            if rank=="Q":
                queen_hearts=PhotoImage(file="./Deck_Images/Qhearts.gif")
                queen_hearts=queen_hearts.zoom(2,2)
                queen_hearts_R=PhotoImage(file="./Deck_Images_R/Qhearts.gif")
                queen_hearts_R=queen_hearts_R.zoom(2,2)
                card=Card(suit,rank,3,queen_hearts,queen_hearts_R,14)
                return card
            if rank=="K":
                king_hearts=PhotoImage(file="./Deck_Images/Khearts.gif")
                king_hearts=king_hearts.zoom(2,2)
                king_hearts_R=PhotoImage(file="./Deck_Images_R/Khearts.gif")
                king_hearts_R=king_hearts_R.zoom(2,2)
                card=Card(suit,rank,4,king_hearts,king_hearts_R,15)
                return card
            if rank=="A":
                ace_hearts=PhotoImage(file="./Deck_Images/Ahearts.gif")
                ace_hearts=ace_hearts.zoom(2,2)
                ace_hearts_R=PhotoImage(file="./Deck_Images_R/Ahearts.gif")
                ace_hearts_R=ace_hearts_R.zoom(2,2)
                card=Card(suit,rank,11,ace_hearts,ace_hearts_R,16)
                return card
        if suit=="Diamonds":
            if rank=="7":
                seven_diamonds=PhotoImage(file="./Deck_Images/7diamonds.gif")
                seven_diamonds=seven_diamonds.zoom(2,2)
                seven_diamonds_R=PhotoImage(file="./Deck_Images_R/7diamonds.gif")
                seven_diamonds_R=seven_diamonds_R.zoom(2,2)
                card=Card(suit,rank,0,seven_diamonds,seven_diamonds_R,25)
                return card
            if rank=="8":
                eight_diamonds=PhotoImage(file="./Deck_Images/8diamonds.gif")
                eight_diamonds=eight_diamonds.zoom(2,2)
                eight_diamonds_R=PhotoImage(file="./Deck_Images_R/8diamonds.gif")
                eight_diamonds_R=eight_diamonds_R.zoom(2,2)  
                card=Card(suit,rank,0,eight_diamonds,eight_diamonds_R,26)
                return card
            if rank=="9":
                nine_diamonds=PhotoImage(file="./Deck_Images/9diamonds.gif")
                nine_diamonds=nine_diamonds.zoom(2,2)
                nine_diamonds_R=PhotoImage(file="./Deck_Images_R/9diamonds.gif")
                nine_diamonds_R=nine_diamonds_R.zoom(2,2)
                card=Card(suit,rank,0,nine_diamonds,nine_diamonds_R,27)
                return card
            if rank=="10":
                ten_diamonds=PhotoImage(file="./Deck_Images/10diamonds.gif")
                ten_diamonds=ten_diamonds.zoom(2,2)
                ten_diamonds_R=PhotoImage(file="./Deck_Images_R/10diamonds.gif")
                ten_diamonds_R=ten_diamonds_R.zoom(2,2)
                card=Card(suit,rank,10,ten_diamonds,ten_diamonds_R,28)
                return card
            if rank=="J":
                jack_diamonds=PhotoImage(file="./Deck_Images/Jdiamonds.gif")
                jack_diamonds=jack_diamonds.zoom(2,2)
                jack_diamonds_R=PhotoImage(file="./Deck_Images_R/Jdiamonds.gif")
                jack_diamonds_R=jack_diamonds_R.zoom(2,2)   
                card=Card(suit,rank,2,jack_diamonds,jack_diamonds_R,29)
                return card
            if rank=="Q":
                queen_diamonds=PhotoImage(file="./Deck_Images/Qdiamonds.gif")
                queen_diamonds=queen_diamonds.zoom(2,2)
                queen_diamonds_R=PhotoImage(file="./Deck_Images_R/Qdiamonds.gif")
                queen_diamonds_R=queen_diamonds_R.zoom(2,2)
                card=Card(suit,rank,3,queen_diamonds,queen_diamonds_R,30)
                return card
            if rank=="K":
                king_diamonds=PhotoImage(file="./Deck_Images/Kdiamonds.gif")
                king_diamonds=king_diamonds.zoom(2,2)
                king_diamonds_R=PhotoImage(file="./Deck_Images_R/Kdiamonds.gif")
                king_diamonds_R=king_diamonds_R.zoom(2,2)
                card=Card(suit,rank,4,king_diamonds,king_diamonds_R,31)
                return card
            if rank=="A":
                ace_diamonds=PhotoImage(file="./Deck_Images/Adiamonds.gif")
                ace_diamonds=ace_diamonds.zoom(2,2)
                ace_diamonds_R=PhotoImage(file="./Deck_Images_R/Adiamonds.gif")
                ace_diamonds_R=ace_diamonds_R.zoom(2,2)
                card=Card(suit,rank,11,ace_diamonds,ace_diamonds_R,32)
                return card
        if suit=="Spades":
            if rank=="7":
                seven_spades=PhotoImage(file="./Deck_Images/7spades.gif")
                seven_spades=seven_spades.zoom(2,2)
                seven_spades_R=PhotoImage(file="./Deck_Images_R/7spades.gif")
                seven_spades_R=seven_spades_R.zoom(2,2)
                card=Card(suit,rank,0,seven_spades,seven_spades_R,17)
                return card
            if rank=="8":
                eight_spades=PhotoImage(file="./Deck_Images/8spades.gif")
                eight_spades=eight_spades.zoom(2,2)
                eight_spades_R=PhotoImage(file="./Deck_Images_R/8spades.gif")
                eight_spades_R=eight_spades_R.zoom(2,2)  
                card=Card(suit,rank,0,eight_spades,eight_spades_R,18)
                return card
            if rank=="9":
                nine_spades=PhotoImage(file="./Deck_Images/9spades.gif")
                nine_spades=nine_spades.zoom(2,2)
                nine_spades_R=PhotoImage(file="./Deck_Images_R/9spades.gif")
                nine_spades_R=nine_spades_R.zoom(2,2)
                card=Card(suit,rank,0,nine_spades,nine_spades_R,19)
                return card
            if rank=="10":
                ten_spades=PhotoImage(file="./Deck_Images/10spades.gif")
                ten_spades=ten_spades.zoom(2,2)
                ten_spades_R=PhotoImage(file="./Deck_Images_R/10spades.gif")
                ten_spades_R=ten_spades_R.zoom(2,2)
                card=Card(suit,rank,10,ten_spades,ten_spades_R,20)
                return card
            if rank=="J":
                jack_spades=PhotoImage(file="./Deck_Images/Jspades.gif")
                jack_spades=jack_spades.zoom(2,2)
                jack_spades_R=PhotoImage(file="./Deck_Images_R/Jspades.gif")
                jack_spades_R=jack_spades_R.zoom(2,2) 
                card=Card(suit,rank,2,jack_spades,jack_spades_R,21)
                return card
            if rank=="Q":
                queen_spades=PhotoImage(file="./Deck_Images/Qspades.gif")
                queen_spades=queen_spades.zoom(2,2)
                queen_spades_R=PhotoImage(file="./Deck_Images_R/Qspades.gif")
                queen_spades_R=queen_spades_R.zoom(2,2)
                card=Card(suit,rank,3,queen_spades,queen_spades_R,22)
                return card
            if rank=="K":
                king_spades=PhotoImage(file="./Deck_Images/Kspades.gif")
                king_spades=king_spades.zoom(2,2)
                king_spades_R=PhotoImage(file="./Deck_Images_R/Kspades.gif")
                king_spades_R=king_spades_R.zoom(2,2)
                card=Card(suit,rank,4,king_spades,king_spades_R,23)
                return card
            if rank=="A":
                ace_spades=PhotoImage(file="./Deck_Images/Aspades.gif")
                ace_spades=ace_spades.zoom(2,2)
                ace_spades_R=PhotoImage(file="./Deck_Images_R/Aspades.gif")
                ace_spades_R=ace_spades_R.zoom(2,2)
                card=Card(suit,rank,11,ace_spades,ace_spades_R,24)
                return card
            
class Player1:
    def __init__(self,canvas):
        self.canvas=canvas
        self.cards=[]
        self.throwed=[0,0,0,0,0,0,0,0]
    def setCard(self,card):
        self.cards.append(card)
    def displayCards(self):
        self.cards.sort(key=self.getSortKey)
        self.id1=canvas.create_image(420, 705, image = self.cards[0].image ,anchor=CENTER,tags="card1")
        self.canvas.tag_bind("card1","<Button-1>",self.throwCard1)
        self.id2=canvas.create_image(470, 705, image = self.cards[1].image ,anchor=CENTER,tags="card2")
        self.canvas.tag_bind("card2","<Button-1>",self.throwCard2)
        self.id3=canvas.create_image(520, 705, image = self.cards[2].image ,anchor=CENTER,tags="card3")
        self.canvas.tag_bind("card3","<Button-1>",self.throwCard3)
        self.id4=canvas.create_image(570, 705, image = self.cards[3].image ,anchor=CENTER,tags="card4")
        self.canvas.tag_bind("card4","<Button-1>",self.throwCard4)
        self.id5=canvas.create_image(620, 705, image = self.cards[4].image ,anchor=CENTER,tags="card5")
        self.canvas.tag_bind("card5","<Button-1>",self.throwCard5)
        self.id6=canvas.create_image(670, 705, image = self.cards[5].image ,anchor=CENTER,tags="card6")
        self.canvas.tag_bind("card6","<Button-1>",self.throwCard6)
        self.id7=canvas.create_image(720, 705, image = self.cards[6].image ,anchor=CENTER,tags="card7")
        self.canvas.tag_bind("card7","<Button-1>",self.throwCard7)
        self.id8=canvas.create_image(770, 705, image = self.cards[7].image ,anchor=CENTER,tags="card8")
        self.canvas.tag_bind("card8","<Button-1>",self.throwCard8)
    def getSortKey(self,card):
        return card.key
    def throwCard1(self,event):
        if self.throwed[0]!=1:
            xCord=420
            yCord=705
            while xCord<600:
                self.canvas.coords(self.id1,xCord,yCord)
                self.canvas.update_idletasks()
                self.canvas.update()
                xCord=xCord+20
                time.sleep(0.04)
            while yCord>430:
                self.canvas.coords(self.id1,xCord,yCord)
                self.canvas.update_idletasks()
                self.canvas.update()
                yCord=yCord-20
                time.sleep(0.04)
            self.throwed[0]=1
    def throwCard2(self,event):
        if self.throwed[1]!=1:
            xCord=470
            yCord=705
            while xCord<600:
                self.canvas.coords(self.id2,xCord,yCord)
                self.canvas.update_idletasks()
                self.canvas.update()
                xCord=xCord+20
                time.sleep(0.04)
            while yCord>430:
                self.canvas.coords(self.id2,xCord,yCord)
                self.canvas.update_idletasks()
                self.canvas.update()
                yCord=yCord-20
                time.sleep(0.04)
            self.throwed[1]=1
    def throwCard3(self,event):
        if self.throwed[2]!=1:
            xCord=520
            yCord=705
            while xCord<600:
                self.canvas.coords(self.id3,xCord,yCord)
                self.canvas.update_idletasks()
                self.canvas.update()
                xCord=xCord+20
                time.sleep(0.04)
            while yCord>430:
                self.canvas.coords(self.id3,xCord,yCord)
                self.canvas.update_idletasks()
                self.canvas.update()
                yCord=yCord-20
                time.sleep(0.04)
            self.throwed[2]=1
    def throwCard4(self,event):
        if self.throwed[3]!=1:
            xCord=570
            yCord=705
            while xCord<600:
                self.canvas.coords(self.id4,xCord,yCord)
                self.canvas.update_idletasks()
                self.canvas.update()
                xCord=xCord+20
                time.sleep(0.04)
            while yCord>430:
                self.canvas.coords(self.id4,xCord,yCord)
                self.canvas.update_idletasks()
                self.canvas.update()
                yCord=yCord-20
                time.sleep(0.04)
            self.throwed[3]=1
    def throwCard5(self,event):
        if self.throwed[4]!=1:
            xCord=620
            yCord=705
            while xCord>600:
                self.canvas.coords(self.id5,xCord,yCord)
                self.canvas.update_idletasks()
                self.canvas.update()
                xCord=xCord-20
                time.sleep(0.04)
            while yCord>430:
                self.canvas.coords(self.id5,xCord,yCord)
                self.canvas.update_idletasks()
                self.canvas.update()
                yCord=yCord-20
                time.sleep(0.04)
            self.throwed[4]=1
    def throwCard6(self,event):
        if self.throwed[5]!=1:
            xCord=670
            yCord=705
            while xCord>600:
                self.canvas.coords(self.id6,xCord,yCord)
                self.canvas.update_idletasks()
                self.canvas.update()
                xCord=xCord-20
                time.sleep(0.04)
            while yCord>430:
                self.canvas.coords(self.id6,xCord,yCord)
                self.canvas.update_idletasks()
                self.canvas.update()
                yCord=yCord-20
                time.sleep(0.04)
            self.throwed[5]=1
    def throwCard7(self,event):
        if self.throwed[6]!=1:
            xCord=720
            yCord=705
            while xCord>600:
                self.canvas.coords(self.id7,xCord,yCord)
                self.canvas.update_idletasks()
                self.canvas.update()
                xCord=xCord-20
                time.sleep(0.04)
            while yCord>430:
                self.canvas.coords(self.id7,xCord,yCord)
                self.canvas.update_idletasks()
                self.canvas.update()
                yCord=yCord-20
                time.sleep(0.04)
            self.throwed[6]=1
    def throwCard8(self,event):
        if self.throwed[7]!=1:
            xCord=770
            yCord=705
            while xCord>600:
                self.canvas.coords(self.id8,xCord,yCord)
                self.canvas.update_idletasks()
                self.canvas.update()
                xCord=xCord-20
                time.sleep(0.04)
            while yCord>430:
                self.canvas.coords(self.id8,xCord,yCord)
                self.canvas.update_idletasks()
                self.canvas.update()
                yCord=yCord-20
                time.sleep(0.04)
            self.throwed[7]=1
            
class Player2:
    def __init__(self,canvas):
        global back_side_R
        self.canvas=canvas
        self.throwed=[0,0,0,0,0,0,0,0]
        self.id1=canvas.create_image(95, 230, image = back_side_R,anchor=CENTER)
        self.id2=canvas.create_image(95, 280, image = back_side_R,anchor=CENTER)
        self.id3=canvas.create_image(95, 330, image = back_side_R,anchor=CENTER)
        self.id4=canvas.create_image(95, 380, image = back_side_R,anchor=CENTER)
        self.id5=canvas.create_image(95, 430, image = back_side_R,anchor=CENTER)
        self.id6=canvas.create_image(95, 480, image = back_side_R,anchor=CENTER)
        self.id7=canvas.create_image(95, 530, image = back_side_R,anchor=CENTER)
        self.id8=canvas.create_image(95, 580, image = back_side_R,anchor=CENTER)
        self.cards=[]
        self.cards.sort(key=self.getSortKey)
    def getSortKey(self,card):
        return card.key
    def setCard(self,card):
        self.cards.append(card)    
           
class Player3:
    def __init__(self,canvas):
        global back_side
        self.canvas=canvas
        self.throwed=[0,0,0,0,0,0,0,0]
        self.id1=canvas.create_image(420, 95, image = back_side,anchor=CENTER)
        self.id2=canvas.create_image(470, 95, image = back_side,anchor=CENTER)
        self.id3=canvas.create_image(520, 95, image = back_side,anchor=CENTER)
        self.id4=canvas.create_image(570, 95, image = back_side,anchor=CENTER)
        self.id5=canvas.create_image(620, 95, image = back_side,anchor=CENTER)
        self.id6=canvas.create_image(670, 95, image = back_side,anchor=CENTER)
        self.id7=canvas.create_image(720, 95, image = back_side,anchor=CENTER)
        self.id8=canvas.create_image(770, 95, image = back_side,anchor=CENTER)
        self.cards=[]
        self.cards.sort(key=self.getSortKey)
    def getSortKey(self,card):
        return card.key
    def setCard(self,card):
            self.cards.append(card)
            
class Player4:
    def __init__(self,canvas):
        global back_side_R
        self.canvas=canvas
        self.throwed=[0,0,0,0,0,0,0,0]
        self.id1=canvas.create_image(1105, 230, image = back_side_R,anchor=CENTER)
        self.id2=canvas.create_image(1105, 280, image = back_side_R,anchor=CENTER)
        self.id3=canvas.create_image(1105, 330, image = back_side_R,anchor=CENTER)
        self.id4=canvas.create_image(1105, 380, image = back_side_R,anchor=CENTER)
        self.id5=canvas.create_image(1105, 430, image = back_side_R,anchor=CENTER)
        self.id6=canvas.create_image(1105, 480, image = back_side_R,anchor=CENTER)
        self.id7=canvas.create_image(1105, 530, image = back_side_R,anchor=CENTER)
        self.id8=canvas.create_image(1105, 580, image = back_side_R,anchor=CENTER)
        self.cards=[]
        self.cards.sort(key=self.getSortKey)
    def getSortKey(self,card):
        return card.key
    def setCard(self,card):
            self.cards.append(card)
        
class PopupWindow:
    def __init__(self,root):
        self.top=Toplevel(root,background="blue",takefocus=True)
        self.top.resizable(0, 0)
        self.top.protocol('WM_DELETE_WINDOW', self.close)
        self.setOnTop(pop_window_Width,pop_window_Height)
        self.lblheadfgcolor="white"
        self.lblheadbgcolor="blue"
        self.lblheadfont=("Times","20","bold")
        self.lblbodyfgcolor="black"
        self.lblbodybgcolor="skyblue2"
        self.lblbodyfont=("Times","14","bold")
        self.kozi=""
        self.bid=0
        self.top_bid=42
        self.dropDownInitial=StringVar()
        self.dropDownValues=[
                             '8','9','10','11','12','13','14','15','16','17','18','19','20','21','22'
                             ,'23','24','25','26','27','28','29','30','31','32','33','34','35','36'
                             ,'37','38','39','40','41','42']
        self.dropDownInitial.set(self.dropDownValues[0])
        self.passcounter=0
        self.doubleFlag=False
        self.reDoubleFlag=False
        self.firstRound=True
        self.setLabels()
        self.setButton()
        self.setInputLabels()
        self.setTurn()
        self.speak()
        root.wait_window(self.top)
        print("Destroying Top Window")
    def decideFirstBid(self):
        global player1,player2,player3,player4
        bid={"kozi":" ","bid":0,"pass":0}
        NoOfCards={"Spades":0,"Clubs":0,"Diamonds":0,"Hearts":0,"Ace":0}
        JackFlag={"Spades":0,"Clubs":0,"Diamonds":0,"Hearts":0}
        NineFlag={"Spades":0,"Clubs":0,"Diamonds":0,"Hearts":0}
        if self.turn==1:
            print("Player 2 thinking:")
            for i in player2.cards:
                if i.suit=="Spades":
                    NoOfCards["Spades"]=NoOfCards["Spades"]+1
                    print("Spades:" + str(NoOfCards["Spades"]))
                    if i.rank=="J":
                        JackFlag["Spades"]=1
                        print("Jack Spades:" + str(JackFlag["Spades"]))
                    if i.rank=="9":
                        NineFlag["Spades"]=1
                        print("Nine Spades:" + str(NineFlag["Spades"]))
                elif i.suit=="Clubs":
                    NoOfCards["Clubs"]=NoOfCards["Clubs"]+1
                    print("Clubs:" + str(NoOfCards["Clubs"]))
                    if i.rank=="J":
                        JackFlag["Clubs"]=1
                        print("Jack Clubs:" + str(JackFlag["Clubs"]))
                    if i.rank=="9":
                        NineFlag["Clubs"]=1
                        print("Nine Clubs:" + str(NineFlag["Clubs"]))
                elif i.suit=="Diamonds":
                    NoOfCards["Diamonds"]=NoOfCards["Diamonds"]+1
                    print("Diamonds:" + str(NoOfCards["Diamonds"]))
                    if i.rank=="J":
                        JackFlag["Diamonds"]=1
                        print("Jack Diamonds:" + str(JackFlag["Diamonds"]))
                    if i.rank=="9":
                        NineFlag["Diamonds"]=1
                        print("Nine Diamonds:" + str(NineFlag["Diamonds"]))
                elif i.suit=="Hearts":
                    NoOfCards["Hearts"]=NoOfCards["Hearts"]+1
                    print("Hearts:" + str(NoOfCards["Hearts"]))
                    if i.rank=="J":
                        JackFlag["Hearts"]=1
                        print("Jack Hearts:" + str(JackFlag["Hearts"]))
                    if i.rank=="9":
                        NineFlag["Hearts"]=1
                        print("Nine Hearts:" + str(NineFlag["Hearts"]))
                if i.rank=="A":
                    NoOfCards["Ace"]=NoOfCards["Ace"]+1
                    print("Ace: "+str(NoOfCards["Ace"]))
            if NoOfCards["Ace"]>=2:
                if NoOfCards["Spades"]>=3 and JackFlag["Spades"]==1 and NineFlag["Spades"]==1:
                    bid["kozi"]="Spades"
                    bid["bid"]=9
                    print("choosing 9 SPADES")
                elif NoOfCards["Clubs"]>=3 and JackFlag["Clubs"]==1 and NineFlag["Clubs"]==1:
                    bid["kozi"]="Clubs"
                    bid["bid"]=9
                    print("choosing 9 Clubs")
                elif NoOfCards["Diamonds"]>=3 and JackFlag["Diamonds"]==1 and NineFlag["Diamonds"]==1:
                    bid["kozi"]="Diamonds"
                    bid["bid"]=9
                    print("choosing 9 Diamonds")
                elif NoOfCards["Hearts"]>=3 and JackFlag["Hearts"]==1 and NineFlag["Hearts"]==1:
                    bid["kozi"]="Hearts"
                    bid["bid"]=9
                    print("choosing 9 Hearts")
                elif NoOfCards["Spades"]>=3 and (JackFlag["Spades"]==1 or NineFlag["Spades"]==1):
                    bid["kozi"]="Spades"
                    bid["bid"]=8
                    print("choosing 8 Spades")
                elif NoOfCards["Clubs"]>=3 and (JackFlag["Clubs"]==1 or NineFlag["Clubs"]==1):
                    bid["kozi"]="Clubs"
                    bid["bid"]=8
                    print("choosing 8 Clubs")
                elif NoOfCards["Diamonds"]>=3 and (JackFlag["Diamonds"]==1 or NineFlag["Diamonds"]==1):
                    bid["kozi"]="Diamonds"
                    bid["bid"]=8
                    print("choosing 8 Diamonds")
                elif NoOfCards["Hearts"]>=3 and (JackFlag["Hearts"]==1 or NineFlag["Hearts"]==1):
                    bid["kozi"]="Hearts"
                    bid["bid"]=8
                    print("choosing 8 Hearts")
                else:
                    bid["pass"]=1
                    print("choosing Pass with 2 Ace")
            else:
                bid["pass"]=1
                print("choosing Pass")
            print(bid)
            return bid
        elif self.turn==2:
            print("Player 3 thinking:")
            for i in player3.cards:
                if i.suit=="Spades":
                    NoOfCards["Spades"]=NoOfCards["Spades"]+1
                    print("Spades:" + str(NoOfCards["Spades"]))
                    if i.rank=="J":
                        JackFlag["Spades"]=1
                        print("Jack Spades:" + str(JackFlag["Spades"]))
                    if i.rank=="9":
                        NineFlag["Spades"]=1
                        print("Nine Spades:" + str(NineFlag["Spades"]))
                elif i.suit=="Clubs":
                    NoOfCards["Clubs"]=NoOfCards["Clubs"]+1
                    print("Clubs:" + str(NoOfCards["Clubs"]))
                    if i.rank=="J":
                        JackFlag["Clubs"]=1
                        print("Jack Clubs:" + str(JackFlag["Clubs"]))
                    if i.rank=="9":
                        NineFlag["Clubs"]=1
                        print("Nine Clubs:" + str(NineFlag["Clubs"]))
                elif i.suit=="Diamonds":
                    NoOfCards["Diamonds"]=NoOfCards["Diamonds"]+1
                    print("Diamonds:" + str(NoOfCards["Diamonds"]))
                    if i.rank=="J":
                        JackFlag["Diamonds"]=1
                        print("Jack Diamonds:" + str(JackFlag["Diamonds"]))
                    if i.rank=="9":
                        NineFlag["Diamonds"]=1
                        print("Nine Diamonds:" + str(NineFlag["Diamonds"]))
                elif i.suit=="Hearts":
                    print("Hearts:" + str(NoOfCards["Hearts"]))
                    NoOfCards["Hearts"]=NoOfCards["Hearts"]+1
                    if i.rank=="J":
                        JackFlag["Hearts"]=1
                        print("Jack Hearts:" + str(JackFlag["Hearts"]))
                    if i.rank=="9":
                        NineFlag["Hearts"]=1
                        print("Nine Hearts:" + str(NineFlag["Hearts"]))
                if i.rank=="A":
                    NoOfCards["Ace"]=NoOfCards["Ace"]+1
                    print("Ace: "+str(NoOfCards["Ace"]))
            if NoOfCards["Ace"]>=2:
                if NoOfCards["Spades"]>=3 and JackFlag["Spades"]==1 and NineFlag["Spades"]==1:
                    bid["kozi"]="Spades"
                    bid["bid"]=9
                    print("choosing 9 SPADES")
                elif NoOfCards["Clubs"]>=3 and JackFlag["Clubs"]==1 and NineFlag["Clubs"]==1:
                    bid["kozi"]="Clubs"
                    bid["bid"]=9
                    print("choosing 9 Clubs")
                elif NoOfCards["Diamonds"]>=3 and JackFlag["Diamonds"]==1 and NineFlag["Diamonds"]==1:
                    bid["kozi"]="Diamonds"
                    bid["bid"]=9
                    print("choosing 9 Diamonds")
                elif NoOfCards["Hearts"]>=3 and JackFlag["Hearts"]==1 and NineFlag["Hearts"]==1:
                    bid["kozi"]="Hearts"
                    bid["bid"]=9
                    print("choosing 9 Hearts")
                elif NoOfCards["Spades"]>=3 and (JackFlag["Spades"]==1 or NineFlag["Spades"]==1):
                    bid["kozi"]="Spades"
                    bid["bid"]=8
                    print("choosing 8 Spades")
                elif NoOfCards["Clubs"]>=3 and (JackFlag["Clubs"]==1 or NineFlag["Clubs"]==1):
                    bid["kozi"]="Clubs"
                    bid["bid"]=8
                    print("choosing 8 Clubs")
                elif NoOfCards["Diamonds"]>=3 and (JackFlag["Diamonds"]==1 or NineFlag["Diamonds"]==1):
                    bid["kozi"]="Diamonds"
                    bid["bid"]=8
                    print("Choosing 8 Diamonds")
                elif NoOfCards["Hearts"]>=3 and (JackFlag["Hearts"]==1 or NineFlag["Hearts"]==1):
                    bid["kozi"]="Hearts"
                    bid["bid"]=8
                    print("Choosing 8 Hearts")
                else:
                    bid["pass"]=1
                    print("choosing Pass with 2 Ace")
            else:
                bid["pass"]=1
                print("choosing Pass")
            print(bid)
            return bid
        elif self.turn==3:
            for i in player3.cards:
                if i.suit=="Spades":
                    NoOfCards["Spades"]=NoOfCards["Spades"]+1
                    if i.rank=="J":
                        JackFlag["Spades"]=1
                    if i.rank=="9":
                        NineFlag["Spades"]=1
                elif i.suit=="Clubs":
                    NoOfCards["Clubs"]=NoOfCards["Clubs"]+1
                    if i.rank=="J":
                        JackFlag["Clubs"]=1
                    if i.rank=="9":
                        NineFlag["Clubs"]=1
                elif i.suit=="Diamonds":
                    NoOfCards["Diamonds"]=NoOfCards["Diamonds"]+1
                    if i.rank=="J":
                        JackFlag["Diamonds"]=1
                    if i.rank=="9":
                        NineFlag["Diamonds"]=1
                elif i.suit=="Hearts":
                    NoOfCards["Hearts"]=NoOfCards["Hearts"]+1
                    if i.rank=="J":
                        JackFlag["Hearts"]=1
                    if i.rank=="9":
                        NineFlag["Hearts"]=1
                if i.rank=="A":
                    NoOfCards["Ace"]=NoOfCards["Ace"]+1
            if NoOfCards["Ace"]>=2:
                if NoOfCards["Spades"]>=3 and JackFlag["Spades"]==1 and NineFlag["Spades"]==1:
                    bid["kozi"]="Spades"
                    bid["bid"]=9
                elif NoOfCards["Clubs"]>=3 and JackFlag["Clubs"]==1 and NineFlag["Clubs"]==1:
                    bid["kozi"]="Clubs"
                    bid["bid"]=9
                elif NoOfCards["Diamonds"]>=3 and JackFlag["Diamonds"]==1 and NineFlag["Diamonds"]==1:
                    bid["kozi"]="Diamonds"
                    bid["bid"]=9
                elif NoOfCards["Hearts"]>=3 and JackFlag["Hearts"]==1 and NineFlag["Hearts"]==1:
                    bid["kozi"]="Hearts"
                    bid["bid"]=9
                elif NoOfCards["Spades"]>=3 and (JackFlag["Spades"]==1 or NineFlag["Spades"]==1):
                    bid["kozi"]="Spades"
                    bid["bid"]=8
                elif NoOfCards["Clubs"]>=3 and (JackFlag["Clubs"]==1 or NineFlag["Clubs"]==1):
                    bid["kozi"]="Clubs"
                    bid["bid"]=8
                elif NoOfCards["Diamonds"]>=3 and (JackFlag["Diamonds"]==1 or NineFlag["Diamonds"]==1):
                    bid["kozi"]="Diamonds"
                    bid["bid"]=8
                elif NoOfCards["Hearts"]>=3 and (JackFlag["Hearts"]==1 or NineFlag["Hearts"]==1):
                    bid["kozi"]="Hearts"
                    bid["bid"]=8
                else:
                    bid["pass"]=1
            else:
                bid["pass"]=1
            print(bid)
            return bid
    def speak(self):
        self.increment=0
        if self.firstRound==True:
            while self.turn!=0:
                if self.turn==1:
                    self.player1Bid=self.decideFirstBid()
                    print(self.player1Bid)
                    self.turn=2
                    if self.player1Bid["pass"]==1:
                        self.btnPass()
                    else:
                        self.increment=self.player1Bid["bid"]-8
                        self.dropDownInitial.set(self.player1Bid["bid"])
                        if self.player1Bid["kozi"]=="Clubs":
                            self.btnclub()
                        elif self.player1Bid["kozi"]=="Diamonds":
                            self.btndiamond()
                        elif self.player1Bid["kozi"]=="Hearts":
                            self.btnhearts()
                        elif self.player1Bid["kozi"]=="Spades":
                            self.btnspade()
                    self.turn=2
                elif self.turn==2:
                    self.player2Bid=self.decideFirstBid()
                    self.turn=3
                    if self.player2Bid["pass"]==1:
                        self.btnPass()
                    else:
                        self.player2Bid["bid"]=self.player2Bid["bid"]+self.increment
                        self.increment=self.player2Bid["bid"]-8
                        self.dropDownInitial.set(self.player2Bid["bid"])
                        if self.player2Bid["kozi"]=="Clubs":
                            self.btnclub()
                        elif self.player2Bid["kozi"]=="Diamonds":
                            self.btndiamond()
                        elif self.player2Bid["kozi"]=="Hearts":
                            self.btnhearts()
                        elif self.player2Bid["kozi"]=="Spades":
                            self.btnspade()
                elif self.turn==3:
                    self.player3Bid=self.decideFirstBid()
                    self.turn=0
                    if self.player3Bid["pass"]==1:
                        self.btnPass()
                    else:
                        self.player3Bid["bid"]=self.player3Bid["bid"]+self.increment
                        self.dropDownInitial.set(self.player3Bid["bid"])
                        if self.player3Bid["kozi"]=="Clubs":
                            self.btnclub()
                        elif self.player3Bid["kozi"]=="Diamonds":
                            self.btndiamond()
                        elif self.player3Bid["kozi"]=="Hearts":
                            self.btnhearts()
                        elif self.player3Bid["kozi"]=="Spades":
                            self.btnspade()
            self.firstRound=False
    def close(self):
        root.destroy()
    def destroy(self):
        global dataArr
        dataArr={"kozi":self.kozi,"bid":self.bid,"double":str(self.doubleFlag),"redouble":str(self.reDoubleFlag),"turn":str(self.turn+1)}
        self.top.destroy()
    def stopBiding(self):
        if self.passcounter==3 and self.bid>0:
            print("Kozi:" + str(self.bid) + " " + self.kozi + " Double: " + str(self.doubleFlag) + " Redouble: " + str(self.reDoubleFlag) + " Playing: " + str(self.turn))
            self.destroy()
        elif self.passcounter==4:
            print("Kozi:" + str(self.bid) + " " + self.kozi + " Double: " + str(self.doubleFlag) + " Redouble: " + str(self.reDoubleFlag) + " Playing: " + str(self.turn))
            self.destroy()
        elif self.reDoubleFlag==True:
            print("Kozi:" + str(self.bid) + " " + self.kozi + " Double: " + str(self.doubleFlag) + " Redouble: " + str(self.reDoubleFlag) + " Playing: " + str(self.turn))
            self.destroy()
    def setTurn(self):
        self.turn=random.choice([0,1,2,3])
        temparr=[]
        for i in range(0,len(self.InputLabelsArr)):
            if i<self.turn:
                self.InputLabelsArr[i].set("-")
            else:
                temparr.append(self.InputLabelsArr[i])
        del self.InputLabelsArr
        self.InputLabelsArr=[]
        for i in temparr:
            self.InputLabelsArr.append(i)
    def btnclub(self):
        self.passcounter=0
        self.selected=self.dropDownInitial.get()
        self.selected=int(self.selected)
        self.kozi="Clubs"
        self.bid=int(self.selected)*10
        self.InputLabelsArr[0].set(str(self.selected)+" "+ self.club_icon)
        #update list of labelinputs
        temparr=[]
        for i in range(1,len(self.InputLabelsArr)):
            temparr.append(self.InputLabelsArr[i])
        del self.InputLabelsArr
        self.InputLabelsArr=[]
        for i in temparr:
            self.InputLabelsArr.append(i)
        #update dropdown
        temp=[]
        for i in self.dropDownValues:
            if int(i)<=self.selected:
                temp.append(i)
        for i in temp:
            self.dropDownValues.remove(i)
        print("kozi: "+ str(self.bid)+" "+self.kozi)
        self.dropDown.destroy()
        if int(self.selected)!=self.top_bid:
            self.dropDownInitial.set(self.dropDownValues[0])
            self.dropDown=OptionMenu(self.top,self.dropDownInitial,*self.dropDownValues)
            self.dropDown.place(x=213,y=190)
    def btndiamond(self):
        self.passcounter=0
        self.selected=self.dropDownInitial.get()
        self.selected=int(self.selected)
        self.kozi="Diamonds"
        self.bid=int(self.selected)*10
        self.InputLabelsArr[0].set(str(self.selected)+" "+ self.diamond_icon)
        #update list of labelinputs
        temparr=[]
        for i in range(1,len(self.InputLabelsArr)):
            temparr.append(self.InputLabelsArr[i])
        del self.InputLabelsArr
        self.InputLabelsArr=[]
        for i in temparr:
            self.InputLabelsArr.append(i)
        #update dropdown
        temp=[]
        for i in self.dropDownValues:
            if int(i)<=self.selected:
                temp.append(i)
        for i in temp:
            self.dropDownValues.remove(i)
        print("kozi: "+ str(self.bid)+" "+self.kozi)
        self.dropDown.destroy()
        if int(self.selected)!=self.top_bid:
            self.dropDownInitial.set(self.dropDownValues[0])
            self.dropDown=OptionMenu(self.top,self.dropDownInitial,*self.dropDownValues)
            self.dropDown.place(x=213,y=190)
    def btnspade(self):
        self.passcounter=0
        self.selected=self.dropDownInitial.get()
        self.selected=int(self.selected)
        self.kozi="Spades"
        self.bid=int(self.selected)*10
        self.InputLabelsArr[0].set(str(self.selected)+" "+ self.spade_icon)
        #update list of labelinputs
        temparr=[]
        for i in range(1,len(self.InputLabelsArr)):
            temparr.append(self.InputLabelsArr[i])
        del self.InputLabelsArr
        self.InputLabelsArr=[]
        for i in temparr:
            self.InputLabelsArr.append(i)
        #update dropdown
        temp=[]
        for i in self.dropDownValues:
            if int(i)<=self.selected:
                temp.append(i)
        for i in temp:
            self.dropDownValues.remove(i)
        print("kozi: "+ str(self.bid)+" "+self.kozi)
        self.dropDown.destroy()
        if int(self.selected)!=self.top_bid:
            self.dropDownInitial.set(self.dropDownValues[0])
            self.dropDown=OptionMenu(self.top,self.dropDownInitial,*self.dropDownValues)
            self.dropDown.place(x=213,y=190)
    def btnhearts(self):
        self.passcounter=0
        self.selected=self.dropDownInitial.get()
        self.selected=int(self.selected)
        self.kozi="Hearts"
        self.bid=int(self.selected)*10
        self.InputLabelsArr[0].set(str(self.selected)+" "+ self.heart_icon)
        #update list of labelinputs
        temparr=[]
        for i in range(1,len(self.InputLabelsArr)):
            temparr.append(self.InputLabelsArr[i])
        del self.InputLabelsArr
        self.InputLabelsArr=[]
        for i in temparr:
            self.InputLabelsArr.append(i)
        #update dropdown
        temp=[]
        for i in self.dropDownValues:
            if int(i)<=self.selected:
                temp.append(i)
        for i in temp:
            self.dropDownValues.remove(i)
        print("kozi: "+ str(self.bid)+" "+self.kozi)
        self.dropDown.destroy()
        if int(self.selected)!=self.top_bid:
            self.dropDownInitial.set(self.dropDownValues[0])
            self.dropDown=OptionMenu(self.top,self.dropDownInitial,*self.dropDownValues)
            self.dropDown.place(x=213,y=190)
    def btnPass(self):
        self.passcounter=self.passcounter+1
        self.InputLabelsArr[0].set("Pass")
        #update list of labelinputs
        temparr=[]
        for i in range(1,len(self.InputLabelsArr)):
            temparr.append(self.InputLabelsArr[i])
        del self.InputLabelsArr
        self.InputLabelsArr=[]
        for i in temparr:
            self.InputLabelsArr.append(i)
        self.stopBiding()
    def btnDouble(self):
        self.doubleFlag=True
        self.passcounter=0
        self.InputLabelsArr[0].set("Double")
        #update list of labelinputs
        temparr=[]
        for i in range(1,len(self.InputLabelsArr)):
            temparr.append(self.InputLabelsArr[i])
        del self.InputLabelsArr
        self.InputLabelsArr=[]
        for i in temparr:
            self.InputLabelsArr.append(i)
        self.club_button.destroy()
        self.diamond_button.destroy()
        self.spade_button.destroy()
        self.heart_button.destroy()
        self.dropDown.destroy()
        self.double_button.destroy()
    def btnRedouble(self):
        self.reDoubleFlag=True
        self.InputLabelsArr[0].set("Redouble")
        #update list of labelinputs
        temparr=[]
        for i in range(1,len(self.InputLabelsArr)):
            temparr.append(self.InputLabelsArr[i])
        del self.InputLabelsArr
        self.InputLabelsArr=[]
        for i in temparr:
            self.InputLabelsArr.append(i)
        time.sleep(3)
        self.stopBiding()
    def setOnTop(self,width,height):
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        self.top.geometry('%dx%d+%d+%d' % (width, height, x, y))
        self.top.lift(aboveThis=root)
        self.top.attributes("-topmost",1)
        self.top.focus_set()
        #self.top.grab_set()
    def setLabels(self):
        #labels
        self.lblplayer1=Label(self.top,text="  Player1  ",fg=self.lblheadfgcolor,bg=self.lblheadbgcolor,relief=GROOVE,font=self.lblheadfont)
        self.lblplayer1.place(x=1,y=0,width=100,height=30)
        self.lblplayer2=Label(self.top,text="  Player2  ",fg=self.lblheadfgcolor,bg=self.lblheadbgcolor,relief=GROOVE,font=self.lblheadfont)
        self.lblplayer2.place(x=101,y=0,width=100,height=30)
        self.lblplayer3=Label(self.top,text="  Player3  ",fg=self.lblheadfgcolor,bg=self.lblheadbgcolor,relief=GROOVE,font=self.lblheadfont)
        self.lblplayer3.place(x=201,y=0,width=100,height=30)
        self.lblplayer4=Label(self.top,text="  Player4  ",fg=self.lblheadfgcolor,bg=self.lblheadbgcolor,relief=GROOVE,font=self.lblheadfont)
        self.lblplayer4.place(x=301,y=0,width=100,height=30)
    def setButton(self):
        #buttons
        self.club_img=PhotoImage(file="./Suit/clubs.gif")
        self.club_img= self.club_img.subsample(3, 3)
        self.club_button=Button(self.top,image=self.club_img,width=30,height=30,command=self.btnclub)
        self.club_button.place(x=10,y=200)
        self.diamond_img=PhotoImage(file="./Suit/diamonds.gif")
        self.diamond_img= self.diamond_img.subsample(3, 3)
        self.diamond_button=Button(self.top,image=self.diamond_img,width=30,height=30,command=self.btndiamond)
        self.diamond_button.place(x=60,y=200)
        self.spades_img=PhotoImage(file="./Suit/spades.gif")
        self.spades_img= self.spades_img.subsample(3, 3)
        self.spade_button=Button(self.top,image=self.spades_img,width=30,height=30,command=self.btnspade)
        self.spade_button.place(x=110,y=200)
        self.heart_img=PhotoImage(file="./Suit/hearts.gif")
        self.heart_img= self.heart_img.subsample(3, 3)
        self.heart_button=Button(self.top,image=self.heart_img,width=30,height=30,command=self.btnhearts)
        self.heart_button.place(x=160,y=200)
        self.dropDown=OptionMenu(self.top,self.dropDownInitial,*self.dropDownValues)
        self.dropDown.place(x=213,y=190)
        self.pass_button=Button(self.top,text="PASS",font=("Times","12","bold"),width=4,height=1,command=self.btnPass)
        self.pass_button.place(x=223,y=225)
        self.double_button=Button(self.top,text="DOUBLE",font=("Times","12","bold"),width=11,height=1,command=self.btnDouble)
        self.double_button.place(x=300,y=190)
        self.redouble_button=Button(self.top,text="REDOUBLE",font=("Times","12","bold"),width=11,height=1,command=self.btnRedouble)
        self.redouble_button.place(x=300,y=220)
    def setInputLabels(self):
        #array that contains all the StringVars
        self.InputLabelsArr=[]
        #unicode sympols
        self.spade_icon='WHITE SPADE SUIT'
        self.spade_icon=unicodedata.lookup(self.spade_icon)
        self.heart_icon='WHITE HEART SUIT'
        self.heart_icon=unicodedata.lookup(self.heart_icon)
        self.club_icon='WHITE CLUB SUIT'
        self.club_icon=unicodedata.lookup(self.club_icon)
        self.diamond_icon='WHITE DIAMOND SUIT'
        self.diamond_icon=unicodedata.lookup(self.diamond_icon)
        #row 1
        self.lbl0player1text=StringVar()
        self.InputLabelsArr.append(self.lbl0player1text)
        self.lbl0player1=Label(self.top,textvariable=self.lbl0player1text,fg=self.lblbodyfgcolor,bg=self.lblbodybgcolor,relief=GROOVE,font=self.lblbodyfont)
        self.lbl0player1.place(x=1,y=30,width=100,height=25)
        self.lbl0player2text=StringVar()
        self.InputLabelsArr.append(self.lbl0player2text)
        self.lbl0player2=Label(self.top,textvariable=self.lbl0player2text,fg=self.lblbodyfgcolor,bg=self.lblbodybgcolor,relief=GROOVE,font=self.lblbodyfont)
        self.lbl0player2.place(x=101,y=30,width=100,height=25)
        self.lbl0player3text=StringVar()
        self.InputLabelsArr.append(self.lbl0player3text)
        self.lbl0player3=Label(self.top,textvariable=self.lbl0player3text,fg=self.lblbodyfgcolor,bg=self.lblbodybgcolor,relief=GROOVE,font=self.lblbodyfont)
        self.lbl0player3.place(x=201,y=30,width=100,height=25)
        self.lbl0player4text=StringVar()
        self.InputLabelsArr.append(self.lbl0player4text)
        self.lbl0player4=Label(self.top,textvariable=self.lbl0player4text,fg=self.lblbodyfgcolor,bg=self.lblbodybgcolor,relief=GROOVE,font=self.lblbodyfont)
        self.lbl0player4.place(x=301,y=30,width=100,height=25)
        #row 2
        self.lbl1player1text=StringVar()
        self.InputLabelsArr.append(self.lbl1player1text)
        self.lbl1player1=Label(self.top,textvariable=self.lbl1player1text,fg=self.lblbodyfgcolor,bg=self.lblbodybgcolor,relief=GROOVE,font=self.lblbodyfont)
        self.lbl1player1.place(x=1,y=55,width=100,height=25)
        self.lbl1player2text=StringVar()
        self.InputLabelsArr.append(self.lbl1player2text)
        self.lbl1player2=Label(self.top,textvariable=self.lbl1player2text,fg=self.lblbodyfgcolor,bg=self.lblbodybgcolor,relief=GROOVE,font=self.lblbodyfont)
        self.lbl1player2.place(x=101,y=55,width=100,height=25)
        self.lbl1player3text=StringVar()
        self.InputLabelsArr.append(self.lbl1player3text)
        self.lbl1player3=Label(self.top,textvariable=self.lbl1player3text,fg=self.lblbodyfgcolor,bg=self.lblbodybgcolor,relief=GROOVE,font=self.lblbodyfont)
        self.lbl1player3.place(x=201,y=55,width=100,height=25)
        self.lbl1player4text=StringVar()
        self.InputLabelsArr.append(self.lbl1player4text)
        self.lbl1player4=Label(self.top,textvariable=self.lbl1player4text,fg=self.lblbodyfgcolor,bg=self.lblbodybgcolor,relief=GROOVE,font=self.lblbodyfont)
        self.lbl1player4.place(x=301,y=55,width=100,height=25)
        #row 3
        self.lbl2player1text=StringVar()
        self.InputLabelsArr.append(self.lbl2player1text)
        self.lbl2player1=Label(self.top,textvariable=self.lbl2player1text,fg=self.lblbodyfgcolor,bg=self.lblbodybgcolor,relief=GROOVE,font=self.lblbodyfont)
        self.lbl2player1.place(x=1,y=80,width=100,height=25)
        self.lbl2player2text=StringVar()
        self.InputLabelsArr.append(self.lbl2player2text)
        self.lbl2player2=Label(self.top,textvariable=self.lbl2player2text,fg=self.lblbodyfgcolor,bg=self.lblbodybgcolor,relief=GROOVE,font=self.lblbodyfont)
        self.lbl2player2.place(x=101,y=80,width=100,height=25)
        self.lbl2player3text=StringVar()
        self.InputLabelsArr.append(self.lbl2player3text)
        self.lbl2player3=Label(self.top,textvariable=self.lbl2player3text,fg=self.lblbodyfgcolor,bg=self.lblbodybgcolor,relief=GROOVE,font=self.lblbodyfont)
        self.lbl2player3.place(x=201,y=80,width=100,height=25)
        self.lbl2player4text=StringVar()
        self.InputLabelsArr.append(self.lbl2player4text)
        self.lbl2player4=Label(self.top,textvariable=self.lbl2player4text,fg=self.lblbodyfgcolor,bg=self.lblbodybgcolor,relief=GROOVE,font=self.lblbodyfont)
        self.lbl2player4.place(x=301,y=80,width=100,height=25)
        #row 4
        self.lbl3player1text=StringVar()
        self.InputLabelsArr.append(self.lbl3player1text)
        self.lbl3player1=Label(self.top,textvariable=self.lbl3player1text,fg=self.lblbodyfgcolor,bg=self.lblbodybgcolor,relief=GROOVE,font=self.lblbodyfont)
        self.lbl3player1.place(x=1,y=105,width=100,height=25)
        self.lbl3player2text=StringVar()
        self.InputLabelsArr.append(self.lbl3player2text)
        self.lbl3player2=Label(self.top,textvariable=self.lbl3player2text,fg=self.lblbodyfgcolor,bg=self.lblbodybgcolor,relief=GROOVE,font=self.lblbodyfont)
        self.lbl3player2.place(x=101,y=105,width=100,height=25)
        self.lbl3player3text=StringVar()
        self.InputLabelsArr.append(self.lbl3player3text)
        self.lbl3player3=Label(self.top,textvariable=self.lbl3player3text,fg=self.lblbodyfgcolor,bg=self.lblbodybgcolor,relief=GROOVE,font=self.lblbodyfont)
        self.lbl3player3.place(x=201,y=105,width=100,height=25)
        self.lbl3player4text=StringVar()
        self.InputLabelsArr.append(self.lbl3player4text)
        self.lbl3player4=Label(self.top,textvariable=self.lbl3player4text,fg=self.lblbodyfgcolor,bg=self.lblbodybgcolor,relief=GROOVE,font=self.lblbodyfont)
        self.lbl3player4.place(x=301,y=105,width=100,height=25)
        #row 5
        self.lbl4player1text=StringVar()
        self.InputLabelsArr.append(self.lbl4player1text)
        self.lbl4player1=Label(self.top,textvariable=self.lbl4player1text,fg=self.lblbodyfgcolor,bg=self.lblbodybgcolor,relief=GROOVE,font=self.lblbodyfont)
        self.lbl4player1.place(x=1,y=130,width=100,height=25)
        self.lbl4player2text=StringVar()
        self.InputLabelsArr.append(self.lbl4player2text)
        self.lbl4player2=Label(self.top,textvariable=self.lbl4player2text,fg=self.lblbodyfgcolor,bg=self.lblbodybgcolor,relief=GROOVE,font=self.lblbodyfont)
        self.lbl4player2.place(x=101,y=130,width=100,height=25)
        self.lbl4player3text=StringVar()
        self.InputLabelsArr.append(self.lbl4player3text)
        self.lbl4player3=Label(self.top,textvariable=self.lbl4player3text,fg=self.lblbodyfgcolor,bg=self.lblbodybgcolor,relief=GROOVE,font=self.lblbodyfont)
        self.lbl4player3.place(x=201,y=130,width=100,height=25)
        self.lbl4player4text=StringVar()
        self.InputLabelsArr.append(self.lbl4player4text)
        self.lbl4player4=Label(self.top,textvariable=self.lbl4player4text,fg=self.lblbodyfgcolor,bg=self.lblbodybgcolor,relief=GROOVE,font=self.lblbodyfont)
        self.lbl4player4.place(x=301,y=130,width=100,height=25)
        #row 6
        self.lbl5player1text=StringVar()
        self.InputLabelsArr.append(self.lbl5player1text)
        self.lbl5player1=Label(self.top,textvariable=self.lbl5player1text,fg=self.lblbodyfgcolor,bg=self.lblbodybgcolor,relief=GROOVE,font=self.lblbodyfont)
        self.lbl5player1.place(x=1,y=155,width=100,height=25)
        self.lbl5player2text=StringVar()
        self.InputLabelsArr.append(self.lbl5player2text)
        self.lbl5player2=Label(self.top,textvariable=self.lbl5player2text,fg=self.lblbodyfgcolor,bg=self.lblbodybgcolor,relief=GROOVE,font=self.lblbodyfont)
        self.lbl5player2.place(x=101,y=155,width=100,height=25)
        self.lbl5player3text=StringVar()
        self.InputLabelsArr.append(self.lbl5player3text)
        self.lbl5player3=Label(self.top,textvariable=self.lbl5player3text,fg=self.lblbodyfgcolor,bg=self.lblbodybgcolor,relief=GROOVE,font=self.lblbodyfont)
        self.lbl5player3.place(x=201,y=155,width=100,height=25)
        self.lbl5player4text=StringVar()
        self.InputLabelsArr.append(self.lbl5player4text)
        self.lbl5player4=Label(self.top,textvariable=self.lbl5player4text,fg=self.lblbodyfgcolor,bg=self.lblbodybgcolor,relief=GROOVE,font=self.lblbodyfont)
        self.lbl5player4.place(x=301,y=155,width=100,height=25)

def window_Location(width, height):
    # get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

def share_cards():
    global deck,player1,player2,player3,player4
    deck.shuffle()
    arrcard=deck.getDeck()
    for i in range(0,32):
        if i>=0 and i<=7:
            player1.setCard(arrcard[i])
        elif i>=8 and i<=15:
            player2.setCard(arrcard[i])
        elif i>=16 and i<=23:
            player3.setCard(arrcard[i])
        elif i>=24 and i<=32:
            player4.setCard(arrcard[i])
    print("Player1")
    for i in range(0,8):
        print(player1.cards[i].getCard())
    print("Player2")
    for i in range(0,8):
        print(player2.cards[i].getCard())
    print("Player3")
    for i in range(0,8):
        print(player3.cards[i].getCard())
    print("Player4")
    for i in range(0,8):
        print(player4.cards[i].getCard())

def changeKoziaPoints(player1,player2,player3,player4,kozia):
    for i in player1.cards:
        if i.suit==kozia:
            if i.rank=="9":
                i.points=14
            elif i.rank=="J":
                i.points=20
    for i in player2.cards:
        if i.suit==kozia:
            if i.rank=="9":
                i.points=14
            elif i.rank=="J":
                i.points=20
    for i in player3.cards:
        if i.suit==kozia:
            if i.rank=="9":
                i.points=14
            elif i.rank=="J":
                i.points=20
    for i in player4.cards:
        if i.suit==kozia:
            if i.rank=="9":
                i.points=14
            elif i.rank=="J":
                i.points=20
#initialize root 
root=Tk()
window_Location(window_Height,window_Width)
root.title("Pillota Application")
root.resizable(0,0)
root.lift()
root.attributes("-topmost",1) #possition of the window

#initializing canvas
canvas=Canvas(root,width=window_Height,height=window_Width,bd=0,highlightthickness=0)
canvas.config(bg=window_Color)
canvas.pack()

#back side cards
back_side=PhotoImage(file="./Deck_Images/back_side.gif")
back_side= back_side.zoom(2,2)
back_side_R=PhotoImage(file="./Deck_Images_R/back_side.gif")
back_side_R= back_side_R.zoom(2,2)

#global variables
dataArr={}

#main
deck=Deck()
player1=Player1(canvas)
player2=Player2(canvas)
player3=Player3(canvas)
player4=Player4(canvas)
share_cards()
player1.displayCards()
speakwindow=PopupWindow(root)
print(dataArr)
changeKoziaPoints(player1,player2,player3,player4,dataArr["kozi"])
#root.mainloop()
    