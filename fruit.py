def main():
    # Create and print a list named fruit.
      
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")

    fruit_list.reverse()
    fruit_list

    print(f"reversed: {fruit_list}")

    fruit_list.append("orange")
    print(f"append orange: {fruit_list}")

    apple_index = fruit_list.index("apple")
    fruit_list.insert(apple_index, "cherry")
    print(f"insert cherry: {fruit_list}")

    remove_fruit = fruit_list.pop()
    print(f"pop {remove_fruit}: {fruit_list}")

    fruit_list.sort()
    print(f"sorted: {fruit_list}")

    fruit_list.clear()
    print(f"cleared: {fruit_list}")

   

main()