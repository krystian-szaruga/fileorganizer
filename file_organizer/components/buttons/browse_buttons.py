import tkinter as tk
from typing import Optional

from file_organizer.commands.directory_browser.directory_browser import DirectoryBrowser
from file_organizer.components.buttons.button import Button


class BrowseButton(Button):
    def __init__(self, main_frame: tk.Frame):
        super().__init__(main_frame)
        self._browser = DirectoryBrowser()
        self._entry: Optional[tk.Entry] = None

    def build(self, entry: tk.Entry):
        self._entry = entry
        self.create_button(
            text="Browse",
            command=self._build_command,
            row=0, column=2, padx=10)

    def _build_command(self):
        self._browser.entry = self._entry
        self._browser.browse_directory()

