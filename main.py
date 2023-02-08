from hello_world.helpers import parse_args
from hello_world.printer import ASCIIPrinter

if __name__ == "__main__":
    args = parse_args()

    printer = ASCIIPrinter(string=args.string)
    printer.print()
