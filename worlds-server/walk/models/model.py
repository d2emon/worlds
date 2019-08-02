from ..database import connect


class Model:
    database_name = "DATABASE"

    def __init__(self, **kwargs):
        pass

    @classmethod
    def database(cls):
        return connect(cls.database_name)

    @classmethod
    def all(cls):
        # print(cls)
        # print(cls.database_name)
        # print(cls.database())
        return (cls(**data) for data in cls.database().all() if data is not None)

    @classmethod
    def get(cls, item_id):
        data = cls.database().get(item_id)()
        return cls(**data) if data is not None else None
