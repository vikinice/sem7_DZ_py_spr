import view as v
import model as m

def menu():
    choice = input('Выберите пункт Меню: ')
    if choice == '1':
        m.export()
        v.select_menu()
    elif choice == '2':
        m.import_cont()
        v.select_menu()
    elif choice == '3':
        m.search_cont()
        v.select_menu()
    elif choice == '4':
        exit
    else:
        print('\n Невверный ввод !!!\n')
        v.select_menu()