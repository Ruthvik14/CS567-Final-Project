from database import (add_item, update_item, get_item, get_items, delete_item, init_db,
                      add_category, get_categories, bulk_update_items, backup_database)

def input_float(prompt):
    """Helper function to safely parse floats from user input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input, please enter a valid number.")

def input_integer(prompt):
    """Helper function to safely parse integers from user input."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input, please enter a valid integer.")

def main_menu():
    """Display the main menu and handle user choices."""
    while True:
        print("\nInventory Management System")
        print("1. Add New Item")
        print("2. Update Existing Item")
        print("3. Delete Item")
        print("4. View All Items")
        print("5. View Single Item")
        print("6. Add Category")
        print("7. View Categories")
        print("8. Bulk Update Items")
        print("9. Backup Database")
        print("10. Quit")
        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Enter the name of the item: ")
            price = input_float("Enter the price of the item: ")
            quantity = input_integer("Enter the quantity of the item: ")
            category = input("Enter the category ID (leave blank for default): ")
            category_id = int(category) if category else 1
            add_item(name, price, quantity, category_id)
        elif choice == '2':
            name = input("Enter the name of the item to update: ")
            if get_item(name):
                quantity = input_integer("Enter the additional quantity (or 0 to skip): ")
                if quantity != 0:
                    update_item(name, quantity=quantity)
                new_price = input_float("Enter the new price (or 0 to skip): ")
                if new_price != 0:
                    update_item(name, price=new_price)
            else:
                print("Item not found.")
        elif choice == '3':
            name = input("Enter the name of the item to delete: ")
            if get_item(name):
                delete_item(name)
                print(f"{name} has been deleted.")
            else:
                print("Item not found.")
        elif choice == '4':
            items = get_items()
            if items:
                for item in items:
                    print(item)
            else:
                print("No items found.")
        elif choice == '5':
            name = input("Enter the name of the item to view: ")
            item = get_item(name)
            if item:
                print(item)
            else:
                print("Item not found.")
        elif choice == '6':
            category_name = input("Enter the name of the new category: ")
            add_category(category_name)
        elif choice == '7':
            categories = get_categories()
            if categories:
                for category in categories:
                    print(category)
            else:
                print("No categories found.")
        elif choice == '8':
            print("Entering bulk update mode. Enter item details. Type 'done' when finished.")
            items_to_update = []
            while True:
                name = input("Item name (type 'done' to finish): ")
                if name.lower() == 'done':
                    break
                price = input_float("New price: ")
                quantity = input_integer("New quantity: ")
                items_to_update.append((price, quantity, name))
            bulk_update_items(items_to_update)
        elif choice == '9':
            backup_database()
        elif choice == '10':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice, please choose again.")

if __name__ == '__main__':
    init_db()  # Ensure the database is initialized
    main_menu()  # Start the main menu
