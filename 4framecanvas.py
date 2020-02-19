import tkinter as tk

# main window
root = tk.Tk()
root.wm_geometry("200x200")
root.grid()

blue_frame = tk.Frame(root, bg="blue", height=100, width=100)
blue_frame.grid(row=0, column=0)

red_frame = tk.Frame(root, bg="red", height=100, width=100)
red_frame.grid(row=1, column=0)

yellow_frame = tk.Frame(root, bg="yellow", height=100, width=100)
yellow_frame.grid(row=1, column=1)

green_frame = tk.Frame(root, bg="green", height=100, width=100)
green_frame.grid(row=0, column=1)

root.mainloop()