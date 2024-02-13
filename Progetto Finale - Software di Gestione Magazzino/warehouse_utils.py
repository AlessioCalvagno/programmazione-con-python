import csv
import os
from Product import *

_FILENAME = "warehouse.csv"
_HEADER_COLUMNS = ["name","sale_price","purchase_price","quantity"]

def file_init():
    """
    Initializes the csv file for warehouse, creating the file 
    (if it doesn't exist) and writing the header.
    """
    file_csv = open(_FILENAME,'a',newline='')
    writer = csv.DictWriter(file_csv,fieldnames=_HEADER_COLUMNS)
    if os.stat(_FILENAME).st_size == 0:
        writer.writeheader()
    file_csv.close()
    
def get_all():
    """
    Get all products from warehouse file.
    Output:
    - all_products_list (list): list of all Product instances found in 
      warehouse.
    """
    file_csv = open(_FILENAME)
    reader = csv.DictReader(file_csv)
    all_products_list = []
    
    for row in reader:
        product = Product(row["name"],
                          float(row["sale_price"]),
                          float(row["purchase_price"]),
                          int(row["quantity"]))
        all_products_list.append(product)
    
    file_csv.close()
    return all_products_list

def add(product):
    """
    Insert a new product into warehouse file.
    Input:
    - product (Product): The new item to add.
    """
    file_csv = open(_FILENAME,'a',newline='')
    writer = csv.DictWriter(file_csv,fieldnames=_HEADER_COLUMNS)
    writer.writerow(product.__dict__())    
    
    file_csv.close()
    
def get_item(name):
    """
    Get a single item from warehouse file, searching it by its name.
    If the product is found, the function returns a Product instance, 
    otherwise it returns None.
    Input:
    - name (str): name of the product to search.
    Output:
    - Product instance or None.
    """
    all_products = get_all()
    product_filter = filter(lambda p: p.get_name()==name,all_products)
    return next(product_filter,None)

def update_product_quantity(name,quantity_to_add):
    """
    Updates the product quantity in warehouse file.
    WARNING: This method doesn't check if the product is already in warehouse.
    Input:
    - name (str): product's name to be updated
    - quantity_to_add (int): product's quantity to add in warehouse.
      This parameter is negative if one needs to record a new sale.  
    """
    updated_rows = []
    file_csv_read = open(_FILENAME,'r')
    reader = csv.DictReader(file_csv_read)
    for row in reader:
        if row["name"] == name:
            product_quantity = int(row["quantity"])
            product_quantity += quantity_to_add
            row["quantity"] = str(product_quantity)
            
        updated_rows.append(row)
    
    file_csv_read.close()
    
    file_csv_write = open(_FILENAME,'w',newline='')
    writer = csv.DictWriter(file_csv_write,fieldnames=_HEADER_COLUMNS)
    writer.writeheader()
    writer.writerows(updated_rows)
    file_csv_write.close()
    
    
    
    
    
    
 