from data.worlds import WORLDS, World


class RecordNotFound(Exception):
    pass


class WorldModel:
    @classmethod
    def __all(cls):
        return WORLDS

    @classmethod
    def __get(cls, **data):
        return World(**data)

    @classmethod
    def all(cls):
        return (cls.__get(**data) for data in cls.__all().all())

    @classmethod
    def by_slug(cls, slug):
        data = cls.__all().by_slug(slug)
        if data is None:
            raise RecordNotFound()
        return cls.__get(**data)

    @classmethod
    def planet(cls, world_id, planet_id):
        item = cls.by_slug(world_id).get_planet(planet_id)
        if item is None:
            raise RecordNotFound()
        return item

    @classmethod
    def wiki(cls, world_id=None, planet_id=None, page_id=None, page_type='page'):
        if world_id is None:
            return None
        return cls.by_slug(world_id).get_wiki(
            planet_id=planet_id,
            page_id=page_id,
            page_type=page_type,
        )
