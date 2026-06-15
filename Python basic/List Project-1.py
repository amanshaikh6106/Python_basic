shopping_list = []

while True:
    print("------ Shopping List Manager ------")
    print("1. Add Item")
    print("2. Display Items")
    print("3. Search Item")
    print("4. Remove Item")
    print("5. Count Items")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter item name: ")
        shopping_list.append(item)
        print("Item added successfully.")

    elif choice == 2:
        print("Shopping List:")
        for item in shopping_list:
            print(item)

    elif choice == 3:
        item = input("Enter item name to search: ")
        if item in shopping_list:
            print("Item found in shopping list")
        else:
            print("Item not found in shopping list")

    elif choice == 4:
        item = input("Enter item name to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print("Item removed successfully")
        else:
            print("Item not found in shopping list")

    elif choice == 5:
        print("Total items in shopping list:", len(shopping_list))

    elif choice == 6:
        print("Exiting program")
        break
    else:
        print("Invalid")

    