import os
from typing import Optional

from file_organizer.commands.organize_files.components.DirectoryValidator import DirectoryValidator
from file_organizer.commands.organize_files.components.FileFinder import FileFinder
from file_organizer.commands.organize_files.components.FileMoverHandler import FileMoverHandler
from file_organizer.components.message_displayer.ErrorDisplayer import ErrorDisplayer
from file_organizer.components.message_displayer.InfoDisplayer import InfoDisplayer


class OrganizeFiles:
    def __init__(self):
        self._directory_path: Optional[str] = None
        self._file_mover = FileMoverHandler()

    def set_directory_path(self, directory_path: str):
        self._directory_path = DirectoryValidator.validate(directory_path)

    def organize_files(self) -> None:
        if self._directory_path is not None and self._directory_path.strip():
            try:
                file_organized = self._organize_files_by_extension()
                if file_organized:
                    InfoDisplayer(
                        "Info",
                        "Files Have Been Organized!").display_message()
            except Exception as e:
                (ErrorDisplayer(
                    title="Error",
                    msg=f"An error occurred: {e}")
                 .display_message())
        else:
            (ErrorDisplayer(
                title="Error",
                msg="Directory path has not been set")
             .display_message())

    def _organize_files_by_extension(self) -> bool:
        identified_files = FileFinder(self._directory_path)

        if len(identified_files.keys()) == 1:
            extension, files = next(iter(identified_files.items()))
            if len(set(os.path.dirname(file) for file in files)) == 1:
                InfoDisplayer("Info", "All files already organized").display_message()
                return False

            self._file_mover.create_dir_and_move(extension, files, self._directory_path)
            return True

        for extension, files in identified_files.items():
            self._file_mover.create_dir_and_move(extension, files, self._directory_path)
        return True



