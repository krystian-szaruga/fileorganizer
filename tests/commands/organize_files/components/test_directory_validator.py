import os
import unittest
from tkinter import messagebox
from unittest.mock import patch

from file_organizer.commands.organize_files.components.directory_validator import DirectoryValidator


class TestDirectoryValidator(unittest.TestCase):
    def setUp(self):
        self.validator = DirectoryValidator()

    def test_existing_directory(self):
        directory_path = os.getcwd()
        result = self.validator.validate(directory_path)
        self.assertEqual(result, directory_path)

    @patch.object(messagebox, "showerror")
    def test_non_existing_directory(self, mock_showerror):
        directory_path = "/path/to/nonexistent/directory"
        result = self.validator.validate(directory_path)
        self.assertEqual(result, "")
        mock_showerror.assert_called_once_with("Error", f"Directory does not exist: {directory_path}")

    @patch.object(messagebox, "showerror")
    def test_empty_directory_path(self, mock_showerror):
        directory_path = ""
        result = self.validator.validate(directory_path)
        self.assertEqual(result, "")
        mock_showerror.assert_called_once_with("Error", f"Directory does not exist: {directory_path}")


if __name__ == '__main__':
    unittest.main()
