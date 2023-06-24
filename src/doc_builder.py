import version_setter
import file_system
import config

class Builder:

    def __init__(self, base_path: str, config: config.Config, file_system: file_system.FileSystem, version_setter: version_setter.VersionSetter):
        self._file_system = file_system
        self._config = config
        self._base_path = base_path

    def build(self):
        if not self._file_system.directory_exists(self._base_path):
            raise FileNotFoundError(f"Input directory is not found {self._base_path}")

        if not self._file_system.directory_exists(self._config.output_dir_part):
            self._file_system.create_directory(self._config.output_dir_part)