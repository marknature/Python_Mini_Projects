import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Class Assignment 1")
window.resizable(True, True)
window.configure(background="#87CEEB")

rb = ttk.LabelFrame(window, text="Robbit Breeder")
rb.grid(column=0, row=0, padx=10, pady=5)

# Mating Details
ttk.Label(rb, text="Mating Details", font=('Arial', 20,"bold")).grid(column=0, row=0)
ttk.Label(rb, text="Fathering Buck:").grid(column=0, row=1)
fb_entered = ttk.Entry(rb, width=16)
fb_entered.grid(column=1, row=1)
ttk.Label(rb, text="Mothering Doe:").grid(column=0, row=2)
md_entered = ttk.Entry(rb, width=16)
md_entered.grid(column=1, row=2)
ttk.Label(rb, text="D.O.M:").grid(column=0, row=3)
dom_entered = ttk.Entry(rb, width=16)
dom_entered.grid(column=1, row=3)
# end

# Litter Details
ttk.Label(rb, text="Litter Details", font=('Arial', 20, "bold")).grid(column=0, row=5)


def addTwoNumber():
    res = int(f_entered.get()) + int(m_entered.get())
    textv.set(res)


def clear():
    res1 = ""
    textv.set(res1)


number = tk.StringVar()
number1 = tk.StringVar()
ttk.Label(rb, text="No of female kits:").grid(column=0, row=6)
f_entered = ttk.Combobox(rb, width=6, text="No of female kits:", textvariable=number, state='readonly')
f_entered.grid(column=1, row=6)
f_entered['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
f_entered.current(0)
ttk.Label(rb, text="No of male kits:").grid(column=0, row=7)
m_entered = ttk.Combobox(rb, text="No of male kits:", width=6, textvariable=number1, state='readonly')
m_entered.grid(column=1, row=7)
m_entered['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
m_entered.current(0)
textv = tk.StringVar()
ttk.Label(rb, text="D.O.M:").grid(column=0, row=3)
ttk.Label(rb, text="Total Litter size: ").grid(column=0, row=8)
result = ttk.Label(rb, textvariable=textv)
result.grid(column=1, row=8)

action1 = ttk.Button(rb, text="UPDATE", width=8, command=addTwoNumber)
action1.grid(column=0, row=9)
action2 = ttk.Button(rb, text="CLEAR", width=6, command=clear)
action2.grid(column=0, row=9, padx=(120, 0))
# end
# How to create a date widget

ttk.Label(rb, text="230378 & 230143", font=('Arial', 8, "bold"), foreground="#A020f0").grid(column=0, row=10, padx=(300,0))
window.mainloop()
