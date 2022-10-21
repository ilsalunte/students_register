from typing import Any, Optional
from statistics import mean, StatisticsError


class WrongInput(Exception):
    pass


StudentName = tuple[str, str]
StudentData = dict[str, Any]
StudentMarks = list[int]

STUDENTS_MARKS: dict[StudentName, StudentData] = \
    {('Donald', 'Kaczor'): {'oceny': [5, 3, 2]}, ('Miki', 'Myszka'): {'oceny': [5, 4, 2]},
     ('Daisy', 'Kaczka'): {'oceny': []}}


def add_mark(last_name: str, first_name: str, mark: int) -> None:
    student_data = (last_name, first_name)
    try:
        STUDENTS_MARKS[student_data]['oceny'].append(mark)
    except KeyError as err:
        raise WrongInput('Nie znaleziono ucznia.') from err


def calculate_one_mean(last_name: str, first_name: str) -> float:
    try:
        student_mean = mean(STUDENTS_MARKS[last_name, first_name]['oceny'])
        return student_mean
    except KeyError as err:
        raise WrongInput('Nie znaleziono ucznia.') from err
    except StatisticsError as err:
        raise WrongInput('Uczeń nie posiada żadnych ocen.') from err


def calculate_all_means() -> list[tuple[StudentName, Optional[float]]]:
    all_students_means = []
    for student_name, student_data in STUDENTS_MARKS.items():
        mean_value: Optional[float] = None
        if student_data['oceny']:
            mean_value = mean(student_data['oceny'])
        all_students_means.append((student_name, mean_value))
    return all_students_means


def delete_student(last_name: str, first_name: str) -> None:
    try:
        STUDENTS_MARKS.pop((last_name, first_name))
    except KeyError as err:
        raise WrongInput('Nie znaleziono ucznia.') from err


def add_student(last_name: str, first_name: str) -> None:
    STUDENTS_MARKS[(last_name, first_name)] = {'oceny': []}


def print_one_student(last_name: str, first_name: str) -> StudentMarks:
    try:
        return STUDENTS_MARKS[(last_name, first_name)]['oceny']
    except KeyError as err:
        raise WrongInput('Nie znaleziono ucznia.') from err


def print_all_students() -> dict[StudentName, StudentData]:
    return STUDENTS_MARKS


def check_student_presence(last_name: str, first_name: str) -> None:
    if (last_name, first_name) not in STUDENTS_MARKS:
        raise WrongInput('Nie znaleziono ucznia')


if __name__ == '__main__':
    result = calculate_all_means()
    print(result)
