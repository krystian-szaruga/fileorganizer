import unittest
from unittest.mock import Mock, patch

from file_organizer.app.FileOrganizer import FileOrganizerApp
from file_organizer.commands.generate_empty_files.extensions.FileData import FileData
from file_organizer.components.DirectoryEntry import DirectoryEntry
from file_organizer.components.MainFrame import MainFrame
from file_organizer.components.buttons.BrowseButton import BrowseButton
from file_organizer.components.buttons.GenerateTestFilesButton import GenerateTestFilesButton
from file_organizer.components.buttons.OrganizeFilesButton import OrganizeFilesButton


class TestFileOrganizerApp(unittest.TestCase):

    def setUp(self):
        self.file_data = FileData()
        self.app = FileOrganizerApp(self.file_data)

    def tearDown(self):
        self.app.root_widget.destroy()

    @patch.object(MainFrame, "set_main_frame")
    @patch.object(DirectoryEntry, "set_directory_entry")
    @patch.object(BrowseButton, "build")
    @patch.object(OrganizeFilesButton, "build")
    @patch.object(GenerateTestFilesButton, "build")
    def test_build(self, mock_generate_button, mock_organize_button, mock_browse_button, mock_directory_entry,
                   mock_main_frame):

        self.app.root_widget = Mock()
        self.app.root_widget.title = Mock()

        self.app.build()

        self.app.root_widget.title.assert_called_once_with("File Organizer")
        mock_main_frame.assert_called_once_with(self.app.root_widget)
        mock_browse_button.assert_called_once_with(self.app.directory_entry)
        mock_organize_button.assert_called_once_with(self.app.directory_entry)
        mock_generate_button.assert_called_once_with()

    # def test_invalid_file_data(self):
    #     with self.assertRaises(TypeError):
    #         app = FileOrganizerApp("invalid_file_data")
    #         app.build()


if __name__ == '__main__':
    unittest.main()
