class Database:
    def __init__(self, data):
        self.__data = data

    def all(self):
        return self.__data

    def get(self, item_id):
        return self.__data[item_id]
