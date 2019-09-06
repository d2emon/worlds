import uuid


class Database:
    def __init__(self):
        self.__items = []

    @classmethod
    def sanitize(cls, data):
        # return {
        #     'id': uuid.uuid4().hex,
        #     'title': data.get('title'),
        #     'author': data.get('author'),
        #     'read': data.get('read')
        # }
        item = {
            'id': uuid.uuid4().hex,
        }
        item.update(data)
        return item

    @classmethod
    def item(cls, data=None):
        if data is None:
            return None
        return lambda: cls.sanitize(data)

    @classmethod
    def filters(
        cls,
        item_id=None,
        slug=None,
    ):
        yield lambda item: True
        if item_id is not None:
            yield lambda item: item.get('id') == item_id
        if slug is not None:
            yield lambda item: item.get('slug') == slug

    @property
    def items(self):
        yield from self.__items

    def filter(self, **kwargs):
        return filter(
            lambda item: all(f(item) for f in self.filters(**kwargs)),
            self.items
        )

    def find(self, **kwargs):
        return (self.item(data)() for data in self.filter(**kwargs))

    def by_item_id(self, item_id):
        return next(self.find(item_id=item_id), None)

    def by_slug(self, slug):
        return next(self.find(slug=slug), None)

    def delete(self, item_id):
        item = next(self.filter(item_id=item_id), None)
        if item is None:
            return False

        self.__items.remove(item)
        return True

    def add(self, data):
        self.__items.append(self.sanitize(data))
        return self.__items[-1]

    def edit(self, item_id, data):
        self.delete(item_id)
        return self.add(data)

    def all(self):
        return self.find()


class ListDatabase(Database):
    def __init__(self, items):
        super().__init__()
        map(self.add, items)

    @property
    def items(self):
        return self.all()
