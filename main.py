dictionary = {}

# Add Keys File
with open("keys.txt") as f:
    keys = f.readlines()

#  Add Value File
with open("values.txt", encoding="utf-8") as f:
    values = f.readlines()

for index in range(len(values)):
    dictionary[keys[index].rstrip()] = values[index].rstrip()

with open("addkeys.txt", "r") as f:
    added_keys = f.readlines()

with open("addvalues.txt", "r", encoding="utf-8") as f:
    added_values = f.readlines()

for index in range(len(added_values)):
    dictionary[added_keys[index].rstrip()] = added_values[index].rstrip()

print("Welcome To Haji Dictionary")
while True:
    order = input("\nHow Can I Help You Sir? (? - For Help)")

    if order == "?":
        print(
            "A - For Add Verb",
            "\nR - For Remove Verb",
            "\nS - For Search Verb\nO - For Show Dictionary",
        )
    elif order == "A":
        added_verb = input("Please Enter Your Verb Want To Add: ")
        # Add Verb To TXT File
        with open("addkeys.txt", "a") as f:
            f.write(added_verb)
            f.write("\n")

        added_verb_meaning = input("Pleas Enter Your Meaning Of Verb: ")
        # Add Meaning To TXT File
        with open("addvalues.txt", "a", encoding="utf-8") as f:
            f.write(added_verb_meaning)
            f.write("\n")

        print(f"{added_verb} Successfully add to your dictionary")

    elif order == "R":
        remove_verb = input("Please Enter Your Verb Want To Remove: ")
        if remove_verb in dictionary:
            # Remove Verb Of Dictionary
            del dictionary[remove_verb]

            print(f"{remove_verb}Successfully removed of your dictionary")
        else:
            print("Your Verb Not Founded")

    elif order == "S":
        search_verb = input("What are you looking for? ")
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
                with open("addvalues.txt", "a", encoding="utf-8") as f:
                    f.write(search_add_meaning)

                print(f"{search_verb} Successfully added to dictionary")
            # If Answer = n
            else:
                print("All Right")
    elif order == "O":
        for words, mean_words in dictionary.items():
            print(f"{words} : {mean_words}")

    with open("addkeys.txt", "w") as f:
        f.write("")

    with open("addvalues.txt", "w", encoding="utf-8") as f:
        f.write("")

    for new_keys, new_values in dictionary.items():
        with open("addkeys.txt", "a") as f:
            f.write(new_keys)
            f.write("\n")

        with open("addvalues.txt", "a", encoding="utf-8") as f:
            f.write(new_values)
            f.write("\n")
