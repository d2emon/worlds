from ..database import World
from .model import Model


class Message(Model):
    def __init__(
        self,
        message_id,
    ):
        super().__init__()
        self.message_id = message_id

    @classmethod
    def database(cls):
        return World.instance.messages

    @classmethod
    def last_message_id(cls):
        return cls.database().last_message_id

    @classmethod
    def read_from(cls, first_message_id):
        last_message_id = Message.last_message_id()
        if first_message_id == -1:
            first_message_id = cls.last_message_id()

        for message_id in range(first_message_id, last_message_id):
            yield readmsg(cls.database(), message_id)


def readmsg(*args):
    # raise NotImplementedError()
    print("readmsg({})".format(args))
    return 0
