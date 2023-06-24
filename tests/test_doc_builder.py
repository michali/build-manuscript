import os
from unittest import TestCase
from unittest.mock import Mock
import sys
sys.path.append('src')
from doc_builder import Builder

class TestDocBuilder(TestCase):

    def test_when_output_dir_does_not_exist_create_it(self):
        output_dir_part = "out"
        mock_config = Mock()
        mock_config.output_dir_part = output_dir_part
        mock_file_system = Mock()
        mock_file_system.directory_exists.side_effect = lambda path: False if path == output_dir_part else True

        builder = Builder('', mock_config, mock_file_system, Mock())

        builder.build()

        mock_file_system.create_directory.assert_called_once_with(output_dir_part)

    def test_when_output_dir_exists_do_not_create_it(self):
        base_path = "/path"
        output_dir_part = "out"
        mock_config = Mock()
        mock_config.output_dir_part = output_dir_part
        mock_file_system = Mock()
       # mock_file_system.directory_exists.side_effect = lambda path: True if path == output_dir_part else False
        mock_file_system.directory_exists.side_effect = lambda path: True if path == base_path else True
        builder = Builder('', mock_config, mock_file_system, Mock())

        builder.build()

        mock_file_system.create_directory.assert_not_called()

    def test_when_the_input_dir_doesnt_exist_exit_with_error(self):
        base_path = "/path/"
        mock_file_system = Mock()
        mock_file_system.directory_exists.side_effect = lambda path: False if path == base_path else True

        builder = Builder(base_path, Mock(), mock_file_system, Mock())

        with self.assertRaises(FileNotFoundError) as err:
            builder.build();

        self.assertEqual(str(err.exception), f"Input directory is not found {base_path}")