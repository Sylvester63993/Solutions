""" Opgave "GUI step 2":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Bruge det, du har lært i GUI-eksempelfilerne, og byg den GUI, der er afbildet i images/gui_2020.png

Genbrug din kode fra "GUI step 1".

GUI-strukturen bør være som følger:
    main window
        labelframe
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

padx = 6
pady = 4

main_window = tk.Tk()
main_window.title('my first GUI')
main_window.geometry("500x500")

# Create a label frame
# A label frame is used like a frame but its borders are visible
# and on the border is placed a label.
# You can find all possible options of tk.LabelFrame() in the following documentations:
# https://tkdocs.com/shipman/labelframe.html
# https://www.tutorialspoint.com/python/tk_labelframe.htm
label_frame_1 = tk.LabelFrame(main_window, text="Container")
label_frame_1.grid(row=0, column=0, padx=padx, pady=pady)

# Create frame no. 1
frame_1 = tk.Frame(label_frame_1)
frame_1.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)

# Create a label
label_2 = tk.Label(frame_1, text="Id")
label_2.grid(row=1, column=1, padx=padx, pady=pady)

label_2 = tk.Label(frame_1, text="Weight")
label_2.grid(row=1, column=2, padx=padx, pady=pady)

label_2 = tk.Label(frame_1, text="Destination")
label_2.grid(row=1, column=3, padx=padx, pady=pady)

label_2 = tk.Label(frame_1, text="Weather")
label_2.grid(row=1, column=4, padx=padx, pady=pady)

# Create an entries
entry_1 = tk.Entry(label_frame_1, width=4, justify="left")
entry_1.grid(row=2, column=1, padx=padx, pady=pady)
entry_1.insert(0, "")

entry_2 = tk.Entry(label_frame_1, width=4, justify="left")
entry_2.grid(row=2, column=2, padx=padx, pady=pady)
entry_2.insert(0, "")

entry_3 = tk.Entry(label_frame_1, width=4, justify="left")
entry_3.grid(row=2, column=3, padx=padx, pady=pady)
entry_3.insert(0, "")

entry_4 = tk.Entry(label_frame_1, width=4, justify="left")
entry_4.grid(row=2, column=4, padx=padx, pady=pady)
entry_4.insert(0, "")

# Create frame no. 2
frame_2 = tk.Frame(label_frame_1)
frame_2.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)

# Create a buttons
button_1 = tk.Button(frame_2, text="Create")
button_1.grid(row=3, column=1, padx=padx, pady=pady)

button_2 = tk.Button(frame_2, text="Update")
button_2.grid(row=3, column=2, padx=padx, pady=pady)

button_3 = tk.Button(frame_2, text="Delete")
button_3.grid(row=3, column=3, padx=padx, pady=pady)

button_4 = tk.Button(frame_2, text="Clear entry boxes")
button_4.grid(row=3, column=4, padx=padx, pady=pady)

if __name__ == "__main__":
    main_window.mainloop()

