from pizzapi import *
from View import *


def run(customer, address):
    global store
    global details
    global menu
    global order
    global search
    store = address.closest_store()
    details = store.get_details()
    menu = store.get_menu()
    search = "Pizza"
    order = Order(store, customer, address)

    while True:
        clear()
        print_customer_info(customer, address)
        print_store_details(details)
        print_order(order.data['Products'])
        print_menu(menu_options)
        switch_to_func(input("Please select your option: "))

def Display():
    print_header("Menu")
    menu.display()
    input("Shift + Up to Scroll - Press enter to continue")

def Search():
    print_header("Search")
    menu.search(Name=input("Please enter a search term: "))
    input("Press enter to continue")

def Add():
    print_header("Add")
    order.add_item(input("Please enter product code: "))
    input("Press enter to continue")

menu_options = {"1" : Display, "2" : Search, "3" : Add}

def switch_to_func(argument):
    switcher = menu_options
    func = switcher.get(argument, lambda : print_header("invalid selection"))
    func()
