from typing import Optional
import tkinter as tk


class MainFrame:
    def __init__(self):
        self._main_frame: Optional[tk.Frame] = None

    def set_main_frame(self, root_widget: tk.Tk) -> tk.Frame:
        self._validate_root_widget(root_widget)
        self._main_frame = tk.Frame(root_widget, padx=20, pady=20)
        self._main_frame.pack()
        return self._main_frame

    @staticmethod
    def _validate_root_widget(root_widget):
        if not isinstance(root_widget, tk.Tk):
            raise TypeError("root_widget should be an instance of tk.Widget")
