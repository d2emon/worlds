import os
from app import app
from ..wikifiles import get_wiki, list_wiki, wikis
from .planet import Planet


class Field:
    def __init__(
        self,
        name,
        default=None,
        is_hidden=False,
        is_main=False,
        normalize=lambda item: item,
        serialize=lambda item: item,
    ):
        self.name = name
        self.default = default
        self.is_hidden = is_hidden
        self.is_main = is_main
        self.normalize = normalize
        self.serialize = serialize

    def get(self, fields):
        return self.normalize(fields.get(self.name, self.default))


class World:
    __fields = {
        'id': Field('id', is_main=True),
        'author': Field('author'),
        'book_pages': Field('book_pages'),
        'created_at': Field('created_at'),
        'data_loader': Field(
            'data_loader',
            is_hidden=True,
            default=lambda: {},
        ),
        'image': Field(
            'image',
            default="portal.jpg",
            is_hidden=True,
            normalize=lambda item: item and '{}/wiki/{}'.format(app.config.get('MEDIA_URL'), item)
        ),
        'index_page': Field('index_page'),
        'isbn': Field('isbn'),
        'language': Field('language'),
        # '__links',
        'loader': Field('loader', is_hidden=True),
        'media': Field('media'),
        'order': Field('order', is_main=True),
        'origin': Field('origin'),
        'pages': Field('pages', default={}, is_hidden=True),
        'planets': Field(
            'planets',
            default=[],
            is_hidden=True,
            normalize=lambda item: (Planet(**data) for data in item),
            serialize=lambda item: [planet.fields for planet in item],
        ),
        'publisher': Field('publisher'),
        'series': Field('series'),
        'slug': Field('slug', is_main=True),
        'text': Field('text', is_hidden=True),
        'title': Field('title', default='', is_main=True),
        'wiki': Field('wiki', default={}),
    }

    def __init__(self, **data):
        # self.id = id
        # self.__data = {key: data.get(key, field.default) for key, field in self.__fields.items()}
        # self.data = {k: v for k, v in data.items() if k not in self.__fields.keys()}
        self.fields = {
            **{key: data.get(key, field.default) for key, field in self.__fields.items()},
            **{key: value for key, value in data.items() if key not in self.__fields.keys()}
        }
        # self.author = author
        # self.created_at = created_at
        # self.__data_loader = data_loader
        # self.__image = image
        # self.index_page = index_page
        # self.__loader = loader
        # self.media = media
        # self.order = order
        # self.origin = origin
        # self.__pages = pages or {}
        # self.__planets = list(planets or [])
        # self.slug = slug
        # self.__text = text
        # self.title = title
        # self.wiki = wiki or {}
        # self.data = data

    @property
    def additional_data(self):
        loader = self.get_field('data_loader')
        return loader and loader()

    # @property
    # def fields(self):
    #     return {
    #         # 'author': self.author,
    #         # 'created_at': self.created_at,
    #         # 'data_loader': self.__data_loader,
    #         # 'image': self.__image,
    #         # 'index_page': self.index_page,
    #         # 'loader': self.__loader,
    #         # 'media': self.media,
    #         # 'order': self.order,
    #         # 'origin': self.origin,
    #         # 'pages': self.__pages,
    #         # 'slug': self.slug,
    #         # 'title': self.title,
    #         # 'text': self.__text,
    #         # 'wiki': self.wiki,
    #         **self.data,
    #         **{field.name: field.get(self.__data) for field in self.__fields},
    #     }

    @property
    def text(self):
        return self.loader and self.loader()

    # Normalizers
    @property
    def pages(self):
        return sorted(
            [
                {
                    'filename': self.get_field('pages').get(file, file),
                    'url': file,
                }
                for file in list_wiki(self.get_field('slug'))
            ],
            key=lambda item: item.get('filename', 0),
        )

    # Loaders
    @property
    def __text_loader(self):
        return lambda: self.get_field('text')

    @property
    def wiki_loader(self):
        return lambda: self.get_wiki()

    @property
    def loader(self):
        loader = self.get_field('loader')
        if loader is not None:
            return loader

        if self.get_field('index_page') is not None:
            return self.wiki_loader
        return self.__text_loader
        # return lambda: self.__fields.get('text')

    # Getters
    def get_field(self, field):
        return self.__fields.get(field).get(self.fields)

    def get_planet(self, planet_id):
        return next((planet for planet in self.get_field('planets') if planet.slug == planet_id), None)

    def get_wiki(
        self,
        page_id=None,
        planet_id=None
    ):
        if page_id is None:
            return get_wiki(self.get_field('index_page'))

        path = self.get_field('slug')
        if planet_id is not None:
            path = os.path.join(path, 'planets', planet_id)
        path = os.path.join(path, "{}.md".format(page_id))
        return get_wiki(path)

    # Dictionary
    def as_dict(self, full=False):
        # result = {
        #     **{field.name: field.get(self.__data) for field in self.__fields if field.is_main},
        #     # 'id': self.id,
        #     # 'image': self.image,
        # }
        fields = (field for field in self.__fields.values() if not field.is_hidden)
        if not full:
            fields = (field for field in fields if field.is_main)
            additional_fields = {}
        else:
            additional_fields = {
                # 'bookPages': self.__fields.get('book_pages'),
                # 'createdAt': self.__fields.get('created_at'),
                'pages': self.pages,
                'planets': [planet.as_dict() for planet in self.get_field('planets')],
                'text': self.text,

                'data': self.additional_data,
            }

        return {
            **{field.name: field.get(self.fields) for field in fields},
            **additional_fields,
        }


class SluggedWorld(World):
    def __init__(
        self,
        slug,
        title,
        image=None,
        wiki=None,

        wikipedia=True,
        lurkmore=True,
        posmotreli=True,
        links=None,

        **data,
    ):
        if wiki is None:
            links = links or {}
            wiki = wikis(
                title,
                wikipedia=wikipedia,
                lurkmore=lurkmore,
                posmotreli=posmotreli,
                **links,
            )

        data.update({
            'title': title,
            'image': image and "{}/{}".format(slug, image),
            'slug': slug,
            'index_page': "{}/index.md".format(slug),
            'wiki': wiki,
        })
        super().__init__(**data)
