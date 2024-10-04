import functions as func


def show_menu():
    print("\nЗаметки.\nФункции:\n1 - вывод всех заметок\n2 - вывод одной заметки\n3 - удаление заметки\n4 - добавить заметку\n5 - редактировать заметку по id\nПустота - выход\nВведите номер функции: ")


def start():
    while True:
        show_menu()
        user_input = input().strip()
        if user_input == '1':
            func.print_all_notes()
        elif user_input == '2':
            func.print_one_note()
        elif user_input == '3':
            func.delete_note()
        elif user_input == '4':
            func.add_note()
        elif user_input == '5':
            func.edit_note()
        else:
            print("Программа завершена")
            break


start()