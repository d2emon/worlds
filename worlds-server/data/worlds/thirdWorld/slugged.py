class Slugged:
    def __init__(self, slug):
        self.slug = slug

    @classmethod
    def get_items(cls):
        raise NotImplementedError()

    @classmethod
    def find(cls, slug):
        return next((item for item in cls.get_items() if item.slug == slug), None)
