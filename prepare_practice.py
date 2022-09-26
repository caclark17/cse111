# Example 2

def main():
    # Create an empty list that will hold fabric names.
    fabrics = []

    # Add three elements at the end of the fabrics list.
    fabrics.append("velvet")
    fabrics.append("denim")
    fabrics.append("cotton")

    # Insert an element at the beginning of the fabrics list.
    fabrics.insert(0, "chiffon")
    print(fabrics)

    # Determine if gingham is in the fabrics list.
    if "gingham" in fabrics:
        print("Gingham is in the fabrics list")
    else:
        print("Gingham is not in the fabrics list")

    # Get the index where velvet is stored in the fabrics list.
    velvet_index = fabrics.index("velvet")

    # Replace velvet with taffeta.
    fabrics[velvet_index] = "taffeta"


    # Remove the last element from the fabrics list.
    fabrics.pop()


    # Remove denim from the fabrics list.
    fabrics.remove("denim")

    # Get the length of the fabrics list and print it.

    length_of_fabrics =  len(fabrics)
    print(f"The fabrics list has {length_of_fabrics} fabrics in it.")
    print(fabrics)
# Call main to start this program.
if __name__ == "__main__":
    main()