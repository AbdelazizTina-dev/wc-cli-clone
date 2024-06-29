import cmd
import os
from pathlib import Path


class WCCloneCli(cmd.Cmd):
    prompt = ">"
    current_dir = os.getcwd()

    def do_ccwc(self, arg):
        operation, file_name = parse(arg)

        match operation:
            case "-c":
                size = Path(f"{self.current_dir}/{file_name}/").stat().st_size
                print(f"{size} {file_name}")


def parse(arg):
    "Convert a series of zero or more args to an argument tuple"
    return tuple(arg.split())


if __name__ == "__main__":
    WCCloneCli().cmdloop()
