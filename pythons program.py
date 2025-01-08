#python program to track inventory of items in a store (CRUD operations on a dictionary)
# CRUD (Create Read Update Delete)
class Inventory:
    def __init__(self):
        self.items = {}

    def create_item(self, name, quantity, price):
        """Create a new item in the inventory."""
        self.items[name] = {"quantity": quantity, "price": price}
        print(f"Item '{name}' added successfully.")

    def read_item(self, name):
        """Read an item's details from the inventory."""
        if name in self.items:
            print(f"Name: {name}")
            print(f"Quantity: {self.items[name]['quantity']}")
            print(f"Price: {self.items[name]['price']}")
        else:
            print(f"Item '{name}' not found.")

    def update_item(self, name, quantity=None, price=None):
        """Update an item's quantity or price in the inventory."""
        if name in self.items:
            if quantity is not None:
                self.items[name]["quantity"] = quantity
            if price is not None:
                self.items[name]["price"] = price
            print(f"Item '{name}' updated successfully.")
        else:
            print(f"Item '{name}' not found.")

    def delete_item(self, name):
        """Delete an item from the inventory."""
        if name in self.items:
            del self.items[name]
            print(f"Item '{name}' deleted successfully.")
        else:
            print(f"Item '{name}' not found.")

    def display_inventory(self):
        """Display all items in the inventory."""
        print("Current Inventory:")
        for name, details in self.items.items():
            print(f"Name: {name}, Quantity: {details['quantity']}, Price: {details['price']}")

def main():
    inventory = Inventory()

    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. View Item")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Display Inventory")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter item name: ")
            quantity = int(input("Enter item quantity: "))
            price = float(input("Enter item price: "))
            inventory.create_item(name, quantity, price)
        elif choice == "2":
            name = input("Enter item name: ")
            inventory.read_item(name)
        elif choice == "3":
            name = input("Enter item name: ")
            quantity = input("Enter new quantity (press Enter to skip): ")
            quantity = int(quantity) if quantity else None
            price = input("Enter new price (press Enter to skip): ")
            price = float(price) if price else None
            inventory.update_item(name, quantity, price)
        elif choice == "4":
            name = input("Enter item name: ")
            inventory.delete_item(name)
        elif choice == "5":
            inventory.display_inventory()
        elif choice == "6":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()




