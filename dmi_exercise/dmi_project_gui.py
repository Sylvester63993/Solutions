import tkinter as tk

padx = 24
pady = 8

main_window = tk.Tk()
main_window.title('my first GUI')
main_window.geometry("320x150")

# Create a label frame
# A label frame is used like a frame but its borders are visible
# and on the border is placed a label.
# You can find all possible options of tk.LabelFrame() in the following documentations:
# https://tkdocs.com/shipman/labelframe.html
# https://www.tutorialspoint.com/python/tk_labelframe.htm

# Create labelframe
labelframe_1 = tk.LabelFrame(main_window)
labelframe_1.grid(row=0, column=0, padx=padx, pady=pady)

# Create a label
label_1 = tk.Label(labelframe_1, text="Indtast start-år:")
label_1.grid(row=1, column=2, padx=padx, pady=pady)

# Create a label
label_2 = tk.Label(labelframe_1, text="Indtast slut-år:")
label_2.grid(row=1, column=3, padx=padx, pady=pady)

# Create an entry
entry_1 = tk.Entry(labelframe_1, width=4, justify="left")
entry_1.grid(row=2, column=2, padx=padx, pady=pady)
entry_1.insert(0, "")

# Create an entry
entry_2 = tk.Entry(labelframe_1, width=4, justify="left")
entry_2.grid(row=2, column=3, padx=padx, pady=pady)
entry_2.insert(0, "")

# Create a button
button_1 = tk.Button(labelframe_1, text="Show")
button_1.grid(row=3, column=2, padx=padx, pady=pady)


if __name__ == "__main__":
    main_window.mainloop()
