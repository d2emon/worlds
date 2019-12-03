def bprintf(message):
    pass


def pbfr():
    return {
        'messages': [],
    }


class Output:
    __dashes = "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"

    def __init__(self):
        self.__is_clean = True
        self.__is_finished = True
        self.__is_reading = True

        self.__prompt = ""
        self.__keyboard_input = ""

    @property
    def __to_reprint(self):
        return not self.__is_reading and not self.__is_clean

    def read_messages(self):
        result = pbfr()
        self.__is_clean = len(result['messages']) > 0

    def error(self, message):
        self.read_messages()
        self.__is_clean = False

        print(self.__dashes)
        print(message)
        print(self.__dashes)
        raise Exception(message)

    @classmethod
    def get_keyboard(cls, max_length):
        return input()[:max_length]

    def get_input(self, prompt, max_length):
        self.__is_reading = False
        self.__prompt = prompt

        bprintf(self.__prompt)
        self.read_messages()
        self.__is_clean = True

        self.__keyboard_input = self.get_keyboard(max_length)
        self.__is_reading = True
        return self.__keyboard_input

    def reprint(self):
        self.__is_finished = False
        self.read_messages()
        if not self.__to_reprint:
            return

        print(self.__prompt + self.__keyboard_input)
        self.__is_clean = False
