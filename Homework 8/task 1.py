path = 'phonebook.txt'

def change_contact():
    with open(path, 'r+', encoding='utf-8') as file:
        data = file.readlines()
        search_contact = input("Введите одну из харктеристик [имя, фамилия, номер, комментарий]: ")
        arr = []
        file_index = []
        count_index = 0
        line_target = -1
        for line in data:
            if search_contact in line:
                arr.append(line)
                file_index.append(count_index)
                line_target = 1
            count_index += 1
        if line_target == -1:
            print('нет контакта')
        else:
            if len(arr) >= 1:
                print('Найденные контакты: ')
                for i, line in enumerate(arr, 1):
                    print(f'{i} : {line}')
                id_change = int(input('Выберите номер контакта: '))
                line_change = arr[id_change - 1]
            name = input("Скорректируйте имя: ")
            surname = input("Скорректируйте фамилию: ")
            phone = input("Скорректируйте номер: ")
            comment = input('Скорректируйте коммент: ')
            replace_contact = f'{name};{surname};{phone};{comment};'
            file.seek(0)
            count_n = 0
            for line in data:
                if line_change == line and file_index[id_change - 1] == count_n:
                    file.write(f'{replace_contact}\n')
                else:
                    file.write(line)
                count_n += 1
            print('контакт изменен')




def delete_contact():
    with open(path, 'r+', encoding="utf8") as file:
        data = file.readlines()
        search_contact = input("Введите одну из харктеристик [имя, фамилия, номер, комментарий]: ")
        arr = []
        file_index = []
        count_index = 0
        line_target = -1
        for line in data:
            if search_contact in line:
                arr.append(line)
                file_index.append(count_index)
                line_target = 1
            count_index += 1
        if line_target == -1:
            print('нет контакта')
        else:
            if len(arr) >= 1:
                print('Найденные контакты: ')
                for i, line in enumerate(arr, 1):
                    print(f'{i} : {line}')
                id_change = int(input('Выберите номер контакта: '))
                line_change = arr[id_change - 1]
            file.seek(0)
            count_n = 0
            for line in data:
                if line_change != line and file_index[id_change - 1] != count_n:
                    file.write(line)
                count_n += 1
            print('Контакт удален')
            file.truncate()


delete_contact()


