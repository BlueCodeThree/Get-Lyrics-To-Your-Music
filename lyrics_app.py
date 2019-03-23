import tkinter as tk

HEIGHT = 500
WIDTH = 600

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH).pack()

frame = tk.Frame(root, bg="#80c1ff")
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8) # relative width etc, the numbers add up to 100%

button = tk.Button(frame, text="Test button", bg="grey", fg="red").pack(side="left", fill="x", expand=True)

label = tk.Label(frame, text="This is a label", bg="yellow").pack(side="left", fill="both")

entry = tk.Entry(frame, bg="green").pack(side="left", fill="both")

root.mainloop()