from tkinter import *
from tkinter import ttk
from tkinter import messagebox


root = Tk()
root.title('codemy.com-currency conversion')
# root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x500")


# create tap
my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=5)

# create two frames
currency_frame = Frame(my_notebook, width=480, height=480)
conversion_frame = Frame (my_notebook, width=480, height=480)


currency_frame.pack(fill="both", expand=1)
conversion_frame.pack(fill="both", expand=1)

# add our tap
my_notebook.add(currency_frame, text="currencies")
my_notebook.add(conversion_frame, text="convert")

"""
currency stuff
"""
def lock():
    if not home_entry.get() or not conversion_entry.get or not rate_entry.get():
        messagebox.showwarning("WARNING!" "You Didn't Fill Out All The Fie")
    else:
        # disabled entry boxes
        home_entry.config(state="disabled")
        conversion_entry.config(state="disabled")
        rate_entry.config(state="disabled")
        # Enable tab
        my_notebook.tab(1, state='normal')
        # change tap field
        amount_label.config(text=f'Amount of {home_entry.get()} to convert {conversion_entry.get()}')
        converted_label.config(text=f'Equals this many {conversion_entry.get()}')
        convert_button.config(text=f'Convert from {home_entry.get()}')

def unlock():
    # Enable entry boxes
    home_entry.config(state="normal")
    conversion_entry.config(state="normal")
    rate_entry.config(state="normal")
    # Disable tab
    my_notebook.tab(1, state='disable')


home = LabelFrame(currency_frame, text="Your home currency")
home.pack(pady=20)

# home currency entry box
home_entry = Entry(home, font=("Helvetica",24))
home_entry.pack(pady=10, padx=10)

# conversion currency frame
conversion = LabelFrame(currency_frame, text="conversion currency")
conversion.pack(pady=20)


# convert to label
conversion_label = Label(conversion, text="currency to convert...")
conversion_label.pack(pady=10)

# convert to entry
conversion_entry = Entry(conversion,font=("Helvetica", 24))
conversion_entry.pack(pady=10, padx=10)




# rate label
rate_label = Label(conversion, text="current conversion rate...")
rate_label.pack(pady=10)

# rate to entry
rate_entry = Entry(conversion,font=("Helvetica", 24))
rate_entry.pack(pady=10, padx=10)

# button frame
button_frame = Frame(currency_frame)
button_frame.pack(pady=20)

# create button
# convert to label
conversion_label = Label(conversion, text="currency to convert...")
conversion_label.pack(pady=10)

# convert to entry
lock_button = Button(button_frame, text="Lock",command=lock)
lock_button.grid(row=0, column=0, padx=10)

unlock_button = Button(button_frame, text="UnLock",command=unlock)
unlock_button.grid(row=0, column=1, padx=10)

"""
         CONVERSION STUFF
"""

def convert():
    # clear converted entry box
    converted_entry.delete(0, END)

    # convert
    conversion = float(rate_entry.get()) * float(amount_entry.get())

    # convert to two decimals
    conversion = round(conversion,2)

    # add commas
    conversion = '{:,}'.format(conversion)

    # update entry box
    converted_entry.insert(0, conversion)

def clear():
    amount_entry.delete(0, END)
    converted_entry.delete(0, END)


amount_label = LabelFrame(conversion_frame, text="Amount To Convert")
amount_label.pack(pady=20)

# Entry box for amount
amount_entry = Entry(amount_label, font=("Helvetica", 24))
amount_entry.pack(pady=10, padx=10)

# Convert button
convert_button = Button(amount_label, text="Convert", command=convert)
convert_button.pack(pady=20)

# Equal frame
converted_label = LabelFrame(conversion_frame, text="Converted Currency")
converted_label.pack(pady=20)

# converted entry
converted_entry = Entry(converted_label, font=("Helvetica", 24), bd=0,)
converted_entry.pack(pady=10, padx=10)

# clear button
clear_button = Button(conversion_frame, text="Clear", command=clear)
clear_button.pack(pady=20)

# Fake label for spacing
spacer = Label(conversion_frame, text="", width=68)
spacer.pack()






root.mainloop()
