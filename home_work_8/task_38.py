def read_file():
    with open(path_file,'r',encoding='UTF-8') as f:
        for line in f:
            print(line.strip())

def write_file():
    with open(path_file,'a',encoding='UTF-8') as f:
        f.writelines('\n'+input())


def find_file():
    find_info = input()
    with open(path_file,'r',encoding='UTF-8') as f:
        for line in f:
            if find_info.casefold() in line.casefold():
                print(line)


def change_file():
    find_info = input("Введите имя или фамилию: ")
    new_info = input("Введите новую информацию: ")
    with open(path_file,'r',encoding='UTF-8') as f:
        lines = f.readlines()
    with open(path_file,'w',encoding='UTF-8') as f:
        for line in lines:
            if find_info.casefold() in line.casefold():
                if input("Вы уверены, что хотите изменить запись? Да/Нет: ") == "Да":
                    line = new_info + "\n"
                    print("Запись изменена.")
                else:
                    continue
            f.write(line)


def delete_file():
    find_info = input("Введите имя или фамилию: ")
    with open(path_file,'r',encoding='UTF-8') as f:
        lines = f.readlines()
    with open(path_file,'w',encoding='UTF-8') as f:
        for line in lines:
            if find_info.casefold() in line.casefold():
                if input("Вы уверены, что хотите удалить запись? Да/Нет: ") == "Да":
                    print("Запись удалена.")
                    continue
            f.write(line)


def console_menu():
    while True:
        print("1. Вывести данные.")
        print("2. Добавить запись.")
        print("3. Найти запись.")
        print("4. Изменить запись.")
        print("5. Удалить запись.")
        print("6. Выход.")
        choice = input("Введите номер операции: ")
        if choice == "1":
            read_file()
        elif choice == "2":
            write_file()
        elif choice == "3":
            find_file()
        elif choice == "4":
            change_file()
        elif choice == "5":
            delete_file()
        elif choice == "6":
            break
        else:
            print("Неправильный ввод, попробуйте еще раз.")


path_file = 'phone_book.txt'
if __name__ == '__main__':
    console_menu()
