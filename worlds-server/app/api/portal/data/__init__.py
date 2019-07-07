from .portal import item_ids, random_items


# Generators
def __get_item(item_id, items, forbidden=()):
    item = random_items(item_id)
    if item is None:
        return None
    elif not item.validate(item, items):
        return None
    elif item in forbidden:
        return None
    else:
        return item


def __next_item(item_id, items, forbidden=()):
    while True:
        item = __get_item(item_id, items, forbidden)
        if item is not None:
            return item


def __get_text(item):
    if item is None:
        return None
    if isinstance(item, list):
        return [str(i) for i in item]
    return str(item)


def generate():
    items = [None]
    for i in item_ids:
        item_id = i + 1
        item = None
        while item is None:
            if item_id in (17, 20):
                item = []
                for _ in range(3):
                    item.append(__next_item(item_id, items, item))
            else:
                item = __next_item(item_id, items)
        items.append(item)

    return [__get_text(item) for item in items]
