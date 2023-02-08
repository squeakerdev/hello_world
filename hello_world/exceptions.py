from typing import *


class InvalidCharactersException(Exception):
    """Called when a string contains invalid characters."""

    def __init__(self, string: str, chars: Iterable[str]):
        super().__init__(f'Invalid characters in string "{string}": {tuple(chars)}')