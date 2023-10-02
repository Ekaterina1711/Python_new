# Создаем пустой справочник в виде списка кортежей, где каждый кортеж содержит информацию о контакте (Фамилия, Имя, Отчество, Номер телефона).
phonebook = []

# Функция для добавления нового контакта в справочник.
def add_contact():
    print("Введите данные нового контакта:")
    last_name = input("Фамилия: ")
    first_name = input("Имя: ")
    middle_name = input("Отчество: ")
    phone_number = input("Номер телефона: ")
    contact = (last_name, first_name, middle_name, phone_number)
    phonebook.append(contact)
    print("Контакт успешно добавлен.")

# Функция для вывода всех контактов из справочника.
def show_contacts():
    if not phonebook:
        print("Справочник пуст.")
    else:
        print("Список контактов:")
        for index, contact in enumerate(phonebook, start=1):
            last_name, first_name, middle_name, phone_number = contact
            print(f"{index}. {last_name} {first_name} {middle_name}, {phone_number}")

# Функция для изменения данных контакта по фамилии или имени.
def edit_contact():
    search_term = input("Введите фамилию или имя контакта для редактирования: ")
    found_contacts = []
    
    for contact in phonebook:
        last_name, first_name, middle_name, phone_number = contact
        if search_term in (last_name, first_name):
            found_contacts.append(contact)
    
    if not found_contacts:
        print("Контакт не найден.")
    else:
        print("Найденные контакты:")
        for index, contact in enumerate(found_contacts, start=1):
            last_name, first_name, middle_name, phone_number = contact
            print(f"{index}. {last_name} {first_name} {middle_name}, {phone_number}")
        
        choice = input("Выберите номер контакта для редактирования: ")
        if choice.isdigit() and 1 <= int(choice) <= len(found_contacts):
            index = int(choice) - 1
            last_name, first_name, middle_name, phone_number = found_contacts[index]
            print(f"Редактирование контакта: {last_name} {first_name} {middle_name}, {phone_number}")
            new_phone_number = input("Введите новый номер телефона: ")
            phonebook.remove(found_contacts[index])
            found_contacts[index] = (last_name, first_name, middle_name, new_phone_number)
            phonebook.append(found_contacts[index])
            print("Контакт успешно отредактирован.")
        else:
            print("Неверный выбор.")

# Функция для удаления контакта по фамилии или имени.
def delete_contact():
    search_term = input("Введите фамилию или имя контакта для удаления: ")
    found_contacts = []
    
    for contact in phonebook:
        last_name, first_name, middle_name, phone_number = contact
        if search_term in (last_name, first_name):
            found_contacts.append(contact)
    
    if not found_contacts:
        print("Контакт не найден.")
    else:
        print("Найденные контакты:")
        for index, contact in enumerate(found_contacts, start=1):
            last_name, first_name, middle_name, phone_number = contact
            print(f"{index}. {last_name} {first_name} {middle_name}, {phone_number}")
        
        choice = input("Выберите номер контакта для удаления: ")
        if choice.isdigit() and 1 <= int(choice) <= len(found_contacts):
            index = int(choice) - 1
            last_name, first_name, middle_name, phone_number = found_contacts[index]
            print(f"Удаление контакта: {last_name} {first_name} {middle_name}, {phone_number}")
            phonebook.remove(found_contacts[index])
            print("Контакт успешно удален.")
        else:
            print("Неверный выбор.")

# Основной цикл программы.
while True:
    print("\nМеню:")
    print("1. Добавить контакт")
    print("2. Вывести список контактов")
    print("3. Редактировать контакт")
    print("4. Удалить контакт")
    print("5. Выход")
    
    choice = input("Выберите действие: ")
    
    if choice == "1":
        add_contact()
    elif choice == "2":
        show_contacts()
    elif choice == "3":
        edit_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        break
    else:
        print("Неверный выбор. Попробуйте ещё раз.")
