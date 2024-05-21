import os
from unittest import TestCase
from unittest.mock import Mock
from unittest.mock import patch
import sys
sys.path.append('../src')
from doc_builder import Builder
import test_extensions

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

    @patch('builtins.print')
    def test_when_directory_is_not_a_git_repo_issue_warning(self, mock_print):
        base_path = "/path/"
        mock_file_system = Mock()
        mock_file_system.directory_exists.side_effect = lambda path: False if path == ".git" else True

        builder = Builder(base_path, Mock(), mock_file_system, Mock())
        yellow_escape_sequence = "\033[33m"
        reset_escape_sequence = "\033[0m"

        builder.build()

        mock_print.assert_called_once_with(f"{yellow_escape_sequence}This is not a git repository. Document will be generated but it will not be versioned.{reset_escape_sequence}")

    @patch('builtins.print')
    def test_when_directory_is_a_git_repo_do_not_issue_warning(self, mock_print):
        base_path = "/path/"
        mock_file_system = Mock()
        mock_file_system.directory_exists.side_effect = lambda path: True if path == ".git" else True

        builder = Builder(base_path, Mock(), mock_file_system, Mock())
        yellow_escape_sequence = "\033[33m"
        reset_escape_sequence = "\033[0m"

        builder.build()

        mock_print.assert_not_called_with(f"{yellow_escape_sequence}This is not a git repository. Document will be generated but it will not be versioned.{reset_escape_sequence}")