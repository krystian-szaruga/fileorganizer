import random
import unittest

from parameterized import parameterized

from file_organizer.commands.generate_empty_files.extensions.Extensions import Extensions
from tests.commands.generate_empty_files.extensions.helpers.get_extensions_test_data import \
    get_extensions_test_data


class TestExtensions(unittest.TestCase):

    @parameterized.expand(get_extensions_test_data())
    def test_get_all_extensions(self, generated_extensions):
        self.assertIn(
            generated_extensions, Extensions.get_ext())

    def test_extensions_with_custom_param(self):
        with self.assertRaises(TypeError):
            Extensions(".custom")

    def test_modifying_extension_obj_attribute(self):
        extensions = Extensions()
        with self.assertRaises(AttributeError):
            setattr(
                extensions,
                random.choice(get_extensions_test_data()).replace(".", ""),
                "new_value")


if __name__ == "__main__":
    unittest.main()


