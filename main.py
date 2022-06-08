from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project

def find_password():
    try:
        with open("data.json", "r") as file:
            load_data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Opps", message="No Data File Found.")
    else:
        try:
            data = load_data[website_entry.get()]
        except KeyError:
            messagebox.showinfo(title="Opps", message="No details for the website exist.")
        else:
            messagebox.showinfo(title="Found", message=f"Website: {website_entry.get()} was found\nEmail: {data['email']}\nPassword: {data['password']}")



def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 15)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


def add():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Opps", message="Please do not leave any of the entries empty.")
    else:
        try:
            with open("data.json", 'r') as file:
                # read old data
                data = json.load(file)

        except FileNotFoundError:
            with open("data.json", 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            # update old data with new data
            data.update(new_data)
            with open("data.json", 'w') as file:
                # saving updated data
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)


# Website label and entry
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=16)
website_entry.grid(column=1, row=1, columnspan=1)
website_entry.focus()

# Search Button
search_button = Button(text="Search",  width=15, command=find_password)
search_button.grid(column=2, row=1)

# Email/Username label and entry
email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

email_username_entry = Entry(width=35)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(0, "test_email@gmail.com")
# password label and entry
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=16)
password_entry.grid(column=1, row=3)

# Generate password button
generate_button = Button(text="Generate Password", width=15, command=generate_password)
generate_button.grid(column=2, row=3)

# Add button
add_button = Button(text="Add", width=36, command=add)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
