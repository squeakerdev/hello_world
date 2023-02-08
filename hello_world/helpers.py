from argparse import ArgumentParser, Namespace


def parse_args() -> Namespace:
    """Parse the command line arguments."""
    parser = ArgumentParser(
        prog="hello_world",
        description="Prints a string to the console.",
    )

    parser.add_argument("-s", "--string", help="The string to print.", default="Hello, world!")

    return parser.parse_args()
