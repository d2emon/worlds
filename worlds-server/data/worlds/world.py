from app import app
from ..wikifiles import get_wiki, list_wiki, wikis


class World:
    def __init__(
        self,
        id=None,
        data_loader=None,
        image='portal.jpg',
        index_page=None,
        loader=None,
        pages=None,
        slug=None,
        text=None,
        title='',
        wiki=None,
        **data,
    ):
        self.__id = id
        self.__data_loader = data_loader
        self.__image = image
        self.index_page = index_page
        self.__loader = loader
        self.__pages = pages or {}
        self.slug = slug
        self.__text = text
        self.title = title
        self.wiki = wiki or {}

        self.data = data

    def wiki_loader(self):
        return self.get_wiki()

    def __text_loader(self):
        return self.__text

    @property
    def fields(self):
        result = {
            'data_loader': self.__data_loader,
            'image': self.__image,
            'index_page': self.index_page,
            'loader': self.__loader,
            'pages': self.__pages,
            'slug': self.slug,
            'title': self.title,
            'text': self.__text,
            'wiki': self.wiki,
        }
        result.update(self.data)
        return result

    @property
    def image(self):
        return '{}/wiki/{}'.format(app.config.get('MEDIA_URL'), self.__image)

    @property
    def loader(self):
        if self.__loader is not None:
            return self.__loader
        if self.index_page is not None:
            return self.wiki_loader
        # return self.__text_loader
        return lambda: self.__text

    @property
    def data_loader(self):
        if self.__data_loader is not None:
            return self.__data_loader
        return lambda: {}

    @property
    def text(self):
        return self.loader and self.loader()

    @property
    def additional_data(self):
        return self.data_loader and self.data_loader()

    @property
    def pages(self):
        return sorted(
            [{
                'filename': self.__pages.get(file) or file,
                'url': "{}/{}".format(self.slug, file),
            } for file in list_wiki(self.slug)],
            key=lambda item: item['filename'],
        )

    def get_wiki(self, filename=None):
        if filename is None:
            filename = self.index_page
        else:
            filename = "{}/{}.md".format(self.slug, filename)
        return get_wiki(filename)

    def as_dict(self, full=False):
        result = {
            'id': self.__id,
            'slug': self.slug,
            'title': self.title,
            'image': self.image,
        }
        if not full:
            return result

        result.update({
            'text': self.text,
            'pages': self.pages,
            'wiki': self.wiki,

            'data': self.additional_data,
        })
        return result


class SluggedWorld(World):
    def __init__(
        self,
        slug,
        title,
        image=None,
        wiki=None,
        **data,
    ):
        if wiki is None:
            wiki = wikis(title)

        data.update({
            'title': title,
            'image': image and "{}/{}".format(slug, image),
            'slug': slug,
            'index_page': "{}/index.md".format(slug),
            'wiki': wiki,
        })
        super().__init__(**data)
