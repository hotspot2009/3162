import pickle as pk

# Import processed datas from folder
infile = open("Stored Data/sample_hotel_info.pickle", "rb")
hotel_info = pk.load(infile)
infile.close()

infile = open("Stored Data/sample_aspect_info.pickle", "rb")
aspect_info = pk.load(infile)
infile.close()


def display_menu():
    print("============")
    print("Menu")
    print("[1] Search")
    print("[2] Exit")
    print("============")
    print("\n")


exit_program = False

while not exit_program:
    display_menu()
    command = input("Input a Numerical Value from the Menu: ")
    print("\n")

    if command == str("1"):
        search_term = (input("Type in a Search Term: ")).lower()
        if search_term in aspect_info:
            for hotel in aspect_info[search_term]:
                print("Score: {} => {}".format(hotel[0], hotel[1]))
            print("\n")

        else:
            print("Sorry. Not found in Database")
            print("\n")

    elif command == str("2"):
        exit_program = True
        print("Good Bye")
        print("\n")

    else:
        print("Read the Instructions Properly")
        print("\n")

