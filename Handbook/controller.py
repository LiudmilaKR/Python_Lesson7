import view
import model

def start():
    while True:
        user_inp = view.main_menu()
        input_handler(user_inp)


def input_handler(inp: int):
    match inp:
        case 1: # Показать все контакты
            if view.db_success(model.get_db()):
                view.show_all(model.get_db())
            else:
                model.read_db('Handbook\database.txt')
                view.show_all(model.get_db())
        case 2: # Создать контакт
            if view.db_success(model.get_db()):
                model.set_db(view.create_contact())
                model.write_db('Handbook\database.txt', model.get_db())
            else:
                model.read_db('Handbook\database.txt')
                model.set_db(view.create_contact())
                model.write_db('Handbook\database.txt', model.get_db())
        case 3: # Изменить контакт
            if view.db_success(model.get_db()):
                model.write_db('Handbook\database.txt', view.change_contact(model.get_db()))
            else:
                model.read_db('Handbook\database.txt')
                model.write_db('Handbook\database.txt', view.change_contact(model.get_db()))
        case 4: # Удалить контакт
            if view.db_success(model.get_db()):
                model.write_db('Handbook\database.txt', view.del_contact(model.get_db()))
            else:
                model.read_db('Handbook\database.txt')
                model.write_db('Handbook\database.txt', view.del_contact(model.get_db()))
        case 5: # Выход
            view.exit_program()
