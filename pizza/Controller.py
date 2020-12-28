from pizzapi import *
from View import *

def run(customer, address):
    store = address.closest_store()
    details = store.get_details()
    menu = store.get_menu()
    search = "Pizza"

    while True:
        clear()
        print_customer_info(customer, address)
        print_store_details(details)
        menu.search(Name=search)
        search = input("\nEnter a search item: ")

