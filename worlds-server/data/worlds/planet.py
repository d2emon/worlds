import json
import os


class Planet:
    def __init__(
        self,
        id=None,
        about=None,
        description=None,
        name=None,
        slug=None,
        **data,
    ):
        self.__id = id
        self.about = about or []
        self.description = description
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
        self.name = name
        # ${1}${2}${3}${4}${5}
        # ${1}${2}${3}${6}
        # ${1}${4}${5}
        # ${3b}${2.0}${1}${2.1}${5}
        # ${3b}${6} ${7.0}${7.1}${7.2}${7.3}
        self.slug = slug

        self.data = data

    @property
    def fields(self):
        result = self.as_dict()
        result.update(self.data)
        return result

    @classmethod
    def load(cls, path, slug):
        root = os.path.join(path, slug)
        filename = os.path.join(root, 'planet.json')
        if not os.path.isfile(filename):
            return cls()
        with open(filename, "r", encoding='utf-8') as f:
            data = json.load(f)

            sort_pages = data.get('sortPages', [])
            pages = {
                title: {
                    'order': order,
                    'title': title,
                }
                for (order, title) in enumerate(sort_pages)
            }
            unsorted = data.get('about', []) + [
                {
                    'title': os.path.splitext(os.path.basename(file))[0],
                }
                for file in os.listdir(root)
                if file.endswith('.md')
            ]
            for page in unsorted:
                title = page.get('title') or page.get('slug')
                pages[title] = {
                    'order': len(pages),
                    **pages.get(title, {}),
                    **page,
                }

            return cls(
                about=sorted(pages.values(), key=lambda __page: __page.get('order')),
                description=data.get('description'),
                name=data.get('name', slug),
                slug=slug,
            )

    def as_dict(self):
        return {
            'about': self.about,
            'description': self.description,
            'name': self.name,
            'slug': self.slug,
        }
