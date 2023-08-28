# Future Leaders Bank

import tkinter as tk
import random
import string

def generate_random_password():
    password_length = 12  # Password Length
    characters = string.ascii_letters + string.digits + string.punctuation
    random_password = ''.join(random.choice(characters) for _ in range(password_length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, random_password)

def register_user():
    username = username_entry.get()
    password = password_entry.get()
    save_credentials(username, password)
    print("Registration successful!")
    show_login_page(username)

def save_credentials(username, password):
    with open("user_credentials.txt", "a") as file:
        file.write(f"Username: {username}\nPassword: {password}\n\n")

def show_login_page(username):
    root.withdraw()  # Hide the registration page

    login_window = tk.Toplevel()
    login_window.title("Future Leaders Bank Login")

    username_label = tk.Label(login_window, text="Username:")
    username_label.pack()
    username_entry = tk.Entry(login_window)
    username_entry.insert(0, username)  # Automatically load the registered username
    username_entry.pack()

    password_label = tk.Label(login_window, text="Password:")
    password_label.pack()
    password_entry = tk.Entry(login_window, show="*")
    password_entry.pack()

    login_button = tk.Button(login_window, text="Login", command=lambda: perform_login(username_entry.get(), password_entry.get(), login_window))
    login_button.pack()

def show_bank_window():
    bank_window = tk.Toplevel()
    bank_window.title("Future Leaders Bank")

    balance = 0  # Initial balance

    def update_balance(amount):
        nonlocal balance
        balance += amount
        balance_label.config(text=f"Balance: R {balance:.2f}")

    deposit_label = tk.Label(bank_window, text="Deposit Amount (R):")
    deposit_label.pack()
    deposit_entry = tk.Entry(bank_window)
    deposit_entry.pack()

    withdraw_label = tk.Label(bank_window, text="Withdraw Amount (R):")
    withdraw_label.pack()
    withdraw_entry = tk.Entry(bank_window)
    withdraw_entry.pack()

    deposit_button = tk.Button(bank_window, text="Deposit", command=lambda: update_balance(float(deposit_entry.get())))
    deposit_button.pack()

    withdraw_button = tk.Button(bank_window, text="Withdraw", command=lambda: update_balance(-float(withdraw_entry.get())))
    withdraw_button.pack()

    balance_label = tk.Label(bank_window, text=f"Balance: R {balance:.2f}")
    balance_label.pack()

def perform_login(username, password, login_window):
    with open("user_credentials.txt", "r") as file:
        lines = file.readlines()
        for i in range(0, len(lines), 3):
            saved_username = lines[i].strip().split(": ")[1]
            saved_password = lines[i + 1].strip().split(": ")[1]
            if username == saved_username and password == saved_password:
                print("Login successful!")
                login_window.destroy() # Close the login window
                show_bank_window()
                return

        print("Login failed!")

root = tk.Tk()
root.title("Future Leaders Bank Account Registration")

# Username input
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

# Password input
password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root)
password_entry.pack()

# Buttons
generate_button = tk.Button(root, text="Generate Password", command=generate_random_password)
generate_button.pack()

register_button = tk.Button(root, text="Register", command=register_user)
register_button.pack()

root.mainloop()