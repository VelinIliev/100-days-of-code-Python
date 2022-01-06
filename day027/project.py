import tkinter

FONT = ("Arial", 16)

window = tkinter.Tk()
window.title("Mile to km Converer")
window.minsize(width=260,height=120)
window.config(padx=20, pady=20)

def calculate_miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609344
    km_result['text'] = f'{km:.2f}' 

miles_input = tkinter.Entry(width = 7)
miles_input.grid(row=0, column=1)
miles_input.focus()

miles_label = tkinter.Label(text="Miles", font=FONT)
miles_label.grid(row=0, column=2)

equal_label = tkinter.Label(text="is euqal to", font=FONT)
equal_label.grid(row=1, column=0)

km_result = tkinter.Label(text="0", font=FONT)
km_result.grid(row=1, column=1)

km_label = tkinter.Label(text="Km", font=FONT)
km_label.grid(row=1, column=2)

button = tkinter.Button(text = "Calculate", command=calculate_miles_to_km)
button.grid(row=2, column=1)

window.mainloop()