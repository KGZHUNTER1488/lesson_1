contacts = ['Aslan', 'Aibek', 'Adinai', 'Ainura', 'Aizada']

while True:
    client = input('Выберите одну цифру из этих функций: 1 - посмотреть контакты, 2 - добавить контакты, 3 - удалить контакты, 4 - обновить контакты, 5 - выйти из программы: ')
    if client == 1:
        print(contacts)
    elif client == 2:
        new_contact = print(input('Введите контакт'))
        contacts.append(new_contact)
        print(contacts)
    elif client == 3:
        delate_contact = print(input('Выберите контакт'))
        if delate_contact == 'Aslan':
            contacts.remove[0]