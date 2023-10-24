from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    symbols = ['!','#','$','%','&','(',')','*','+']
    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbool = [choice(symbols) for _ in range(randint(2, 4))]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_symbool + password_number
    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_info():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if website_input.get() == "" or password_input.get() == "":
        messagebox.showinfo(title="Oops!", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as f:
                data = json.load(f)
                
        except FileNotFoundError:
            with open("data.json", "w") as f:
                json.dump(new_data, f, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as f:
                json.dump(new_data, f, indent=4)
                print(data)
        finally:        
            website_input.delete(0,END)
            password_input.delete(0, END)

# ------------------------ IIND PASSWORD --------------------------- #

def find_password():
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found.")
    else:
        site = website_input.get()
        email = data[site]['email']
        password = data[site]['password']
        if site in data:
            messagebox.showinfo(title=site, message=f"Email: {email},\n Password: {password}")
        else:
            messagebox.showerror(title="Error", message=f"No details for the {site} exists")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200,width=200)
password_image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=password_image)
canvas.grid(column=1,row=0)

website_text = Label(text="Website:")
website_text.grid(column=0,row=1)

email_user = Label(text="Email/Username:")
email_user.grid(column=0, row=2)

password_text = Label(text="Password:")
password_text.grid(column=0, row=3)

website_input = Entry(width=29)
website_input.grid(column=1, row=1)

email_input = Entry(width=45)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "seon@gmail.com")

password_input = Entry(width=29)
password_input.grid(column=1, row=3)

search = Button(width=14, text="Search", command=find_password)
search.grid(column=2,row=1)

generate = Button(text="Generate Password", command=generate_password)
generate.grid(column=2, row=3)

add = Button(text="Add", width=44, command=add_info)
add.grid(column=1, row=4, columnspan=2)

window.mainloop()