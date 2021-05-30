from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to Password Generator!")
    no_letters = random.randint(8, 10)
    no_symbols = random.randint(2, 4)
    no_numbers = random.randint(2, 4)

    # with shuffling
    password_letters = [random.choice(letters) for _ in range(no_letters)]
    password_symbols = [random.choice(symbols) for _ in range(no_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(no_numbers)]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """Take the required fields from the user and stores the data in json format"""
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "email": email,
        "password": password,
    }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Data warning", message="Please don't leave any fields empty")

    else:
        try:
            with open("password data.json", "r") as data_file:
               data = json.load(data_file) # reading the data
        except FileNotFoundError:
            with open("password data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("password data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ----------------------------FIND PASSWORD SETUP ------------------------------- #

def find_password():
    """Finds the password from the stored dataset"""
    website = website_entry.get()
    if website == "":
        messagebox.showinfo(title="Warning", message="Please specify the name of the website")
    try:
        with open("password data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Warning", message="File not found")
    else:
        if website in data:
            messagebox.showinfo(title=website, message= f"Email: {data[website]['email']}\n "
                                                        f"password: {data[website]['password']}")
        else:
            messagebox.showinfo(title="Warning", message=f"There are no details of {website} available")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("My Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=270, height=200)
logo_img = PhotoImage(file="password.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", font=("Arial", 12))
website_label.grid(column=0, row=1)
website_entry = Entry(text="", width=21)
website_entry.grid(column=1, row=1, columnspan=1)
website_entry.focus()

search_button = Button(text="Search",font=("Arial", 12), command=find_password)
search_button.grid(column=2, row=1)


email_label = Label(text="Email/Username:", font=("Arial", 12))
email_label.grid(column=0, row=2)
email_entry = Entry(text="", width=39)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "enter your email@gmail.com")


password_label = Label(text="Password:", font=("arial", 12))
password_label.grid(column=0, row=3)
password_entry = Entry(text="", width=21)
password_entry.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password", font=("Arial", 12), command=generate_password)
generate_password_button.grid(column=2, row=3, columnspan=2)

add_button = Button(text="Add", width=36, font=("Arial", 12), command=save)
add_button.grid(column=1, row=4, columnspan=3)

window.mainloop()
