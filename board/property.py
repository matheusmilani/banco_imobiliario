import random


class Property():
    """Initialize the property"""
    def __init__(self, min_sell_value, max_sell_value, percentage_rent_value):
        self.sell_value = random.randint(min_sell_value, max_sell_value)
        self.rent_value = self.sell_value * percentage_rent_value
        self.buyed = False
        self.owner = None

    def buy(self, new_owner):
        """Set the owner of a property"""
        self.buyed = True
        self.owner = new_owner
        return self

    def pay_rent(self, tenant):
        """Set a rent for propeorty"""
        self.owner.balance += self.rent_value
        tenant.balance -= self.rent_value
        return self

    def return_to_board(self):
        """Reset the property"""
        self.buyed = False
        self.owner = None
        return self
