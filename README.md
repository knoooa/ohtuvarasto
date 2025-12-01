# ohtuvarasto

[![Build Status](https://github.com/knoooa/ohtuvarasto/actions/workflows/main.yml/badge.svg)](https://github.com/knoooa/ohtuvarasto/actions)
[![codecov](https://codecov.io/github/knoooa/ohtuvarasto/graph/badge.svg?token=F6OE9GD6VC)](https://codecov.io/github/knoooa/ohtuvarasto)

A warehouse management system with a web-based user interface for managing multiple inventories.

## Features

- **Inventory Management**: Create, rename, and delete inventories
- **Item Management**: Add and remove items from inventories
- **Real-time Updates**: Visual progress bars showing inventory capacity
- **Intuitive UI**: Modern, responsive web interface with modal dialogs
- **Multiple Inventories**: Manage multiple warehouses simultaneously

## Installation

1. Install dependencies using Poetry:
```bash
poetry install
```

## Running the Web Application

Start the web server:
```bash
cd src
poetry run python app.py
```

The application will be available at `http://localhost:5000`

## Running Tests

Run the test suite:
```bash
poetry run pytest src/tests/ -v
```

Run with coverage:
```bash
poetry run coverage run --branch -m pytest
poetry run coverage report
```

## Code Quality

Check code quality with pylint:
```bash
poetry run pylint src
```

## Usage

### Web Interface

1. **Create an Inventory**: Click "+ Create New Inventory" and enter a name and capacity
2. **Add Items**: Click "Add Items" on any inventory card and enter the amount
3. **Remove Items**: Click "Remove Items" and enter the amount to remove
4. **Rename**: Click "Rename" to change an inventory's name
5. **Delete**: Click "Delete" to remove an inventory (confirmation required)

### Programmatic Usage

The core `Varasto` class can also be used programmatically:

```python
from varasto import Varasto

# Create a warehouse with capacity 100
warehouse = Varasto(100.0)

# Add items
warehouse.lisaa_varastoon(50.0)

# Remove items
taken = warehouse.ota_varastosta(10.0)

# Check status
print(warehouse)  # Shows balance and available space
```
