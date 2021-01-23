from os import system, name
from tabulate import tabulate


def clear():
    _ = system('clear')

def print_header(message):
    print("\n" + "┌" + "─" * len(message) + "┐")
    print("│" + message + "│")
    print("└" + "─" * len(message) + "┘")

def print_customer_info(customer, address):
    print_header("CUSTOMER INFO")
    print("Name: " + customer.first_name + " " + customer.last_name + "\n" +
          "Email: " + customer.email + "\n" +
          "Phone: " + customer.phone + "\n" +
          "Address: " + address.street + ", " + address.city + ", " +
          address.region + " " + address.zip)
    new_line()

def print_store_details(details):
    print_header("CLOSEST STORE")
    print("Store ID: " + details["StoreID"] + "\n" +
          "Store Address: " + details["StreetName"] + "\n" +
          "Store Phone: " + details["Phone"])
    new_line()

def print_menu(menu_options):
    print_header("Main Menu")
    for key in menu_options:
        print(key, menu_options[key].__name__)

def print_order(order):
    data = []
    total = 0
    print_header("Order")
    for i in order:
        data.append([i['Name'], i['Price']])
        total = total + float(i['Price'])

    print(tabulate(data,headers=["Name", "Price ($)"]))
    print("\nTotal: $%.2f" % total)
    new_line()

def new_line():
    print("")
