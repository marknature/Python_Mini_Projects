import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta

# Create a window
window = tk.Tk()
window.title("VAP-Hatchery Incubation Service Receipt")
window.configure(bg="orange")

# Create widgets
frame = tk.Frame(window, bg="orange")
frame.pack(padx=20, pady=20)

title_label = tk.Label(frame, text="VAP-Hatchery Incubation Service Receipt", bg="orange", fg="white", font=("Arial", 14, "bold"))
title_label.pack(pady=10)

breed_label2 = tk.Label(frame, text="Name of Client:", bg="orange", fg="white")
breed_label2.pack(pady=5)
breed_entry = tk.Entry(frame, fg="white")
breed_entry.pack(pady=5)

breed_label3 = tk.Label(frame, text="Contact Number:", bg="orange", fg="white")
breed_label3.pack(pady=5)
breed_entry2 = tk.Entry(frame, fg="white")
breed_entry2.pack(pady=5)

breed_label4 = tk.Label(frame, text="Breed Incubated:", bg="orange", fg="white")
breed_label4.pack(pady=5)

breed_var = tk.StringVar()
breeds = [
    ('Chicken', '21'),
    ('Duck', '28')
]
for breed in breeds:
    r = ttk.Radiobutton(frame, text=breed[0], value=breed[1], variable=breed_var)
    r.pack(pady=5)

breed_combobox = ttk.Combobox(frame, textvariable=breed_var)
breed_combobox['values'] = ('Chicken', 'Duck')
breed_combobox.pack(pady=5)

incubation_date_label = tk.Label(frame, text="Date of Incubation:", bg="orange", fg="white")
incubation_date_label.pack(pady=5)

incubation_date_entry = tk.Entry(frame, bg="white")
incubation_date_entry.insert(0, datetime.now().strftime("%d-%m-%Y"))
incubation_date_entry.pack(pady=5)

expected_hatch_date_label = tk.Label(frame, text="Expected Date of Hatch:", bg="orange", fg="white")
expected_hatch_date_label.pack(pady=5)


def calculate_expected_hatch_date():
    incubation_date = datetime.strptime(incubation_date_entry.get(), "%d-%m-%Y")
    if breed_combobox.get() in ["Chicken", "21"]:
        incubation_period = 21
        expected_hatch_date = incubation_date + timedelta(days=incubation_period)
    else:
        incubation_period = 28
        expected_hatch_date = incubation_date + timedelta(days=incubation_period)
    expected_hatch_date_entry.delete(0, 'end')
    expected_hatch_date_entry.insert(0, expected_hatch_date.strftime("%d-%m-%Y"))


calculate_expected_hatch_date_button = tk.Button(frame, text="Calculate Expected Hatch Date", bg="green", fg="white", command=calculate_expected_hatch_date)
calculate_expected_hatch_date_button.pack(pady=5)

expected_hatch_date_entry = tk.Entry(frame, bg="white")
expected_hatch_date_entry.pack(pady=5)


def reset_entries():
    breed_entry.delete(0, 'end')
    breed_entry2.delete(0, 'end')
    incubation_date_entry.delete(0, 'end')
    expected_hatch_date_entry.delete(0, 'end')


reset_button = tk.Button(frame, text="Reset", bg="red", fg="white", command=reset_entries)
reset_button.pack(pady=10)

# Run the application (by Nature)
window.mainloop()
