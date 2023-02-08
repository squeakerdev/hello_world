from typing import *


class ASCIICharacter:
    """Represents a single ASCII character."""

    def __init__(self, char: str):
        if len(char) != 1:
            raise ValueError(
                f"{type(self).__name__} can only represent a single character"
            )

        self.char: str = char

    def __add__(self, other):
        if isinstance(other, ASCIIString):
            return ASCIIString((str(self), *other.chars))
        elif isinstance(other, str):
            return ASCIIString((str(self), *ASCIIString(other).chars))
        else:
            raise TypeError(
                f"Cannot add {type(self).__name__} to {type(other).__name__}"
            )

    def __eq__(self, other):
        if type(other) is type(self):
            return self.char == other.char
        else:
            return False

    def __hash__(self):
        return hash(self.char)

    def __str__(self):
        return self.char

    def __repr__(self):
        return f"{type(self).__name__}({self.char})"

    @property
    def is_valid(self) -> bool:
        """Whether the string contains only valid ASCII characters."""
        return self.char.isascii()

    @property
    def string(self) -> str:
        """Equivalent to str(self)."""
        return self.__str__()


class ASCIIString:
    """Represents a string of ASCII characters."""

    def __init__(self, chars: Iterable[ASCIICharacter]):
        self.chars: List[ASCIICharacter] = list(chars)

    def __add__(self, other):
        if isinstance(other, ASCIIString):
            return ASCIIString(self.chars + other.chars)
        elif isinstance(other, str):
            return ASCIIString(self.chars + ASCIIString(other).chars)
        else:
            raise TypeError(
                f"Cannot add {type(self).__name__} to {type(other).__name__}"
            )

    def __eq__(self, other):
        if type(other) is type(self):
            return self.chars == other.chars
        else:
            return False

    def __hash__(self):
        return hash(tuple(self.chars))

    def __iter__(self, *, as_strings: bool = False) -> Iterable[Union[ASCIICharacter, str]]:
        if as_strings:
            return iter(map(str, self.chars))
        else:
            return iter(self.chars)

    def __str__(self):
        return "".join(map(str, self.chars))

    def __repr__(self):
        return f"{type(self).__name__}({self.__str__()!r})"

    def iter_strings(self) -> Iterable[str]:
        """Iterate over all characters, formatted as strings."""
        return self.__iter__(as_strings=True)

    @property
    def is_valid(self) -> bool:
        """Whether the string contains only valid ASCII characters."""
        return all(map(lambda c: c.isascii(), self))

    @property
    def string(self) -> str:
        """Equivalent to str(self)."""
        return self.__str__()
