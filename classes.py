import sqlite3
from datetime import datetime

conn = sqlite3.connect('Base.db')
cursor = conn.cursor()
date = datetime.now().date()

class System_of_Projects_and_Contracts:
    def __init__(self):
        conn.execute(
            'CREATE TABLE IF NOT EXISTS Contract(название PRIMARY KEY, дата_создания, дата_подписания, статус, '
            'проект)')
        conn.commit()
        conn.execute('CREATE TABLE IF NOT EXISTS Project(название PRIMARY KEY, дата_создания, ссылка)')
        conn.commit()

    def main_menu(self):
        print(
            "Введите 1 - созданить договор, 2 - просмотреть все договоры, 3 - создать проект, 4 - просмотреть все проекты, "
            "5 - завершить работу программы")
        a = int(input())
        while a != 5:
            if a == 1:
                return Button1.button(self)
            elif a == 2:
                return Button2.button(self)
            elif a == 3:
                return Button3.button(self)
            elif a == 4:
                return Button4.button(self)
            else:
                print("Вы ввели неправильное число, работа с программой завершена")
                return
        print("Спасибо за работу с программой!")
        conn.close()

class Button1(System_of_Projects_and_Contracts):
    def button(self):
        dog = input("Введите название договора: ")
        cursor.execute('INSERT INTO Contract VALUES(?,?,?,?,?)', (dog, date, "Не подписан", 'черновик','не задан'))
        conn.commit()
        print("Договор успешно создан!")
        print("Для продолжения создания договоров нажмите 1, для просмотра договоров - 2, для просмотра проектов - 3, "
              "для завершения - 4")
        choise = int(input())
        if choise == 1:
            pass
        elif choise == 2:
            dog_all = cursor.execute('SELECT * FROM Contract').fetchall()
            print(dog_all)
            print("Продолжить создание договоров - 1, выбрать договор для активации - 2, выбрать договор для "
                  "завершения - 3, выйти - 4")
            choise = int(input())
            if choise == 1:
                pass
            elif choise == 2:
                choise_dog = input("Выберите название договора для подтверждения: ")
                cursor.execute("SELECT * FROM Contract WHERE статус = ?", ("черновик",))
                act = ""
                for dog in cursor.fetchall():
                    name_dog = (dog[0] + ", ")
                    act += name_dog
                if choise_dog in act:
                    cursor.execute('UPDATE Contract SET статус = ?, дата_подписания = ? WHERE название '
                                   '= ?', ("активен", date, choise_dog))
                    conn.commit()
                    print("Договор активирован!")
                    return Button5.button(self)
                else:
                    print("Договор не в статусе черновик или не существует!")
                    return Button5.button(self)
            elif choise == 3:
                choise_dog = input("Выберите название активного договора для завершения: ")
                cursor.execute('SELECT * FROM Contract WHERE статус = ?',("активен",))
                act = ""
                for dog in cursor.fetchall():
                    name_dog = (dog[0] + ", ")
                    act += name_dog
                if choise_dog in act:
                    cursor.execute('UPDATE Contract SET статус = ? WHERE название = ?', ("завершен", choise_dog))
                    conn.commit()
                    print("Договор завершен!")
                    return Button5.button(self)
                else:
                    print("Этот договор не активен или не существует!")
                    return Button5.button(self)
            else:
                return Button5.button(self)
        elif choise == 3:
            pro_all = cursor.execute('SELECT * FROM Project').fetchall()
            if len(pro_all) == 0:
                print("Нет проектов!")
                return Button5.button(self)
            else:
                print(pro_all)
                return Button5.button(self)
        else:
            return Button5.button(self)

class Button2(System_of_Projects_and_Contracts):
    def button(self):
        dog_all = cursor.execute('SELECT * FROM Contract').fetchall()
        if len(dog_all) == 0:
            print("Нет записей!")
            return Button5.button(self)
        else:
            print(dog_all)
        print("Если вы хотите выбрать договор для активации, введите - 1, выбрать договор для завершения - 2, "
              "просмотреть все проекты - 3, выйти - 4")
        choise = int(input())
        if choise == 1:
            choise_dog = input("Выберите название договора для активации: ")
            cursor.execute("SELECT * FROM Contract WHERE статус = ?", ("черновик",))
            act = ""
            for dog in cursor.fetchall():
                name_dog = (dog[0] + ", ")
                act += name_dog
            if choise_dog in act:
                cursor.execute('UPDATE Contract SET статус = ?, дата_подписания = ? WHERE название '
                               '= ?', ("активен", date, choise_dog))
                conn.commit()
                print("Договор активирован!")
                return Button5.button(self)
            else:
                print("Договор не в статусе черновик или не существует!")
                return Button5.button(self)
        elif choise == 2:
            choise_dog = input("Выберите название активного договора для завершения: ")
            cursor.execute('SELECT * FROM Contract WHERE статус = ?', ("активен",))
            act = ""
            for dog in cursor.fetchall():
                name_dog = (dog[0] + ", ")
                act += name_dog
            if choise_dog in act:
                cursor.execute('UPDATE Contract SET статус = ? WHERE название = ?', ("завершен", choise_dog))
                conn.commit()
                print("Договор завершен!")
                return Button5.button(self)
            else:
                print("Этот договор не активен или не существует!")
                return Button5.button(self)
        elif choise == 3:
            pro_all = cursor.execute('SELECT * FROM Project').fetchall()
            if len(pro_all) == 0:
                print("Нет записей!")
                return Button5.button(self)
            else:
                print(pro_all)
                return Button5.button(self)
        else:
            return Button5.button(self)

class Button3(System_of_Projects_and_Contracts):
    def button(self):
        pro = input("Введите название проекта: ")
        cursor.execute('INSERT INTO Project VALUES(?,?,?)', (pro, date, 'не задан'))
        conn.commit()
        print("Проект успешно создан!")
        print("Для продолжения создания проектов нажмите 1, для просмотра проектов - 2, для просмотра договоров - "
              "3, для добавления договора к проекту - 4, для завершения договора в проекте - 5, для завершения - 6")
        choise = int(input())
        if choise == 1:
            pass
        elif choise == 2:
            print(cursor.execute('SELECT * FROM Project').fetchall())
            print("Продолжить создание проектов - 1, нет - 2")
            choise = int(input())
            if choise == 1:
                pass
            else:
                return Button5.button(self)
        elif choise == 3:
            print(cursor.execute('SELECT * FROM Contract').fetchall())
            return Button5.button(self)
        elif choise == 4:
            choise_pro = input("Введите название проекта: ")
            cursor.execute('SELECT * FROM Project')
            go = ""
            for name in cursor.fetchall():
                name_pro = (name[0] + ", ")
                go += name_pro
            if choise_pro in go:
                pro_url = cursor.execute('SELECT * FROM Project WHERE название = ?', (choise_pro,)).fetchone()
                if pro_url[2] == "не задан":
                    print(f"Хотите добавить к проекту {choise_pro} договор? 1 - да, 2 - нет")
                    choise = int(input())
                    if choise == 1:
                        cursor.execute('SELECT * FROM Contract WHERE статус = ?', ("активен",))
                        if len(cursor.fetchall()) == 0:
                            print("Нет активных договоров, добавьте хотя бы один активный договор!")
                            return Button5.button(self)
                        else:
                            print("Список активных договоров:")
                            print(
                                cursor.execute('SELECT * FROM Contract WHERE статус = ? AND проект = ?', ("активен",
                                                                                                          "не задан"
                                                                                                          )).fetchall())
                            dog = input("Введите название активного договора, который хотите добавить к проекту: ")
                            dog_stat = cursor.execute('SELECT * FROM Contract WHERE название = ?', (dog,)).fetchone()
                            if dog_stat[4] == "не задан":
                                print(f"Хотите внести договор {dog} в проект {choise_pro}? 1 - да, 2 - нет")
                                choise = int(input())
                                if choise == 1:
                                    cursor.execute('UPDATE Contract SET проект = ? WHERE название = ?',
                                                   (choise_pro, dog))
                                    conn.commit()
                                    cursor.execute('UPDATE Project SET ссылка = ? WHERE название = ?',
                                                   (dog, choise_pro))
                                    conn.commit()
                                    print("Договор успешно добавлен в проект")
                                    return Button5.button(self)
                                else:
                                    return Button5.button(self)
                            else:
                                print("Данный договор уже добавлен к проекту!")
                                return Button5.button(self)
                    else:
                        return Button5.button(self)
                else:
                    print("У проекта может быть только один активный договор!")
                    return Button5.button(self)
            else:
                print("Выбранного проекта не существует!")
                return Button5.button(self)
        elif choise == 5:
            choise_pro = input("Введите название проекта: ")
            cursor.execute('SELECT * FROM Project')
            go = ""
            for name in cursor.fetchall():
                name_pro = (name[0] + ", ")
                go += name_pro
            if choise_pro in go:
                pro_act = cursor.execute('SELECT * FROM Contract WHERE проект = ?', (choise_pro,)).fetchone()
                if pro_act[4] == "не задан":
                    print("В данном проекте нет активных договоров!")
                    return Button5.button(self)
                elif pro_act[3] == "активен":
                    print(f"Вы уверены, что хотите завершить договор {pro_act[0]}? 1 - да, 2 - нет")
                    choise = int(input())
                    if choise == 1:
                        cursor.execute('UPDATE Contract SET статус = ? WHERE название = ?', ("завершен", pro_act[0]))
                        conn.commit()
                        print("Договор завершен")
                        return Button5.button(self)
                    else:
                        return Button5.button(self)
                else:
                    print("Договор в проекте уже завершен!")
                    return Button5.button(self)
            else:
                print("Выбранного проекта не существует!")
                return Button5.button(self)
        else:
            return Button5.button(self)

class Button4(System_of_Projects_and_Contracts):
    def button(self):
        pro_all = cursor.execute('SELECT * FROM Project').fetchall()
        if len(pro_all) == 0:
            print("Нет записей!")
            return Button5.button(self)
        else:
            print(pro_all)
            print("Что вы хотите сделать: 1 - Выбрать проект для добавления договора, 2 - Выбрать проект для "
                  "завершения договора, 3 - Просмотреть все договоры, 4 - Выйти")
            choise = int(input())
            if choise == 1:
                choise_pro = input("Введите название проекта: ")
                cursor.execute('SELECT * FROM Project')
                go = ""
                for name in cursor.fetchall():
                    name_pro = (name[0] + ", ")
                    go += name_pro
                if choise_pro in go:
                    pro_url = cursor.execute('SELECT * FROM Project WHERE название = ?', (choise_pro,)).fetchone()
                    if pro_url[2] == "не задан":
                        print(f"Хотите добавить к проекту {choise_pro} договор? 1 - да, 2 - нет")
                        choise = int(input())
                        if choise == 1:
                            cursor.execute('SELECT * FROM Contract WHERE статус = ?', ("активен",))
                            if len(cursor.fetchall()) == 0:
                                print("Нет активных договоров, добавьте хотя бы один активный договор")
                                return Button5.button(self)
                            else:
                                print("Список активных договоров:")
                                print(cursor.execute('SELECT * FROM Contract WHERE статус = ? AND проект = ?', ("активен",
                                          "не задан")).fetchall())
                                dog = input("Введите название активного договора, который хотите добавить к проекту: ")
                                dog_stat = cursor.execute('SELECT * FROM Contract WHERE название = ?',
                                                          (dog,)).fetchone()
                                if dog_stat[4] == "не задан":
                                    print(f"Хотите внести договор {dog} в проект {choise_pro}? 1 - да, 2 - нет")
                                    choise = int(input())
                                    if choise == 1:
                                        cursor.execute('UPDATE Contract SET проект = ? WHERE название = ?',
                                                       (choise_pro, dog))
                                        conn.commit()
                                        cursor.execute('UPDATE Project SET ссылка = ? WHERE название = ?',
                                                       (dog, choise_pro))
                                        conn.commit()
                                        print("Договор успешно добавлен в проект")
                                        return Button5.button(self)
                                    else:
                                        return Button5.button(self)
                                else:
                                    print("Данный договор уже добавлен к проекту!")
                                    return Button5.button(self)
                        else:
                            return Button5.button(self)
                    else:
                        print("У проекта может быть только один договор")
                        return Button5.button(self)
                else:
                    print("Выбранного проекта не существует!")
                    return Button5.button(self)
            elif choise == 2:
                choise_pro = input("Введите название проекта: ")
                cursor.execute('SELECT * FROM Project')
                go = ""
                for name in cursor.fetchall():
                    name_pro = (name[0] + ", ")
                    go += name_pro
                if choise_pro in go:
                    pro_act = cursor.execute('SELECT * FROM Contract WHERE проект = ?', (choise_pro,)).fetchone()
                    if pro_act[4] == "не задан":
                        print("В данном проекте нет активных договоров!")
                        return Button5.button(self)
                    elif pro_act[3] == "активен":
                        print(f"Вы уверены, что хотите завершить договор {pro_act[0]}? 1 - да, 2 - нет")
                        choise = int(input())
                        if choise == 1:
                            cursor.execute('UPDATE Contract SET статус = ? WHERE название = ?',
                                           ("завершен", pro_act[0]))
                            conn.commit()
                            print("Договор завершен")
                            return Button5.button(self)
                        else:
                            return Button5.button(self)
                    else:
                        print("Договор в проекте уже завершен!")
                        return Button5.button(self)
                else:
                    print("Выбранного проекта не существует!")
                    return Button5.button(self)
            elif choise == 3:
                dog_all = cursor.execute('SELECT * FROM Contract').fetchall()
                if len(dog_all) == 0:
                    print("Нет записей!")
                    return Button5.button(self)
                else:
                    print(dog_all)
                    return Button5.button(self)
            else:
                return Button5.button(self)

class Button5(System_of_Projects_and_Contracts):
    def button(self):
        print(
            "Введите 1 - созданить договор, 2 - просмотреть все договоры, 3 - создать проект, 4 - просмотреть все проекты, "
            "5 - завершить работу программы")
        a = int(input())
        if a == 1:
            return Button1.button(self)
        elif a == 2:
            return Button2.button(self)
        elif a == 3:
            return Button3.button(self)
        elif a == 4:
            return Button4.button(self)
        elif a == 5:
            print ("Спасибо за работу с программой!")
            conn.close()
        else:
            print("Вы ввели неправильное число, работа с программой завершена")
            return


a = System_of_Projects_and_Contracts()
a.__init__()
a.main_menu()