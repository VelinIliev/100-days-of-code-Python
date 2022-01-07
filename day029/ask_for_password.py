import tkinter as tk



def define_password():
    def go_quit():
        letters = letters_input.get()
        numbers = numbers_input.get()
        symbols = symbols_input.get()
        window2.quit()
        return (letters, numbers, symbols)

    window2 = tk.Tk()
    window2.title("Define Password")
    window2.minsize(width=200,height=200)
    window2.config(padx = 20, pady = 20)

    # letters label
    lettes_label = tk.Label(text="How many letters:")
    lettes_label.grid(column=0, row=0)

    # letters input
    letters_input = tk.Entry()
    letters_input.grid(column=1, row=0)
    letters_input.focus()

    # numbers label
    numbers_label = tk.Label(text="How many numbers:")
    numbers_label.grid(column=0, row=1)

    # numbers input
    numbers_input = tk.Entry()
    numbers_input.grid(column=1, row=1)

    # symbols label
    symbols_label = tk.Label(text="How many symbols:")
    symbols_label.grid(column=0, row=2)

    # numbers input
    symbols_input = tk.Entry()
    symbols_input.grid(column=1, row=2)

    # OK btn
    ok_btn = tk.Button(text = "OK", command=go_quit)
    ok_btn.grid(column=1, row=4)

    window2.mainloop()

define_password()