class ATM(object):
   def __init__(self,card,cardNumber,pinNumber):
       self.money=card.money
       self.cardNumber=cardNumber
       self.pinNumber=pinNumber
       self.letUser=(card.cardNumber==self.cardNumber and card.pinNumber==self.pinNumber)

       if not self.letUser:
           print('wrong number or pin')
       
       self.update=False
       while self.update:
          card.money=self.money


   def checkBalance(self):
        if self.letUser:
            print(self.money)
            self.update=True
        elif not self.letUser:
            print('please enter the correct number or pin')    
    
   def withDraw(self, amount):
        if self.letUser:
            if(self.money >= amount):
                newAmount = self.money-amount
                self.money = newAmount
                print('your remaining balance is {0}'.format(self.money))
            else:
                print('not enough money')

        elif not self.letUser:
            print('please enter the correct number or pin')       

   def getBalance(self):
        if self.letUser:
            return self.money
        elif not self.letUser:
            print('please enter the correct number or pin')           

    