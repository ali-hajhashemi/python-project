dictionary = {}

# Add Keys File
with open("keys.txt") as f:
    keys = f.readlines()

#  Add Value File
with open("values.txt", encoding="utf-8") as f:
    values = f.readlines()

for index in range(len(values)):
    dictionary[keys[index].rstrip()] = values[index].rstrip()

print("Welcome To Haji Dictionary")
while True:
    order = input("\nHow Can I Help You Sir? (? - For Help)")

    if order == "?":
        print("A - For Add Verb", "\nR - For Remove Verb", "\nS - For Search Verb")
    elif order == "A":
        added_verb = input("Please Enter Your Verb Want To Add: ")
        # Add Verb To TXT File
        with open("addkeys.txt", "a") as f:
            f.write(added_verb)
        added_verb_meaning = input("Pleas Enter Your Meaning Of Verb: ")
        # Add Meaning To TXT File
        with open("addvalues.txt", "a") as f:
            f.write(added_verb_meaning)
        print(f"{added_verb} Successfully add to your dictionary")
    elif order == "R":
        remove_verb = input("Please Enter Your Verb Want To Remove: ")
        print(f"{remove_verb}Successfully removed of your dictionary")
    elif order == "S":
        search_verb = input("What are you looking for?")
        if search_verb in dictionary:
            print(dictionary[search_verb])
        else:
            print("\nYour Searched Verb Not Found")
            search_not = input("Do You Want To Add That To Your Dictionary? (y or n) ")
            # If Answer = y
            if search_not == "y":
                search_add_meaning = input("Pleas Enter Your Meaning Of Verb: ")
                # Add Verb To TXT File
                with open("addkeys.txt", "a") as f:
                    f.write(search_verb)
                # Add Meaning To TXT File
                with open("addvalues.txt", "a") as f:
                    f.write(search_add_meaning)
                print(f"{search_verb} Successfully added to dictionary")
            # If Answer = n
            else:
                print("All Right")
