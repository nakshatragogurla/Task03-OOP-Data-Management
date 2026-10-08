from inventory.models import ElectronicProduct, GroceryProduct
from inventory.storage import InventoryStorage


def create_products():
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

    return [laptop, rice]


def test_save_and_load_json(tmp_path):
    products = create_products()

    file_path = tmp_path / "inventory.json"

    InventoryStorage.save_json(products, file_path)

    loaded_products = InventoryStorage.load_json(file_path)

    assert len(loaded_products) == 2
    assert loaded_products[0].product_id == "E001"
    assert loaded_products[0].name == "Laptop"
    assert loaded_products[0].quantity == 2
    assert loaded_products[0].warranty_years == 2

    assert loaded_products[1].product_id == "G001"
    assert loaded_products[1].name == "Rice"
    assert loaded_products[1].quantity == 10
    assert loaded_products[1].expiry_date == "2027-01-15"


def test_save_and_load_csv(tmp_path):
    products = create_products()

    file_path = tmp_path / "inventory.csv"

    InventoryStorage.save_csv(products, file_path)

    loaded_products = InventoryStorage.load_csv(file_path)

    assert len(loaded_products) == 2

    assert loaded_products[0].product_id == "E001"
    assert loaded_products[0].name == "Laptop"
    assert loaded_products[0].price == 50000
    assert loaded_products[0].quantity == 2

    assert loaded_products[1].product_id == "G001"
    assert loaded_products[1].name == "Rice"
    assert loaded_products[1].price == 60
    assert loaded_products[1].quantity == 10


def test_json_and_csv_contain_same_products(tmp_path):
    products = create_products()

    json_path = tmp_path / "inventory.json"
    csv_path = tmp_path / "inventory.csv"

    InventoryStorage.save_json(products, json_path)
    InventoryStorage.save_csv(products, csv_path)

    json_products = InventoryStorage.load_json(json_path)
    csv_products = InventoryStorage.load_csv(csv_path)

    assert len(json_products) == len(csv_products)

    for json_product, csv_product in zip(json_products, csv_products):
        assert json_product.product_id == csv_product.product_id
        assert json_product.name == csv_product.name
        assert json_product.quantity == csv_product.quantity