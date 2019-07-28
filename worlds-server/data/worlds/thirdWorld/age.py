from .slugged import Slugged


class Age(Slugged):
    def __init__(
        self,
        slug,
        name,
    ):
        super().__init__(slug)
        self.name = name

    @classmethod
    def get_items(cls):
        return AGES


class Date:
    def __init__(
        self,
        age=None,
        year=None,
        month=None,
        day=None,
    ):
        self.__age = age
        self.year = year
        self.month = month
        self.day = day

    @property
    def age(self):
        return Age.find(self.__age)


AGES = [
    Age(
        # 1
        slug='first-age',
        name="Третья Эпоха",
    ),
    Age(
        # 2
        slug='second-age',
        name="Третья Эпоха",
    ),
    Age(
        # 3
        slug='gondor-age',
        name="Гондорийская Эра",
    ),
    Age(
        # 4
        slug='fourth-age',
        name="Четвертая Эпоха",
    ),
]