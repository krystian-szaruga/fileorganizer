from file_organizer.components.buttons.Button import Button
import tkinter as tk

from file_organizer.commands.generate_empty_files.GenerateEmptyFiles import GenerateEmptyFiles
from file_organizer.commands.generate_empty_files.extensions.FileData import FileData


class GenerateTestFilesButton(Button):
    def __init__(self, main_frame: tk.Frame, file_data: FileData = FileData()):
        super().__init__(main_frame)
        self._generator = GenerateEmptyFiles(file_data)

    def build(self):
        self.create_button(
            text="Generate Test Files",
            command=self._generator.generate_empty_files,
            row=1, column=2, padx=10)
