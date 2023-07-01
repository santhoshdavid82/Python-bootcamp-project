# DS T12 Compulsory Task 1 - Beginner Data Structures - Lists and Dictionaries

# Create a list of menu items in the cafe
menu = ['coffee', 'tea', 'cake', 'sandwich']

# Create a dictionary to store the stock values for each item
stock = {'coffee': 100, 'tea': 75, 'cake': 50, 'sandwich': 25}

# Create a dictionary to store the price for each item in £
price = {'coffee': 2.5, 'tea': 2, 'cake': 3, 'sandwich': 5}

# Calculate the total stock worth in the cafe
# Define function to perform the calculation using a loop.
def calculate_stock_value():
    total_stock_value = 0
    for item in menu:
        item_value = stock[item] * price[item]
        total_stock_value += item_value

# Printing stock amount, price and value of each item
        print(f"{item}: stock amount: {stock[item]}, price: £{price[item]}, value: £{item_value}")

# Print the total stock value in the cafe
    print("The total value of stock in the cafe is £{:.2f}: " .format(total_stock_value))
    
calculate_stock_value()

