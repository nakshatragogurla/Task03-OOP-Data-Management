import pytest

from inventory.models import ElectronicProduct, GroceryProduct


def test_electronic_product():
    product = ElectronicProduct(
        "E001",
        "Laptop",
        50000,
        2,
        2
    )

    assert product.product_id == "E001"
    assert product.name == "Laptop"
    assert product.price == 50000
    assert product.quantity == 2
    assert product.warranty_years == 2
    assert product.get_category() == "Electronics"
    assert product.calculate_value() == 100000


def test_grocery_product():
    product = GroceryProduct(
        "G001",
        "Rice",
        60,
        10,
        "2027-01-15"
    )

    assert product.product_id == "G001"
    assert product.name == "Rice"
    assert product.quantity == 10
    assert product.expiry_date == "2027-01-15"
    assert product.get_category() == "Grocery"
    assert product.calculate_value() == 600


def test_quantity_update():
    product = ElectronicProduct(
        "E002",
        "Phone",
        20000,
        5,
        1
    )

    product.quantity = 10

    assert product.quantity == 10


def test_negative_quantity():
    product = ElectronicProduct(
        "E003",
        "Tablet",
        15000,
        2,
        1
    )

    with pytest.raises(ValueError):
        product.quantity = -1