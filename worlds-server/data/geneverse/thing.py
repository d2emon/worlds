import random


class ChildrenGenerator:
    def __init__(self, slug="", count=None, percent=100):
        if count is None:
            count = ()

        self.slug = slug
        self.count = count
        self.percent = percent

    def as_array(self):
        return self.slug, self.count, self.percent

    def chance(self):
        if self.percent >= 100:
            return True
        else:
            return random.uniform(0, 100) < self.percent

    def __iter__(self):
        return self

    def __next__(self):
        from . import GENEVERSE

        if len(self.slug) > 0 and self.slug[0] == ".":
            data = GENEVERSE.by_slug(self.slug[1:])
            if data is None:
                return []
            return Thing(**data).children()

        if len(self.count) != 2:
            count = 1
        else:
            count = random.randint(*self.count)

        return [self.slug for _ in range(count) if self.chance()]


class Thing:
    def __init__(self, slug, children=(), name_generator=None, id=None):
        self.__id = id
        self.slug = slug
        self.children_generators = [ChildrenGenerator(*children_group) for children_group in children]
        self.name_generator = name_generator
        self.__name = None

    @property
    def name(self):
        if self.__name is None:
            if self.name_generator is None:
                self.__name = self.slug
            else:
                self.__name = next(self.name_generator)
        return self.__name

    @property
    def fields(self):
        return {
            'slug': self.slug,
            'children': [children.as_array() for children in self.children_generators],
            'name_generator': self.name_generator,
        }

    def children(self):
        for children_generator in self.children_generators:
            yield from next(children_generator)

    def as_dict(self):
        return {
            'id': self.__id,
            'slug': self.slug,
            'name': self.name,
            'children': list(self.children())
        }
