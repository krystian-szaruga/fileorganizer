from tkinter import messagebox

from file_organizer.components.message_displayer.message_displayer import MessageDisplayer


class ErrorDisplayer(MessageDisplayer):
    def __init__(self, title: str = "Error", msg: str = ""):
        super().__init__(title, msg)

    def display_message(self):
        messagebox.showerror(self.title, self.msg)
