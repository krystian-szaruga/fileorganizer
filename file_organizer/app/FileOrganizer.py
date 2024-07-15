from file_organizer.app.App import App
from file_organizer.commands.generate_empty_files.extensions.FileData import FileData
from file_organizer.components.DirectoryEntry import DirectoryEntry
from file_organizer.components.MainFrame import MainFrame
from file_organizer.components.buttons.BrowseButton import BrowseButton
from file_organizer.components.buttons.GenerateTestFilesButton import GenerateTestFilesButton
from file_organizer.components.buttons.OrganizeFilesButton import OrganizeFilesButton


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
