# Name: Joshua Smith
# Section: 07


class Student:
    '''Represents a student.
    '''
    def __init__(self, first, last, major, gpa):
        self.first = first
        self.last = last
        self.name = ' '.join([first, last])

        self.major = major
        self.gpa = float(gpa)

    def __repr__(self) -> str:
        return '%s %s %.2f' % (self.name, self.major, self.gpa)


# Purpose: Read std_info.txt
def open_file() -> list:
    with open('std_info.txt') as f:
        return f.read().splitlines()


# Purpose: Turn the lines into a list of students
def parse_lines(lines: list) -> list:
    return [Student(*x.split()) for x in lines]


# Purpose: Get average GPA of students that meet the requirements specified
# by major_check. An ideal use would be, for example, to only get the gpas of
# CPE students by making it lambda x: x.major == 'CPE', or, for example, every
# student by making it lambda x: True
def get_avg(students: list, major_check: bool) -> float:
    gpas = [x.gpa for x in students if major_check(x)]
    return sum(gpas) / len(gpas)


# Purpose: Call all functions, write to output file.
def main() -> None:
    lines = open_file()
    students = parse_lines(lines)

    major_checks = [
        (lambda x: x.major == 'EE', 'EE'),
        (lambda x: x.major == 'CPE', 'CPE'),
        (lambda x: True, 'Total')
    ]

    with open('student_avg.txt', 'w') as f:
        f.write('\n'.join(map(str, students)) + '\n')
        for function, major in major_checks:
            avg = get_avg(students, function)
            f.write('%s average = %.2f\n' % (major, avg))


if __name__ == '__main__':
    main()
