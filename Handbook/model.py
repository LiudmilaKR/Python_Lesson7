import controller

db_list = []

def read_db(path: str) -> list:
    global db_list
    with open(path, 'r', encoding='UTF-8') as file:
        my_list = file.readlines()
        for line in my_list:
            id_dict = dict()
            line = line.strip().split(';')
            id_dict['lastname'] = line[0]
            id_dict['firstname'] = line[1]
            id_dict['phone'] = line[2]
            id_dict['comment'] = line[3]
            set_db(id_dict)


def get_db():
    global db_list
    return db_list


def set_db(new_data: str):
    global db_list
    db_list.append(new_data)


def write_db(path: str, db: dict) -> list:
    with open(path, 'w', encoding='UTF-8') as file:
        for i in db:
            for v in i.values():
                file.write(v + ';')
            file.write('\n')
            