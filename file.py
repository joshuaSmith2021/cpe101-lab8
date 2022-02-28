# Name: Joshua Smith
# Section: 07


# Purpose: Read in.txt and return lines as a list of strings
def open_file() -> list:
    with open('in.txt') as f:
        return f.read().splitlines()


# Purpose: Given line and its line number, make a string detailing the line
def line_info(line: str, i: int) -> str:
    return 'Line %d (%d chars): %s' % (i + 1, len(line), line)


# Print out all of the lines, and call line_info for each line
def print_file(lines: list) -> None:
    print('\n'.join([line_info(x, i) for i, x in enumerate(lines)]))


# Purpose: Open file and print everything
def main() -> None:
    lines = open_file()
    print_file(lines)


if __name__ == '__main__':
    main()
