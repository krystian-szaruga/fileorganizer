import unittest
import tkinter as tk

from file_organizer.components.buttons.button import Button
from tests.components.buttons.helpers.dummy_command import dummy_command


class TestButton(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.frame = tk.Frame(self.root)
        self.frame.grid()

    def tearDown(self):
        self.root.destroy()

    def test_create_button(self):
        button_creator = Button(self.frame)
        button_creator.create_button("Click Me", dummy_command, row=0, column=0)
        button_found = None
        for child in self.frame.children.values():
            if isinstance(child, tk.Button) and child.cget("text") == "Click Me":
                button_found = child
                break
        self.assertIsNotNone(button_found)
        self.assertEqual(button_found.cget("text"), "Click Me")
        self.assertTrue(button_found['command'])

    def test_crate_button_wrong_args(self):
        button_creator = Button(self.frame)
        with self.assertRaises(tk.TclError):
            button_creator.create_button(
                "Click Me", dummy_command,
                not_valid_arg1=0, not_valid_arg2=0)


if __name__ == '__main__':
    unittest.main()
