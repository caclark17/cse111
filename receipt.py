import csv
import math
from datetime import datetime

print("Food King")

current_date_and_time = datetime.now(tz=None)


def main():
    # Index of the product name column
    # in the products.csv file.
    try: 
        PRODUCT_NUM = 0

        # Read the contents of the products.csv into a
        # compound dictionary named products_dict. Use
        # the producrs numbers as the keys in the dictionary.
        products_dict = read_dict("products.csv", PRODUCT_NUM)

        print("All Products: ")

        # Print the products compound dictionary.
        print(products_dict)

        # Read the request.csv file into a list
        with open("request.csv", "rt") as order:

            string = order.read()

        products_ordered = string.splitlines()
        #print(products_ordered)

        total_cost = 0

        for product_number in products_ordered:
            value = products_dict[product_name]
            product_name = value[1]
            price = value[2]
            print(product_name, price)
            total_cost += price

        total_cost = price * .06
        print(f"Total amount due: {total_cost}")

        print("Thank you for shopping at Food King")
        #Print the current day of the week and current time
        print(f"{current_date_and_time: %A %I: %M %p}")

    except FileNotFoundError as file_error:
        print(file_error)

    except PermissionError as perm_error:
        print(perm_error)

    except KeyError as key_error:
        print(key_error)


def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    # Create an empty dictionary that will
    # store the data from the CSV file.
    all_products = {}

    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        # Skip the column headings of the csv file 
        next(reader)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:

            # If the current row is not blank, add the
            # data from the current to the dictionary.
            if len(row_list) != 0:

                # From the current row, retrieve the data
                # from the column that contains the key.
                key = row_list[key_column_index]

                # Store the data from the current
                # row into the dictionary.
                all_products[key] = row_list

    # Return the dictionary.
    return all_products





# Call main to start this program.
if __name__ == "__main__":
    main()
