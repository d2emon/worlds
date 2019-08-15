from .en import generators as generators_en
from .ru import generators as generators_ru


LANGUAGE = 'ru'


class GeneratorItem:
    def __init__(self, generator_id, language, group_id, item_id, text):
        self.generator_id = generator_id
        self.language = language
        self.group_id = group_id
        self.item_id = item_id
        self.text = text

    def __str__(self):
        return self.text

    def serialize(self):
        return {
            'generator_id': self.generator_id,
            'language': self.language,
            'group_id': self.group_id,
            'item_id': self.item_id,
            'text': self.text,
        }

    @classmethod
    def fill(cls, item):
        return cls(**item.serialize())

    @classmethod
    def validate(cls, item, items):
        return item is not None


def __parse_group(generator_id, group_id, group, language="en"):
    return [
        GeneratorItem(
            generator_id,
            language,
            group_id,
            item_id + 1,
            text,
        )
        for item_id, text in enumerate(group)
    ]


def __parse_generator(generator_id, groups, language="en"):
    result = []
    for group_id, group in enumerate(groups):
        result += __parse_group(
            generator_id=generator_id,
            group_id=group_id + 1,
            group=group,
            language=language,
        )
    return result


def __parse_language(generators, language="en"):
    result = []
    for generator_id, groups in generators.items():
        result += __parse_generator(
            generator_id=generator_id,
            language=language,
            groups=groups,
        )
    return result


# Fill DB

if LANGUAGE == 'ru':
    data = __parse_language(generators_ru, "ru")
else:
    data = __parse_language(generators_en)
