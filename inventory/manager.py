from .models import Product
from .exceptions import (
    InvalidProductError,
    ProductNotFoundError,
    DuplicateProductError,
)


class InventoryManager:
    """Manages products in the inventory."""

    def __init__(self):
        self.__products = {}

    def add_product(self, product):
        """Add a product to the inventory."""
        if not isinstance(product, Product):
            raise InvalidProductError("Only Product objects can be added.")

        if product.product_id in self.__products:
            raise DuplicateProductError(
                f"Product ID '{product.product_id}' already exists."
            )

        self.__products[product.product_id] = product

    def remove_product(self, product_id):
        """Remove a product from the inventory."""
        if product_id not in self.__products:
            raise ProductNotFoundError(
                f"Product ID '{product_id}' was not found."
            )

        del self.__products[product_id]

    def get_product(self, product_id):
        """Return a product using its ID."""
        if product_id not in self.__products:
            raise ProductNotFoundError(
                f"Product ID '{product_id}' was not found."
            )

        return self.__products[product_id]

    def update_quantity(self, product_id, quantity):
        """Update the quantity of a product."""
        product = self.get_product(product_id)

        if quantity < 0:
            raise InvalidProductError(
                "Product quantity cannot be negative."
            )

        product.quantity = quantity

    def get_all_products(self):
        """Return all products."""
        return list(self.__products.values())

    def get_total_inventory_value(self):
        """Calculate the total value of all products."""
        return sum(
            product.calculate_value()
            for product in self.__products.values()
        )

    def get_product_count(self):
        """Return the number of products."""
        return len(self.__products)