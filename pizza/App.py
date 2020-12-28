from pizzapi import *
from View import *
from Controller import *


cust_name = "John"
cust_last_name = "Joe"
cust_email = "jb@email.com"
cust_phone = "5551235432"
customer = Customer(cust_name, cust_last_name, cust_email, cust_phone)

cust_street_address = "2233 N Summit Ave"
cust_city = "Milwaukee"
cust_state = "WI"
cust_zip = "53202"
address = Address(cust_street_address, cust_city, cust_state, cust_zip)

run(customer, address)
