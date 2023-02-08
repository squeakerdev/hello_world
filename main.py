from io import TextIOWrapper
from sys import stdout
from typing import *


class InvalidCharactersException(Exception):
    """Called when a string contains invalid characters."""

    def __init__(self, string: str, chars: Iterable[str]):
        super().__init__(f'Invalid characters in string "{string}": {tuple(chars)}')


class ASCIICharacter:
    """Represents a single ASCII character."""

    def __init__(self, char: str):
        if len(char) != 1:
            raise ValueError(
                f"{type(self).__name__} can only represent a single character"
            )

        self.char = char

    def __str__(self):
        return self.char

    def __repr__(self):
        return f"{type(self).__name__}({self.char})"


class ASCIIPrinter:
    """Prints a string from either a file or str."""

    def __init__(
        self,
        *,
        string: Optional[str] = None,
        file: Optional[Union[str, TextIOWrapper]] = None,
    ):
        """
        :param string: The string to print.
        :param file: The file to read the string from.
        """
        if string is not None and file is not None:
            raise ValueError("Must provide either string or file, not both")

        if string is None and file is None:
            raise ValueError("Must provide either string or file")

        self._string: str = string or self.read_file(file)
        self._chars_allowed: Set[ASCIICharacter] = self._get_chars()
        self.has_printed: bool = False

    def __str__(self):
        return self._string

    def __repr__(self):
        return f"{type(self).__name__}({self._string!r})"

    @property
    def has_string(self):
        """Whether the printer has a string ready to print."""
        return bool(self._string)

    @staticmethod
    def read_file(file: Union[str, TextIOWrapper]) -> Optional[str]:
        """
        Reads a file and returns its contents as a string.
        :param file: The file to read.
        :returns: The contents of the file.
        """
        if isinstance(file, str):
            with open(file, "r") as f:
                return f.read()
        elif isinstance(file, TextIOWrapper):
            return file.read()
        else:
            raise TypeError(
                f"file must be of type str or TextIO, got {type(file).__name__}"
            )

    def _get_chars(self) -> Set[ASCIICharacter]:
        """
        Get a list of the characters in a string.
        :returns: A set of the characters in the string.
        """
        chars = set()

        # Iterate over all ASCII characters
        for char in (chr(i) for i in range(128)):
            if char in self._string:
                chars.add(ASCIICharacter(char))

        return chars

    def print(self, file: Optional[TextIOWrapper] = None) -> int:
        """
        Prints the string to the console or given file.
        :param file: The file to write to. Defaults to stdout.
        :returns: The number of bytes written.
        """
        # Type check
        if file and not isinstance(file, TextIOWrapper):
            raise TypeError(
                f"file must be of type None or TextIOWrapper, got {type(file).__name__}"
            )

        string = self._string

        # Check for invalid characters
        invalid_chars = tuple(
            c
            for c in self._string
            if c not in map(lambda x: x.char, self._chars_allowed)
        )
        if invalid_chars:
            raise InvalidCharactersException(string, invalid_chars)

        # Print
        bytes_printed = file.write(string) if file else stdout.write(string)
        self.has_printed = True

        return bytes_printed


if __name__ == "__main__":
    printer = ASCIIPrinter(string="Hello, world!")
    printer.print()
