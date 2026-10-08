class InventoryError(Exception):
    """Base exception for inventory-related errors."""
    pass


class InvalidProductError(InventoryError):
    """Raised when product data is invalid."""
    pass


class ProductNotFoundError(InventoryError):
    """Raised when a requested product does not exist."""
    pass


class DuplicateProductError(InventoryError):
    """Raised when a product ID already exists."""
    pass