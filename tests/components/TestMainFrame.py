import unittest
import tkinter as tk
from unittest.mock import MagicMock

from file_organizer.components.MainFrame import MainFrame


class TestMainFrame(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.instance = MainFrame()

    def tearDown(self):
        self.root.destroy()
        self.instance = None

    def test_set_main_frame(self):
        main_frame = self.instance.set_main_frame(self.root)
        self.assertIsInstance(main_frame, tk.Frame)
        self.assertEqual(main_frame['padx'], 20)
        self.assertEqual(main_frame['pady'], 20)
        self.assertTrue(main_frame.winfo_manager() is not None, "Frame is not managed")

    def test_set_main_frame_invalid_root(self):
        with self.assertRaises(TypeError):
            self.instance.set_main_frame(None)


if __name__ == '__main__':
    unittest.main()
