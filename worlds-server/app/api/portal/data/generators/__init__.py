from .realm import realm


class GeneratorItem:
    def __init__(self, generator_id, group_id, item_id, text):
        self.generator_id = generator_id
        self.group_id = group_id + 1
        self.item_id = item_id + 1
        self.text = text

    def __str__(self):
        return self.text

    @classmethod
    def fill(cls, item):
        return cls(item.generator_id, item.group_id, item.item_id, item.text)

    @classmethod
    def validate(cls, item, items):
        return item is not None


def __parse_group(generator_id, group_id, group):
    return [GeneratorItem(generator_id, group_id, item_id, text) for item_id, text in enumerate(group)]


def __parse_generator(generator_id, groups):
    result = []
    for group_id, group in enumerate(groups):
        result += __parse_group(generator_id, group_id, group)
    return result


data = [] \
       + __parse_generator('realm', realm)
