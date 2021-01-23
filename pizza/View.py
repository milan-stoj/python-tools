from os import system, name


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

def print_store_details(details):
    print_header("CLOSEST STORE")
    print("Store ID: " + details["StoreID"] + "\n" +
          "Store Address: " + details["StreetName"] + "\n" +
          "Store Phone: " + details["Phone"] + "\n")

def print_menu(menu_options):
    for key in menu_options:
        print(key, menu_options[key].__name__)

def print_order(order):
    print_header("Order")
    for i in order:
        print(i['Name'])
