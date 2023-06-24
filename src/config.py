class Config:

    def __init__(self):
        self._output_dir_part = None   

    @property
    def output_dir_part(self):
        return self._output_dir_part