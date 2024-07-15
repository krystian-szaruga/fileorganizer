import os
import shutil
from typing import Optional


class FileMoverHandler:
    def __init__(self):
        self._directory_path: Optional[str] = None

    def create_dir_and_move(self, extension: str, files: list[str], path: str) -> None:
        self._directory_path = path
        self._create_extension_directory(extension)
        for file in files:
            self._move_file(file, extension)

    def _create_extension_directory(self, file_extension: str) -> None:
        extension_dir = os.path.join(self._directory_path, file_extension)
        if not os.path.exists(extension_dir):
            os.makedirs(extension_dir)

    def _move_file(self, file: str, file_extension: str) -> None:
        shutil.move(
            file,
            os.path.join(
                self._directory_path, file_extension, os.path.basename(file)))
