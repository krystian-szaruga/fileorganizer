import unittest
from tkinter import messagebox
from unittest.mock import MagicMock, patch, call

from file_organizer.commands.organize_files.OrganizeFiles import OrganizeFiles
from file_organizer.commands.organize_files.components.DirectoryValidator import DirectoryValidator
from file_organizer.components.message_displayer.ErrorDisplayer import ErrorDisplayer
from file_organizer.components.message_displayer.InfoDisplayer import InfoDisplayer


class TestOrganizeFiles(unittest.TestCase):

    def setUp(self):
        self.organizer = OrganizeFiles()

    @patch.object(messagebox, "showinfo")
    @patch.object(messagebox, "showerror")
    @patch.object(OrganizeFiles, "_organize_files_by_extension")
    @patch.object(DirectoryValidator, "validate")
    def test_organize_files_success(
            self, mock_validator, mock_by_extension, mock_error, mock_info):
        mock_by_extension.return_value = True
        directory = "test_directory"
        mock_validator.return_value = directory
        self.organizer.set_directory_path(directory)
        self.organizer.organize_files()

        mock_by_extension.assert_called_once()
        mock_info.assert_called_once_with("Info", "Files Have Been Organized!")
        mock_error.assert_not_called()

    @patch.object(messagebox, "showinfo")
    @patch.object(messagebox, "showerror")
    @patch.object(DirectoryValidator, "validate")
    def test_organize_files_success_dir_empty(
            self, mock_validator, mock_error, mock_info):
        directory = "test_directory"
        mock_validator.return_value = directory
        self.organizer.set_directory_path(directory)
        self.organizer.organize_files()
        mock_info.assert_has_calls([
            call("Info", "Directory is Empty"),
            call("Info", "Files Have Been Organized!")])
        mock_error.assert_not_called()

    @patch.object(messagebox, "showinfo")
    @patch.object(messagebox, "showerror")
    def test_organize_files_no_dir_set(
            self, mock_error, mock_info):
        self.organizer.organize_files()
        mock_info.assert_not_called()
        mock_error.assert_called_once_with(
            "Error", "Directory path has not been set")

    @patch.object(messagebox, "showinfo")
    @patch.object(messagebox, "showerror")
    @patch.object(OrganizeFiles, "_organize_files_by_extension")
    @patch.object(DirectoryValidator, "validate")
    def test_organize_files_unsuccessful(
            self, mock_validator, mock_by_extension, mock_error, mock_info):
        mock_by_extension.side_effect = Exception("Unexpected error")
        directory = "test_directory"
        mock_validator.return_value = directory
        self.organizer.set_directory_path(directory)
        self.organizer.organize_files()

        mock_by_extension.assert_called_once()
        mock_info.assert_not_called()
        mock_error.assert_called_once_with("Error", "An error occurred: Unexpected error")

    @patch.object(messagebox, "showinfo")
    @patch.object(messagebox, "showerror")
    def test_organize_files_not_valid_dir(self, mock_error, mock_info):
        self.organizer.set_directory_path("path")
        self.organizer.organize_files()
        mock_error.assert_has_calls([
            call('Error', 'Directory does not exist: path'),
            call('Error', 'Directory path has not been set')])
        mock_info.assert_not_called()


if __name__ == '__main__':
    unittest.main()
