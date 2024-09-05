import tkinter as tk
from tkinter import ttk


# Importering af egne filer og forkortelse af filnavne:
import plusbus_data as pbd
import plusbus_sql as pbsql

# region global constants
padx = 8  # Horizontal distance to neighboring objects
pady = 4  # Vertical distance to neighboring objects
rowheight = 24  # rowheight in treeview
treeview_background = "#eeeeee"  # color of background in treeview
treeview_foreground = "black"  # color of foreground in treeview
treeview_selected = "#206030"  # color of selected row in treeview
oddrow = "#dddddd"  # color of odd row in treeview
evenrow = "#cccccc"  # color of even row in treeview
# endregion global constants

# region kunde functions
# endregion kunde functions

# region common functions
# endregion common functions

# region common widgets
main_window = tk.Tk()  # Define the main window
main_window.title('AspIT S2: PlusBus')  # Text shown in the top window bar
main_window.geometry("1200x500")  # window size


style = ttk.Style()  # Add style
style.theme_use('default')  # Pick theme


# Configure treeview colors and formatting. A treeview is an object that can contain a data table.
style.configure("Treeview", background=treeview_background, foreground=treeview_foreground, rowheight=rowheight, fieldbackground=treeview_background)
style.map('Treeview', background=[('selected', treeview_selected)])  # Define color of selected row in treeview
# endregion common widgets

# region kunde widgets
# Define Labelframe which contains all container related GUI objects (data table, labels, buttons, ...)
labelframe_kunde = tk.LabelFrame(main_window, text="Kunde")  # https://www.tutorialspoint.com/python/tk_labelframe.htm
labelframe_kunde.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)  # https://www.tutorialspoint.com/python/tk_grid.htm

# Define data table (Treeview) and its scrollbar. Put them in a Frame.
tree_frame_kunde = tk.Frame(labelframe_kunde)  # https://www.tutorialspoint.com/python/tk_frame.htm
tree_frame_kunde.grid(row=0, column=0, padx=padx, pady=pady)
tree_scroll_kunde = tk.Scrollbar(tree_frame_kunde)
tree_scroll_kunde.grid(row=0, column=1, padx=0, pady=pady, sticky='ns')
tree_kunde = ttk.Treeview(tree_frame_kunde, yscrollcommand=tree_scroll_kunde.set, selectmode="browse")  # https://docs.python.org/3/library/tkinter.ttk.html#treeview
tree_kunde.grid(row=0, column=0, padx=0, pady=pady)
tree_scroll_kunde.config(command=tree_kunde.yview)

# Define the data table's formatting and content
tree_kunde['columns'] = ("id", "efternavn", "kontakt")  # Define columns
tree_kunde.column("#0", width=0, stretch=tk.NO)  # Format columns. Suppress the irritating first empty column.
tree_kunde.column("id", anchor=tk.E, width=40)  # "E" stands for East, meaning Right. Possible anchors are N, NE, E, SE, S, SW, W, NW and CENTER
tree_kunde.column("efternavn", anchor=tk.E, width=80)
tree_kunde.column("kontakt", anchor=tk.W, width=200)
tree_kunde.heading("#0", text="", anchor=tk.W)  # Create column headings
tree_kunde.heading("id", text="Id", anchor=tk.CENTER)
tree_kunde.heading("efternavn", text="Efternavn", anchor=tk.CENTER)
tree_kunde.heading("kontakt", text="Kontakt", anchor=tk.CENTER)
tree_kunde.tag_configure('oddrow', background=oddrow)  # Create tags for rows in 2 different colors
tree_kunde.tag_configure('evenrow', background=evenrow)

# Define Frame which contains labels, entries and buttons
controls_frame_kunde = tk.Frame(labelframe_kunde)
controls_frame_kunde.grid(row=3, column=0, padx=padx, pady=pady)

# Define Frame which contains labels (text fields) and entries (input fields)
edit_frame_kunde = tk.Frame(controls_frame_kunde)  # Add tuple entry boxes
edit_frame_kunde.grid(row=0, column=0, padx=padx, pady=pady)
# label and entry for kunde id
label_kunde_id = tk.Label(edit_frame_kunde, text="Id")  # https://www.tutorialspoint.com/python/tk_label.htm
label_kunde_id.grid(row=0, column=0, padx=padx, pady=pady)
entry_kunde_id = tk.Entry(edit_frame_kunde, width=4, justify="right")  # https://www.tutorialspoint.com/python/tk_entry.htm
entry_kunde_id.grid(row=1, column=0, padx=padx, pady=pady)
# label and entry for kunde efternavn
label_kunde_efternavn = tk.Label(edit_frame_kunde, text="Efternavn")
label_kunde_efternavn.grid(row=0, column=1, padx=padx, pady=pady)
entry_kunde_efternavn = tk.Entry(edit_frame_kunde, width=8, justify="right")
entry_kunde_efternavn.grid(row=1, column=1, padx=padx, pady=pady)
# label and entry for kunde kontakt
label_kunde_kontakt = tk.Label(edit_frame_kunde, text="Kontakt")
label_kunde_kontakt.grid(row=0, column=2, padx=padx, pady=pady)
entry_kunde_kontakt = tk.Entry(edit_frame_kunde, width=20)
entry_kunde_kontakt.grid(row=1, column=2, padx=padx, pady=pady)
# label and entry for kunde kontakt
label_kunde_weather = tk.Label(edit_frame_kunde, text="N/A")
label_kunde_weather.grid(row=0, column=3, padx=padx, pady=pady)
entry_kunde_weather = tk.Entry(edit_frame_kunde, width=14)
entry_kunde_weather.grid(row=1, column=3, padx=padx, pady=pady)

# Define Frame which contains buttons
button_frame_kunde = tk.Frame(controls_frame_kunde)
button_frame_kunde.grid(row=1, column=0, padx=padx, pady=pady)
# Define buttons
button_create_kunde = tk.Button(button_frame_kunde, text="Create")
button_create_kunde.grid(row=0, column=1, padx=padx, pady=pady)
button_update_kunde = tk.Button(button_frame_kunde, text="Update")
button_update_kunde.grid(row=0, column=2, padx=padx, pady=pady)
button_delete_kunde = tk.Button(button_frame_kunde, text="Delete")
button_delete_kunde.grid(row=0, column=3, padx=padx, pady=pady)
button_clear_boxes = tk.Button(button_frame_kunde, text="Clear Entry Boxes")
button_clear_boxes.grid(row=0, column=4, padx=padx, pady=pady)

# endregion kunde widgets

# region main program
if __name__ == "__main__":  # Executed when invoked directly. We use this so main_window.mainloop() does not keep our unit tests from running.
    main_window.mainloop()  # Wait for button clicks and act upon them
# endregion main program


