from json import load, dump


def get_higher_id(items):
    items_sorted_by_id = sorted(
        items,
        key=lambda item: item['id'],
        reverse=True)
    return items_sorted_by_id[0]['id'] + \
        1 if len(items_sorted_by_id) > 0 else 0


def get_higher_id_from_db(db_path):
    file = open(db_path)
    db_items = load(file)
    file.close()
    return get_higher_id(db_items)


def get_db_rows(db_path):
    file = open(db_path)
    db_rows = load(file)
    file.close()
    return lambda: db_rows


def save_into_db(db_path):
    return lambda data: dump(data, open(db_path, mode='w'))
