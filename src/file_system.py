import os

class FileSystem:
    def __init__(self, base_path):
        self.base_path = base_path

    def create_directory(self, path):
        full_path = os.path.join(self.base_path, path)
        os.makedirs(full_path, exist_ok=True)

    def directory_exists(self, path):
        full_path = os.path.join(self.base_path, path)
        return os.path.isdir(full_path)