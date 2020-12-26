from pizzapi import *
from os import system, name

def clear():
    _ = system('clear')

cust_name = "Joe"
cust_last_name = "Body"
cust_email = "jb@email.com"
cust_phone = "5551235432"
customer = Customer(cust_name, cust_last_name, cust_email, cust_phone)

cust_street_address = "2233 N Summit Ave"
cust_city = "Milwaukee"
cust_state = "WI"
cust_zip = "53202"
address = Address(cust_street_address, cust_city, cust_state, cust_zip)

# cust_name = input("Enter your name: ")
# cust_last_name = input("Enter your last name: ")
# cust_email = input("Enter your email: ")
# cust_phone = input("Enter your phone number (xxxxxxxxxx): ")
# customer = Customer(cust_name, cust_last_name, cust_email, cust_phone)

# cust_street_address = input("Enter your street address: ")
# cust_city = input("Enter your city: ")
# cust_state = input("Enter your state (xx): ")
# cust_zip = input("Enter your zip-code: ")
# address = Address(cust_street_address, cust_city, cust_state, cust_zip)

def print_customer_info(customer):
    print("-" * 10 + "CUSTOMER INFO" + "-" * 10 + "\n" +
          "Name: " + customer.first_name + " " + customer.last_name + "\n" +
          "Email: " + customer.email + "\n" +
          "Phone: " + customer.phone + "\n" +
          "Address: " + address.street + ", " + address.city + ", " +
          address.region + " " + address.zip)

def print_store_details(details):
    print("\n" + "-" * 10 + "CLOSEST STORE" + "-" * 10 + "\n" +
          "Store ID: " + details["StoreID"] + "\n" +
          "Store Address: " + details["StreetName"] + "\n" +
          "Store Phone: " + details["Phone"] + "\n")

store = address.closest_store()
details = store.get_details()


menu = store.get_menu()
search = 'Pizza'

while True:
    clear()
    print_customer_info(customer)
    print_store_details(details)
    menu.search(Name=search)
    search = input("\nEnter a search item: ")


