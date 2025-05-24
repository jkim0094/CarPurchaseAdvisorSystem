# Car Purchase Advisor System

This project is a text-based Car Purchase Advisor System implemented in Python. It allows users to locate nearby car retailers, receive car recommendations, view available stock, and place orders. The system is designed using an object-oriented programming structure and is composed of four main classes.

---

## Key Features

### 1. Automatic Test Data Generation

* Upon launch, the program generates data for 12 cars and 3 car retailers.
* The generated data is stored in `stock.txt` and loaded into program memory.

### 2. Text-Based User Interface

Users are presented with the following menu options:

1. Find the nearest car retailer (based on postcode proximity)
2. Get car purchase advice and check stock

   * View all stock
   * Filter by car type (e.g., FWD, RWD, AWD)
   * View only probationary licence-permitted vehicles
3. Place a car order

   * Orders can only be placed during the retailer's business hours
   * Order details are saved in `order.txt`
4. Exit the application

---

## Class Overview

### Car

* Stores information such as car code, name, seating capacity, horsepower, weight, and drivetrain type.
* Determines whether a vehicle is prohibited for probationary licence holders (based on power-to-weight ratio).

### Retailer

* Manages retailer ID and name.
* Includes functionality for generating a unique 8-digit retailer ID.

### CarRetailer (Inherits from Retailer)

* Manages address, business hours, and stock of vehicles.
* Implements methods to add/remove stock, recommend a random car, filter cars, and handle orders.
* Updates are reflected in `stock.txt`.

### Order

* Generates unique order IDs using a specified algorithm.
* Creates and stores order records in `order.txt`.

---

## How to Run

1. Run `main.py` to initialize the system and generate test data.
2. Use the menu to navigate available options.
3. Order and inventory data will be automatically written to `stock.txt` and `order.txt`.

