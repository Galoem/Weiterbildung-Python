import passgen
import tkinter as tk

def generate_password():
    lowers = int(spinbox_lowers.get()) if wanted_lowers.get() else 0
    uppers = int(spinbox_uppers.get()) if wanted_uppers.get() else 0
    numbers = int(spinbox_numbers.get()) if wanted_numbers.get() else 0
    specials = int(spinbox_specials.get()) if wanted_specials.get() else 0
    password = passgen.pwgenPro2(lowers, uppers, numbers, specials)
    label_password.config(text=password)

def copy_to_clipboard():
    app.clipboard_clear()
    app.clipboard_append(label_password.cget("text"))

def create_default_value(value):
    default_value = tk.IntVar(app, value)
    return default_value

def create_checkbox_in_grid(text: str, checked: tk.BooleanVar, row: int, col: int = 1):
    checkbox = tk.Checkbutton(text=text, variable=checked)
    checkbox.grid(row=row, column=col, sticky="W")
    return checkbox

def create_spinbox_in_grid(row: int, col: int = 2, start_value: int = 5):
    spinbox = tk.Spinbox(master=app, from_=0, to=10, textvariable=create_default_value(start_value))
    spinbox.grid(row=row, column=col, sticky="E")
    return spinbox

app = tk.Tk()
app.resizable(False, False)
app.geometry("300x200")

app.columnconfigure(0, weight=1)
app.columnconfigure(1, weight=1)
app.columnconfigure(2, weight=1)
app.columnconfigure(3, weight=1)

wanted_lowers = tk.BooleanVar(app, True)
wanted_uppers = tk.BooleanVar(app, True)
wanted_numbers = tk.BooleanVar(app, True)
wanted_specials = tk.BooleanVar(app, True)

checkbox_lowers = create_checkbox_in_grid(text="Include lowers", checked=wanted_lowers, row=1)
checkbox_uppers = create_checkbox_in_grid(text="Include uppers", checked=wanted_uppers, row=2)
checkbox_numbers = create_checkbox_in_grid(text="Include numbers", checked=wanted_numbers, row=3)
checkbox_specials = create_checkbox_in_grid(text="Include specials", checked=wanted_specials, row=4)

spinbox_lowers = create_spinbox_in_grid(row=1)
spinbox_uppers = create_spinbox_in_grid(row=2)
spinbox_numbers = create_spinbox_in_grid(row=3)
spinbox_specials = create_spinbox_in_grid(row=4)

button_generate_password = tk.Button(master=app, text="Generate Password", command=generate_password)
button_generate_password.grid(row=5, column=1, columnspan=2, sticky="EW", padx=5)

app.rowconfigure(6, weight=1)

label_password = tk.Label(background="light grey", width=1)
label_password.grid(row=7, column=1, columnspan=2, sticky="EW")

app.rowconfigure(8, weight=1)

button_copy_password = tk.Button(master=app, text="Copy Password", command=copy_to_clipboard)
button_copy_password.grid(row=9, column=1, columnspan=2, sticky="EW", padx=5)

app.rowconfigure(10, weight=1)

app.mainloop()
