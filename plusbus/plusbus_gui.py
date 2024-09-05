import tkinter as tk
from tkinter import ttk


# Derudover importer dine egne filer:
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
# endregion kunde widgets

# region main program
# endregion main program

