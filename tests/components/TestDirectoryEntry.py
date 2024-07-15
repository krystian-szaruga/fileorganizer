import os
import tkinter as tk
import unittest

from file_organizer.components.DirectoryEntry import DirectoryEntry


class TestDirectoryEntry(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()

    def tearDown(self):
        self.root.destroy()

    def test_set_directory_entry(self):
        main_frame = tk.Frame(self.root)
        main_frame.pack()
        directory_entry = DirectoryEntry()
        entry_widget = directory_entry.set_directory_entry(main_frame)
        self.assertIsInstance(entry_widget, tk.Entry)
        initial_value = entry_widget.get()
        self.assertEqual(initial_value, os.getcwd())


if __name__ == '__main__':
    unittest.main()
