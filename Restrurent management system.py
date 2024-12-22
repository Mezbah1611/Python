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



# Abstract Base Class  # 2
class Person(ABC):
    def __init__(self, name):
        self.__name = validate_name(name)  # Private variable

    @abstractmethod
    def display_info(self):
        pass

    def get_name(self):
        return self.__name

class Customer(Person):
    def __init__(self, name, phone, address):
        super().__init__(name)
        self.__phone = phone
        self.__address = address
        self.orders = []  # Orders will be a list of (item, quantity) tuples

    def get_phone(self):
        return self.__phone

    def get_address(self):
        return self.__address

    def place_order(self, item, quantity, delivery_option, payment_method, amount_paid):
        if item.is_available():
            self.orders.append((item, quantity, delivery_option, payment_method))
            print(f"{self.get_name()} ordered {quantity} x {item.get_name()} via {delivery_option}.")
            print(f"Payment Method: {payment_method}, Amount Paid: ${amount_paid:.2f}")
            print("Order placed successfully!\n")
        else:
            print(f"Sorry, {item.get_name()} is unavailable!")

    def get_bill(self):
        return sum(item.get_price() * quantity for item, quantity, _, _ in self.orders)

    def display_info(self):
        return f"Customer: {self.get_name()}, Phone: {self.get_phone()}, Address: {self.get_address()}"


class VipCustomer(Customer):
    def get_bill(self):
        return super().get_bill() * 0.9  # 10% discount for VIP customers

    def display_info(self):
        return f"VIP Customer: {self.get_name()}, Phone: {self.get_phone()}, Address: {self.get_address()}"


class Employee(Person):
    def __init__(self, employee_id, name, role):
        super().__init__(name)
        self.employee_id = employee_id
        self.role = role

    def display_info(self):
        return f"Employee ID: {self.employee_id}, Name: {self.get_name()}, Role: {self.role}"


class Manager(Employee,Person):
    def __init__(self, employee_id, name, role):
        super().__init__(employee_id, name, role)

    def approve_discount(self, customer):
        if isinstance(customer, VipCustomer):
            print(f"{self.get_name()} approved discount for {customer.get_name()}.")
        else:
            print(f"{self.get_name()} does not provide discounts for regular customers.")


# Dictionary
restaurant = {
    "menu": [
        MenuItem(1, "Burger", 5.99, True),
        MenuItem(2, "Pizza", 8.99, True),
        MenuItem(3, "Pasta", 7.49, False),
    ],
    "customers": [
        Customer("Hafiz", "018-2323-2323", "Ashulia"),
        VipCustomer("Mehedi", "017-4545-6767", "Savar"),
        Customer("Rasel", "019-8787-8787", "Dhanmodi"),
    ],
    "employees": [
        Employee(1, "Sazzad", "Chef"),
        Manager(2, "Charu", "Manager"),
        Employee(3, "Tonmoy", "Waiter"),
    ]
}


def safe_input(prompt, input_type):
    while True:
        try:
            return input_type(input(prompt))
        except ValueError:
            print(f"Invalid input! Please enter a valid {input_type.__name__}.")


def add_menu_item():
    item_id = len(restaurant["menu"]) + 1
    name = input("Enter item name: ")
    price = safe_input("Enter item price: ", float)
    availability = input("Is the item available? (yes/no): ").strip().lower() == "yes"
    restaurant["menu"].append(MenuItem(item_id, name, price, availability))
    print("Menu item added successfully!")


def view_menu():
    if not restaurant["menu"]:
        print("No items on the menu!")
        return
    print("\n--- Menu ---")
    for item in restaurant["menu"]:
        print(item.display_info())


def add_customer():
    name = input("Enter customer name: ")
    phone = input("Enter customer phone number: ")
    address = input("Enter customer address: ")
    role = input("Enter customer type (regular/vip): ").strip().lower()
    if role == "regular":
        restaurant["customers"].append(Customer(name, phone, address))
    elif role == "vip":
        restaurant["customers"].append(VipCustomer(name, phone, address))
    else:
        print("Invalid customer type!")
    print(f"{name} added as a {role} customer.")


def view_customers():
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
    elif role == "chef":
        restaurant["employees"].append(Employee(employee_id, name, role))
    elif role == "waiter":
        restaurant["employees"].append(Employee(employee_id, name, role))
    else:
        print("Invalid role!")
    print(f"Employee {name} added as a {role}.")


def view_employees():
    if not restaurant["employees"]:
        print("No employees yet!")
        return
    print("\n--- Employees ---")
    for employee in restaurant["employees"]:
        print(employee.display_info())


def place_order():
    view_menu()
    item_id = safe_input("Enter the menu item ID to order: ", int)
    view_customers() 
    customer_id = safe_input("Enter customer index (or enter -1 for new customer): ", int)  
    if customer_id == -1:  
        name = input("Enter customer name: ")
        phone = input("Enter customer phone number: ")
        address = input("Enter customer address: ")
        role = input("Enter customer type (regular/vip): ").strip().lower()       
        if role == "regular":
            new_customer = Customer(name, phone, address)
        elif role == "vip":
            new_customer = VipCustomer(name, phone, address)
        else:
            print("Invalid customer type! Defaulting to regular.")
            new_customer = Customer(name, phone, address)      
        restaurant["customers"].append(new_customer)
        customer_id = len(restaurant["customers"]) - 1  
        print(f"New customer {name} added as a {role} customer.")
        selected_customer = new_customer 
    elif 0 <= customer_id < len(restaurant["customers"]):  
        selected_customer = restaurant["customers"][customer_id]
    else:
        print("Invalid customer selection!")
        return
    if 0 < item_id <= len(restaurant["menu"]):  
        quantity = safe_input("Enter the quantity: ", int)
        delivery_option = input("Do you want delivery? (yes/no): ").strip().lower()
        delivery_option = "Delivery" if delivery_option == "yes" else "Pickup"
        payment_method = input("Payment method (cash/online banking): ").strip().lower()
        amount_paid = safe_input("Enter the amount paid: ", float)
        selected_item = restaurant["menu"][item_id - 1]
        selected_customer.place_order(selected_item, quantity, delivery_option, payment_method, amount_paid)
    else:
        print("Invalid menu item selection!")



def calculate_total_revenue():
    total_revenue = sum(customer.get_bill() for customer in restaurant["customers"])
    print(f"Total Revenue: ${total_revenue:.2f}")


def view_order_details():
    if not restaurant["customers"]:
        print("No customers yet!")
        return

    print("\n--- Order Details ---")
    for customer in restaurant["customers"]:
        if customer.orders:
            print(f"\nCustomer: {customer.get_name()}")
            for i, (item, quantity, delivery_option, payment_method) in enumerate(customer.orders, start=1):
                print(f"  {i}. Item: {item.get_name()}, Quantity: {quantity}, "
                      f"Delivery: {delivery_option}, Payment: {payment_method}, "
                      f"Total: ${item.get_price() * quantity:.2f}")
        else:
            print("\n")
def login():
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username == "admin" and password == "password":
            print("Login successful!\n")
            return True
        else:
            print("Invalid username or password. Please try again.")


# Add the option in the restaurant menu
def restaurant_menu():
    login()
    while True:
        print("\n--- Restaurant Management System ---")
        print("1. Add Menu Item")
        print("2. Add Customer")
        print("3. Add Employee")
        print("4. View Menu")
        print("5. View Customers")
        print("6. View Employees")
        print("7. Place Order")        
        print("8. Calculate Total Revenue")
        print("9. View Order Details")  # New option for order details
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
            calculate_total_revenue()
        elif choice == "9":
            view_order_details()  # Call the new function
        elif choice == "10":
            print("Exiting the restaurant system. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

# Start the application
restaurant_menu()
