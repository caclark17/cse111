def main():
    provinces_list = read_provinces("provinces.txt")

    print(provinces_list)

    provinces_list.pop(0)

    print()

    print(provinces_list)

    print()

    provinces_list.pop()

    print(provinces_list)

    for i in range(len(provinces_list)):
        if provinces_list[i] == "AB":
            provinces_list[i] = "Alberta"
    
    print(provinces_list)

    count = provinces_list.count("Alberta")

    print()

    print(f"Alberta is the new list {count} times.")

def read_provinces(filename):

    provinces_list = []

    with open(filename, mode="rt") as text_file:
         for line in text_file:

            clean_line = line.strip()

            provinces_list.append(clean_line)


    return provinces_list

if __name__ == "__main__":
    main()