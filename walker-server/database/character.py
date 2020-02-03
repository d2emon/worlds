class Character:
    __items = [{} for _ in range(16)]

    @classmethod
    def find(cls, name):
        return (character for character in cls.__items if character.get('name') == name)
