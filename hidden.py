# Name: Joshua Smith
# Section: 07


# Purpose: Read hidden.ppm
def open_file() -> list:
    with open('hidden.ppm') as f:
        return f.read().splitlines()


# Purpose: Get RGB triples from lines
def get_triples(lines: list) -> list:
    return [lines[3 * i: 3 * (i + 1)] for i in range(1, len(lines) // 3)]


# Purpose: Change number * 10 but below 255
def change(num):
    new = num * 10
    return new if new < 255 else 255


# Purpose: Modify triples to r *= 10 and every element is r
def modify_lines(triples: list) -> list:
    return [[change(int(x[0]))] * 3 for x in triples]


# Purpose: Call functions
def main() -> None:
    lines = open_file()
    triples = get_triples(lines)
    corrected = modify_lines(triples)
    unwrapped = [x for triple in corrected for x in triple]

    with open('discovered.ppm', 'w') as f:
        f.write('\n'.join(lines[:3]) + '\n')
        f.write('\n'.join(map(str, unwrapped)) + '\n')


if __name__ == '__main__':
    main()
