import os.path
import shutil
import unittest

from file_organizer.commands.generate_empty_files.extensions.FileData import FileData


class TestFileData(unittest.TestCase):

    def setUp(self):
        self.file_data = FileData()

    def tearDown(self):
        shutil.rmtree(self.file_data.default_dir)

    def test_creating_directory(self):
        self.file_data.create_dir()
        self.assertTrue(os.path.exists("./empty_files/"))


if __name__ == "__main__":
    unittest.main()
