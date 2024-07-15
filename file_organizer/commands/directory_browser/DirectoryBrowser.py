import tkinter as tk
from tkinter import filedialog, Entry
from typing import Optional, Union

from file_organizer.components.message_displayer.ErrorDisplayer import ErrorDisplayer


class DirectoryBrowser:
    def __init__(self):
        self._entry: Optional[tk.Entry] = None

    @property
    def entry(self) -> tk.Entry:
        return self._entry

    @entry.setter
    def entry(self, value: tk.Entry) -> None:
        self._entry = value

    def browse_directory(self) -> Union[Entry, None]:
        if self._entry is None:
            ErrorDisplayer(
                title="Error", msg="tk.entry has not been set").display_message()
            return
        directory_path = filedialog.askdirectory()
        if directory_path:
            self._entry.delete(0, tk.END)
            self._entry.insert(tk.END, directory_path)
