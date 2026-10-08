import pytest

from inventory.models import ElectronicProduct, GroceryProduct
from inventory.manager import InventoryManager
from inventory.exceptions import (
    InvalidProductError,
    ProductNotFoundError,
    DuplicateProductError,
)


def test_add_product():
    manager = InventoryManager()

    product = ElectronicProduct(
        "E001",
        "Laptop",
        50000,
        2,
        2
    )

    manager.add_product(product)

    assert manager.get_product("E001") == product
    assert manager.get_product_count() == 1


def test_add_multiple_products():
    manager = InventoryManager()

    laptop = ElectronicProduct(
        "E001",
        "Laptop",
        50000,
        2,
        2
    )

    rice = GroceryProduct(
        "G001",
        "Rice",
        60,
        10,
        "2027-01-15"
    )

    manager.add_product(laptop)
    manager.add_product(rice)

    assert manager.get_product_count() == 2
    assert manager.get_total_inventory_value() == 100600


def test_duplicate_product():
    manager = InventoryManager()

    product = ElectronicProduct(
        "E001",
        "Laptop",
        50000,
        2,
        2
    )

    manager.add_product(product)

    with pytest.raises(DuplicateProductError):
        manager.add_product(product)


def test_product_not_found():
    manager = InventoryManager()

    with pytest.raises(ProductNotFoundError):
        manager.get_product("E999")


def test_remove_product():
    manager = InventoryManager()

    product = ElectronicProduct(
        "E001",
        "Laptop",
        50000,
        2,
        2
    )

    manager.add_product(product)
    manager.remove_product("E001")

    assert manager.get_product_count() == 0

    with pytest.raises(ProductNotFoundError):
        manager.get_product("E001")


def test_update_quantity():
    manager = InventoryManager()

    product = GroceryProduct(
        "G001",
        "Rice",
        60,
        10,
        "2027-01-15"
    )

    manager.add_product(product)
    manager.update_quantity("G001", 20)

    assert manager.get_product("G001").quantity == 20


def test_invalid_product():
    manager = InventoryManager()

    with pytest.raises(InvalidProductError):
        manager.add_product("Not a product")


def test_negative_quantity_update():
    manager = InventoryManager()

    product = GroceryProduct(
        "G001",
        "Rice",
        60,
        10,
        "2027-01-15"
    )

    manager.add_product(product)

    with pytest.raises(InvalidProductError):
        manager.update_quantity("G001", -5)