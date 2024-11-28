import numpy as np


# String Methods
def validate_name(name):
    return name.strip().title()  # Capitalizes properly and removes extra spaces


# Tuple (Menu Item Fields)
MENU_FIELDS = ("ID", "Name", "Price", "Availability")


# Class & Object
class MenuItem:
    def __init__(self, item_id, name, price, availability):
        self.__item_id = item_id  # Private variable
        self.__name = validate_name(name)  # String methods
        self.__price = price
        self.__availability = availability

    # Private method
    def __format_info(self):
        return f"{self.__item_id}: {self.__name} - ${self.__price:.2f}"

    # Public method to access formatted information
    def display_info(self):
        status = "Available" if self.__availability else "Unavailable"
        return f"{self.__format_info()} ({status})"

    def is_available(self):
        return self.__availability

    def get_price(self):
        return self.__price

    def get_name(self):
        return self.__name


# Base Class: Customer
class Customer:
    def __init__(self, name):
        self.__name = validate_name(name)  # Private variable
        self.orders = []  # List of ordered items

    def place_order(self, item):
        if item.is_available():
            self.orders.append(item)  # Add to order list
            print(f"{self.__name} ordered {item.get_name()}.")
        else:
            print(f"Sorry, {item.get_name()} is unavailable!")

    def get_bill(self):
        return sum(item.get_price() for item in self.orders)

    def get_name(self):
        return self.__name


# Derived Class: VipCustomer (Inheritance)
class VipCustomer(Customer):
    def get_bill(self):
        return super().get_bill() * 0.9  # 10% discount for VIP customers


# New Class: Employee
class Employee:
    def __init__(self, employee_id, name, role):
        self.employee_id = employee_id
        self.name = validate_name(name)
        self.role = role

    def display_info(self):
        print(f"Employee ID: {self.employee_id}, Name: {self.name}, Role: {self.role}")


# Multiple Inheritance: Manager
class Manager(Employee, Customer):  # Manager inherits both Employee and Customer
    def __init__(self, employee_id, name, role):
        Employee.__init__(self, employee_id, name, role)
        Customer.__init__(self, name)  # Allows a manager to order too

    def approve_discount(self, customer):
        if isinstance(customer, VipCustomer):
            print(f"{self.name} approved discount for {customer.get_name()}.")
        else:
            print(f"{self.name} does not provide discounts for regular customers.")


# Exception Handling
def safe_input(prompt, input_type):
    while True:
        try:
            return input_type(input(prompt))
        except ValueError:
            print(f"Invalid input! Please enter a valid {input_type.__name__}.")


# Lambda Function
is_available = lambda item: item.is_available()


# Numpy
def calculate_average_price(menu_items):
    prices = [item.get_price() for item in menu_items]
    return np.mean(prices) if prices else 0


# Dictionary (For storing menu and customer data)
restaurant = {
    "menu": [],
    "customers": [],
    "employees": []
}


# Functions
def add_menu_item():
    item_id = len(restaurant["menu"]) + 1
    name = input("Enter item name: ")
    price = safe_input("Enter item price: ", float)
    availability = input("Is the item available? (yes/no): ").strip().lower() == "yes"
    restaurant["menu"].append(MenuItem(item_id, name, price, availability))
    print("Menu item added successfully!")


def add_customer():
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


def add_employee():
    employee_id = len(restaurant["employees"]) + 1
    name = input("Enter employee name: ")
    role = input("Enter role (chef/waiter/manager): ").strip().lower()
    if role == "manager":
        restaurant["employees"].append(Manager(employee_id, name, role))
    else:
        restaurant["employees"].append(Employee(employee_id, name, role))
    print(f"Employee {name} added as a {role}.")


def view_menu():
    if not restaurant["menu"]:
        print("No items on the menu!")
        return
    print("\n--- Menu ---")
    for item in restaurant["menu"]:
        print(item.display_info())


def view_customers():
    if not restaurant["customers"]:
        print("No customers yet!")
        return
    print("\n--- Customers ---")
    for customer in restaurant["customers"]:
        print(f"{customer.get_name()} (Orders: {len(customer.orders)}, Total Bill: ${customer.get_bill():.2f})")


def view_employees():
    if not restaurant["employees"]:
        print("No employees yet!")
        return
    print("\n--- Employees ---")
    for employee in restaurant["employees"]:
        employee.display_info()


def place_order():
    view_menu()
    item_id = safe_input("Enter the menu item ID to order: ", int)
    view_customers()
    customer_id = safe_input("Enter customer index: ", int)
    if 0 < item_id <= len(restaurant["menu"]) and 0 <= customer_id < len(restaurant["customers"]):
        restaurant["customers"][customer_id].place_order(restaurant["menu"][item_id - 1])
    else:
        print("Invalid menu item or customer selection!")


def calculate_total_revenue():
    total_revenue = sum(customer.get_bill() for customer in restaurant["customers"])
    print(f"Total Revenue: ${total_revenue:.2f}")


# Loop with Break/Continue
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
            break  # Exit the loop
        else:
            print("Invalid choice! Please try again.")
            continue


# Main Program
if __name__ == "__main__":
    restaurant_menu()
