import numpy as np  # 1
from abc import ABC, abstractmethod  # 2


# String Methods
def validate_name(name):  # 1
    return name.strip().title()  # Capitalizes and removes extra spaces


# Tuple  # 1
MENU_FIELDS = ("ID", "Name", "Price", "Availability")


class MenuItem:  # 1
    def __init__(self, item_id, name, price, availability):
        self.__item_id = item_id  # Private variable
        self.__name = validate_name(name)  # String methods
        self.__price = price
        self.__availability = availability

    def __format_info(self):
        return f"{self.__item_id}: {self.__name} - ${self.__price:.2f}"

    def display_info(self):
        status = "Available" if self.__availability else "Unavailable"
        return f"{self.__format_info()} ({status})"

    def is_available(self):
        return self.__availability

    def get_price(self):
        return self.__price

    def get_name(self):
        return self.__name


# Lambda Function  # 1
is_available = lambda item: item.is_available()

# NumPy  # 1
def calculate_average_price(menu_items):
    prices = [item.get_price() for item in menu_items]
    return np.mean(prices) if prices else 0


# Abstract Base Class  # 2
class Person(ABC):
    def __init__(self, name):
        self.__name = validate_name(name)  # Private variable

    @abstractmethod
    def display_info(self):
        pass

    def get_name(self):
        return self.__name


class Customer(Person):  # Updated to handle quantities in orders
    def __init__(self, name):
        super().__init__(name)
        self.orders = []  # Orders will be a list of (item, quantity) tuples

    def place_order(self, item, quantity):
        if item.is_available():
            self.orders.append((item, quantity))
            print(f"{self.get_name()} ordered {quantity} x {item.get_name()}.")
        else:
            print(f"Sorry, {item.get_name()} is unavailable!")

    def get_bill(self):
        # Calculate total by considering item price and quantity
        return sum(item.get_price() * quantity for item, quantity in self.orders)

    def display_info(self):
        return f"Customer: {self.get_name()}, Orders: {len(self.orders)}, Total Bill: ${self.get_bill():.2f}"


class VipCustomer(Customer):  # Updated to handle quantities in orders
    def get_bill(self):
        # Apply a 10% discount for VIP customers
        return super().get_bill() * 0.9

    def display_info(self):
        return f"VIP Customer: {self.get_name()}, Orders: {len(self.orders)}, Total Bill (after discount): ${self.get_bill():.2f}"


class Employee(Person):  # 2
    def __init__(self, employee_id, name, role):
        super().__init__(name)
        self.employee_id = employee_id
        self.role = role

    def display_info(self):
        return f"Employee ID: {self.employee_id}, Name: {self.get_name()}, Role: {self.role}"


def safe_input(prompt, input_type):  # 2
    while True:
        try:
            return input_type(input(prompt))
        except ValueError:
            print(f"Invalid input! Please enter a valid {input_type.__name__}.")


class Manager(Employee, Customer):
    def __init__(self, employee_id, name, role):
        Employee.__init__(self, employee_id, name, role)
        Customer.__init__(self, name)

    def approve_discount(self, customer):
        if isinstance(customer, VipCustomer):
            print(f"{self.get_name()} approved discount for {customer.get_name()}.")
        else:
            print(f"{self.get_name()} does not provide discounts for regular customers.")


# Dictionary
restaurant = {
    "menu": [],
    "customers": [],
    "employees": []
}


def add_menu_item():  # 1
    item_id = len(restaurant["menu"]) + 1
    name = input("Enter item name: ")
    price = safe_input("Enter item price: ", float)
    availability = input("Is the item available? (yes/no): ").strip().lower() == "yes"
    restaurant["menu"].append(MenuItem(item_id, name, price, availability))
    print("Menu item added successfully!")


def view_menu():  # 1
    if not restaurant["menu"]:
        print("No items on the menu!")
        return
    print("\n--- Menu ---")
    for item in restaurant["menu"]:
        print(item.display_info())


def add_customer():  # 2
    name = input("Enter customer name: ")
    role = input("Enter customer type (regular/vip): ").strip().lower()
    if role == "regular":
        restaurant["customers"].append(Customer(name))
    elif role == "vip":
        restaurant["customers"].append(VipCustomer(name))
    else:
        print("Invalid customer type!")
        return
    print(f"{name} added as a {role} customer.")


def view_customers():  # 2
    if not restaurant["customers"]:
        print("No customers yet!")
        return
    print("\n--- Customers ---")
    for i, customer in enumerate(restaurant["customers"]):
        print(f"{i}: {customer.display_info()}")


def add_employee():
    employee_id = len(restaurant["employees"]) + 1
    name = input("Enter employee name: ")
    role = input("Enter role (chef/waiter/manager): ").strip().lower()
    if role == "manager":
        restaurant["employees"].append(Manager(employee_id, name, role))
    else:
        restaurant["employees"].append(Employee(employee_id, name, role))
    print(f"Employee {name} added as a {role}.")


def view_employees():
    if not restaurant["employees"]:
        print("No employees yet!")
        return
    print("\n--- Employees ---")
    for employee in restaurant["employees"]:
        print(employee.display_info())


def place_order():
    # Step 1: Display the menu to the user
    view_menu()

    # Step 2: Ask the user to select a menu item by entering its ID
    item_id = safe_input("Enter the menu item ID to order: ", int)

    # Step 3: Display the list of customers
    view_customers()

    # Step 4: Ask the user to select a customer by entering their index
    customer_id = safe_input("Enter customer index: ", int)

    # Step 5: Validate the item ID and customer index
    if 0 < item_id <= len(restaurant["menu"]) and 0 <= customer_id < len(restaurant["customers"]):
        # Step 6: Ask for the quantity of the selected item
        quantity = safe_input("Enter the quantity: ", int)

        if quantity <= 0:
            print("Quantity must be at least 1.")
            return

        # Step 7: Place the order
        selected_item = restaurant["menu"][item_id - 1]
        selected_customer = restaurant["customers"][customer_id]
        selected_customer.place_order(selected_item, quantity)
    else:
        # Step 8: Inform the user if the input is invalid
        print("Invalid menu item or customer selection!")


def calculate_total_revenue():
    total_revenue = sum(customer.get_bill() for customer in restaurant["customers"])
    print(f"Total Revenue: ${total_revenue:.2f}")


def restaurant_menu():
    while True:
        print("\n--- Restaurant Management System ---")
        print("1. Add Menu Item")
        print("2. Add Customer")
        print("3. Add Employee")
        print("4. View Menu")
        print("5. View Customers")
        print("6. View Employees")
        print("7. Place Order")
        print("8. Calculate Average Price")
        print("9. Calculate Total Revenue")
        print("10. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_menu_item()
        elif choice == "2":
            add_customer()
        elif choice == "3":
            add_employee()
        elif choice == "4":
            view_menu()
        elif choice == "5":
            view_customers()
        elif choice == "6":
            view_employees()
        elif choice == "7":
            place_order()
        elif choice == "8":
            print(f"Average Price of Menu Items: ${calculate_average_price(restaurant['menu']):.2f}")
        elif choice == "9":
            calculate_total_revenue()
        elif choice == "10":
            print("Exiting the restaurant system. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")
            continue


if __name__ == "__main__":
    restaurant_menu()
