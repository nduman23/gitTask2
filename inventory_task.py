#!/usr/bin/env python

class Shoe:
    """
    A class representing a shoe with attributes for country, code, product, cost, and quantity.
    """
    def __init__(self, country, code, product, cost, quantity):
        """
        Initialize a new Shoe instance.

        Parameters:
        country (str): The country where the shoe is produced!
        code (str): The unique code identifying the shoe!
        product (str): The name or type of the shoe!
        cost (int/float): The cost of the shoe!
        quantity (int): The available quantity of the shoe!
        """
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
 
    def get_cost(self):
        """
        Return the cost of the shoe/s.

        Returns:
        int/float: The cost of the shoe/s.
        """
        return self.cost
    
    
    def get_quantity(self):
        """
        Return the quantity of the shoe/s

        Returns:
        int: The quantity of the shoe.
        """
        return self.quantity
      
    
    def __str__(self):
        """
        Return a string representation of the Shoe instance.

        Returns:
        str: A formatted string displaying the shoe's details.
        """
        return f"Country: {self.country}\nCode: {self.code}\nProduct: {self.product}\nCost: {self.cost}\nQuantity: {self.quantity}\n"
    

# Creating list to store a list of objects of shoes
shoes_list = []



def read_shoes_data():
    """
    Read shoe data from 'inventory.txt', creates Shoe objects, and append them to a list.

    This function opens 'inventory.txt', reads each line (except the first header line), 
    creates Shoe objects from the data, and appends these objects to a global list1
    """
    try:
        with open("inventory.txt", "r") as file:
            lines = file.readlines()
            for line in lines[1:]:
                data = line.strip().split(",")
                country, code, product, cost, quantity = data
                cost = int(cost)
                quantity = int(quantity)
                shoe = Shoe(country, code, product, cost, quantity)
                shoes_list.append(shoe)
                pass
        print("Shoes data has been read from the file!")
    except FileNotFoundError:
        print("Error: The file inventory.txt was not found.")
    except IOError:
        print("Error: An I/O error occurred while handling 'inventory.txt'.")
    except Exception as e:
        print(f"An error occured while reading file: {e}")
        
# Function to capture integer input with validation
def capture_integer_value(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid Input. Please enter a valid number.")

# Function to allow user to capture shoe data and append to the shoes list   
def capture_shoes():
    country = input("Enter the country: ")
    code = input("Enter the code: ")
    product = input("Enter the product: ")
    cost = int(input("Enter the cost: "))
    quantity = int(input("Enter the quantity: "))
    shoe = Shoe(country, code, product, cost, quantity)
    shoes_list.append(shoe)

    print("Shoe details captured successfully!")
 
# Function that iterates over shoes list and prints details
def view_all():
    for shoe in shoes_list:
        print(shoe)

# Function finds the shoe object with the lowest quantity, which is the shoes that need to be re-stocked
# Ask the user if they want to add this quantity of shoes and then update it.
def re_stock():
    lowest_quantity_shoes = min(shoes_list, key=lambda shoe: shoe.quantity)
    lowest_quantity_shoe = lowest_quantity_shoes[0]
    print(f"The shoe with the lowest quantity is:\n{lowest_quantity_shoe}")

    add_quantity = int(input("Enter the quantity to restock: "))
    lowest_quantity_shoe.quantity += add_quantity
    print("Restock successful.")

    # Updating the shoe quantity in the file
    with open("inventory.txt", "w") as file:
        file.write("Country,Code,Product,Cost,Quantity\n")
        for shoe in shoes_list:
            file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")

# Function will search for a shoe from the list using the shoe code and return this object so that it will be printed
def search_shoe():
    code = input("Enter the code of the shoe to search: ")
    for shoe in shoes_list:
        if shoe.code == code:
            print(f"Shoe found:\n{shoe}")
            return
    print("Shoe not found.")
    
# Function will calculate the total value for each item
def value_per_item():
    for shoe in shoes_list:
        value = shoe.cost * shoe.quantity
        print(f"Product: {shoe.product}, Value: {value}")

# Function to determine the product with the highest quantity 
def highest_qty():
    highest_quantity_shoes = sorted(shoes_list, key=lambda shoe: shoe.quantity, reverse=True)
    highest_quantity_shoe = highest_quantity_shoes[0]

    print(f"This shoes is currently on SALE:\n{highest_quantity_shoe}")
    
# Main Menu

while True:
    print("\n===== Shoe Inventory Management =====")
    user_choice = int(input('''\n What would you like to do?: 
    1. Read Shoes Data from File
    2. Capture Shoe Details
    3. View All Shoes
    4. Restock Shoe
    5. Search Shoe
    6. Value of Shoe in stock
    7. Highest Quantity Shoe
    8. Exit
    
    Enter selection: '''))

    if user_choice == 1:
        # Read shoes data from a file
        read_shoes_data()

    elif user_choice == 2:
        # Capture shoe details
        capture_shoes()

    elif user_choice == 3:
        # View all shoes
        view_all()

    elif user_choice == 4:
        # Restock a shoe
        re_stock()

    elif user_choice == 5:
        # Search for a shoe
        search_shoe()

    elif user_choice == 6:
        # Calculate the value of shoes in stock
        value_per_item()

    elif user_choice == 7:
        # Find the shoe with the highest quantity
        highest_qty()

    elif user_choice == 8:
        # Exit the program
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Oops, Incorrect input. Please enter a valid selection!")