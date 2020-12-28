from os import system, name

def clear():
    _ = system('clear')

def print_customer_info(customer, address):
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


