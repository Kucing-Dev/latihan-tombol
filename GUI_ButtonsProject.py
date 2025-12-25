import tkinter as tk

# jendela
root = tk.Tk()
root.title("Dasar tombol")
root.geometry("400x300")
root.configure(bg="#c2d3fd")

counter = 0

def increment():
    global counter
    counter += 1
    counter_label.config(text=f"Click: {counter}")

def reset():
    global counter
    counter = 0
    counter_label.config(text="Click: 0")

title_label = tk.Label(root, text="Click Counter", font=("Arial", 20), bg="#c2d3fd")
title_label.pack(pady=20)

counter_label = tk.Label(root, text="Click: 0", font=("Arial", 16), bg="#f6dec9")
counter_label.pack(pady=10)

increment_button = tk.Button(root, text="Click me", command=increment, font=("Arial", 12), bg="#f5cae6")
increment_button.pack(pady=10)

reset_button = tk.Button(root, text="Reset", command=reset, font=("Arial", 12), bg="#c3e6fc")
reset_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=root.destroy, font=("Arial", 12), bg="#ffc0cb")
exit_button.pack(pady=20)

root.mainloop()
