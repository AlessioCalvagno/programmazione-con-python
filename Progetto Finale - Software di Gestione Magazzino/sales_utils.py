import csv
import os
from Product import *

_FILENAME = "sales.csv"
_HEADER_COLUMNS = ["sale","purchase"]

def file_init():
    """
    Initializes the csv file for sales, creating the file 
    (if it doesn't exist) and writing the header.
    """
    file_csv = open(_FILENAME,'a',newline='')
    writer = csv.DictWriter(file_csv,fieldnames=_HEADER_COLUMNS)
    if os.stat(_FILENAME).st_size == 0:
        writer.writeheader()
    file_csv.close()
    
    
def add(sale):
    """
    Insert a new sale into sales file.
    Input:
     - sale (list): The new sale to add.
       First element is total sale price (float), second element 
       is total purchase price (float).
    """
    file_csv = open(_FILENAME,'a',newline='')
    writer = csv.writer(file_csv)
    writer.writerow(sale)    
    
    file_csv.close()
    
    
def calculate_earnings():
    """
    This function computes and returns gross and net earnings from all sales.
    output:
    - earnings (list): first element is total gross earning (float), 
      second element is total net earning (float).
    """
    sale_total = 0.0
    purchase_total = 0.0
    
    file_csv = open(_FILENAME)
    reader = csv.DictReader(file_csv)
    
    for row in reader:
        sale_total += float(row["sale"])
        purchase_total += float(row["purchase"])
        
    file_csv.close()
    
    gross_total = sale_total
    net_total = gross_total - purchase_total
    earnings = [gross_total, net_total]
    return earnings
    
    
    
    

    
    
    
    