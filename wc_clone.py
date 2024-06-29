import cmd
import os
from pathlib import Path


class WCCloneCli(cmd.Cmd):
    prompt = ">"
    current_dir = os.getcwd()

    def do_ccwc(self, arg):
        operation, file_name = parse(arg)


def parse(arg):
    "Convert a series of zero or more args to an argument tuple"
    return tuple(arg.split())


if __name__ == "__main__":
    WCCloneCli().cmdloop()
