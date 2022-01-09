import tkinter as tk
import random
from tkinter.constants import W
import pandas
import os

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
    to_learn = data.to_dict(orient='records')
except FileNotFoundError:
    data = pandas.read_csv("./data/en_to_bg.csv")
    to_learn = data.to_dict(orient='records')

current_card = {}

def right_answer():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()

def flip_card():
    bg_word = current_card["Bulgarian"]
    canvas.itemconfig(card_bg_image, image = card_back_image)
    canvas.itemconfig(title_text, text="Български", fill="white")
    canvas.itemconfig(word_text, text=f"{bg_word}", fill="white")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    if len(to_learn) < 1:
        canvas.itemconfig(word_text, text=f"Няма повече думи", fill="red")
        os.remove("./data/words_to_learn.csv")
    else:
        current_card = random.choice(to_learn)
        eng_word = current_card["English"]

        canvas.itemconfig(card_bg_image, image = card_front_image)
        canvas.itemconfig(title_text, text="English", fill="black")
        canvas.itemconfig(word_text, text=f"{eng_word}", fill="black")

        flip_timer = window.after(3000, flip_card)


window = tk.Tk()
window.title("Guess the word")
window.config(padx = 50, pady=50, bg = BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = tk.Canvas(width=800, height=526)
card_front_image = tk.PhotoImage(file = "./images/card_front.png")
card_back_image = tk.PhotoImage(file="./images/card_back.png")
card_bg_image = canvas.create_image(400,263,image=card_front_image)
title_text = canvas.create_text(400, 150, text = "Title", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text = "word", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

cross_image = tk.PhotoImage(file="./images/wrong.png")
wrong_btn = tk.Button(image=cross_image, highlightthickness=0, command=next_card)
wrong_btn.grid(column=1, row=1)

check_image = tk.PhotoImage(file="./images/right.png")
right_btn = tk.Button(image=check_image, highlightthickness=0, command=right_answer)
right_btn.grid(column=0, row=1)

next_card()

window.mainloop()