import tkinter as tk
import unittest
from unittest.mock import patch

from file_organizer.commands.directory_browser.DirectoryBrowser import DirectoryBrowser
from file_organizer.components.buttons.BrowseButton import BrowseButton


class TestBrowseButton(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.main_frame = tk.Frame(self.root)
        self.entry = tk.Entry(self.main_frame)
        self.browse_button = BrowseButton(self.main_frame)

    def tearDown(self):
        self.root.destroy()

    def test_build(self):
        self.browse_button.build(self.entry)
        self.assertEqual(self.browse_button._entry, self.entry)

    @patch.object(BrowseButton, "create_button")
    def test_button_creation(self, mock_create_button):
        self.browse_button.build(self.entry)
        mock_create_button.assert_called_once_with(
            text="Browse",
            command=self.browse_button._build_command,
            row=0, column=2, padx=10)

    @patch.object(DirectoryBrowser, "browse_directory")
    def test_build_command(self, mock_browser):
        self.browse_button.build(self.entry)
        for elem in self.main_frame.children.values():
            if isinstance(elem, tk.Button):
                elem.invoke()
        mock_browser.assert_called_once()


if __name__ == '__main__':
    unittest.main()
