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

# Define data table (Treeview) and its scrollbar. Put them in a Frame.
tree_frame_kunde = tk.Frame(labelframe_kunde)  # https://www.tutorialspoint.com/python/tk_frame.htm
tree_frame_kunde.grid(row=0, column=0, padx=padx, pady=pady)
tree_scroll_kunde = tk.Scrollbar(tree_frame_kunde)
tree_scroll_kunde.grid(row=0, column=1, padx=0, pady=pady, sticky='ns')
tree_kunde = ttk.Treeview(tree_frame_kunde, yscrollcommand=tree_scroll_kunde.set, selectmode="browse")  # https://docs.python.org/3/library/tkinter.ttk.html#treeview
tree_kunde.grid(row=0, column=0, padx=0, pady=pady)
tree_scroll_kunde.config(command=tree_kunde.yview)
# endregion kunde widgets

# region main program
if __name__ == "__main__":  # Executed when invoked directly. We use this so main_window.mainloop() does not keep our unit tests from running.
    main_window.mainloop()  # Wait for button clicks and act upon them
# endregion main program


