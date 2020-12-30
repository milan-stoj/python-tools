from pizzapi import *
from View import *


def run(customer, address):
    store = address.closest_store()
    details = store.get_details()
    menu = store.get_menu()
    search = "Pizza"
    order = Order(store, customer, address)

    while True:
        clear()
        print_customer_info(customer, address)
        print_store_details(details)
        print_menu(menu_options)
        switch_to_func(input("Please select your option: "))

def Search():
    print_header("Search")

def Add():
    print_header("Add")

menu_options = {"1" : Search, "2" : Add}

def switch_to_func(argument):
    switcher = menu_options
    func = switcher.get(argument, lambda : print_header("invalid selection"))
    func()
