import tkinter as tk
from functools import partial

def on_click(key):
    if key == 'C':
        display.set('0')
    elif key == '=':
        try:
            display.set(str(eval(display.get())))
        except:
            display.set("Error")
    else:
        display.set(key if display.get() == '0' else display.get() + key)

root = tk.Tk()
root.title("Casibua Calculator")
root.configure(bg="black")
root.geometry("400x600+800+180")

display = tk.StringVar(value='0')
tk.Label(root, textvariable=display, font=('Arial', 32), bg='gray', fg='white', anchor='e').grid(row=0, column=0, columnspan=4, sticky="nsew")

buttons = [('*', '//', '%', 'C'), ('7', '8', '9', '+'), ('4', '5', '6', '-'), ('1', '2', '3', '**'), ('.', '0', '=', '/')]
for r, row in enumerate(buttons, 1):
    for c, char in enumerate(row):
        tk.Button(root, text=char, font=('Arial', 24), bg='black', fg='white', command=partial(on_click, char)).grid(row=r, column=c, sticky="nsew")
for i in range(5): root.rowconfigure(i, weight=1)
for i in range(4): root.columnconfigure(i, weight=1)

root.mainloop()
