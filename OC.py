'''
Imagine we are building an e-commerce platform that allows users to pay
with different payment methods. For this, we have a PaymentProcessor class
that handles all payment logic.
'''

class PaymentProcessor:
    def __init__(self, order_amount):
        self.order_amount = order_amount
        
    def process_payment(self, card_number, cvv):
        print(f"Processing payment of ${self.order_amount} using credit or debit card")
        
    def check_payment_status(self):
        #logic
        return True
    
if __name__ == '__main__':
    order_amount = 100
    processor = PaymentProcessor(order_amount)
    processor.process_payment('1234567891234567', "123")
    if processor.check_payment_status():
        print(f"Payment Successful!")
    else:
        print("Payment Failed!")
        
        
'''
Now what if we want to add another payment method like Online payment with Paypal
then we would have to modify the PaymentProcessor class. Such changes can introduce bugs.
'''

'''
To introduce extensibility, we can use interfaces and polymorphism.
We can create an abstract base class with an abstract method for PaymentProcessor.
Then we can have concrete classes for specific payment methods(credit card, debit card, paypal, ..)
with their own logic implementation.
'''

from abc import ABC, abstractmethod

class OCPaymentProcessor(ABC):
        
    @abstractmethod
    def process_payment(self):
        return NotImplementedError
    
class CreditCardProcessor(OCPaymentProcessor):
    def __init__(self, order_amount, card_number, cvv):
        self.order_amount = order_amount
        self.card_number = card_number
        self.cvv = cvv
        
    def process_payment(self):
        print(f"Processing payment of ${self.order_amount} using credit card")
    
class PayPalProcessor(OCPaymentProcessor):
    def __init__(self, order_amount, email):
        self.order_amount = order_amount
        self.email = email
        
    def process_payment(self):
        print(f"Processing payment of ${self.order_amount} using Paypal with email: {self.email}")
    
