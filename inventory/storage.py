import csv
import json

from .models import ElectronicProduct, GroceryProduct


class InventoryStorage:
    """Handles saving and loading inventory data."""

    @staticmethod
    def save_json(products, filename):
        """Save products to a JSON file."""
        data = []

        for product in products:
            product_data = {
                "product_id": product.product_id,
                "name": product.name,
                "price": product.price,
                "quantity": product.quantity,
                "category": product.get_category(),
            }

            if isinstance(product, ElectronicProduct):
                product_data["warranty_years"] = product.warranty_years

            elif isinstance(product, GroceryProduct):
                product_data["expiry_date"] = product.expiry_date

            data.append(product_data)

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def load_json(filename):
        """Load products from a JSON file."""
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        products = []

        for item in data:
            if item["category"] == "Electronics":
                product = ElectronicProduct(
                    item["product_id"],
                    item["name"],
                    item["price"],
                    item["quantity"],
                    item["warranty_years"],
                )

            elif item["category"] == "Grocery":
                product = GroceryProduct(
                    item["product_id"],
                    item["name"],
                    item["price"],
                    item["quantity"],
                    item["expiry_date"],
                )

            else:
                continue

            products.append(product)

        return products

    @staticmethod
    def save_csv(products, filename):
        """Save products to a CSV file."""
        fieldnames = [
            "product_id",
            "name",
            "price",
            "quantity",
            "category",
            "warranty_years",
            "expiry_date",
        ]

        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for product in products:
                row = {
                    "product_id": product.product_id,
                    "name": product.name,
                    "price": product.price,
                    "quantity": product.quantity,
                    "category": product.get_category(),
                    "warranty_years": "",
                    "expiry_date": "",
                }

                if isinstance(product, ElectronicProduct):
                    row["warranty_years"] = product.warranty_years

                elif isinstance(product, GroceryProduct):
                    row["expiry_date"] = product.expiry_date

                writer.writerow(row)

    @staticmethod
    def load_csv(filename):
        """Load products from a CSV file."""
        products = []

        with open(filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row["category"] == "Electronics":
                    product = ElectronicProduct(
                        row["product_id"],
                        row["name"],
                        float(row["price"]),
                        int(row["quantity"]),
                        int(row["warranty_years"]),
                    )

                elif row["category"] == "Grocery":
                    product = GroceryProduct(
                        row["product_id"],
                        row["name"],
                        float(row["price"]),
                        int(row["quantity"]),
                        row["expiry_date"],
                    )

                else:
                    continue

                products.append(product)

        return products