# First GUI
import tkinter as tk
from time import sleep
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg
from tkinter import Tk
from tkinter import Spinbox

root = Tk()
root.withdraw()
msg.showinfo("Welcome to Nature", "Python GUI created using tkinter:\nThe year is 2023")

win = tk.Tk()
win.title("Nature's Python GUI")
win.resizable(True, True)

tabControl = ttk.Notebook(win)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text="Tab 1")
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text="Tab 2")
tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text="Tab 3")
tabControl.pack(expand=1, fill='both')


# Tab 1
#  Frame - Mighty Design
mighty = ttk.LabelFrame(tab1, text='Mighty Design')
mighty.grid(column=0, row=0, padx=8, pady=4)


def click():
    action.configure(text="**Welcome to Nature!**")
    a_label.configure(background="#A020F0")
    a_label.configure(text="Code By NatureBoy")


a_label = ttk.Label(mighty, text="marknature_")
a_label.grid(column=0, row=0, sticky='W')
action = ttk.Button(mighty, text="Click Here!", command=click)
action.grid(column=1, row=0)


def clickme():
    action1.configure(text="Hello " + name_entered.get() + ". You have chosen: " + number_chosen.get())


ttk.Label(mighty, text="Enter name:").grid(column=0, row=1)
name = tk.StringVar()
name_entered = ttk.Entry(mighty, width=12, textvariable=name)
name_entered.grid(column=0, row=2)
action1 = ttk.Button(mighty, text="Click me!", command=clickme)
action1.grid(column=2, row=1)

ttk.Label(mighty, text="Choose a number:").grid(column=1, row=1)
number = tk.StringVar()
number_chosen = ttk.Combobox(mighty, width=12, textvariable=number)
number_chosen['values'] = (1, 3, 5, 7, 9)
number_chosen.grid(column=1, row=2)
number_chosen.current(0)

chVarDis = tk.IntVar()
check1 = tk.Checkbutton(mighty, text="Disabled", variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=3, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(mighty, text="Unchecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=3, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(mighty, text="Enabled", variable=chVarEn)
check3.select()
check3.grid(column=2, row=3, sticky=tk.W)

scrol_w = 30
scrol_h = 3
scr = scrolledtext.ScrolledText(mighty, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr.grid(column=0, row=4, sticky='WE', columnspan=3)

COLOR1 = 'Green'
COLOR2 = 'Purple'
COLOR3 = 'Gold'


def radcall():
    radsel = radVar.get()
    if radsel == 1:
        tab1.configure(foreground=COLOR1)
    elif radsel == 2:
        tab1.configure(foreground=COLOR2)
    elif radsel == 3:
        tab1.configure(foreground=COLOR3)


radVar = tk.IntVar()
rad1 = tk.Radiobutton(mighty, text=COLOR1, variable=radVar, value=1, command=radcall)
rad1.grid(column=0, row=8, sticky=tk.W, columnspan=3)
rad2 = tk.Radiobutton(mighty, text=COLOR2, variable=radVar, value=2, command=radcall)
rad2.grid(column=1, row=8, sticky=tk.W, columnspan=3)
rad3 = tk.Radiobutton(mighty, text=COLOR3, variable=radVar, value=3, command=radcall)
rad3.grid(column=2, row=8, sticky=tk.W, columnspan=3)

button_frame = ttk.LabelFrame(mighty, text=' ~ Attributes of Nature.')
button_frame.grid(column=0, row=13, padx=20, pady=40)
ttk.Label(button_frame, text="1_Independent - Can survive even without the existence of humans").grid(column=0, row=0)
ttk.Label(button_frame, text="2_Wild - In which all states can be both peaceful and dangerous").grid(column=0, row=1)
ttk.Label(button_frame, text="3_Mysterious - Has its own universe and is governed by its OwnLaws").grid(column=0, row=2)
ttk.Label(button_frame, text="4_Beautiful - Beauty lies in the eye of the beholder.").grid(column=0, row=3)
ttk.Label(button_frame, text="By NatureBoy").grid(column=0, row=4, sticky=tk.W)
for child in button_frame.winfo_children():
    child.grid_configure(padx=8, pady=4)

scrol_w = 30
scrol_h = 3
scr = scrolledtext.ScrolledText(mighty, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr.grid(column=0, row=10, columnspan=3)
# end


# Tab 2
# Frame - Nature Design
nature = ttk.LabelFrame(tab2, text='Nature Design')
nature.grid(column=0, row=0, padx=8, pady=4)


def clickme1():
    action3.configure(text="Hello " + name_entered1.get() + "! Are you " + number_chosen1.get() + " years old? ")


ttk.Label(nature, text="Enter name:").grid(column=0, row=1)
name1 = tk.StringVar()
name_entered1 = ttk.Entry(nature, width=12, textvariable=name1)
name_entered1.grid(column=0, row=2)
action3 = ttk.Button(nature, text="Click me!", command=clickme1)
action3.grid(column=2, row=1)

ttk.Label(nature, text="Your AGE:").grid(column=1, row=1)
number1 = tk.StringVar()
number_chosen1 = ttk.Combobox(nature, width=12, textvariable=number1)
number_chosen1['values'] = (19, 20, 21, 22, 23, 24, "old")
number_chosen1.grid(column=1, row=2)
number_chosen1.current(0)

chVarUn1 = tk.IntVar()
check21 = tk.Checkbutton(nature, text="Yes, i am.", variable=chVarUn1)
check21.deselect()
check21.grid(column=0, row=3, sticky=tk.W)

chVarEn1 = tk.IntVar()
check31 = tk.Checkbutton(nature, text="No, I'm not.", variable=chVarEn1)
check31.select()
check31.grid(column=1, row=3, sticky=tk.W)

chVarA = tk.IntVar()
check312 = tk.Checkbutton(nature, text="Age not represented.", variable=chVarA)
check312.select()
check312.grid(column=2, row=3, sticky=tk.W)

scrol_w1 = 30
scrol_h1 = 3
scr1 = scrolledtext.ScrolledText(nature, width=scrol_w1, height=scrol_h1, wrap=tk.WORD)
scr1.grid(column=0, row=4, columnspan=3)


def radcall1():
    radsel1 = radVar1.get()
    if radsel1 == 0:
        win.configure(background=colors[0])
    elif radsel1 == 1:
        win.configure(background=colors[1])
    elif radsel1 == 2:
        win.configure(background=colors[2])


colors = ["Blue", "Orange", "Red"]
radVar1 = tk.IntVar()
radVar1.set(99)
for col in range(3):
    curRad = tk.Radiobutton(nature, text=colors[col], variable=radVar1, value=col, command=radcall1)
    curRad.grid(column=col, row=9, sticky=tk.W)

button_frame = ttk.LabelFrame(nature, text=' ~ Attributes of Nature.')
button_frame.grid(column=0, row=13, padx=20, pady=40)
ttk.Label(button_frame, text="1_Independent").grid(column=0, row=0)
ttk.Label(button_frame, text="2_Wild").grid(column=0, row=1)
ttk.Label(button_frame, text="3_Mysterious").grid(column=0, row=2)
ttk.Label(button_frame, text="4_Beautiful").grid(column=0, row=3)
ttk.Label(button_frame, text="By NatureBoy").grid(column=0, row=4, sticky=tk.W)
for child in button_frame.winfo_children():
    child.grid_configure(padx=8, pady=4)


def _spin():
    value = spin.get()
    scrol.insert(tk.INSERT, value)


ttk.Label(nature, text="Enter a number:").grid(column=0, row=15)
number2 = tk.StringVar()
spin = Spinbox(nature, values=(1, 2, 4, 42, 100), width=5, bd=8, command=_spin, relief=tk.RIDGE)
spin.grid(column=0, row=16)

ttk.Label(nature, text="Choose a number:").grid(column=1, row=15)
number4 = tk.StringVar()
spin1 = Spinbox(nature, from_=19, to=30, width=5, bd=20)
spin1.grid(column=1, row=16)


class ToolTip(object):
    def __init__(self, widget):
        self.widget = widget
        self.tip_window = None

    def show_tip(self, tip_text):
        "Display text in a tooltip window"
        if self.tip_window or not tip_text:
            return
        x, y, _cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 25
        y = y + cy + self.widget.winfo_rooty() + 25
        self.tip_window = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry("+%d+%d" % (x, y))

        label = tk.Label(tw, text=tip_text, justify=tk.LEFT, background="#ffffe0", relief=tk.SOLID, borderwidth=1, font=("tahama", "8", "normal"))
        label.pack(ipadx=1)

    def hide_tip(self):
        tw = self.tip_window
        self.tip_window = None
        if tw:
            tw.destroy()


def create_ToolTip(widget, text):
    toolTip = ToolTip(widget)

    def enter(event):
        toolTip.show_tip(text)

    def leave(event):
        toolTip.hide_tip()
    widget.bind("<Enter>", enter)
    widget.bind("<Leave>", leave)


class AClass():
    pass


instance_of_a_class = AClass()
print(instance_of_a_class)

scrol_w2 = 30
scrol_h2 = 3
scrol = scrolledtext.ScrolledText(nature, width=scrol_w2, height=scrol_h2, wrap=tk.WORD)
scrol.grid(column=0, row=17, sticky='WE', columnspan=4)
create_ToolTip(scrol, "This is a ScrolledText widget")


def run_progressbar():
    progress_bar["maximum"] = 100
    for i in range(101):
        sleep(0.05)
        progress_bar["value"] = 1
        progress_bar.update()
    progress_bar["value"] = 0


def start_progressbar():
    progress_bar.start()


def stop_immediately():
    progress_bar.stop()


def progressbar_stop_after(wait_ms=1000):
    win.after(wait_ms, progress_bar.stop)


ttk.Button(button_frame, text=" Run Progressbar ", command=run_progressbar).grid(column=0, row=0, sticky='w')
ttk.Button(button_frame, text=" Start Progressbar ", command=start_progressbar).grid(column=0, row=1, sticky='w')
ttk.Button(button_frame, text=" Stop Immediately ", command=stop_immediately).grid(column=0, row=2, sticky='w')
ttk.Button(button_frame, text=" Stop after a second ", command=progressbar_stop_after).grid(column=0, row=3, sticky='w')

progress_bar = ttk.Progressbar(tab2, orient="horizontal", length=286, mode="determinate")
progress_bar.grid(column=0, row=18, pady=2)
# end

# Tab 3
tab3_frame = tk.Frame(tab3, bg='blue')
tab3_frame.pack()
for orange_color in range(2):
    canvas = tk.Canvas(tab3_frame, width=150, height=80, highlightthickness=0, bg='orange')
    canvas.grid(row=orange_color, column=orange_color)

def _quit():
    win.quit()
    win.destroy()
    exit()


menu_bar = Menu(win)
win.config(menu=menu_bar)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_separator()
file_menu.add_command(label="Add")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=_quit)
menu_bar.add_cascade(label="File", menu=file_menu)
# end


def _msgBox():
    msg.showinfo("Python Message Info Box", 'A Python GUI created using tkinter:\nThe year is 2023.')


def _mgBox():
    msg.showwarning("Python Message Warning Box", 'This warning was created using tkinter by Nature:\nThe year is 2023.')


def _mBox():
    msg.showerror("Python Message Error Box", 'This Error was created using tkinter by NatureBoy:\nThe year is 2023.')


def _answerBox():
    answer = msg.askyesnocancel("Python Message Multi Choice Box", "Are you sure really wish to do this?")
    if (answer == True):
       print("You may continuing.")
    elif (answer == False):
       print("Thank you for not continuing.")
    else:
       print(answer)


help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Äbout", command=_msgBox)
help_menu.add_command(label="Warning", command=_mgBox)
help_menu.add_command(label="Error", command=_mBox)
help_menu.add_command(label="Proceed", command=_answerBox)

win.iconbitmap(r'icon.ico')  # ICO Convert
name_entered.focus()
win.mainloop()
