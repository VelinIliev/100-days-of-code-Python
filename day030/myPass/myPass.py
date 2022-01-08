import tkinter as tk
from tkinter import messagebox
from generate_pass import generate_random_password
import pyperclip
import json

FONT = ("Arial", 10)
WIDTHx = 38
window = tk.Tk()
window.title("MyPass App")
# window.minsize(width=540,height=380)
window.config(padx = 20, pady = 20)

# search in json
# def search_data():
#     try:
#         with open("./mypasswords.json", mode = "r") as file:
#             data = json.load(file)
#             web_site = web_input.get()
#             email = data[web_site]["email"]
#             password = data[web_site]["password"]
#     except KeyError:
#         messagebox.showinfo(title = "Error", message=f"No such record: {web_site}")
#     except FileNotFoundError:
#         messagebox.showinfo(title = "Error", message="No records yet")
#     else: 
#         messagebox.showinfo(title = f"{web_site}", message=f'site: {web_site}\nemail: {email}\npassword: {password}')
#     finally:
#         web_input.delete(0, tk.END)  

def search_data():
    try:
        with open("./mypasswords.json", mode = "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title = "Error", message="No records yet")
    else: 
        web_site = web_input.get()
        if web_site in data: 
            email = data[web_site]["email"]
            password = data[web_site]["password"]
            messagebox.showinfo(title = f"{web_site}", message=f'site: {web_site}\nemail: {email}\npassword: {password}')
        else:
            messagebox.showinfo(title = "Error", message=f"No such record: {web_site}")

# generate random password & copy to clipboard
def generate_password():
    pass_input.delete(0,tk.END)
    password = generate_random_password(10,2,2)
    pass_input.insert(0, string = password)

    pyperclip.copy(password)
    messagebox.showinfo(title = "succes", message="Password is copied to clipboard")

# save password to file
def add_password():
    web_site = web_input.get()
    email = email_input.get()
    password = pass_input.get()
    new_data = {
        web_site:
        {
            "email": email,
            "password": password
        }
    }

    if len(web_site)==0 or len(password)==0:
        messagebox.showinfo(title = "Ooops", message="Please provide info")
    else:
        try:
            with open("./mypasswords.json", mode = "r") as file:
                # read data
                data = json.load(file)
                # update data
                data.update(new_data)
        except FileNotFoundError:
            with open("./mypasswords.json", mode = "w") as file:
                # save data if no file
                json.dump(new_data, file, indent=4)
                messagebox.showinfo(title = "Confirmation", message="Password was saved")
        else:
            with open("./mypasswords.json", mode = "w") as file:
                # save data if there is exsisting file
                json.dump(data, file, indent=4)
                messagebox.showinfo(title = "Confirmation", message="Password was saved")
        finally:
            pass_input.delete(0,tk.END)
            web_input.delete(0, tk.END)  

# MyPass image
canvas = tk.Canvas(width=200, height=200)
mypass_image = tk.PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image = mypass_image)
canvas.grid(column=1, row=0)

# Website label
website_label = tk.Label(text="Website:", font= FONT)
website_label.grid(column=0, row=1)

# website input
web_input = tk.Entry(width = 21)
web_input.grid(column=1, row=1)
web_input.focus()

# search button
search_btn = tk.Button(text = "Search", command=search_data, width=12)
search_btn.grid(column=2, row=1)

# email/username label
email_label = tk.Label(text="Email/Username:", font= FONT)
email_label.grid(column=0, row=2)

# email/username input
email_input = tk.Entry(width = WIDTHx)
email_input.insert(tk.END, string = "veliniliev@gmail.com")
email_input.grid(column=1, row=2, columnspan=2)

# password label
pass_labael = tk.Label(text="Password:", font= FONT)
pass_labael.grid(column=0, row=3)

# password input
pass_input = tk.Entry(width=21)
pass_input.grid(column=1, row=3)

# generate password button
gen_pass_btn = tk.Button(text = "Generate password", command=generate_password)
gen_pass_btn.grid(column=2, row=3)

# add button
add_btn = tk.Button(text = "Add", command=add_password, width=WIDTHx-2)
add_btn.grid(column=1, row=4, columnspan=2)
window.mainloop()