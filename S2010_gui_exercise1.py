"""
Opgave "GUI step 1":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Bruge det, du har lært i GUI-eksempelfilerne, og byg den GUI, der er afbildet i images/gui_2010.png

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""

import tkinter as tk

padx = 24
pady = 8

main_window = tk.Tk()
main_window.title('my first GUI')
main_window.geometry("500x500")

# Create a label frame
# A label frame is used like a frame but its borders are visible
# and on the border is placed a label.
# You can find all possible options of tk.LabelFrame() in the following documentations:
# https://tkdocs.com/shipman/labelframe.html
# https://www.tutorialspoint.com/python/tk_labelframe.htm
frame_1 = tk.LabelFrame(main_window, text="Container")
frame_1.grid(row=0, column=0, padx=padx, pady=pady)


# Create a label
label_1 = tk.Label(frame_1, text="Id")
label_1.grid(row=1, column=2, padx=padx, pady=pady)

# Create an entry
entry_1 = tk.Entry(frame_1, width=4, justify="left")
entry_1.grid(row=2, column=2, padx=padx, pady=pady)
entry_1.insert(0, "")

# Create a button
button_1 = tk.Button(frame_1, text="Create")
button_1.grid(row=3, column=2, padx=padx, pady=pady)


if __name__ == "__main__":
    main_window.mainloop()
