class FileManager:

    def __init__(self, file_name: str, mode: str) -> None:

        self.file_name: str = file_name
        self.mode: str = mode


    def __enter__(self):

        self.file_wrapper = open(self.file_name, self.mode)


    def __exit__(self exc_type, exc_value, traceback):

        self.file_wrapper.