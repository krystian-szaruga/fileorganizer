import tkinter as tk
from typing import Callable


class Button:
    def __init__(self, main_frame: tk.Frame):
        self.main_frame = main_frame

    def create_button(self, text: str, command: Callable, **grid):
        tk.Button(
            self.main_frame,
            text=text,
            command=command).grid(**grid)
