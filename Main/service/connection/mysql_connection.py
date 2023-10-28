import mysql.connector
import pandas as pd
from sqlalchemy import create_engine

password = ''

def database_checker():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password=password,
    )
    my_cursor = mydb.cursor()
    con = create_engine(f"mysql+mysqlconnector://root:{password}@localhost")
    df = pd.read_sql_query('show databases;', con=con)
    list1 = [str(i[0]) for i in df.values.tolist()]

    if 'inventory_management' not in list1:
        my_cursor.execute("CREATE DATABASE inventory_management;")
        mydb = mysql.connector.connect(host="localhost", user="root", password=password, database='inventory_management')
        my_cursor = mydb.cursor()
        my_cursor.execute("CREATE TABLE products(product_id INT PRIMARY KEY AUTO_INCREMENT,category VARCHAR(25) NOT NULL, name VARCHAR(255), quantity INT NOT NULL,price DECIMAL(10, 2) NOT NULL, image VARCHAR(25));")
        #  my_cursor.execute("CREATE TABLE customers(customer_id INT PRIMARY KEY AUTO_INCREMENT,name VARCHAR(255) NOT NULL,phone_number VARCHAR(20));")
        my_cursor.execute("CREATE TABLE sales(sales_id INT PRIMARY KEY AUTO_INCREMENT, product_id INT NOT NULL,order_date DATETIME NOT NULL, total_amount DECIMAL(10, 2) NOT NULL, FOREIGN KEY (product_id) REFERENCES products(product_id));")


def display_product():
    con = create_engine(f"mysql+mysqlconnector://root:{password}@localhost/inventory_management")
    df = pd.read_sql_query('SELECT * FROM products;', con=con)
    return df


def display_sales():
    con = create_engine(f"mysql+mysqlconnector://root:{password}@localhost/inventory_management")
    df = pd.read_sql_query('SELECT * FROM sales;', con=con)
    return df


def add_product(data):
    mydb = mysql.connector.connect(host="localhost", user="root", password=password, database='inventory_management')
    my_cursor = mydb.cursor()
    sql = "INSERT INTO products (category, name, quantity, price, image) VALUES (%s, %s, %s, %s, %s)"
    val = (data[0], data[1], data[2], data[3], data[4])
    my_cursor.execute(sql, val)
    mydb.commit()


def edit_product(data):
    mydb = mysql.connector.connect(host="localhost", user="root", password=password, database='inventory_management')
    my_cursor = mydb.cursor()

    sql = "UPDATE products SET quantity = %s, price=%s WHERE product_id=%s"
    val = (data[1], data[2], data[0])
    my_cursor.execute(sql, val)

    mydb.commit()


def delete_product(data):
    mydb = mysql.connector.connect(host="localhost", user="root", password=password, database='inventory_management')
    my_cursor = mydb.cursor()

    sql = f"DELETE FROM products WHERE product_id = {data}"
    my_cursor.execute(sql)
    mydb.commit()


def display_product_by_id(data):
    con = create_engine(f"mysql+mysqlconnector://root:{password}@localhost/inventory_management")
    df = pd.read_sql_query(f'SELECT * FROM products WHERE product_id = {data};', con=con)
    return df.values[0]


def display_product_by_category(data):
    con = create_engine(f"mysql+mysqlconnector://root:{password}@localhost/inventory_management")
    df = pd.read_sql_query(f'SELECT * FROM products WHERE category = "{data}";', con=con)
    return df


def display_product_by_name(data):
    con = create_engine(f"mysql+mysqlconnector://root:{password}@localhost/inventory_management")
    df = pd.read_sql_query(f'SELECT * FROM products WHERE name = "{data}";', con=con)
    return df


def save_sales(data):
    mydb = mysql.connector.connect(host="localhost", user="root", password=password, database='inventory_management')
    my_cursor = mydb.cursor()

    sql = "UPDATE products SET quantity = %s WHERE product_id=%s"
    val = (data[2], data[0])
    my_cursor.execute(sql, val)

    sql = "INSERT INTO sales (product_id, order_date, total_amount) VALUES (%s, now(), %s)"
    val = (data[0], data[1])
    my_cursor.execute(sql, val)
    mydb.commit()


