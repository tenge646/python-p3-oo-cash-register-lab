#!/usr/bin/env python3

# CashRegister class implementation

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        if quantity > 1:
            self.items.append((title, price, quantity))
        else:
            self.items.append((title, price))

    def apply_discount(self):
     if self.discount > 0:
        discount_amount = self.total * (self.discount / 100)
        self.total -= discount_amount
        print(f"After the discount, the total comes to ${self.total:.2f}.")
     else:
        print("There is no discount to apply.")




    def void_last_transaction(self):
        if self.items:
            last_item = self.items.pop()
            if len(last_item) > 2:
                self.total -= last_item[1] * last_item[2]
            else:
                self.total -= last_item[1]
