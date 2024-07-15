import os
from collections import defaultdict
from typing import Callable

from file_organizer.components.message_displayer.InfoDisplayer import InfoDisplayer


def call_file_finder(cls) -> Callable:
    def wrapper(*args, **kwargs) -> defaultdict[str, list]:
        instance = cls()
        result = instance.find_all_files(*args, **kwargs)
        if not len(result.keys()):
            InfoDisplayer("Info", "Directory is Empty").display_message()
        return result

    return wrapper


@call_file_finder
class FileFinder:
    def __init__(self):
        self._files_by_extension = defaultdict(list)

    def find_all_files(self, path: str) -> defaultdict[str, list]:
        [self._files_by_extension[os.path.splitext(file)[-1]].append(
            os.path.join(root, file))
            for root, _, files in os.walk(path)
            for file in files]
        return self._files_by_extension




