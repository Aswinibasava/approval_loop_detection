import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from utils import detect_loops

def open_file():
    filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if not filepath:
        return
    try:
        df = pd.read_csv(filepath)
        loops = detect_loops(df)
        output_text.delete("1.0", tk.END)
        if loops:
            for idx, loop in enumerate(loops, 1):
                output_text.insert(tk.END, f"Loop {idx}: {' ➝ '.join(loop)}\n")
        else:
            output_text.insert(tk.END, "✅ No loops found.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Approval Loop Detector")

tk.Button(root, text="Upload CSV", command=open_file).pack(pady=10)
output_text = tk.Text(root, height=20, width=80)
output_text.pack()

root.mainloop()
