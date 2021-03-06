import json
import os
from ..wikifiles import WikiFile


class WikiPage:
    def __init__(
        self,
        title,
        order=None,
        url=None,
        path=None,
    ):
        self.__fields = {'title': title}
        if order is not None:
            self.__fields['order'] = order
        if url is not None:
            self.__fields['url'] = url
        self.__path = path

    @classmethod
    def from_file(cls, file):
        return cls(**file.as_dict())

    @property
    def title(self):
        return self.__fields['title']

    @property
    def url(self):
        return self.__fields.get('url', self.title)

    def update(self, fields):
        self.__fields.update(fields)

    def as_dict(self):
        return {
            **self.__fields,
            'url': self.url,
        }


class Field:
    def __init__(
        self,
        name,
        export_name=None,
        is_main=False,
    ):
        self.name = name
        self.export_name = export_name or name
        self.is_main = is_main


class Planet:
    __fields = [
        Field('id'),
        Field('about'),
        Field('description', is_main=True),
        Field('radius'),
        Field('magnet'),
        Field('name', is_main=True),
        Field('planetMap', export_name='map'),
        Field('surface'),
        Field('slug', is_main=True),
    ]

    def __init__(
        self,
        **data,
    ):
        self.__id = data.get('id')
        """
        The planet ${1:Qo'noS}${2:, named so by its discoverer}, is a ${3:desert planet} in a ${4:small solar system
        with }${5: ten} other planets.

        ${1:Qo'noS} is about ${6:15.9} times bigger than Earth and its gravity is about ${7:5.04} times that of Earth.

        
        A single day lasts ${8:47.21} hours and a year lasts ${9:487} days. The planet is made up of ${10:13}
        continents, which make up ${11:46}% of the planet's landmass.

        ${12:1} moon(s) orbit the planet and ${1:Qo'noS} itself orbits a${13: white} sun in an ${14:elliptic orbit}.

        
        The plant-like organisms on this planet are ${21:almost entirely made up of grasses and bushes, both of which
        work together to reach the nutrients they need. Their intertwined growth leads to spectacular shapes and
        colors, but they leave almost no nutrients for other species. So only small flowers and some fungi manage to
        live of what's left. Trees and shrubs are non-existent.}

        
        ${22:Most plant-like organisms tend to grow in one place or at least float around in water, but a small amount
        of species on this planet isn't content with this, mainly due to the risk of a lack of nutrients in the soil
        around it. So instead these species try to attach themselves to small animals. Their survival has a better
        chance if they manage to intertwine with a furry animal for more grasp. After they've attached themselves to an
        animal, it will use dirt, dead skin and anything else that may fall on the animal's skin as nutrients, but some
        may even pierce the skin to take nutrients from the animal's blood.}

        
        ${22:The aquatic organisms aren't very large in numbers, but they are huge in size. They can grow to sizes of
        nearly 100 meters (328ft) and a diameter of up to 5 meters (16ft). These underwater giants give this aquatic
        world an eerie atmosphere as you never know what could lurk behind that pillar. But at the same time, they
        provide homes to thousands of species on all depths, which makes studying even 1 giant coral an absolute
        delight.}

        
        ${23:Evil alien species who wish to destroy the universe are a common theme in sci-fi movies. However, it turns
        out it's not that far from reality. The species on this planet are what we'd consider truly evil. Their
        superior technology has been the end of many species, both on their own planet and others. Having virtually
        destroyed most life their own planet, these hostile creatures now search the universe for resources they can
        use on their home-planet. No other species has had the capabilities to stand in their way, yet.}
        """
        # ${1}${2}${3}${4}${5}
        # ${1}${2}${3}${6}
        # ${1}${4}${5}
        # ${3b}${2.0}${1}${2.1}${5}
        # ${3b}${6} ${7.0}${7.1}${7.2}${7.3}
        self.fields = data
        # self.about = data.get('about', [])
        # self.description = data.get('description')
        # self.name = data.get('name')
        # self.planet_map = data.get('planetMap')
        # self.slug = data.get('slug')
        # self.surface = data.get('surface')

        # self.data = {k: v for k, v in data.items()}

    # @property
    # def fields(self):
    #     # result = self.serialize()
    #     # result.update(self.data)
    #     # return result
    #     return {
    #         'about': self.about,
    #         'description': self.description,
    #         'name': self.name,
    #         'planetMap': self.planet_map,
    #         'surface': self.surface,
    #         'slug': self.slug,
    #         **self.data,
    #     }

    @property
    def slug(self):
        return self.fields.get('slug')

    @classmethod
    def __about(
        cls,
        files=(),
        pages=(),
        sorted_pages=()
    ):
        pages = [WikiPage(page) for page in pages]
        file_pages = [WikiPage.from_file(file) for file in files]
        new_pages = [
            WikiPage(title, order=order)
            for (order, title) in enumerate(sorted_pages)
        ] + file_pages
        # Add files
        for new_page in new_pages:
            page = next((page for page in pages if page.title == new_page.title), None)
            if page is None:
                pages.append(new_page)
            else:
                page.update(new_page.as_dict())
        return sorted(
            (page.as_dict() for page in pages),
            key=lambda p: p.get('order', len(pages)),
        )

    @classmethod
    def __planet_map(cls, root, wiki_path):
        root = os.path.join(root, 'map')
        planet_map = {
            # 'title': '',
            'wiki': [],
        }
        # From JSON
        filename = os.path.join(root, 'map.json')
        if os.path.isfile(filename):
            with open(filename, "r", encoding='utf-8') as f:
                data = json.load(f)
                planet_map.update({
                    **data,
                    'wiki': [
                        WikiPage(title, order=order).as_dict()
                        for (order, title) in enumerate(data.get('wiki'))
                    ]
                })
        # From files
        for file in WikiFile.pages("{}/{}".format(wiki_path, 'map')):
            if any(page for page in planet_map['wiki'] if page.get('title') == file.title):
                continue
            planet_map['wiki'].append(WikiPage.from_file(file).as_dict())
        return planet_map

    @classmethod
    def load(cls, path, world, slug):
        root = os.path.join(path, slug)
        wiki_path = "{}/{}".format(world, slug)
        filename = os.path.join(root, 'planet.json')
        if not os.path.isdir(root) or not os.path.isfile(filename):
            return cls()
        with open(filename, "r", encoding='utf-8') as f:
            data = json.load(f)

            # files = os.listdir(root)
            fields = [
                'description',
                'magnet',
                'surface',
            ]
            return cls(**{
                **{field: data.get(field) for field in fields},
                'about': cls.__about(
                    files=WikiFile.pages(wiki_path),
                    pages=data.get('about', []),
                    sorted_pages=data.get('sortPages', []),
                ),
                'name': data.get('name', slug),
                'planetMap': cls.__planet_map(
                    root=os.path.join(root),
                    wiki_path=wiki_path,
                ),
                'slug': slug,
            })

    def as_dict(self, full=False):
        if full:
            fields = self.__fields
        else:
            fields = [field for field in self.__fields if field.is_main]
        return {field.export_name: self.fields.get(field.name) for field in fields}
