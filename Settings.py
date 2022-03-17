class Settings:
    def __init__(self, file_name='settings.properties'):
        self.file_name = file_name
        self._load()

    def _load(self):
        with open(self.file_name, "rt") as f:
            self._dim = self.get_option(f).rstrip("\n ")
            self._count= self.get_option(f).rstrip("\n ")
    @property
    def dim(self):
        return self._dim

    @property
    def count(self):
        return self._count

    @staticmethod
    def get_option(file):
        option = file.readline()
        option = option.split("=")
        return option[1].rstrip("\n")
