import tkinter as tk
from tkinter import ttk

# Importering af egne filer og forkortelse af filnavne:
import plusbus_data as pbd
import plusbus_sql as pbsql
import plusbus_func as pbf

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
def read_kunde_entries():  # Read content of entry boxes
    return entry_kunde_id.get(), entry_kunde_efternavn.get(), entry_kunde_kontakt.get(),


def clear_kunde_entries():  # Clear entry boxes
    entry_kunde_id.delete(0, tk.END)  # Delete text in entry box, beginning with the first character (0) and ending with the last character (tk.END)
    entry_kunde_efternavn.delete(0, tk.END)
    entry_kunde_kontakt.delete(0, tk.END)
    # entry_kunde_weather.delete(0, tk.END)


def write_kunde_entries(values):  # Fill entry boxes
    entry_kunde_id.insert(0, values[0])
    entry_kunde_efternavn.insert(0, values[1])
    entry_kunde_kontakt.insert(0, values[2])


def edit_kunde(event, tree):  # Copy selected tuple into entry boxes. Parameter event is mandatory but we don't use it.
    index_selected = tree.focus()  # Index of selected tuple
    values = tree.item(index_selected, 'values')  # Values of selected tuple
    clear_kunde_entries()  # Clear entry boxes
    write_kunde_entries(values)  # Fill entry boxes


def create_kunde(tree, record):  # add new tuple to database
    kunde = pbd.Kunde.convert_from_tuple(record)  # Convert tuple to Kunde
    pbsql.create_record(kunde)  # Update database
    clear_kunde_entries()  # Clear entry boxes
    refresh_treeview(tree, pbd.Kunde)  # Refresh treeview table


def update_kunde(tree, record):  # update tuple in database
    kunde = pbd.Kunde.convert_from_tuple(record)  # Convert tuple to Kunde
    pbsql.update_kunde(kunde)  # Update database
    clear_kunde_entries()  # Clear entry boxes
    refresh_treeview(tree, pbd.Kunde)  # Refresh treeview table


def delete_kunde(tree, record):  # delete tuple in database
    kunde = pbd.Kunde.convert_from_tuple(record)  # Convert tuple to Kunde
    pbsql.delete_soft_kunde(kunde)  # Update database
    clear_kunde_entries()  # Clear entry boxes
    refresh_treeview(tree, pbd.Kunde)  # Refresh treeview table
# endregion kunde functions

# region rejse functions
def read_rejse_entries():  # Read content of entry boxes
    return entry_rejse_id.get(), entry_rejse_rute.get(), entry_rejse_dato.get(), entry_rejse_pladskapacitet.get()


def clear_rejse_entries():  # Clear entry boxes
    entry_rejse_id.delete(0, tk.END)  # Delete text in entry box, beginning with the first character (0) and ending with the last character (tk.END)
    entry_rejse_rute.delete(0, tk.END)
    entry_rejse_dato.delete(0, tk.END)
    entry_rejse_pladskapacitet.delete(0, tk.END)


def write_rejse_entries(values):  # Fill entry boxes
    entry_rejse_id.insert(0, values[0])
    entry_rejse_rute.insert(0, values[1])
    entry_rejse_dato.insert(0, values[2])
    entry_rejse_pladskapacitet.insert(0, values[3])


def edit_rejse(event, tree):  # Copy selected tuple into entry boxes. Parameter event is mandatory but we don't use it.
    index_selected = tree.focus()  # Index of selected tuple
    values = tree.item(index_selected, 'values')  # Values of selected tuple
    clear_rejse_entries()  # Clear entry boxes
    write_rejse_entries(values)  # Fill entry boxes


def create_rejse(tree, record):  # add new tuple to database
    rejse = pbd.Rejse.convert_from_tuple(record)  # Convert tuple to Rejse
    # if rejse.dato != "": # midlertidig hotfix
    pbsql.create_record(rejse)  # Update database
    clear_rejse_entries()  # Clear entry boxes
    refresh_treeview(tree, pbd.Rejse)  # Refresh treeview table


def update_rejse(tree, record):  # update tuple in database
    rejse = pbd.Rejse.convert_from_tuple(record)  # Convert tuple to Rejse
    # if rejse.dato != "":  # midlertidig hotfix
    pbsql.update_rejse(rejse)  # Update database
    clear_rejse_entries()  # Clear entry boxes
    refresh_treeview(tree, pbd.Rejse)  # Refresh treeview table


def delete_rejse(tree, record):  # delete tuple in database
    rejse = pbd.Rejse.convert_from_tuple(record)  # Convert tuple to Rejse
    pbsql.delete_soft_rejse(rejse)  # Update database
    clear_rejse_entries()  # Clear entry boxes
    refresh_treeview(tree, pbd.Rejse)  # Refresh treeview table
# endregion rejse functions

# region booking functions
def read_booking_entries():  # Read content of entry boxes
    return entry_booking_id.get(), entry_booking_kunde_id.get(), entry_booking_rejse_id.get(), entry_booking_pladser.get(),


def clear_booking_entries():  # Clear entry boxes
    entry_booking_id.delete(0, tk.END)  # Delete text in entry box, beginning with the first character (0) and ending with the last character (tk.END)
    entry_booking_kunde_id.delete(0, tk.END)
    entry_booking_rejse_id.delete(0, tk.END)
    entry_booking_pladser.delete(0, tk.END)


def write_booking_entries(values):  # Fill entry boxes
    entry_booking_id.insert(0, values[0])
    entry_booking_kunde_id.insert(0, values[1])
    entry_booking_rejse_id.insert(0, values[2])
    entry_booking_pladser.insert(0, values[3])


def edit_booking(event, tree):  # Copy selected tuple into entry boxes. Parameter event is mandatory but we don't use it.
    index_selected = tree.focus()  # Index of selected tuple
    values = tree.item(index_selected, 'values')  # Values of selected tuple
    clear_booking_entries()  # Clear entry boxes
    write_booking_entries(values)  # Fill entry boxes


def create_booking(tree, record):  # add new tuple to database
    booking = pbd.Booking.convert_from_tuple(record)  # Convert tuple to Booking
    pbsql.create_record(booking)  # Update database
    clear_booking_entries()  # Clear entry boxes
    refresh_treeview(tree, pbd.Booking)  # Refresh treeview table

# def create_booking2(tree, record):  # add new tuple to database
#     booking = pbd.Booking.convert_from_tuple(record)  # Convert tuple to Booking
#     capacity_ok = pbf.capacity_available(pbsql.get_record(pbd.Rejse, booking.rejse_id), booking.date, pbsql.get_record(pbd.Kunde, booking.kunde_id))
#     destination_ok = pbf.max_one_destination(pbsql.get_record(pbd.Rejse, booking.rejse_id), booking.date, pbsql.get_record(pbd.Kunde, booking.kunde_id))
#     if destination_ok:
#         if capacity_ok:
#             pbsql.create_record(booking)  # Update database
#             clear_booking_entries()  # Clear entry boxes
#             refresh_treeview(tree, pbd.Booking)  # Refresh treeview table
#         else:
#             global INTERNAL_ERROR_CODE
#             INTERNAL_ERROR_CODE = 1
#             messagebox.showwarning("", "Not enough capacity on rejse!")
#     else:
#         messagebox.showwarning("", "Rejse already has another destination!")
        
def update_booking(tree, record):  # update tuple in database
    booking = pbd.Booking.convert_from_tuple(record)  # Convert tuple to Booking
    pbsql.update_booking(booking)  # Update database
    clear_booking_entries()  # Clear entry boxes
    refresh_treeview(tree, pbd.Booking)  # Refresh treeview table


def delete_booking(tree, record):  # delete tuple in database
    booking = pbd.Booking.convert_from_tuple(record)  # Convert tuple to Booking
    pbsql.delete_soft_booking(booking)  # Update database
    clear_booking_entries()  # Clear entry boxes
    refresh_treeview(tree, pbd.Booking)  # Refresh treeview table
# endregion booking functions

# region common functions
def read_table(tree, class_):  # fill tree from database
    count = 0  # Used to keep track of odd and even rows, because these will be colored differently.
    result = pbsql.select_all(class_)  # Read all kunder(customers) from database
    for record in result:
        if record.valid():  # this condition excludes soft deleted records from being shown in the data table
            if count % 2 == 0:  # even
               tree.insert(parent='', index='end', iid=str(count), text='', values=record.convert_to_tuple(), tags=('evenrow',))  # Insert one row into the data table
            else:  # odd
               tree.insert(parent='', index='end', iid=str(count), text='', values=record.convert_to_tuple(), tags=('oddrow',))  # Insert one row into the data table
            count += 1

def empty_treeview(tree):  # Clear treeview table
    tree.delete(*tree.get_children())

def refresh_treeview(tree, class_):  # Refresh treeview table
    empty_treeview(tree)  # Clear treeview table
    read_table(tree, class_)  # Fill treeview from database
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
# Define Labelframe which contains all kunde related GUI objects (data table, labels, buttons, ...)
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
tree_kunde.bind("<ButtonRelease-1>", lambda event: edit_kunde(event, tree_kunde))  # Define function to be called, when an item is selected.

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
# label_kunde_weather = tk.Label(edit_frame_kunde, text="N/A")
# label_kunde_weather.grid(row=0, column=3, padx=padx, pady=pady)
# entry_kunde_weather = tk.Entry(edit_frame_kunde, width=14)
# entry_kunde_weather.grid(row=1, column=3, padx=padx, pady=pady)

# Define Frame which contains buttons
button_frame_kunde = tk.Frame(controls_frame_kunde)
button_frame_kunde.grid(row=1, column=0, padx=padx, pady=pady)
# Define buttons
button_create_kunde = tk.Button(button_frame_kunde, text="Create", command=lambda: create_kunde(tree_kunde, read_kunde_entries()))
button_create_kunde.grid(row=0, column=1, padx=padx, pady=pady)
button_update_kunde = tk.Button(button_frame_kunde, text="Update", command=lambda: update_kunde(tree_kunde, read_kunde_entries()))
button_update_kunde.grid(row=0, column=2, padx=padx, pady=pady)
button_delete_kunde = tk.Button(button_frame_kunde, text="Delete", command=lambda: delete_kunde(tree_kunde, read_kunde_entries()))
button_delete_kunde.grid(row=0, column=3, padx=padx, pady=pady)
button_clear_boxes = tk.Button(button_frame_kunde, text="Clear Entry Boxes", command=clear_kunde_entries)
button_clear_boxes.grid(row=0, column=4, padx=padx, pady=pady)
# endregion kunde widgets

# region rejse widgets
labelframe_rejse = tk.LabelFrame(main_window, text="Rejse")  # https://www.tutorialspoint.com/python/tk_labelframe.htm
labelframe_rejse.grid(row=0, column=1, padx=padx, pady=pady, sticky=tk.N)  # https://www.tutorialspoint.com/python/tk_grid.htm

# Define data table (Treeview) and its scrollbar. Put them in a Frame.
tree_frame_rejse = tk.Frame(labelframe_rejse)  # https://www.tutorialspoint.com/python/tk_frame.htm
tree_frame_rejse.grid(row=0, column=0, padx=padx, pady=pady)
tree_scroll_rejse = tk.Scrollbar(tree_frame_rejse)
tree_scroll_rejse.grid(row=0, column=1, padx=0, pady=pady, sticky='ns')
tree_rejse = ttk.Treeview(tree_frame_rejse, yscrollcommand=tree_scroll_rejse.set, selectmode="browse")  # https://docs.python.org/3/library/tkinter.ttk.html#treeview
tree_rejse.grid(row=0, column=0, padx=0, pady=pady)
tree_scroll_rejse.config(command=tree_rejse.yview)

# Define the data table's formatting and content
tree_rejse['columns'] = ("id", "rute", "dato", "pladskapacitet")  # Define columns
tree_rejse.column("#0", width=0, stretch=tk.NO)  # Format columns. Suppress the irritating first empty column.
tree_rejse.column("id", anchor=tk.E, width=40)  # "E" stands for East, meaning Right. Possible anchors are N, NE, E, SE, S, SW, W, NW and CENTER
tree_rejse.column("rute", anchor=tk.E, width=100)
tree_rejse.column("dato", anchor=tk.W, width=100)
tree_rejse.column("pladskapacitet", anchor=tk.W, width=100)
tree_rejse.heading("#0", text="", anchor=tk.W)  # Create column headings
tree_rejse.heading("id", text="Id", anchor=tk.CENTER)
tree_rejse.heading("rute", text="Rute", anchor=tk.CENTER)
tree_rejse.heading("dato", text="Dato", anchor=tk.CENTER)
tree_rejse.heading("pladskapacitet", text="Pladskapacitet", anchor=tk.CENTER)
tree_rejse.tag_configure('oddrow', background=oddrow)  # Create tags for rows in 2 different colors
tree_rejse.tag_configure('evenrow', background=evenrow)
tree_rejse.bind("<ButtonRelease-1>", lambda event: edit_rejse(event, tree_rejse))  # Define function to be called, when an item is selected.

# Define Frame which contains labels, entries & buttons
controls_frame_rejse = tk.Frame(labelframe_rejse)
controls_frame_rejse.grid(row=3, column=0, padx=padx, pady=pady)

# Define Frame which contains labels, entries and buttons
controls_frame_rejse = tk.Frame(labelframe_rejse)
controls_frame_rejse.grid(row=1, column=0, padx=padx, pady=pady)

# Define Frame which contains labels (text fields) and entries (input fields)
edit_frame_rejse = tk.Frame(controls_frame_rejse)  # Add tuple entry boxes
edit_frame_rejse.grid(row=0, column=0, padx=padx, pady=pady)
# label and entry for rejse id
label_rejse_id = tk.Label(edit_frame_rejse, text="Id")  # https://www.tutorialspoint.com/python/tk_label.htm
label_rejse_id.grid(row=0, column=0, padx=padx, pady=pady)
entry_rejse_id = tk.Entry(edit_frame_rejse, width=4, justify="right")  # https://www.tutorialspoint.com/python/tk_entry.htm
entry_rejse_id.grid(row=1, column=0, padx=padx, pady=pady)
# label and entry for rejse rute
label_rejse_rute = tk.Label(edit_frame_rejse, text="Rute")
label_rejse_rute.grid(row=0, column=1, padx=padx, pady=pady)
entry_rejse_rute = tk.Entry(edit_frame_rejse, width=16, justify="right")
entry_rejse_rute.grid(row=1, column=1, padx=padx, pady=pady)
# label and entry for rejse dato
label_rejse_dato = tk.Label(edit_frame_rejse, text="Dato")
label_rejse_dato.grid(row=0, column=2, padx=padx, pady=pady)
entry_rejse_dato = tk.Entry(edit_frame_rejse, width=10)
entry_rejse_dato.grid(row=1, column=2, padx=padx, pady=pady)
# label and entry for rejse pladskapacitet
label_rejse_pladskapacitet = tk.Label(edit_frame_rejse, text="Pladskapacitet")
label_rejse_pladskapacitet.grid(row=0, column=3, padx=padx, pady=pady)
entry_rejse_pladskapacitet = tk.Entry(edit_frame_rejse, width=14)
entry_rejse_pladskapacitet.grid(row=1, column=3, padx=padx, pady=pady)

# Define Frame which contains buttons
button_frame_rejse = tk.Frame(controls_frame_rejse)
button_frame_rejse.grid(row=1, column=0, padx=padx, pady=pady)
# Define buttons
button_create_rejse = tk.Button(button_frame_rejse, text="Create", command=lambda: create_rejse(tree_rejse, read_rejse_entries()))
button_create_rejse.grid(row=0, column=1, padx=padx, pady=pady)
button_update_rejse = tk.Button(button_frame_rejse, text="Update", command=lambda: update_rejse(tree_rejse, read_rejse_entries()))
button_update_rejse.grid(row=0, column=2, padx=padx, pady=pady)
button_delete_rejse = tk.Button(button_frame_rejse, text="Delete", command=lambda: delete_rejse(tree_rejse, read_rejse_entries()))
button_delete_rejse.grid(row=0, column=3, padx=padx, pady=pady)
button_clear_boxes = tk.Button(button_frame_rejse, text="Clear Entry Boxes", command=clear_rejse_entries)
button_clear_boxes.grid(row=0, column=4, padx=padx, pady=pady)
# endregion rejse widgets

# region booking widgets
labelframe_booking = tk.LabelFrame(main_window, text="Booking")  # https://www.tutorialspoint.com/python/tk_labelframe.htm
labelframe_booking.grid(row=0, column=2, padx=padx, pady=pady, sticky=tk.N)  # https://www.tutorialspoint.com/python/tk_grid.htm

# Define data table (Treeview) and its scrollbar. Put them in a Frame.
tree_frame_booking = tk.Frame(labelframe_booking)  # https://www.tutorialspoint.com/python/tk_frame.htm
tree_frame_booking.grid(row=0, column=0, padx=padx, pady=pady)
tree_scroll_booking = tk.Scrollbar(tree_frame_booking)
tree_scroll_booking.grid(row=0, column=1, padx=0, pady=pady, sticky='ns')
tree_booking = ttk.Treeview(tree_frame_booking, yscrollcommand=tree_scroll_booking.set, selectmode="browse")  # https://docs.python.org/3/library/tkinter.ttk.html#treeview
tree_booking.grid(row=0, column=0, padx=0, pady=pady)
tree_scroll_booking.config(command=tree_booking.yview)

# Define the data table's formatting and content
tree_booking['columns'] = ("id", "kunde_id", "rejse_id", "pladser")  # Define columns
tree_booking.column("#0", width=0, stretch=tk.NO)  # Format columns. Suppress the irritating first empty column.
tree_booking.column("id", anchor=tk.E, width=40)  # "E" stands for East, meaning Right. Possible anchors are N, NE, E, SE, S, SW, W, NW and CENTER
tree_booking.column("kunde_id", anchor=tk.E, width=100)
tree_booking.column("rejse_id", anchor=tk.W, width=100)
tree_booking.column("pladser", anchor=tk.W, width=100)
tree_booking.heading("#0", text="", anchor=tk.W)  # Create column headings
tree_booking.heading("id", text="Id", anchor=tk.CENTER)
tree_booking.heading("kunde_id", text="Kunde_id", anchor=tk.CENTER)
tree_booking.heading("rejse_id", text="Rejse_id", anchor=tk.CENTER)
tree_booking.heading("pladser", text="Pladser", anchor=tk.CENTER)
tree_booking.tag_configure('oddrow', background=oddrow)  # Create tags for rows in 2 different colors
tree_booking.tag_configure('evenrow', background=evenrow)
tree_booking.bind("<ButtonRelease-1>", lambda event: edit_booking(event, tree_booking))  # Define function to be called, when an item is selected.

# Define Frame which contains labels, entries & buttons
controls_frame_booking = tk.Frame(labelframe_booking)
controls_frame_booking.grid(row=3, column=0, padx=padx, pady=pady)

# Define Frame which contains labels, entries and buttons
controls_frame_booking = tk.Frame(labelframe_booking)
controls_frame_booking.grid(row=1, column=0, padx=padx, pady=pady)

# Define Frame which contains labels (text fields) and entries (input fields)
edit_frame_booking = tk.Frame(controls_frame_booking)  # Add tuple entry boxes
edit_frame_booking.grid(row=0, column=0, padx=padx, pady=pady)
# label and entry for booking id
label_booking_id = tk.Label(edit_frame_booking, text="Id")  # https://www.tutorialspoint.com/python/tk_label.htm
label_booking_id.grid(row=0, column=0, padx=padx, pady=pady)
entry_booking_id = tk.Entry(edit_frame_booking, width=4, justify="right")  # https://www.tutorialspoint.com/python/tk_entry.htm
entry_booking_id.grid(row=1, column=0, padx=padx, pady=pady)
# label and entry for booking kunde_id
label_booking_kunde_id = tk.Label(edit_frame_booking, text="Kunde Id")
label_booking_kunde_id.grid(row=0, column=1, padx=padx, pady=pady)
entry_booking_kunde_id = tk.Entry(edit_frame_booking, width=16, justify="right")
entry_booking_kunde_id.grid(row=1, column=1, padx=padx, pady=pady)
# label and entry for booking booking_id
label_booking_rejse_id = tk.Label(edit_frame_booking, text="Rejse Id")
label_booking_rejse_id.grid(row=0, column=2, padx=padx, pady=pady)
entry_booking_rejse_id = tk.Entry(edit_frame_booking, width=10)
entry_booking_rejse_id.grid(row=1, column=2, padx=padx, pady=pady)
# label and entry for booking pladskapacitet
label_booking_pladser = tk.Label(edit_frame_booking, text="Pladser")
label_booking_pladser.grid(row=0, column=3, padx=padx, pady=pady)
entry_booking_pladser = tk.Entry(edit_frame_booking, width=14)
entry_booking_pladser.grid(row=1, column=3, padx=padx, pady=pady)

# Define Frame which contains buttons
button_frame_booking = tk.Frame(controls_frame_booking)
button_frame_booking.grid(row=1, column=0, padx=padx, pady=pady)
# Define buttons
button_create_booking = tk.Button(button_frame_booking, text="Create", command=lambda: create_booking(tree_booking, read_booking_entries()))
button_create_booking.grid(row=0, column=1, padx=padx, pady=pady)
button_update_booking = tk.Button(button_frame_booking, text="Update", command=lambda: update_booking(tree_booking, read_booking_entries()))
button_update_booking.grid(row=0, column=2, padx=padx, pady=pady)
button_delete_booking = tk.Button(button_frame_booking, text="Delete", command=lambda: delete_booking(tree_booking, read_booking_entries()))
button_delete_booking.grid(row=0, column=3, padx=padx, pady=pady)
button_clear_boxes = tk.Button(button_frame_booking, text="Clear Entry Boxes", command=clear_booking_entries)
button_clear_boxes.grid(row=0, column=4, padx=padx, pady=pady)
# endregion booking widgets

# region main program
if __name__ == "__main__":  # Executed when invoked directly. We use this so main_window.mainloop() does not keep our unit tests from running.
    refresh_treeview(tree_kunde, pbd.Kunde)  # Load data from database
    refresh_treeview(tree_rejse, pbd.Rejse)  # Load data from database
    refresh_treeview(tree_booking, pbd.Booking)  # Load data from database
    main_window.mainloop()  # Wait for button clicks and act upon them
# endregion main program



