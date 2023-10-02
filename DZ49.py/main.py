from logger import input_contact, print_contacts, find_contact, edit_contact, delete_contact

def menu():
    text = "Главное меню:\n" \
           "1. Добавить контакт\n" \
           "2. Посмотреть все контакты\n" \
           "3. Найти контакт\n" \
           "4. Редактировать контакт\n" \
           "5. Удалить контакт\n" \
           "0. Выход\n"

    print(text)
    while True:
        command = input('Введите команду: ')
        if command == '1':
            input_contact()
        elif command == '2':
            print_contacts()
        elif command == '3':
            find_contact()
        elif command == '4':
            edit_contact()
        elif command == '5':
            delete_contact()
        elif command == '0':
            break
        else:
            print('Неверная команда.')

if __name__ == '__main__':
    menu()
