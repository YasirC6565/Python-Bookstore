
'''
import time 

def collect_card_details():
    name_on_card = input(" \n -----------Card Details ------------- \n \n \n \nEnter the name on the card: ")
    card_number = input("Enter your card number: ")
    expiry_date = input("Enter card expiry date: ")
    cvv = input("Enter CVV: ")
    return name_on_card, card_number, expiry_date, cvv

def collect_billing_details():
    address = input("Enter Billing Address: ")
    city = input("Enter city: ")
    post_code = input("Enter Post Code: ")
    return address, city, post_code 

def confirm_order():
    confirmation = input("Do you want to confirm your order? (yes/no): ")
    return confirmation.lower() == 'yes'

def checkout():
    card_details = collect_card_details()
    billing_address = collect_billing_details()
    if confirm_order():
        print("Order confirmed. Processing payment...")

        time.sleep(3)

        print("Payment sucessful. Thank you for your purchase!")
    else:
        print("Transaction denied") 
        
'''


import time

def collect_card_details():
    name_on_card = input(" \n -----------Card Details ------------- \n \n \nEnter the name on the card: ")
    card_number = input("Enter your card number: ")
    expiry_date = input("Enter card expiry date: ")
    cvv = input("Enter CVV: ")
    return name_on_card, card_number, expiry_date, cvv

def collect_billing_details():
    address = input("Enter Billing Address: ")
    city = input("Enter city: ")
    post_code = input("Enter Post Code: ")
    return address, city, post_code 

def confirm_order():
    confirmation = input("Do you want to confirm your order? (yes/no): ")
    return confirmation.lower() == 'yes'

def save_user_history(user):
    filename = f"{user.email}_user_history.txt"
    try:
        with open(filename, 'a') as file:
            for book in user.order_history:
                file.write(f"Title: {book.title}, Author: {book.author}\n")
    except Exception as e:
        print(f"An error occurred while saving order history: {e}")

def update_order_history(current_user):
    for book in current_user.shopping_basket:
        current_user.add_order_history(book)
        save_user_history(current_user)
        print(f"'{book.title}' has been added to your order history.")
    current_user.shopping_basket.clear()
    print("Thank you for your purchase!")

def checkout(current_user):
    if not current_user or current_user.email == "":
        print("Please login to complete purchase.")
        return False

    if not current_user.shopping_basket:
        print("Your shopping basket is empty.")
        return False

    card_details = collect_card_details()
    billing_address = collect_billing_details()
    
    if confirm_order():
        print("Order confirmed. Processing payment...")
        time.sleep(3)  # Simulate payment processing delay
        update_order_history(current_user)  # Update order history upon successful payment
        return True
    else:
        print("Checkout has failed, please try")
        return False
