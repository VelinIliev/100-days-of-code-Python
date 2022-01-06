import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width = 500, height = 600)

# Label
my_label = tkinter.Label(text="I am a label", font= ("Arial", 24, "bold"))
my_label.pack()
# pack(side="left" expand=True)
# my_label["text"] = "New text"

# Button

def button_clicked():
    my_label["text"] = input.get()


button = tkinter.Button(text = "Click me", command=button_clicked)
button.pack()

# Entry

input = tkinter.Entry(width = 20)
input.insert(tkinter.END, string = "placeholder")
input.pack()
print(input.get())

# Text
text = tkinter.Text(height=5, width=30)
text.focus()
text.insert(tkinter.END, "Example of multy-line text entry.")
print(text.get("1.0", tkinter.END))
text.pack()

# Spinbox
def spinbox_used():
    print(spinbox.get())

spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

# Scale
def scale_used(value):
    print(value)

scale = tkinter.Scale(from_=0, to=100, command=scale_used)
scale.pack()

# Checkbox
def checkbutton_used():
    print(checked_state.get())

checked_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text="is ON?", variable = checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

# Radiobutton
def radio_used():
    print(radio_state.get())

radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tkinter.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

# Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = tkinter.Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()