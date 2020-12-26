from pizzapi import *

cust_name = input("Enter your name: ")
cust_last_name = input("Enter your last name: ")
cust_email = input("Enter your email: ")
cust_phone = input("Enter your phone number (xxxxxxxxxx): ")
customer = Customer(cust_name, cust_last_name, cust_email, cust_phone)


cust_street_address = input("Enter your street address: ")
cust_city = input("Enter your city: ")
cust_state = input("Enter your state (xx): ")
cust_zip = input("Enter your zip-code: ")
address = Address(cust_street_address, cust_city, cust_state, cust_zip)

def print_customer_info():
    print("-" * 10 + "CUSTOMER INFO" + "-" * 10 + "\n" +
          "Name: " + customer.first_name + " " + customer.last_name + "\n" +
          "Email: " + customer.email + "\n" +
          "Phone: " + customer.phone + "\n" +
          "Address: " + address.street + ", " + address.city + ", " +
          address.region + " " + address.zip)



print_customer_info()

