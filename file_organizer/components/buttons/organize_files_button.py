from typing import Optional

from file_organizer.components.buttons.button import Button
import tkinter as tk

from file_organizer.commands.organize_files.organize_files import OrganizeFiles


class OrganizeFilesButton(Button):
    def __init__(self, main_frame: tk.Frame):
        super().__init__(main_frame)
        self._organizer = OrganizeFiles()
        self._directory_entry: Optional[tk.Entry] = None

    def build(self, directory_entry: tk.Entry):
        self._directory_entry = directory_entry
        self.create_button(
            text="Organize Files",
            command=self._build_command,
            row=1, column=1, padx=10)

    def _build_command(self):
        self._organizer.set_directory_path(self._directory_entry.get())
        self._organizer.organize_files()
