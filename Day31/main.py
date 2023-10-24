from tkinter import *
from pandas import *
from random import *

BACKGROUND_COLOR = "#B1DDC6"
currnet_card = {}
to_learn= {}

# Read the CSV File
try:
    data = read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")

else:
    to_learn = data.to_dict(orient="records")

    
# New Flash card
def new_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(card_image, image=card_front)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    window.after(3000, func=flip_card)

# Filp the card
def flip_card():
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")

def is_known():
    to_learn.remove(current_card)
    data = DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    new_card()


# UI Interface

window = Tk()
window.title("Flashcard")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width = 800, height = 526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back =PhotoImage(file="images/card_back.png")

card_image = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="", font = ("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong = Button(image=wrong_image, highlightthickness=0, command=new_card)
wrong.grid(column=0, row=1)

right_image = PhotoImage(file="images/right.png")
right = Button(image=right_image, highlightthickness=0, command=is_known)
right.grid(column=1, row=1)

new_card()

window.mainloop()