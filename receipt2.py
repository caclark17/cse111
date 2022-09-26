import csv
import math
from datetime import datetime

print("Food King")

current_date_and_time = datetime.now(tz=None)

# Create an empty dictionary
all_products = {}

# Open the products.csv file and store into the all_products dictionary
with open("products.csv", "rt") as receipt_file:
    reader = csv.reader(receipt_file)

    # Skip the column headings 
    next(reader)

    # Read each row from csv file 
    for row in reader: 

        # For the current row get the product #, name, and price
        product_number = row[0]
        product_name = row[1]
        price = row[2]

        # Store data in all_products dictionary  
        all_products[product_number] = [product_name, price]

 # Read the request.csv file into a list
    with open("request.csv", "rt") as order:

        string = order.read()

    products_ordered = string.splitlines()
    #print(products_ordered)

    total_cost = 0

    for product_number in products_ordered:
        value = all_products[product_name]
        product_name = value[1]
        price = value[2]
        print(product_name, price)
        total_cost += price

    print(price)

    print("Thank you for shopping at Food King")
    print(f"{current_date_and_time: %A %I: %M %p}"
