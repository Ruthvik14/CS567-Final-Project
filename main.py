from database import add_item, update_item, get_item, get_items, delete_item, init_db

def input_float(prompt):
    """Helper function to safely parse floats from user input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input, please enter a number.")

def input_integer(prompt):
    """Helper function to safely parse integers from user input."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input, please enter an integer.")

def main_menu():
    """Display the main menu and handle user choices."""
    while True:
        print("\nInventory Management System")
        print("1. Add New Item")
        print("2. Update Existing Item")
        print("3. Delete Item")
        print("4. View All Items")
        print("5. View Single Item")
        print("6. Quit")
        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Enter the name of the item: ")
            price = input_float("Enter the price of the item: ")
            quantity = input_integer("Enter the quantity of the item: ")
            add_item(name, price, quantity)
        elif choice == '2':
            name = input("Enter the name of the item to update: ")
            if get_item(name):
                quantity = input_integer("Enter the additional quantity (or 0 to skip): ")
                if quantity:
                    update_item(name, quantity=quantity)
                new_price = input_float("Enter the new price (or 0 to skip): ")
                if new_price:
                    update_item(name, price=new_price)
            else:
                print("Item not found.")
        elif choice == '3':
            name = input("Enter the name of the item to delete: ")
            if get_item(name):
                delete_item(name)
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
            print("Exiting the system.")
            break
        else:
            print("Invalid choice, please choose again.")

if __name__ == '__main__':
    init_db()  # Initialize the database tables
    main_menu()  # Start the main menu
