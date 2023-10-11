from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)


#Label

def converter():
    miles = float(input.get())
    km = miles * 1.609
    result.config(text=f"{km}")

is_equal = Label(text="is equal to")
is_equal.grid(column=0, row=1)

result = Label(text="0")
result.grid(column=1, row=1)

mile = Label(text="Miles")
mile.grid(column=2, row=0)

km = Label(text="Km")
km.grid(column=2, row=1)

#Button
    
button = Button(text="Calculate", command=converter)
button.grid(column=1, row=2)

#Entry

input = Entry(width=7)
input.grid(column=1, row=0)

window.mainloop()
