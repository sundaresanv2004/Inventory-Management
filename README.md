# Inventory-Management

Inventory management for a grocery shop involves overseeing and controlling the stock of products, ensuring they are adequately stocked, fresh, and readily available to meet customer demands.

## Grocery Shop Inventory Management

Welcome to the Grocery Shop Inventory Management system. This project allows you to efficiently manage your grocery shop's inventory. The system consists of a frontend built using FlatLib in Python and a backend using MySQL.

![Product Output](https://github.com/sundaresanv2004/Inventory-Management/blob/main/Main/assets/product1.jpg)

### Installation

To install the required libraries, follow these steps:

1. Clone this repository to your local machine:
   ```sh
   git clone https://github.com/yourusername/inventory-management.git
   cd inventory-management
   ```
   ```
   pip install -r requirements.txt
   ```

### Prerequisites

Before you get started, make sure you have the following prerequisites installed on your system:

- **MySQL**: You need to have MySQL installed on your system. If you don't have it, please download and install it from [MySQL's official website](https://dev.mysql.com/downloads/).

### Configuration

To configure the MySQL connection, follow these steps:


1. Open the `Main/service/connection/mysql_connection.py` file in your code editor.

2. Locate the following lines and change the database connection details to match your MySQL configuration:

```
password = ""
```

Enter your MySQL password there.

### Usage

To launch the application, run `main.py`:

```bash
python main.py
```

### License
Inventory-Management is licensed under the **MIT License**.

