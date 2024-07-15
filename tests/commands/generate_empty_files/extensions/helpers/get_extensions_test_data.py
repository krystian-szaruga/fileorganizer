from dataclasses import fields

from file_organizer.commands.generate_empty_files.extensions.Extensions import Extensions


def get_extensions_test_data() -> list[str]:
    return [f".{field_obj.name}"
            for field_obj in fields(Extensions)]


