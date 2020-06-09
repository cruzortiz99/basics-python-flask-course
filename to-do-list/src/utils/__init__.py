from json import load, dump


def get_higher_id(db_path):
    file = open(db_path)
    db_items = load(file)
    file.close()
    db_items_sorted_by_id = sorted(
        db_items,
        lambda db_item: db_item['id'],
        reverse=True)
    return db_items_sorted_by_id[0]['id'] + \
        1 if len(db_items_sorted_by_id) > 0 else 0


def get_db_rows(db_path):
    print(db_path)
    file = open(db_path)
    print(len([line for line in file]))
    db_rows = load(file)
    file.close()
    def wrapped_function(): return db_rows
    return wrapped_function


def save_into_db(db_path):
    def wrapped_function(data): return dump(data, open(db_path, mode='w'))
    return wrapped_function
