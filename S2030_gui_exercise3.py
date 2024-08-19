"""Opgave "GUI step 3":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Bruge det, du har lært i GUI-eksempelfilerne, og byg den GUI, der er afbildet i images/gui_2030.png

Genbrug din kode fra "GUI step 2".

GUI-strukturen bør være som følger:
    main window
        labelframe
            frame
                treeview and scrollbar
            frame
                labels and entries
            frame
                buttons

Funktionalitet:
    Klik på knappen "clear entry boxes" sletter teksten i alle indtastningsfelter (entries).


Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""

import tkinter as tk
from tkinter import ttk

# function which deletes all entries
def empty_entry():
    print("All entry boxes cleared!")
    entry_1.delete(0, tk.END)  # Delete text in the entry box, beginning with the first character (0) and ending with the last character (tk.END)
    entry_2.delete(0, tk.END)  # Delete text in the entry box, beginning with the first character (0) and ending with the last character (tk.END)
    entry_3.delete(0, tk.END)  # Delete text in the entry box, beginning with the first character (0) and ending with the last character (tk.END)
    entry_4.delete(0, tk.END)  # Delete text in the entry box, beginning with the first character (0) and ending with the last character (tk.END)


# padding værdier sættes
padx = 8
pady = 4

# hovedvindue oprettes, navngives og størrelse defineres
main_window = tk.Tk()
main_window.title('my first GUI')
main_window.geometry("500x500")

# Create a label frame
# A label frame is used like a frame but its borders are visible
# and on the border is placed a label.
# You can find all possible options of tk.LabelFrame() in the following documentations:
# https://tkdocs.com/shipman/labelframe.html
# https://www.tutorialspoint.com/python/tk_labelframe.htm
labelframe_1 = tk.LabelFrame(main_window, text="Container")
labelframe_1.grid(row=0, column=0, padx=pady, pady=pady)

# frames created and positioned
frame_1 = tk.Frame(labelframe_1)
frame_1.grid(row=0, column=0, padx=padx, pady=pady)
frame_2 = tk.Frame(labelframe_1)
frame_2.grid(row=1, column=0, padx=padx, pady=pady)

# labels created and positioned
label_1 = tk.Label(frame_1, text="Id")
label_1.grid(row=0, column=0, padx=padx, pady=pady)
label_2 = tk.Label(frame_1, text="Weight")
label_2.grid(row=0, column=1, padx=padx, pady=pady)
label_3 = tk.Label(frame_1, text="Destination")
label_3.grid(row=0, column=2, padx=padx, pady=pady)
label_4 = tk.Label(frame_1, text="Weather")
label_4.grid(row=0, column=3, padx=padx, pady=pady)

# entries created and positioned
entry_1 = tk.Entry(frame_1, width=4, justify="left")
entry_1.grid(row=1, column=0, padx=padx, pady=pady)
entry_1.insert(0, "This is an entry. Edit me!")
entry_2 = tk.Entry(frame_1, width=10, justify="left")
entry_2.grid(row=1, column=1, padx=padx, pady=pady)
entry_2.insert(0, "This is an entry. Edit me!")
entry_3 = tk.Entry(frame_1, width=20, justify="left")
entry_3.grid(row=1, column=2, padx=padx, pady=pady)
entry_3.insert(0, "This is an entry. Edit me!")
entry_4 = tk.Entry(frame_1, width=14, justify="left")
entry_4.grid(row=1, column=3, padx=padx, pady=pady)
entry_4.insert(0, "This is an entry. Edit me!")

# buttons created and positioned
button_1 = tk.Button(frame_2, text="Create")
button_1.grid(row=2, column=0, padx=padx, pady=pady)
button_2 = tk.Button(frame_2, text="Update")
button_2.grid(row=2, column=1, padx=padx, pady=pady)
button_3 = tk.Button(frame_2, text="Delete")
button_3.grid(row=2, column=2, padx=padx, pady=pady)
button_4 = tk.Button(frame_2, text="Clear Entry Boxes", command=empty_entry)  # button number 4 set to clear all entries
button_4.grid(row=2, column=3, padx=padx, pady=pady)

if __name__ == "__main__":
    main_window.mainloop()



