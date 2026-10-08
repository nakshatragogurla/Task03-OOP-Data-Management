# Inventory Management Engine

A Python-based object-oriented inventory management system demonstrating
inheritance, encapsulation, polymorphism, custom exception handling,
JSON/CSV data persistence, and unit testing.

## Features

- Object-oriented product management
- Inheritance using product subclasses
- Encapsulation using private attributes and properties
- Polymorphism using category and value calculation methods
- Custom exception handling
- JSON data persistence
- CSV data persistence
- Inventory value calculation
- Product addition, removal, searching, and quantity updates
- Unit testing using pytest
- 96% test coverage

## Project Structure

```text
Task03-OOP-Data-Management/
│
├── data/
│   ├── inventory.json
│   └── inventory.csv
│
├── inventory/
│   ├── __init__.py
│   ├── models.py
│   ├── exceptions.py
│   ├── manager.py
│   └── storage.py
│
├── tests/
│   ├── __init__.py
│   ├── test_models.py
│   ├── test_manager.py
│   └── test_storage.py
│
├── main.py
├── requirements.txt
└── README.md