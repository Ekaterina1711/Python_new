import os

def input_contact():
    if not os.path.isfile('data.txt'):
        open('data.txt', 'w').close()

    with open('data.txt', 'a', encoding='utf-8') as f:
        user = input('Введите имя, фамилию и телефон: ').strip().split()
        f.write(';'.join(user) + '\n')

def print_contacts():
    with open('data.txt', 'r', encoding='utf-8') as f:
        contacts = f.readlines()
    for contact in contacts:
        print(*contact.strip().split(';'))

def find_contact():
    with open('data.txt', 'r', encoding='utf-8') as f:
        contacts = f.readlines()
    while True:
        print('По каким параметрам ищем контакт?:\n1. Имя\n2. Фамилия\n3. Телефон')
        command_index = input('Команда: ')
        if command_index not in '123':
            print('Других параметров нет.')
        else:
            break
    data = input('Введите данные: ')
    print('Найденные контакты: ')
    for contact in contacts:
        full_contact = contact.strip().split(';')
        if data == full_contact[int(command_index) - 1]:
            print(' '.join(full_contact))

def edit_contact():
    with open('data.txt', 'r', encoding='utf-8') as f:
        contacts = f.readlines()
    while True:
        print('Введите имя или фамилию для редактирования контакта:')
        command_index = input('Команда (1 - имя, 2 - фамилия): ')
        if command_index not in '12':
            print('Других параметров нет.')
        else:
            break
    data = input('Введите данные: ')
    found_contacts = []
    for contact in contacts:
        full_contact = contact.strip().split(';')
        if data == full_contact[int(command_index) - 1]:
            found_contacts.append(full_contact)

    if found_contacts:
        print('Найденные контакты: ')
        for i, contact in enumerate(found_contacts, start=1):
            print(f'{i}. {" ".join(contact)}')

        contact_number = input('Введите номер контакта для редактирования: ')
        if contact_number.isdigit() and 1 <= int(contact_number) <= len(found_contacts):
            new_data = input('Введите новые данные для контакта: ')
            contacts.remove(';'.join(found_contacts[int(contact_number) - 1]) + '\n')
            contacts.append(new_data + '\n')
            with open('data.txt', 'w', encoding='utf-8') as f:
                f.writelines(contacts)
            print('Контакт успешно отредактирован.')
        else:
            print('Неверный номер контакта.')
    else:
        print('Контакты не найдены.')

def delete_contact():
    with open('data.txt', 'r', encoding='utf-8') as f:
        contacts = f.readlines()
    while True:
        print('Введите имя или фамилию для удаления контакта:')
        command_index = input('Команда (1 - имя, 2 - фамилия): ')
        if command_index not in '12':
            print('Других параметров нет.')
        else:
            break
    data = input('Введите данные: ')
    found_contacts = []
    for contact in contacts:
        full_contact = contact.strip().split(';')
        if data == full_contact[int(command_index) - 1]:
            found_contacts.append(full_contact)

    if found_contacts:
        print('Найденные контакты: ')
        for i, contact in enumerate(found_contacts, start=1):
            print(f'{i}. {" ".join(contact)}')

        contact_number = input('Введите номер контакта для удаления: ')
        if contact_number.isdigit() and 1 <= int(contact_number) <= len(found_contacts):
            contacts.remove(';'.join(found_contacts[int(contact_number) - 1]) + '\n')
            with open('data.txt', 'w', encoding='utf-8') as f:
                f.writelines(contacts)
            print('Контакт успешно удален.')
        else:
            print('Неверный номер контакта.')
    else:
        print('Контакты не найдены.')
