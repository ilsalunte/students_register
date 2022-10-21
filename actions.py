from typing import Any
from .storage import add_mark, calculate_one_mean, calculate_all_means, delete_student, WrongInput, add_student, \
    print_one_student, print_all_students, check_student_presence

StudentName = tuple[str, str]
StudentData = dict[str, Any]
StudentMarks = list[int]


def action_add_mark() -> None:
    last_name, first_name = retrieve_student_data()
    check_student_presence(last_name=last_name, first_name=first_name)
    mark = retrieve_student_mark()
    add_mark(last_name=last_name, first_name=first_name, mark=mark)
    print('Ocena dodana :)')


def action_calculate_mean() -> None:
    print('Chcesz obliczyć średnią: 1 - jednego ucznia czy 2 - wszystkich uczniów? ')
    choice = input()
    if choice == '1':
        last_name, first_name = retrieve_student_data()
        check_student_presence(last_name=last_name, first_name=first_name)
        student_mean = calculate_one_mean(last_name=last_name, first_name=first_name)
        print(f'{last_name} {first_name} średnia: {student_mean}')
    elif choice == '2':
        all_students_means = calculate_all_means()
        if all_students_means:
            for item in all_students_means:
                if item[1] is not None:
                    mean_str = f'{item[1]:.2f}'
                else:
                    mean_str = '-'
                print(f"{' '.join(item[0])} średnia: {mean_str}")
        else:
            print('Brak uczniów w dzienniku.')
    else:
        print('Nieprawidłowy wybór.')


def action_delete_student() -> None:
    last_name, first_name = retrieve_student_data()
    check_student_presence(last_name=last_name, first_name=first_name)
    delete_student(last_name=last_name, first_name=first_name)
    print('Uczeń usunięty.')


def action_add_student() -> None:
    last_name, first_name = retrieve_student_data()
    add_student(last_name=last_name, first_name=first_name)
    print('Uczeń został dodany.')


def action_print_one_student() -> None:
    last_name, first_name = retrieve_student_data()
    check_student_presence(last_name=last_name, first_name=first_name)
    marks = print_one_student(last_name=last_name, first_name=first_name)
    print(f"{last_name} {first_name} oceny: {', '.join(str(x) for x in marks)}")


def action_print_all_students() -> None:
    students = print_all_students()
    for student_name, student_data in students.items():
        print(f"{' '.join(student_name)} oceny: {', '.join(str(o) for o in student_data['oceny'])}")


def retrieve_student_data() -> tuple[str, str]:
    print('Podaj nazwisko ucznia:')
    students_second_name = input().capitalize()
    print('Podaj imię ucznia:')
    students_name = input().capitalize()
    return students_second_name, students_name


def retrieve_student_mark() -> int:
    print('Podaj ocenę:')
    new_mark_str = input()
    try:
        new_mark = int(new_mark_str)
    except ValueError as err:
        raise WrongInput('Podano nieprawidłową wartość oceny.') from err

    if new_mark in [1, 2, 3, 4, 5, 6]:
        return new_mark
    raise WrongInput('Podano nieprawidłową wartość oceny.')
