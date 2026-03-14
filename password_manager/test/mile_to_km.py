from tkinter import *


window = Tk()
window.title("Miles to Kilometer")
window.geometry("500x250")
window.config(padx=20, pady=20)


miles = StringVar(value="0")

miles_entry = Entry(window, font=("Consolas", 15), textvariable=miles)
miles_entry.grid(row=0, column=1)

miles_label = Label(window, text="Miles", font=("Consolas", 15))
miles_label.grid(row=0, column=2)

is_eqt = Label(window, text="is equal to:", font=("Consolas", 15))
is_eqt.grid(row=1, column=0)


km_output = Label(window, text="0.0", font=("Consolas", 15))
km_output.grid(row=1, column=1)

km_label = Label(window, text="KM", font=("Consolas", 15))
km_label.grid(row=1, column=2)

calc_button = Button(window, text="calculate", font=("Consolas", 12), command= lambda: calculate())
calc_button.grid(row=2, column=1)

nonsense_label = Label(window, text='Nonsense Slider Multiplier',font=("Consolas", 12))
nonsense_label.grid(row=3, column=1, pady=(20, 10))

def scale_miles(val):
    km_val = km_output.cget("text")
    try:
        float(km_val)
    except ValueError:
        return
        
    scaled_km_val = float(km_val) * int(val)
    print(scaled_km_val)
    km_output.config(text=str(scaled_km_val))


scale = Scale(window, from_=0, to=100, orient=HORIZONTAL, length=200, command=scale_miles)
scale.set(1)  # Set initial volume to 50%
scale.grid(row=4, column=1)




def calculate():
    mile_to_convert = miles.get()
    if not mile_to_convert.isdigit() or int(mile_to_convert) < 0:
        km_output.config(text="Invalid input", fg='red')
        return
    km = round(int(mile_to_convert) * 1.6093, 4)
    km_output.config(text=str(km))
    

window.mainloop()









