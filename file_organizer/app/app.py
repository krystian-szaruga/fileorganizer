from abc import ABC
import tkinter as tk
from typing import Optional


class App(ABC):
    def __init__(self):
        self.root_widget: tk.Tk = tk.Tk()
        self.directory_entry: Optional[tk.Entry] = None
        self.main_frame: Optional[tk.Frame] = None
