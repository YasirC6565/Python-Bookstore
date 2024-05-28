class User:
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.is_registered = False
        self.shopping_basket = []
        self.order_history = []

    def view_account_details(self):
        print(f"First Name: {self.first_name}\nLast Name: {self.last_name}\nEmail: {self.email}")

    def modify_account_details(self, first_name=None, last_name=None, email=None, password=None):
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        if email:
            self.email = email
        if password:
            self.password = password
        print("Account details updated successfully.")

    def add_order_history(self, book):
        self.order_history.append(book)

class Book:
    def __init__(self, title, author, isbn, overview):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.overview = overview

#Sample Books

books = [
    Book("Python Programming Essentials", "John Smith", "1234567890", "An essential guide for beginners."),
    Book("Advanced Python Techniques", "Jane Doe", "2345678901", "A comprehensive deep dive into advanced Python."),
    Book("Data Science with Python", "Alex Johnson", "3456789012", "Exploring data science techniques using Python."),
    Book("Machine Learning Fundamentals", "Emily Brown", "4567890123", "The definitive handbook for ML practitioners."),
    Book("Deep Learning Applications", "Michael Davis", "5678901234", "Practical applications of deep learning."),
    Book("AI Fundamentals", "Sarah Miller", "6789012345", "A beginner's guide to artificial intelligence."),
    Book("Web Development with Flask", "Chris Wilson", "7890123456", "Building web applications using Flask."),
    Book("Cybersecurity Best Practices", "Laura Martinez", "8901234567", "Essential cybersecurity techniques and best practices."),
    Book("Cloud Computing in Action", "Robert Garcia", "9012345678", "Implementing effective cloud solutions."),
    Book("Blockchain Basics", "Linda Williams", "0123456789", "An introduction to blockchain technology."),
    Book("Intro to IoT", "Samuel Lee", "1122334455", "Understanding the Internet of Things and its impact."),
    Book("Quantum Computing 101", "Angela Hart", "2233445566", "A beginner's guide to quantum computing."),
    Book("Ethical Hacking", "Marcus Chen", "3344556677", "Learn the skills of ethical hacking and cybersecurity."),
    Book("VR and AR Development", "Jessica Tan", "4455667788", "Developing immersive virtual and augmented reality experiences."),
    Book("UI/UX Design Principles", "Derek Luo", "5566778899", "Fundamentals of designing user interfaces and experiences."),
    Book("Game Development with Unity", "Nina Patel", "6677889900", "Creating engaging games using Unity."),
    Book("Introduction to Algorithms", "Carlos Vega", "7788990011", "Comprehensive guide to algorithms and their applications."),
    Book("Cloud Infrastructure and AWS", "Fiona Murphy", "8899001122", "Deploying scalable solutions with Amazon Web Services."),
    Book("Data Visualization Techniques", "Harold Kim", "9900112233", "Techniques for visualizing and interpreting data."),
    Book("Practical Docker Usage", "Sandra Adams", "0011223344", "Utilizing Docker for development and deployment."),
    Book("Responsive Web Design", "Leo Ortiz", "1231231234", "Creating web designs that adapt across devices."),
    Book("Mobile App Development", "Katie Bell", "2342342345", "Building native and cross-platform mobile applications."),
    Book("SEO Strategies and Marketing", "Aaron Zhu", "3453453456", "Optimizing web content for search engines."),
    Book("Python for Data Analysis", "Miriam Quick", "4564564567", "Data analysis techniques using Python."),
    Book("Starting with Flask", "Omar Ahmad", "5675675678", "Building web applications step by step with Flask."),
    Book("Kubernetes in Action", "Sophia Sun", "6786786789", "Managing containerized applications with Kubernetes."),
    Book("Building RESTful APIs", "Evan Yu", "7897897890", "Design and develop RESTful API services."),
    Book("Learning React Native", "Irene Wang", "8908908901", "Developing native mobile apps using React Native."),
    Book("Cybersecurity Fundamentals", "Neil Patel", "9019019012", "The basics of securing digital environments."),
    Book("Blockchain for Dummies", "Alice Johnson", "0120120123", "Simplifying blockchain technology for beginners.")]

'''
books = []
# Function to load books from a text file
def load_books(filename = 'Books.txt'):
    try:
        with open(filename, 'r') as file:
            for line in file:
                title, author, isbn, overview = line.strip().split('|')
                books.append(Book(title, author, isbn, overview))
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
for book in books:
        print(book.title, book.author)
'''

users = []
current_user = None  

def save_user_details(user):
    with open('registered_users.txt', 'a') as file:
        file.write(f"{user.email}|{user.password}|{user.first_name}|{user.last_name}\n")

import bcrypt

def register_user():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    email = input("Enter email: ")
    password = input("Create password: ")

    with open('registered_users.txt', 'r') as users_file:
            registered_emails = [line.split('|')[0] for line in users_file]
            if email in registered_emails:
                print("Email is already in use.")
                return 
   
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    new_user = User(first_name, last_name, email, hashed_password.decode('utf-8'))
    new_user.is_registered = True
    users.append(new_user)
    save_user_details(new_user)
    print("Registration successful!")
    return registered_user_menu() 
'''
def login_user():
    email = input("Enter email: ")
    password = input("Enter password: ")
    global current_user
    current_user = next((user for user in users if user.email == email and user.password == password), None)
    if current_user:
        print("Login successful!")
        registered_user_menu()
    else:
        print("Login failed.")

def login_user():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    global current_user 
    with open('registered_users.txt', 'r') as file:
        for line in file:
            saved_email, saved_password, _, _ = line.strip().split('|')
            if email == saved_email and password == saved_password:
                print("Login successful!")
                registered_user_menu()
    print("Login failed. Please check your email and password.")
    return False
'''
def login_user():
    global current_user
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    with open('registered_users.txt', 'r') as file:
        for line in file:
            saved_email, saved_hashed_pw, first_name, last_name = line.strip().split('|')
            if email == saved_email and bcrypt.checkpw(password.encode('utf-8'), saved_hashed_pw.encode('utf-8')):
                current_user = User(first_name, last_name, email, saved_hashed_pw)
                print("Login successful!")
                registered_user_menu()
                return True
    user_input = input("Login failed. Please click enter to try again or type exit to return to main menu: ")
    if user_input == 'exit':
        main_menu()
    else:
        login_user()


def continue_as_guest():
    global current_user
    current_user = User(first_name="Guest", last_name="", email="", password="")
    print("Continuing as guest. You can add books to the basket and purchase them.")
    guest_menu() 

def search_books():
    query = input("Enter book title or author to search: ").lower()
    results = [book for book in books if query in book.title.lower() or query in book.author.lower()]
    for book in results:
        print(f"Title: {book.title}, Author: {book.author}, Overview: {book.overview}")
    else: 
        print("Book not found")

def view_all_books():
    if not books:
        print("There are no books available.")
        return
    print("\nAvailable Books:")
    for book in books:
        print(f"Title: {book.title}, Author: {book.author}, Overview: {book.overview}")

def view_account():
    if not current_user:
        print("Please login first.")
        return
    current_user.view_account_details()

def modify_account():
    if not current_user:
        print("Please login first.")
        return
    first_name = input("Enter new first name (leave blank to keep current): ")
    last_name = input("Enter new last name (leave blank to keep current): ")
    email = input("Enter new email (leave blank to keep current): ")
    password = input("Enter new password (leave blank to keep current): ")
    current_user.modify_account_details(first_name or None, last_name or None, email or None, password or None)

def view_order_history():
    if not current_user:
        print("Please login first.")
        return
    filename = f"{current_user.email}_user_history.txt"

    try:
        with open(filename, 'r') as file:
            view_order_history = file.readlines()
        
        if not view_order_history:
            print("Your order history is empty.")
            return
    
        print("Order History:")
        for line in view_order_history:
            print(line.strip())
    except FileNotFoundError:
        print("Your order history is empty")
        
'''
def purchase_books():
    if not current_user or current_user.email == "":
        print("Please login to complete purchase.")
        return
    if not current_user.shopping_basket:
        print("Your shopping basket is empty.")
        return
    for book in current_user.shopping_basket:
        current_user.add_order_history(book)
    current_user.shopping_basket.clear()
    confirmation = input("Are you sure you would like to purchase: " )
    if confirmation.lower() == 'Yes':
        purchase_books()
        print("Purchase successful. Your order history has been updated.")
    else:
        registered_user_menu() 
'''
from checkout import checkout
'''
def purchase_books():
    if not current_user or current_user.email == "":
        print("Please login to complete purchase.")
        return
    if not current_user.shopping_basket:
        print("Your shopping basket is empty.")
        return
    confirmation = input("Are you sure you would like to purchase the items in your basket? (yes/no): ")
    if confirmation.lower() == 'yes':
        checkout_success = checkout()
        if checkout_success:
            for book in current_user.shopping_basket:
                current_user.add_order_history(book)
            current_user.shopping_basket.clear()
            print("Purchase completed successfully.")
    else:
        print("Purchase cancelled. Returning to the registered user menu.")
        registered_user_menu()
'''
def purchase_books():
    global current_user  # Ensure current_user is accessible
    if not current_user or current_user.email == "":
        print("Please login to complete purchase.")
        return

    if not current_user.shopping_basket:
        print("Your shopping basket is empty.")
        return
    
    checkout_success = checkout(current_user)
    if checkout_success:
        print("Checkout and order history update successful.")
    else:
        print("Checkout failed or was cancelled.") 
'''
    confirmation = input("Are you sure you would like to purchase the items in your basket? (yes/no): ")
    if confirmation.lower() == 'yes':
        # Assuming checkout() is a placeholder for actual checkout logic
        # For the purpose of this example, let's directly proceed with the assumption that checkout is successful
        checkout_success = checkout()  # Directly set to True for this example
        if checkout_success:
            for book in current_user.shopping_basket:
                current_user.add_order_history(book)
                print(f"'{book.title}' has been added to your order history.")

            # Clear the shopping basket after adding to order history
            current_user.shopping_basket.clear()
            print("Purchase completed successfully. Your order history has been updated.")
        else:
            print("There was an issue with the checkout process.")
    else:
        print("Purchase cancelled. Returning to the registered user menu.")
        # registered_user_menu() # Call to return to menu, assuming function exists
'''
def add_to_basket():
    global current_user
    if current_user is None:
        current_user = User("Guest", "", "", "")   
    while True:
        book_title = input("Enter the book title you want to add to your basket or type 'exit' to go back: ")
        if book_title.lower() == 'exit':
            break  # Allows the user to exit the loop
        
        book = next((book for book in books if book.title.lower() == book_title.lower()), None)
        
        if book:
            if book not in current_user.shopping_basket:  # Check for duplicates
                current_user.shopping_basket.append(book)
                print(f"{book.title} has been added to your basket.")
            else:
                print("This book is already in your basket.")
        else:
            print("Book not found. Please try again.")

def view_basket():
    if not current_user or not current_user.shopping_basket:
        print("Your basket is empty.")
        return
    for book in current_user.shopping_basket:
        print(f"Title: {book.title}, Author: {book.author}")

def guest_menu():
    while True:
        print("\n1. Search Books")
        print("2. View All Books")
        print("3. Add to Basket")
        print("4. View Basket")
        print("5. Purchase Books")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            search_books()
        elif choice == '2':
            view_all_books()
            input1 = input("Would you like to Purchase (yes/no): ")
            if input1 == 'yes':
                purchase_books()
        elif choice == '3':
            print("\nAvailable Books:")
            for idx, book in enumerate(books, 1):
                print(f"{idx}. Title: {book.title}, Author: {book.author}")
            add_to_basket()
            input1 = input("Would you like to Purchase (yes/no): ")
            if input1 == 'yes':
                purchase_books()
        elif choice == '4':
            view_basket()
        elif choice == '5':
            purchase_books()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

def registered_user_menu():
    while True:
        print("\n1. Search Books")
        print("2. View All Books")
        print("3. View Basket")
        print("4. Add to Basket")
        print("5. Purchase Books")
        print("6. View Order History")
        print("7. View Account Details")
        print("8. Modify Account Details")
        print("9. Logout")
        choice = input("Enter your choice: ")
        if choice == '1':
            search_books()
        elif choice == '2':
            view_all_books()
        elif choice == '3':
            view_basket()
            input1 = input("Would you like to Purchase (yes/no): ")
            if input1 == 'yes':
                purchase_books()
            input1 = input("Would you like to Purchase (yes/no): ")
            if input1 == 'yes':
                purchase_books() 
            else:
                registered_user_menu() 
        elif choice == '4':
            print("\nAvailable Books:")
            for idx, book in enumerate(books, 1):
                print(f"{idx}. Title: {book.title}, Author: {book.author}")
            add_to_basket()
            input1 = input("Would you like to Purchase (yes/no): ")
            if input1 == 'yes':
                purchase_books()
        elif choice == '5':
            purchase_books()
        elif choice == '6':
            view_order_history()
        elif choice == '7':
            view_account()
        elif choice == '8':
            modify_account()
        elif choice == '9':
            logout_user()
            break
        else:
            print("Invalid choice. Please try again.")

def main_menu():
    while True:
        print("\n1. Login")
        print("2. Create an Account")
        print("3. Continue as Guest")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            login_user()
        elif choice == '2':
            register_user()
        elif choice == '3':
            guest_menu()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.") 
def logout_user():
    global current_user
    current_user = None
    print("You have been logged out.")

if __name__ == "__main__":
    main_menu()

