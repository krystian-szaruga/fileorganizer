import tkinter as tk
import unittest
from unittest.mock import patch

from file_organizer.commands.organize_files.OrganizeFiles import OrganizeFiles
from file_organizer.commands.organize_files.components.DirectoryValidator import DirectoryValidator
from file_organizer.components.buttons.OrganizeFilesButton import OrganizeFilesButton


class TestOrganizeFilesButton(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.main_frame = tk.Frame(self.root)
        self.entry = tk.Entry(self.main_frame)
        self.organize_button = OrganizeFilesButton(self.main_frame)

    def tearDown(self):
        self.root.destroy()

    def test_build(self):
        self.organize_button.build(self.entry)
        self.assertEqual(self.organize_button._directory_entry, self.entry)

    @patch.object(OrganizeFilesButton, "create_button")
    def test_button_creation(self, mock_organize_button):
        self.organize_button.build(self.entry)
        mock_organize_button.assert_called_once_with(
            text="Organize Files",
            command=self.organize_button._build_command,
            row=1, column=1, padx=10)

    @patch.object(OrganizeFiles, "organize_files")
    @patch.object(DirectoryValidator, "validate")
    def test_build_command(self, mock_validator, mock_organizer):
        mock_validator.return_value = "path"
        self.organize_button.build(self.entry)
        for elem in self.main_frame.children.values():
            if isinstance(elem, tk.Button):
                elem.invoke()
        mock_organizer.assert_called_once()


if __name__ == '__main__':
    unittest.main()
