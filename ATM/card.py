class Card(object):
    def __init__(self,cardNumber,securityPin):
        self.cardNumber=cardNumber
        self.pinNumber=securityPin
        self.money=5000

    def credit(self,amount):
        newAmount=self.money-amount
        self.money=newAmount
        print(newAmount)
    
    def debit(self,amount):
        newAmount=self.money+amount
        self.money=newAmount
        print(newAmount)