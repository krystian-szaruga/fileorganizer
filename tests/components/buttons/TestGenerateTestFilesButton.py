
import tkinter as tk
import unittest
from unittest.mock import patch

from file_organizer.commands.generate_empty_files.GenerateEmptyFiles import GenerateEmptyFiles
from file_organizer.components.buttons.GenerateTestFilesButton import GenerateTestFilesButton


class TestGenerateTestFilesButton(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.main_frame = tk.Frame(self.root)
        self.generate_test_files = GenerateTestFilesButton(self.main_frame)

    def tearDown(self):
        self.root.destroy()

    @patch.object(GenerateTestFilesButton, "create_button")
    @patch.object(GenerateEmptyFiles, "generate_empty_files")
    def test_button_creation(self, mock_generate_empty_files, mock_generate_button):
        self.generate_test_files.build()
        mock_generate_button.assert_called_once_with(
            text="Generate Test Files",
            command=mock_generate_empty_files,
            row=1, column=2, padx=10)

    @patch.object(GenerateEmptyFiles, "generate_empty_files")
    def test_build_command(self, mock_generate_empty_files):
        self.generate_test_files.build()
        for elem in self.main_frame.children.values():
            if isinstance(elem, tk.Button):
                elem.invoke()
        mock_generate_empty_files.assert_called_once()


if __name__ == '__main__':
    unittest.main()
