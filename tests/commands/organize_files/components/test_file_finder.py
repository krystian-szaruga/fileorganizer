import unittest
from tkinter import messagebox
from unittest.mock import patch
from collections import defaultdict

from file_organizer.commands.organize_files.components.file_finder import FileFinder
from file_organizer.components.message_displayer.info_displayer import InfoDisplayer


class TestFileFinder(unittest.TestCase):
    @patch('os.walk')
    def test_find_all_files(self, mock_os_walk):
        mock_os_walk.return_value = [
            ('/mocked_path', ('subdir',),
             ('file1.txt', 'file2.txt', 'file3.md', 'file4.py', 'file5.py')),
            ('/mocked_path/subdir', (), ('file6.txt', 'file7.md'))
        ]

        result = FileFinder('/mocked_path')

        expected_result = defaultdict(list, {
            '.txt': [
                '/mocked_path/file1.txt',
                '/mocked_path/file2.txt',
                '/mocked_path/subdir/file6.txt'
            ],
            '.md': [
                '/mocked_path/file3.md',
                '/mocked_path/subdir/file7.md'
            ],
            '.py': [
                '/mocked_path/file4.py',
                '/mocked_path/file5.py'
            ]
        })
        self.assertEqual(dict(result), dict(expected_result))

    @patch('os.walk')
    @patch.object(messagebox, "showinfo")
    def test_empty_dir(self, mock_info_displayer, mock_os_walk):
        mock_os_walk.return_value = []
        result = FileFinder('/mocked_path')
        expected_result = defaultdict(list)
        self.assertEqual(dict(result), dict(expected_result))
        mock_info_displayer.assert_called_once_with("Info", "Directory is Empty")


if __name__ == '__main__':
    unittest.main()
