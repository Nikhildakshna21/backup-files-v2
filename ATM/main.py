from card import Card
from atm import ATM

def createATM(cardDetail):
    arr = []
    for c in cardDetail:
        arr.append(ATM(c[0],c[1],c[2]))
    return arr    

card = Card(49053,2002)
card1 = Card(63438,5671)

atm = createATM([[card,49053,2002],[card1,63438,5671]])

atm[0].withDraw(2000)
atm[1].withDraw(3000)

atm[0].checkBalance()
atm[1].checkBalance()

print('hi')