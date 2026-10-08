from inventory.models import ElectronicProduct, GroceryProduct
from inventory.manager import InventoryManager
from inventory.storage import InventoryStorage


def main():
    inventory = InventoryManager()

    laptop = ElectronicProduct(
        "E001",
        "Laptop",
        55000,
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

    inventory.add_product(laptop)
    inventory.add_product(rice)

    print("=== INVENTORY ===")

    for product in inventory.get_all_products():
        print(
            f"ID: {product.product_id} | "
            f"Name: {product.name} | "
            f"Category: {product.get_category()} | "
            f"Quantity: {product.quantity} | "
            f"Value: ₹{product.calculate_value()}"
        )

    print("\nTotal Inventory Value:")
    print(f"₹{inventory.get_total_inventory_value()}")

    json_file = "data/inventory.json"
    csv_file = "data/inventory.csv"

    InventoryStorage.save_json(
        inventory.get_all_products(),
        json_file
    )

    InventoryStorage.save_csv(
        inventory.get_all_products(),
        csv_file
    )

    print("\nData saved successfully!")
    print(f"JSON: {json_file}")
    print(f"CSV: {csv_file}")


if __name__ == "__main__":
    main()