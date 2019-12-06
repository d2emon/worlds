from back.bprintf import get_messages, post_add_message


class Output:
    __dashes = "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"

    def __init__(self):
        self.__is_clean = True
        self.__is_finished = True
        self.__is_reading = True

        self.__prompt = ""
        self.__keyboard_input = ""

        self.__user_id = None
        self.__name = None

    @property
    def __to_reprint(self):
        return not self.__is_reading and not self.__is_clean

    def send_message(self, message):
        post_add_message(message)

    def read_messages(self):
        result = get_messages(self.__is_finished, self.__user_id, self.__name)
        self.__is_clean = len(result['messages']) > 0
        for message in result['messages']:
            print(message)

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

        self.send_message(self.__prompt)
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
