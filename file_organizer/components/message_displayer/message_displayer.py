from abc import ABC, abstractmethod


class MessageDisplayer(ABC):
    def __init__(self, title: str = "Error", msg: str = ""):
        self.title = title
        self.msg = msg

    @abstractmethod
    def display_message(self):
        pass
