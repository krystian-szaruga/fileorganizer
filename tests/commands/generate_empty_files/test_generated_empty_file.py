import os
import random
import shutil
import unittest
from unittest.mock import patch

from file_organizer.commands.generate_empty_files.generated_empty_file import GenerateEmptyFiles
from file_organizer.commands.generate_empty_files.extensions.extensions import Extensions
from file_organizer.commands.generate_empty_files.extensions.file_data import FileData
from tests.commands.generate_empty_files.extensions.helpers.count_files import count_files, \
    count_files_per_ext


class TestGenerateEmptyFiles(unittest.TestCase):

    def tearDown(self):
        shutil.rmtree("./empty_files")

    @patch.object(Extensions, attribute="get_ext", return_value=['.txt', '.py'])
    def test_generate_empty_files(self, mock_get_ext):
        file_data = FileData(number_per_extension=3)
        GenerateEmptyFiles(file_data).generate_empty_files()
        expected_files = ['file1.txt', 'file2.txt', 'file3.txt', 'file1.py', 'file2.py', 'file3.py']
        not_expected_files = ['file1.js', 'file2.js', 'file3.js']
        for filename in expected_files:
            file_path = os.path.join(file_data.default_dir, filename)
            self.assertTrue(os.path.exists(file_path), f"File {filename} not found")

        for filename in not_expected_files:
            file_path = os.path.join(file_data.default_dir, filename)
            self.assertTrue(not os.path.exists(file_path), f"file {filename} found")

    @patch('builtins.open', side_effect=IOError("mocked IOError"))
    def test_save_file_io_error(self, mock_open):
        generator = GenerateEmptyFiles()
        with self.assertRaises(IOError):
            generator.generate_empty_files()

    @patch.object(Extensions, attribute="get_ext", return_value=['.js', '.txt'])
    def test_number_of_file_per_extension(self, mock_get_ext):
        random_number = random.randint(1, 200)
        file_data = FileData(number_per_extension=random_number)
        generator = GenerateEmptyFiles(file_data)
        generator.generate_empty_files()
        total_files = count_files(file_data.default_dir)
        total_files_per_ext = count_files_per_ext(
            file_data.default_dir,
            random.choice(['.js', '.txt']))
        self.assertEqual(random_number*2, total_files)
        self.assertEqual(random_number, total_files_per_ext)


if __name__ == '__main__':
    unittest.main()
