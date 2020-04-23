class Model:
    def __init__(self, **kwargs):
        pass

    @property
    def id(self):
        raise NotImplementedError()

    @property
    def _item(self):
        raise NotImplementedError()

    def serialize(self):
        raise NotImplementedError()

    @classmethod
    def all(cls):
        return (cls(**item) for item in cls._items())

    @classmethod
    def get(cls, item_id):
        return (item for item in cls.all() if item.id == item_id)

    def save(self):
        if self._item is not None:
            self._item.update(self.serialize())
        else:
            self._items().append(self.serialize())

    def remove(self):
        self._items().remove(self._item)
        return True

    @classmethod
    def _items(cls):
        raise NotImplementedError()
