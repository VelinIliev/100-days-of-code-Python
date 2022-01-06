import tkinter
def button_clicked():
    my_label["text"] = input.get()

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width = 500, height = 600)
window.config(padx=20, pady=20)

my_label = tkinter.Label(text="I am a label", font= ("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=20)

button = tkinter.Button(text = "Click me", command=button_clicked)
button.grid(column=1, row=1)

button2 = tkinter.Button(text = "BUT 2", command=button_clicked)
button2.grid(column=2, row=0)

input = tkinter.Entry(width = 20)
input.insert(tkinter.END, string = "placeholder")
input.grid(column=3, row=2)
# print(input.get())

window.mainloop()