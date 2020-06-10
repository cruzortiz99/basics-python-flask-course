from json import load, dump


def get_higher_id(items):
    '''
    Get an id higher than the one in the list

    :param items: list of dictionaries with id
    '''
    items_sorted_by_id = sorted(
        items,
        key=lambda item: item['id'],
        reverse=True)
    return items_sorted_by_id[0]['id'] + \
        1 if len(items_sorted_by_id) > 0 else 0


def get_higher_id_from_db(db_path):
    '''
    Get an id higher than the one in the db json

    :param db_path: route of the data base
    '''
    file = open(db_path)
    db_items = load(file)
    file.close()
    return get_higher_id(db_items)


def get_db_rows(db_path):
    '''
    Wrapper that get all the registers on the data base

    :param db_path: route of the data base
    '''
    file = open(db_path)
    db_rows = load(file)
    file.close()
    return lambda: db_rows


def save_into_db(db_path):
    '''
    Wrapper of a function to save a data into a data base
    '''
    return lambda data: dump(data, open(db_path, mode='w'))
