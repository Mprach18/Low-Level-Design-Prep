# SOLID Principles

## S - Single responsibility
This principle signifies the importance of having a single repsonisbility for a particular class. If a class has multiple responsibilities, then there is a possibility of introducing new bugs as any changes made to any of the functionality can affect the others.

[Example with explanation](SRP.py)

```Python

'''
Imagine we have an e-commerce application with a class named Product.
This class: 
- stores product information
- stores the product stock and handles management
- perform order processing
'''


class Product:
    def __init__(self, id, name, price, stock):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
        
    def __str__(self):
        print(f"Product ID: {self.id}, Name: {self.name}, Price: {self.price}")
        
    def check_stock(self, quantity):
        return self.stock >= quantity
    
    def process_order(self, quantity):
        if self.check_stock(quantity):
            self.stock -= quantity
            print(f"Order is processed for {quantity} units of {self.name}")
        else:
            print(f"Insufficient stock for {self.name}")
            
         
            
'''
This class violates the single responsibility principle as it handles multiple functionalities:
- storing product information
- storing the product stock and handles management
- performing order processing
In the future, whenever there are any changes for any of these functionalities, it would require us
to modify this class, leading to new bugs unknowingly.
'''



'''
To adhere to SRP, we can split this class into separate classes
'''

class SRP_product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price
        
    def __str__(self):
        print(f"Product ID: {self.id}, Name: {self.name}, Price: {self.price}")
    
class SRP_InventoryManager:
    def __init__(self, product, stock):
        self.product = product
        self.stock = stock
        
    def check_stock(self, quantity):
        return self.stock >= quantity
    
    def use_stock(self, quantity):
        self.stock -= quantity
        
class SRP_OrderProcessor:
    def __init__(self, product, inventory_manager):
        self.product = product
        self.inventory_manager = inventory_manager
        
    def process_order(self, quantity):
        if self.inventory_manager.check_stock(quantity):
            self.inventory_manager.use_stock(quantity)
            print(f"Order is processed for {quantity} units of {self.product.name}")
        else:
            print(f"Insufficient stock for {self.product.name}")
            
if __name__ == '__main__':
    product = SRP_product('1', 'watch', 30.49)
    inventory = SRP_InventoryManager(product, 20)
    order_processor = SRP_OrderProcessor(product, inventory)
    order_processor.process_order(5)

```

## O - Open-closed
Classes should be open for extension and closed for modification

```
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
    

```

#### References:
- https://blog.algomaster.io/p/solid-principles-explained-with-code
- github.com/mpotoczny/python_zadania


