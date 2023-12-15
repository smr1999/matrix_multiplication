from io import (
    TextIOWrapper,
)


class FileUtil:
    @classmethod
    def write_file(cls, file_name: str) -> TextIOWrapper:
        return open(
            file=file_name,
            mode='w'
        )

    @classmethod
    def read_file(cls, file_name: str) -> TextIOWrapper:
        return open(
            file=file_name,
            mode='r'
        )
