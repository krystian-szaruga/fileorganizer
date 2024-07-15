import os
import tkinter as tk
import unittest
from tkinter import filedialog, messagebox
from unittest.mock import MagicMock, patch

from file_organizer.commands.directory_browser.DirectoryBrowser import DirectoryBrowser
from file_organizer.components.message_displayer.ErrorDisplayer import ErrorDisplayer

browser = DirectoryBrowser()


class TestDirectoryBrowser(unittest.TestCase):
    def setUp(self):
        self.browser = DirectoryBrowser()
        self.entry = tk.Entry()

    def test_browse_directory_success(self):
        expected_path = "/mock/directory/path"
        filedialog.askdirectory = MagicMock(return_value=expected_path)

        self.browser.entry = self.entry
        self.browser.browse_directory()

        self.assertEqual(self.entry.get(), expected_path)

    @patch.object(messagebox, "showerror")
    def test_browse_directory_no_entry_set(self, mock_showerror):
        self.browser.entry = None
        self.assertEqual(self.browser.browse_directory(), None)
        mock_showerror.assert_called_once_with(
            'Error', 'tk.entry has not been set')



if __name__ == '__main__':
    unittest.main()
