from file_organizer.app.FileOrganizer import FileOrganizerApp

if __name__ == "__main__":
    app = FileOrganizerApp()
    app.build()
    app.root_widget.mainloop()
