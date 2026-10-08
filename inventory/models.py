from abc import ABC, abstractmethod


class Product(ABC):
    """Base class for all products."""

    def __init__(self, product_id, name, price, quantity):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    @property
    def product_id(self):
        return self.__product_id

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError("Quantity cannot be negative.")
        self.__quantity = value

    @abstractmethod
    def get_category(self):
        """Return the category of the product."""
        pass

    @abstractmethod
    def calculate_value(self):
        """Calculate the total inventory value."""
        pass


class ElectronicProduct(Product):
    """Product class for electronic items."""

    def __init__(self, product_id, name, price, quantity, warranty_years):
        super().__init__(product_id, name, price, quantity)
        self.__warranty_years = warranty_years

    @property
    def warranty_years(self):
        return self.__warranty_years

    def get_category(self):
        return "Electronics"

    def calculate_value(self):
        return self.price * self.quantity


class GroceryProduct(Product):
    """Product class for grocery items."""

    def __init__(self, product_id, name, price, quantity, expiry_date):
        super().__init__(product_id, name, price, quantity)
        self.__expiry_date = expiry_date

    @property
    def expiry_date(self):
        return self.__expiry_date

    def get_category(self):
        return "Grocery"

    def calculate_value(self):
        return self.price * self.quantity