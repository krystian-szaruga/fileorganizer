import os
from typing import Optional
import tkinter as tk


class DirectoryEntry:
    def __init__(self):
        self._directory_entry: Optional[tk.Entry] = None

    def set_directory_entry(self, main_frame: tk.Frame) -> tk.Entry:
        tk.Label(main_frame, text="Select Directory:").grid(row=0, column=0, sticky=tk.W)
        self._directory_entry = tk.Entry(main_frame, width=50)
        self._directory_entry.grid(row=0, column=1, padx=10, pady=5)
        self._directory_entry.insert(tk.END, os.getcwd())
        return self._directory_entry
