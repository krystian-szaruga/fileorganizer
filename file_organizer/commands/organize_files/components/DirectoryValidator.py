import os

from file_organizer.components.message_displayer.ErrorDisplayer import ErrorDisplayer


class DirectoryValidator:
    @staticmethod
    def validate(directory_path: str) -> str:
        if os.path.exists(directory_path):
            return directory_path
        ErrorDisplayer("Error", f"Directory does not exist: {directory_path}").display_message()
        return ""

