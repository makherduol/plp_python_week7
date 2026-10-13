# shopping_list.py

shopping_list = []

while True:
    choice = input("\nChoose an action (add / remove / show / done): ").strip().lower()
    
    if choice == "add":
        item = input("Enter the item to add: ").strip()
        if item:
            shopping_list.append(item)
            print(f"'{item}' has been added to your list.")
        else:
            print("Item name cannot be empty.")
            
    elif choice == "remove":
        item = input("Enter the item to remove: ").strip()
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' has been removed from your list.")
        else:
            print("That item is not on your list.")
            
    elif choice == "show":
        print("\n--- Current Shopping List ---")
        if not shopping_list:
            print("Your shopping list is empty.")
        else:
            for idx, item in enumerate(shopping_list, start=1):
                print(f"{idx}. {item}")
        print("-----------------------------")
        
    elif choice == "done":
        print("\nThank you for using the Shopping List Manager. Goodbye!")
        break
        
    else:
        print("Invalid choice. Please type add, remove, show, or done.")
