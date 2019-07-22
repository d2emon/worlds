from app import app
from ..wikifiles import get_wiki, list_wiki, wikis


class World:
    def __init__(
        self,
        id=None,
        image='portal.jpg',
        loader=None,
        pages=None,
        slug=None,
        title='',
        text=None,
        index_page=None,
        wiki=None,
        **data,
    ):
        self.__id = id
        self.__image = image
        self.__loader = loader
        self.__pages = pages or {}
        self.slug = slug
        self.title = title
        self.__text = text
        self.index_page = index_page
        self.wiki = wiki or {}

        self.data = data

    def wiki_loader(self):
        return self.get_wiki()

    def __text_loader(self):
        return self.__text

    @property
    def fields(self):
        result = {
            'image': self.__image,
            'loader': self.__loader,
            'pages': self.__pages,
            'slug': self.slug,
            'title': self.title,
            'text': self.__text,
            'index_page': self.index_page,
            'wiki': self.wiki,
        }
        result.update(self.data)
        return result

    @property
    def image(self):
        return '{}/worlds/{}'.format(app.config.get('RESIZE_URL'), self.__image)

    @property
    def loader(self):
        if self.__loader is not None:
            return self.__loader
        if self.index_page is not None:
            return self.wiki_loader
        return self.__text_loader

    @property
    def text(self):
        return self.loader and self.loader()

    @property
    def pages(self):
        return [{
            'filename': self.__pages.get(file) or file,
            'url': "{}/{}".format(self.slug, file),
        } for file in list_wiki(self.slug)]

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
