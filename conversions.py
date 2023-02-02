from tkinter import *

def mi_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    km_result_label.config(text=f"{km}")

window = Tk()
window.title("Miles to Kilometer conversion")
window.config(padx=20, pady=20)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Enter Miles")
miles_label.grid(column=2, row=0)

equal_to_label = Label(text="entered miles is equal to")
equal_to_label.grid(column=0, row=1)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

km_label = Label(text="KM")
km_label.grid(column=2, row=1)

calculate = Button(text="Calculate", command=mi_to_km)
calculate.grid(column=1, row=2)

window.mainloop()
