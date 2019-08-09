from ..database import Database


class Messages(Database):
    def __init__(self):
        self.value0 = 1
        self.value1 = 1
        self.__last_message_id = 0

    @property
    def last_message_id(self):
        return self.__last_message_id

    def all(self):
        yield from []

    def get(self, item_id):
        return lambda: None

    def reset(self):
        self.value0 = 1
        self.value1 = 1
