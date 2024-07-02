import cmd
import os
import sys
from pathlib import Path


class WCCloneCli(cmd.Cmd):
    prompt = ">"
    current_dir = os.getcwd()

    def do_ccwc(self, arg):
        args = parse(arg)
        operation = args[0]
        file_name = args[1] if len(args) > 1 else None

        file_content = (
            Path(file_name).read_text() if file_name else sys.stdin.readlines()
        )

        match operation:
            case "-c":
                size = Path(f"{self.current_dir}/{file_name}/").stat().st_size
                print(f"{size} {file_name}")
            case "-l":
                print(f"{count_lines(file_content)} {file_name}")
            case "-w":
                print(f"{count_words(file_content)} {file_name}")
            case "-m":
                print(f"{count_chars(file_content)} {file_name}")


def count_chars(file_content: str) -> int:
    return len(file_content)


def count_words(file_content: str) -> int:
    return len(file_content.split())


def count_lines(file_content: str) -> int:
    return file_content.count("\n")


def parse(arg: str) -> tuple[str, str]:
    return arg.split(" ")


if __name__ == "__main__":
    WCCloneCli().cmdloop()
