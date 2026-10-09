import os
import unittest
from unittest.mock import patch, call

from file_organizer.commands.organize_files.components.file_mover_handler import FileMoverHandler


class TestFileMoverHandler(unittest.TestCase):
    @patch('shutil.move')
    @patch('os.makedirs')
    @patch('os.path.exists', side_effect=lambda path: False)
    def test_create_dir_and_move(self, mock_exists, mock_makedirs, mock_move):
        handler = FileMoverHandler()

        extension = 'txt'
        files = ['/path/to/file1.txt', '/path/to/file2.txt']
        path = '/destination'

        handler.create_dir_and_move(extension, files, path)

        self.assertEqual(handler._directory_path, path)
        mock_exists.assert_called_once_with(os.path.join(path, extension))
        mock_makedirs.assert_called_once_with(os.path.join(path, extension))
        mock_move.assert_has_calls([
            call('/path/to/file1.txt', os.path.join(path, extension, 'file1.txt')),
            call('/path/to/file2.txt', os.path.join(path, extension, 'file2.txt'))
        ], any_order=True)


if __name__ == '__main__':
    unittest.main()
