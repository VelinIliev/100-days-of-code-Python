import tkinter as tk
from tkinter import messagebox
from generate_pass import generate_random_password
import pyperclip

FONT = ("Arial", 10)
WIDTHx = 55

window = tk.Tk()
window.title("MyPass App")
# window.minsize(width=540,height=380)
window.config(padx = 50, pady = 50)

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
    if len(web_site)==0 or len(password)==0:
        messagebox.showinfo(title = "Ooops", message="Please provide info")
    else:
        is_ok = messagebox.askokcancel(title = f'{web_site}', message=f"These are the details entered\n website: {web_site}\n email:{email}\npassword: {password}\nIs it OK to save?")
        if is_ok:
            with open("./mypasswords.txt", mode = "a") as file:
                file.write(f"{web_site} | {email} | {password}\n")
                pass_input.delete(0,tk.END)
                web_input.delete(0, tk.END)
                messagebox.showinfo(title = "Confirmation", message="Password was saved")

# MyPass image
canvas = tk.Canvas(width=200, height=200)
mypass_image = tk.PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image = mypass_image)
canvas.grid(column=1, row=0)

# Website label
website_label = tk.Label(text="Website:", font= FONT)
website_label.grid(column=0, row=1)

# website input
web_input = tk.Entry(width = WIDTHx)
web_input.grid(column=1, row=1, columnspan=2)
web_input.focus()

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
pass_input = tk.Entry(width=36)
pass_input.grid(column=1, row=3)

# generate password button
gen_pass_btn = tk.Button(text = "Generate password", command=generate_password)
gen_pass_btn.grid(column=2, row=3)

# add button
add_btn = tk.Button(text = "Add", command=add_password, width=WIDTHx-8)
add_btn.grid(column=1, row=4, columnspan=2)
window.mainloop()