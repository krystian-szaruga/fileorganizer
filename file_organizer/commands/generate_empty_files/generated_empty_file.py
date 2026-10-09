import logging
import os.path
from itertools import product
from typing import Optional

from file_organizer.commands.generate_empty_files.extensions.extensions import Extensions
from file_organizer.commands.generate_empty_files.extensions.file_data import FileData


class GenerateEmptyFiles:
    def __init__(self, file_data: Optional[FileData] = None):
        self._file_data = file_data if file_data is not None else FileData()
        self._extensions = Extensions

    def _save_file(self, idx: int, ext: str) -> None:
        file_path = os.path.join(self._file_data.default_dir, f"file{idx}{ext}")
        try:
            with open(file_path, 'w'):
                pass
        except IOError as e:
            logging.error(f"Error saving file: {file_path}. Reason: {e}")
            raise e

    def _get_range(self) -> range:
        return range(1, self._file_data.number_per_extension + 1)

    def generate_empty_files(self) -> None:
        self._file_data.create_dir()
        for ext, idx in product(self._extensions.get_ext(), self._get_range()):
            self._save_file(idx, ext)


if __name__ == '__main__':
    GenerateEmptyFiles(FileData(200)).generate_empty_files()
