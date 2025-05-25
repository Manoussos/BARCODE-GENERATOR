import tkinter as tk
from tkinter import filedialog, messagebox
import os
from barcode import EAN13
from barcode.writer import ImageWriter

def generate_barcode():
    data = entry_data.get()
    file_name = entry_name.get()
    file_format = format_var.get()

    if not data or not file_name or not file_format:
        messagebox.showerror("Σφάλμα", "Συμπληρώστε όλα τα πεδία!")
        return

   
    if len(data) != 12:
        messagebox.showerror("Σφάλμα", "Τα δεδομένα πρέπει να περιέχουν ακριβώς 12 ψηφία.")
        return

    try:
    
        barcode_instance = EAN13(data, writer=ImageWriter())
        
      
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        file_path = os.path.join(desktop_path, f"{file_name}.{file_format}")
        barcode_instance.save(file_path)

        messagebox.showinfo("Επιτυχία", f"Το αρχείο αποθηκεύτηκε: {file_path}")
    except Exception as e:
        messagebox.showerror("Σφάλμα", str(e))


def validate_input(input_value):
    if len(input_value) > 12:
        return False
    return True


root = tk.Tk()
root.title("Barcode Generator")

tk.Label(root, text="Προσθήκη Δεδομένων:").grid(row=0, column=0, padx=10, pady=10)


vcmd = root.register(validate_input)

entry_data = tk.Entry(root, validate="key", validatecommand=(vcmd, '%P'))
entry_data.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Όνομα αρχείου:").grid(row=1, column=0, padx=10, pady=10)
entry_name = tk.Entry(root)
entry_name.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Μορφή αρχείου:").grid(row=2, column=0, padx=10, pady=10)
format_var = tk.StringVar(value="svg")
tk.OptionMenu(root, format_var, "svg", "eps", "ai", "png").grid(row=2, column=1, padx=10, pady=10)

tk.Button(root, text="Δημιουργία", command=generate_barcode).grid(row=3, columnspan=2, pady=20)

root.mainloop()
