import os
from app import app
from ..wikifiles import wikis, WikiFile
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
        serialize_name=None,
    ):
        self.name = name
        self.default = default
        self.is_hidden = is_hidden
        self.is_main = is_main
        self.normalize = normalize
        self.serialize = serialize
        self.serialize_name = serialize_name or name

    def get(self, fields):
        return self.normalize(fields.get(self.name, self.default))


class World:
    __fields = {
        'id': Field('id', is_main=True),
        'author': Field('author'),
        'books': Field('books'),
        'book_pages': Field('book_pages', serialize_name='bookPages'),
        'created_at': Field('created_at', serialize_name='createdAt'),
        'data_loader': Field(
            'data_loader',
            is_hidden=True,
            default=lambda: {},
        ),
        'image': Field('image'),
        'image_url': Field(
            'image_url',
            default="portal.jpg",
            is_main=True,
            normalize=lambda item: item and '{}/wiki/{}'.format(app.config.get('MEDIA_URL'), item),
            serialize_name='imageUrl',
        ),
        'index_page': Field('index_page', serialize_name='indexPage'),
        'isbn': Field('isbn'),
        'language': Field('language'),
        # '__links',
        'loader': Field('loader', is_hidden=True),
        'media': Field('media'),
        'order': Field('order', is_main=True),
        'origin': Field('origin'),
        'pages': Field(
            'pages',
            default={},
            is_hidden=True,
            normalize=lambda item: item or {},
        ),
        'planets': Field(
            'planets',
            default=[],
            is_hidden=True,
            normalize=lambda item: (Planet(**data) for data in item),
            serialize=lambda item: [planet.fields for planet in item],
        ),
        'publisher': Field('publisher'),
        'series': Field('series'),
        'slug': Field('slug', default='', is_main=True),
        'text': Field('text', is_hidden=True),
        'title': Field('title', default='', is_main=True),
        'wiki': Field('wiki', default={}),
    }

    def __init__(self, **data):
        self.fields = {
            **{key: data.get(key, field.default) for key, field in self.__fields.items()},
            **{key: value for key, value in data.items() if key not in self.__fields.keys()}
        }

    @property
    def additional_data(self):
        loader = self.get_field('data_loader')
        return loader and loader()

    @property
    def text(self):
        return self.loader and self.loader()

    # Normalizers
    @property
    def pages(self):
        return sorted(
            [
                {
                    'title': self.get_field('pages').get(file.title, file.title),
                    'url': file.title,
                }
                for file in WikiFile.pages(self.get_field('slug'))
            ],
            key=lambda item: item.get('title', 0),
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

    # Getters
    def get_field(self, field):
        return self.__fields.get(field).get(self.fields)

    def get_planet(self, planet_id):
        return next((planet for planet in self.get_field('planets') if planet.slug == planet_id), None)

    def get_wiki(
        self,
        page_id=None,
        planet_id=None,
        page_type='page',
    ):
        if page_type not in ('page', 'map'):
            return None

        if page_id is None:
            return WikiFile(path=self.get_field('index_page')).get_wiki()

        path = self.get_field('slug')
        if planet_id is not None:
            path = os.path.join(path, 'planets', planet_id)
        if page_type == 'map':
            path = os.path.join(path, 'map')
        path = os.path.join(path, "{}.md".format(page_id))
        return WikiFile(path=path).get_wiki()

    # Dictionary
    def as_dict(self, full=False):
        fields = (field for field in self.__fields.values() if not field.is_hidden)
        if not full:
            fields = (field for field in fields if field.is_main)
            additional_fields = {}
        else:
            additional_fields = {
                'pages': self.pages,
                'planets': [planet.as_dict() for planet in self.get_field('planets')],
                'text': self.text,

                'data': self.additional_data,
            }

        return {
            **{field.serialize_name: field.get(self.fields) for field in fields},
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
