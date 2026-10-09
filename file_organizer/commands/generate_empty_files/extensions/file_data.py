import logging
import os
import shutil
from dataclasses import dataclass, field


@dataclass(frozen=True)
class FileData:
    default_dir: str = field(
        default='./empty_files/', init=False)
    number_per_extension: int = 100

    def create_dir(self) -> None:
        if os.path.exists(self.default_dir):
            self._delete_dir()
        os.makedirs(self.default_dir)

    def _delete_dir(self) -> None:
        try:
            shutil.rmtree(self.default_dir)
            logging.info(f"Folder '{self.default_dir}' and all its contents have been deleted.")
        except OSError as e:
            logging.error(f"Error: {self.default_dir} : {e.strerror}")
