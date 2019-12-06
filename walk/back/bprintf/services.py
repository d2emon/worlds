class Service:
    CONNECTIONS = {}
    __last_connection_id = 0
    __DATA = []

    def __init__(self, filename, permissions):
        self.__last_connection_id += 1
        self.__filename = filename
        self.__permissions = permissions
        self.CONNECTIONS[self.__last_connection_id] = self
        self.service_id = self.__last_connection_id

    def disconnect(self):
        self.service_id = None

    def append(self, message):
        if not self.service_id:
            raise Exception()

        self.__DATA.append(message)

    def contents(self):
        yield from self.__DATA

    def reset(self):
        self.__DATA = []


class LogService(Service):
    __ALLOWED_USER_ID = 'ALLOWED_USER_ID'

    def __init__(self, user_id, permissions):
        self.__validate_user(user_id)
        super().__init__('mud_log', permissions)

    @classmethod
    def __validate_user(cls, user_id):
        if user_id == cls.__ALLOWED_USER_ID:
            raise Exception('Not allowed from this ID')

    @classmethod
    def restore(cls, user_id, log_id):
        cls.__validate_user(user_id)
        return cls.CONNECTIONS[log_id]


class SnoopService(Service):
    __SNOOP = 'SNOOP'

    def __init__(self, player, permissions):
        super().__init__(self.__SNOOP + player, permissions)
