import random


class NameGenerator:
    def __init__(self, *data):
        self.data = data

    def __iter__(self):
        return self

    def __next__(self):
        return "".join([random.choice(part) for part in self.data]).title()


class ThingName(NameGenerator):
    def __next__(self):
        return random.choice(self.data)
