import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(str(entry.get())))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Setup
root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, font="Arial 20", borderwidth=2, relief=tk.RIDGE, justify=tk.RIGHT)
entry.pack(padx=10, pady=10, fill=tk.BOTH)

# Buttons
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', 'C', '=', '+']
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for item in row:
        btn = tk.Button(frame, text=item, font="Arial 18", height=2, width=5)
        btn.pack(side=tk.LEFT, expand=True, fill="both")
        btn.bind("<Button-1>", click)

root.mainloop()
