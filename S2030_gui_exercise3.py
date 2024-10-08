"""Opgave "GUI step 3":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Bruge det, du har lært i GUI-eksempelfilerne, og byg den GUI, der er afbildet i images/gui_2030.png

Genbrug din kode fra "GUI step 2".

GUI-strukturen bør være som følger :
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

# def read_table(tree):  # fill tree with test data
#     count = 0  # Use counter to keep track of odd and even rows, because these will be colored differently. (2)
#     for record in test_data_list:
#         if count % 2 == 0:  # even
#             tree.insert(parent='', index='end', text='', values=record, tags=('evenrow',))  # Insert one row into the data table
#         else:  # odd
#             tree.insert(parent='', index='end', text='', values=record, tags=('oddrow',))  # Insert one row into the data table
#         count += 1


# padding værdier sættes
padx = 8
pady = 4
# værdier for treeview
rowheight = 24
treeview_background = "#eeeeee"
treeview_foreground = "black"
treeview_selected = "#773333"
oddrow = "#ddeedd"  # color of odd row in treeview (1)
evenrow = "#cce0cc"  # color of even row in treeview

# add test data by hard coding a list of tuples
# test_data_list = []
# test_data_list.append(("1", "hello", 7000))
# test_data_list.append(("2", "data!", 3000))
# test_data_list.append(("3", "tests", 3000))
# test_data_list.append(("4", "users", 8000))
# test_data_list.append(("1", "hello", 6000))
# test_data_list.append(("2", "data!", 2000))
# test_data_list.append(("3", "tests", 1000))
# test_data_list.append(("4", "users", 3000))
# test_data_list.append(("1", "hello", 4000))
# test_data_list.append(("2", "data!", 5000))
# test_data_list.append(("3", "tests", 9000))
# test_data_list.append(("4", "users", 7000))

# hovedvindue oprettes, navngives og størrelse defineres
main_window = tk.Tk()
main_window.title('my first GUI')
main_window.geometry("900x500")

style = ttk.Style()  # Configure treeview style and colors
style.theme_use('default')
style.configure("Treeview", background=treeview_background, foreground=treeview_foreground, rowheight=rowheight, fieldbackground=treeview_background)
style.map('Treeview', background=[('selected', treeview_selected)])

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
frame_3 = tk.Frame(labelframe_1, padx=padx, pady=pady)
frame_3.grid(row=2, column=0, padx=padx)

# labels created and positioned
label_1 = tk.Label(frame_2, text="Id")
label_1.grid(row=0, column=0, padx=padx, pady=pady)
label_2 = tk.Label(frame_2, text="Weight")
label_2.grid(row=0, column=1, padx=padx, pady=pady)
label_3 = tk.Label(frame_2, text="Destination")
label_3.grid(row=0, column=2, padx=padx, pady=pady)
label_4 = tk.Label(frame_2, text="Weather")
label_4.grid(row=0, column=3, padx=padx, pady=pady)

# entries created and positioned
entry_1 = tk.Entry(frame_2, width=4, justify="left")
entry_1.grid(row=1, column=0, padx=padx, pady=pady)
entry_1.insert(0, "This is an entry. Edit me!")
entry_2 = tk.Entry(frame_2, width=10, justify="left")
entry_2.grid(row=1, column=1, padx=padx, pady=pady)
entry_2.insert(0, "This is an entry. Edit me!")
entry_3 = tk.Entry(frame_2, width=20, justify="left")
entry_3.grid(row=1, column=2, padx=padx, pady=pady)
entry_3.insert(0, "This is an entry. Edit me!")
entry_4 = tk.Entry(frame_2, width=14, justify="left")
entry_4.grid(row=1, column=3, padx=padx, pady=pady)
entry_4.insert(0, "This is an entry. Edit me!")

# buttons created and positioned
button_1 = tk.Button(frame_3, text="Create")
button_1.grid(row=2, column=0, padx=padx, pady=pady)
button_2 = tk.Button(frame_3, text="Update")
button_2.grid(row=2, column=1, padx=padx, pady=pady)
button_3 = tk.Button(frame_3, text="Delete")
button_3.grid(row=2, column=2, padx=padx, pady=pady)
button_4 = tk.Button(frame_3, text="Clear Entry Boxes", command=empty_entry)  # button number 4 set to clear all entries
button_4.grid(row=2, column=3, padx=padx, pady=pady)

# Create a data table (Treeview) and its scrollbar.
# Treeviews present data (for example from a database) in a table.
# You can find all possible options of ttk.Treeview() in the following documentations:
# https://docs.python.org/3/library/tkinter.ttk.html#treeview
# Additionaly, create a scrollbar and connect it to the treeview
# You can find all possible options of tk.Scrollbar() in the following documentations:
# https://tkdocs.com/shipman/scrollbar.html
# https://www.tutorialspoint.com/python/tk_scrollbar.htm
tree_1_scrollbar = tk.Scrollbar(frame_1)  # define the scrollbar
tree_1_scrollbar.grid(row=0, column=0, padx=padx, pady=pady, sticky='ns')  # place the scrollbar
tree_1 = ttk.Treeview(frame_1, yscrollcommand=tree_1_scrollbar.set, selectmode="browse")  # define the treeview, connect it with the scrollbar
tree_1.grid(row=0, column=0, padx=0, pady=pady)  # place the treeview
tree_1_scrollbar.config(command=tree_1.yview)  # connect the scrollbar with the treeview

tree_1['columns'] = ("col1", "col2", "col3")  # Define treeview columns
tree_1.column("#0", width=0, stretch=tk.NO)
tree_1.column("col1", anchor=tk.E, width=90)
tree_1.column("col2", anchor=tk.W, width=130)
tree_1.column("col3", anchor=tk.W, width=180)

tree_1.heading("#0", text="", anchor=tk.W) # Create treeview column headings
tree_1.heading("col1", text="Id", anchor=tk.CENTER)
tree_1.heading("col2", text="Weight", anchor=tk.CENTER)
tree_1.heading("col3", text="Destination", anchor=tk.CENTER)

# tree_1.tag_configure('oddrow', background=oddrow)  # Create tags for rows in 2 different colors (3)
# tree_1.tag_configure('evenrow', background=evenrow)

# read_table(tree_1)  # read the test data into the treeview

if __name__ == "__main__":
    main_window.mainloop()



