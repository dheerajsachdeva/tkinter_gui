from tkinter import *

window = Tk()
window.title("Miles to km converter")
window.minsize(500, 500)

input_text = Entry(width=10)
input_text.grid(column=5, row=1)

main_heading = Label(text="Enter Miles:")
main_heading.grid(column=0, row=0)

def button_clicked():
    global km_value
    get_value = float(input_text.get())
    result = get_value * 1.609
    km_value.config(text=f"{result}")


button_click = Button(text="Submit", command=button_clicked)
button_click.grid(column=5, row=6)

km_label = Label(text="Total km is")
km_value = Label(text="0")
km_value.grid(column=6, row=10)
km_label.grid(column=5, row=10)

window.mainloop()