from dziennik.storage import WrongInput
from dziennik.actions import action_delete_student, action_add_student, \
    action_add_mark, action_calculate_mean, action_print_one_student, action_print_all_students


def main():
    while True:
        print('Wybierz czynność: (D)odanie oceny, (O)bliczenie średniej, '
              '(U)sunięcie ucznia, do(P)isanie ucznia, (W)yświetl, (Z)akończ')
        action = input().upper()
        try:
            if action == 'D':
                action_add_mark()

            elif action == 'O':
                action_calculate_mean()

            elif action == 'U':
                action_delete_student()

            elif action == 'P':
                action_add_student()

            elif action == 'W':
                print('Czy chcesz wyświetlić 1- dane jednego ucznia czy 2 - cały dziennik?')
                choice = input()
                if choice == '1':
                    action_print_one_student()
                elif choice == '2':
                    action_print_all_students()
                else:
                    print('Nieprawidłowy wybór.')

            elif action == 'Z':
                print('Finito')
                break
            else:
                print('Nieprawidłowo wybrana czynność.')
                continue
        except WrongInput as ex:
            print(f'Wystąpił błąd: {ex}')
            continue


if __name__ == '__main__':
    main()
