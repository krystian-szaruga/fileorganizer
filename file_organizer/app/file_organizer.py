from file_organizer.app.app import App
from file_organizer.commands.generate_empty_files.extensions.file_data import FileData
from file_organizer.components.directory_entry import DirectoryEntry
from file_organizer.components.main_frame import MainFrame
from file_organizer.components.buttons.browse_buttons import BrowseButton
from file_organizer.components.buttons.generate_test_files_button import GenerateTestFilesButton
from file_organizer.components.buttons.organize_files_button import OrganizeFilesButton


class FileOrganizerApp(App):
    def __init__(self, file_data: FileData = FileData()):
        super().__init__()
        self._file_data = file_data

    def build(self):
        self.root_widget.title("File Organizer")
        self.main_frame = MainFrame().set_main_frame(
            self.root_widget)
        self.directory_entry = DirectoryEntry().set_directory_entry(
            self.main_frame)
        BrowseButton(self.main_frame).build(self.directory_entry)
        OrganizeFilesButton(self.main_frame).build(self.directory_entry)
        GenerateTestFilesButton(self.main_frame, self._file_data).build()
