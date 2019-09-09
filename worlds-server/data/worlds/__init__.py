import json
import os
from config import Config
from ..wikifiles import wikis
from .database import WorldsDB
from .planet import Planet
from .world import World, SluggedWorld

from .futureMoscow import future_moscow
from .spectre import spectre


class WorldFolder:
    field_names = [
        'author',
        'book_pages',
        'created_at',
        'image',
        'isbn',
        # 'index_page',
        'language',
        '__links',
        'media',
        'order',
        'origin',
        'publisher',
        'series',
        # 'slug',
        'title',
        'wiki',
    ]
    serializable = [
        'author',
        'book_pages',
        'created_at',
        'image',
        'index_page',
        'isbn',
        'language',
        'media',
        'order',
        'origin',
        'publisher',
        'series',
        'slug',
    ]

    def __init__(self, slug):
        self.is_loaded = False
        self.fields = {
            '__links': {},
            'slug': slug,
        }

    @property
    def image(self):
        image = self.fields.get('image')
        return "{}/images/{}".format(self.slug, image) if image else None

    @property
    def images(self):
        return os.path.join(self.root, 'images')

    @property
    def index_page(self):
        return os.path.join(self.slug, self.fields.get('index_page', 'index.md'))

    @property
    def links(self):
        return self.fields.get('__links', {})

    @property
    def planets(self):
        path = os.path.join(self.root, 'planets')
        if not os.path.exists(path):
            return
        for file in os.listdir(path):
            yield Planet.load(path, os.path.splitext(os.path.basename(file))[0])

    @property
    def root(self):
        return os.path.join(Config.WIKI_ROOT, self.slug)

    @property
    def slug(self):
        return self.fields.get('slug')

    @property
    def title(self):
        return self.fields.get('title', self.slug)

    @property
    def wiki(self):
        if self.fields.get('wiki') is None:
            # links = links or {}
            # self.__wiki = wikis(
            #     title,
            #     wikipedia=wikipedia,
            #     lurkmore=lurkmore,
            #     posmotreli=posmotreli,
            #     **links,
            # )
            self.fields['wiki'] = wikis(self.title)
        return self.fields.get('wiki', wikis(self.title))

    @property
    def __world_file(self):
        return os.path.join(self.root, 'world.json')

    def load(self):
        if not os.path.isfile(self.__world_file):
            return
        with open(self.__world_file, "r", encoding='utf-8') as fp:
            data = json.load(fp)
            self.fields.update({k: data.get(k) for k in self.field_names})
            # wikipedia=True,
            # lurkmore=True,
            # posmotreli=True,

    def serialize(self):
        if not self.is_loaded:
            self.load()

        computed = {
            'image': self.image,
            'index_page': self.index_page,
            'planets': [__planet.fields for __planet in self.planets],
            'slug': self.slug,
            'title': self.title,
            'wiki': self.wiki,
        }
        return {
            **{key: self.fields.get(key) for key in self.serializable},
            **computed,
        }


# worlds = [world for world in os.listdir(Config.WIKI_ROOT)]
# worlds = [world for world in worlds if os.path.isdir(os.path.join(Config.WIKI_ROOT, world))]
WORLD_FOLDERS = (
    WorldFolder(slug)
    for slug in os.listdir(Config.WIKI_ROOT)
    if os.path.isdir(os.path.join(Config.WIKI_ROOT, slug))
)
WORLDS_DATA = [
    {
        'title': 'Assassin\'s Creed',
        'image': 'assassins-creed/images/assassins.jpg',
        'slug': 'assassins-creed',
        'index_page': 'assassins-creed/index.md',
    },
    {
        'title': 'Birthright',
        'image': 'birthright/images/br-logos.gif',
        'slug': 'birthright',
        'index_page': 'birthright/index.md',
    },
    {
        'title': 'Blackmoor',
        'image': 'blackmoor/images/Blackmoor_logo.png',
        'slug': 'blackmoor',
        'index_page': 'blackmoor/index.md',
    },
    # {
    #     'title': 'Council of Wyrms',
    #     'image': 'council-of-wyrms/images/Council_of_Wyrms.jpg',
    #     'slug': 'council-of-wyrms',
    #     'index_page': 'council-of-wyrms/index.md',
    # },
    # {
    #     'title': 'Creature Crucible',
    #     'image': 'creature-crucible/images/cc-logos.gif',
    #     'slug': 'creature-crucible',
    #     'index_page': 'creature-crucible/index.md',
    # },
    SluggedWorld(
        title='Cyberpunk20XX',
        slug='cyberpunk-20xx',
    ),
    {
        'title': 'Dangerous Fantasy 2',
        'image': 'dangerous-fantasy-2/images/df2.gif',
        'slug': 'dangerous-fantasy-2',
        'index_page': 'dangerous-fantasy-2/index.md',
    },
    {
        'title': 'Dark Sun',
        'image': 'dark-sun/images/ds-logos.gif',
        'slug': 'dark-sun',
        'index_page': 'dark-sun/index.md',
    },
    # {
    #     'title': 'Dragon Fist',
    #     'image': 'dragon-fist/images/DragonFist.jpg',
    #     'slug': 'dragon-fist',
    #     'index_page': 'dragon-fist/index.md',
    # },
    {
        'title': 'Dragonlance',
        'image': 'dragonlance/images/fa-logos.gif',
        'slug': 'dragonlance',
        'index_page': 'dragonlance/index.md',
    },
    {
        'title': 'Eberron',
        'image': 'eberron/images/eb-logos.gif',
        'slug': 'eberron',
        'index_page': 'eberron/index.md',
    },
    {
        'title': 'Forgotten Realms',
        'image': 'forgotten-realms/images/fr-logos.gif',
        'slug': 'forgotten-realms',
        'index_page': 'forgotten-realms/index.md',
    },
    {
        'title': 'Ghostwalk',
        'image': 'ghostwalk/images/Ghostwalk_coverthumb.jpg',
        'slug': 'ghostwalk',
        'index_page': 'ghostwalk/index.md',
    },
    {
        'title': 'Greyhawk',
        'image': 'greyhawk/images/gh-logos.gif',
        'slug': 'greyhawk',
        'index_page': 'greyhawk/index.md',
    },
    # {
    #     'title': 'Jakandor',
    #     'image': 'jakandor/images/Jakandor.jpg',
    #     'slug': 'jakandor',
    #     'index_page': 'jakandor/index.md',
    # },
    {
        'title': 'Kingdoms of Kalamar',
        'image': 'kingdoms-of-kalamar/images/kk-logos.gif',
        'slug': 'kingdoms-of-kalamar',
        'index_page': 'kingdoms-of-kalamar/index.md',
    },
    {
        'title': 'Lankhmar',
        'image': 'lankhmar/images/lm-logos.gif',
        'slug': 'lankhmar',
        'index_page': 'lankhmar/index.md',
    },
    {
        'title': 'Mahasarpa',
        'image': 'mahasarpa/images/Mahasarpa.jpg',
        'slug': 'mahasarpa',
        'index_page': 'mahasarpa/index.md',
    },
    {
        'title': 'Mortal Kombat',
        'image': 'mortal-kombat/images/MortalKombat.jpg',
        'slug': 'mortal-kombat',
        'index_page': 'mortal-kombat/index.md',
    },
    {
        'title': 'Mystara',
        'image': 'mystara/images/ms-logos.gif',
        'slug': 'mystara',
        'index_page': 'mystara/index.md',
    },
    {
        'title': 'Nentir Vale',
        'image': 'nentir-vale/images/NentirVale.jpg',
        'slug': 'nentir-vale',
        'index_page': 'nentir-vale/index.md',
    },
    {
        'title': 'Odyssey',
        'image': 'odyssey/images/od-logos.gif',
        'slug': 'odyssey',
        'index_page': 'odyssey/index.md',
    },
    {
        'title': 'Oriental Adventures',
        'image': 'oriental-adventures/images/oa-logos.gif',
        'slug': 'oriental-adventures',
        'index_page': 'oriental-adventures/index.md',
    },
    {
        'title': 'Pelinore',
        'image': 'pelinore/images/Pelinore.jpg',
        'slug': 'pelinore',
        'index_page': 'pelinore/index.md',
    },
    {
        'title': 'Planescape',
        'image': 'planescape/images/PlanescapeLogo.jpg',
        'slug': 'planescape',
        'index_page': 'planescape/index.md',
    },
    {
        'title': 'Ravenloft',
        'image': 'ravenloft/images/rv-logos.gif',
        'slug': 'ravenloft',
        'index_page': 'ravenloft/index.md',
    },
    # {
    #     'title': 'S.T.A.L.K.E.R.',
    #     'image': 'stalker/images/Stalker.jpg',
    #     'slug': 'stalker',
    #     'index_page': 'stalker/index.md',
    # },
    {
        'title': 'SCP Foundation',
        'slug': 'scp-foundation',
        'index_page': 'scp-foundation/index.md',
    },
    {
        'title': 'Spelljammer',
        'image': 'spelljammer/images/sj-logos.gif',
        'slug': 'spelljammer',
        'index_page': 'spelljammer/index.md',
    },
    SluggedWorld(
        title='The Elder Scrolls',
        slug='the-elder-scrolls',
    ),
    {
        'title': 'Thunder Rift',
        'image': 'thunder-rift/images/ThunderRift.jpg',
        'slug': 'thunder-rift',
        'index_page': 'thunder-rift/index.md',
    },
    {
        'title': 'Warcraft',
        'image': 'warcraft/images/wc-logos.gif',
        'slug': 'warcraft',
        'index_page': 'warcraft/index.md',
    },
    {
        'title': 'Warhammer 40.000',
        'slug': 'warhammer-40000',
        'index_page': 'warhammer-40000/index.md',
    },
    SluggedWorld(
        title='Warhammer Fantasy Battles',
        slug='warhammer-fantasy',
        image=None,

        links={
            'en': "https://warhammerfantasy.fandom.com/",
            'ru': "https://warhammerfantasy.fandom.com/ru/",
        },

        lurkmore=False,
    ),
    {
        'title': 'Wilderlands of High Fantasy',
        'image': 'wilderlands-of-high-fantasy/images/WilderlandsOfHighFantasy.jpg',
        'slug': 'wilderlands-of-high-fantasy',
        'index_page': 'wilderlands-of-high-fantasy/index.md',
    },
    {
        'title': 'Авенхейм',
        'image': 'avenheim/images/avenheim.jpg',
        'slug': 'avenheim',
        'index_page': 'avenheim/index.md',
    },
    SluggedWorld(
        title='Аллоды',
        slug='allods',
    ),
    {
        'title': 'Амбер',
        'image': 'amber/images/amber.jpg',
        'slug': 'amber',
        'index_page': 'amber/index.md',
    },
    SluggedWorld(
        title='Американские боги',
        slug='american-gods',
        image='images/start-3.jpg',

        lurkmore=False,
    ),
    {
        'title': 'Арда',
        'image': 'arda/images/tolkien.jpg',
        'slug': 'arda',
        'index_page': 'arda/index.md',
    },
    {
        'title': 'Белория',
        'image': 'beloriya/images/beloria.jpg',
        'slug': 'beloriya',
        'index_page': 'beloriya/index.md',
    },
    SluggedWorld(
        title='Ведьмак',
        slug='vedmak',
    ),
    {
        'title': 'Вестерос',
        'index_page': 'vesteros/index.md',
    },
    SluggedWorld(
        title='Вечный Воитель',
        slug='vechnyy-voitel',
        image='images/eternal_warrior.jpg',

        wiki={
            'wikipedia': 'https://ru.wikipedia.org/wiki/%D0%92%D0%B5%D1%87%D0%BD%D1%8B%D0%B9_%D0%92%D0%BE%D0%B8%D1%82%D0%B5%D0%BB%D1%8C',
            'posmotreli': 'https://posmotre.li/Michael_John_Moorcock',
            'tanelorn': 'http://moorcock.narod.ru/',
        },

        pages={
            'elrik': 'Элрик Мелнибонийский Майкла Муркока и его мир',
        },
    ),
    {
        'title': 'Волшебная Страна',
        'image': 'volshebnaya-strana/images/emerald.jpg',
        'slug': 'volshebnaya-strana',
        'index_page': 'volshebnaya-strana/index.md',
    },
    {
        'title': 'Геройский Мир',
        'image': 'geroyskiy-mir/images/HoMM.jpg',
        'slug': 'geroyskiy-mir',
        'index_page': 'geroyskiy-mir/index.md',
    },
    SluggedWorld(
        title='Гиперион',
        slug='giperion',
    ),
    {
        'title': 'Дино',
        'slug': 'dino',
        'index_page': 'dino/index.md',
    },
    {
        'title': 'Звездные Войны',
        'slug': 'star-wars',
        'index_page': 'star-wars/index.md',
    },
    # SluggedWorld(
    #     title='Земноморье',
    #     slug='zemnomorye',
    #     # image='images/Pet9.png',
    # ),
    {
        'title': 'Кинг',
        'slug': 'king',
        'index_page': 'king/index.md',
    },
    {
        'title': 'Конан',
        'image': 'conan/images/cn-logos.gif',
        'slug': 'conan',
        'index_page': 'conan/index.md',
    },
    {
        'title': 'Король и Шут',
        'image': 'korol-i-shut/images/KiSh.jpg',
        'slug': 'korol-i-shut',
        'index_page': 'korol-i-shut/index.md',
    },
    {
        'title': 'Крон',
        'image': 'kron/images/chronos.jpg',
        'slug': 'kron',
        'index_page': 'kron/index.md',
    },
    {
        'title': 'Мир Полудня',
        'image': 'mir-poludnya/images/midday.jpg',
        'slug': 'mir-poludnya',
        'index_page': 'mir-poludnya/index.md',
    },
    {
        'title': 'Мир номер три',
        'image': 'mir-nomer-tri/images/TretiyMir.jpg',
        'slug': 'mir-nomer-tri',
        'index_page': 'mir-nomer-tri/index.md',
    },
    {
        'title': 'Миры Ктулху',
        'slug': 'mir-ktulhu',
        'index_page': 'mir-ktulhu/index.md',
    },
    future_moscow,
    SluggedWorld(
        title='Нарния',
        slug='narniya',
    ),
    SluggedWorld(
        title='Невендаар',
        slug='nevendaar',
    ),
    SluggedWorld(
        title='Плоский мир',
        slug='discworld',
        image='images/discworld-wallpaper-768x480.jpg',

        links={
            'en': "https://discworld.fandom.com/",
            'ru': "https://discworld.fandom.com/ru/",
            'disc': "https://disc.fandom.com/ru/",
        },
    ),
    SluggedWorld(
        title='Путеводитель по коридорам Ада',
        slug='putevoditel-po-koridoram-ada',
        image='images/Hell.jpg',

        wiki={
            'lurkmore': "http://lurkmore.to/Путеводитель по коридорам Ада"
        },
    ),
    SluggedWorld(
        title='Рик и Морти',
        slug='rick-and-morty',
        image='images/LabRick.png',

        links={
            'en': "https://rickandmorty.fandom.com/",
            'ru': "https://rickandmorty.fandom.com/ru/",
        },

        pages={
            'science': '«Рик и Морти» с точки зрения науки',
            'references': 'Obscure Pop Culture References From Rick And Morty, Explained',
            'easter-eggs': '13 Important "Rick And Morty" Easter Eggs That Prove '
                           'It\'s The Smartest Show On Television',
            'universes': 'Вселенные',
        },
    ),

    # spectre,
    # SluggedWorld(
    #     title='Утиные истории',
    #     slug='duck-tales',
    # ),
    # SluggedWorld(
    #     title='Этория',
    #     slug='etoriya',
    # ),

    # SluggedWorld(
    #     title='Юрий Петухов',
    #     slug='yuriy-petuhov',
    #     # image='images/Pet9.png',
    #
    #     wiki={
    #         'lurkmore': "http://lurkmore.to/Юрий_Петухов"
    #     },
    # ),
]
# 'image': '3e-logos.gif',
# 'image': 'hw-logos.gif',
# 'image': 'dd-logos.gif',
# 'image': 'gz-logos.gif',
# 'image': 'cm-logos.gif',
# 'image': 'd20-logos.jpg',
worlds = [world.fields if isinstance(world, World) else world for world in WORLDS_DATA]


def parse_folder(folder):
    def f():
        world = next((world for world in worlds if world.get('slug') == folder.slug), None) or {}
        return {
            **folder.serialize(),
            **world,
        }
    return f


# ITEMS = map(parse_folder, WORLD_FOLDERS)
# for w in WORLD_FOLDERS:
#     world = next((world for world in worlds if world.get('slug') == w.slug), None)
#     if world is None:
#         world = {}
#     serialized = w.serialize()
#     print(serialized)
#     serialized.update(world)
#     ITEMS.append(serialized)

# WORLDS = WorldsDB([world.fields if isinstance(world, World) else world for world in WORLDS_DATA])


def folder_loader():
    for slug in os.listdir(Config.WIKI_ROOT):
        if not os.path.isdir(os.path.join(Config.WIKI_ROOT, slug)):
            continue
        yield parse_folder(WorldFolder(slug))


WORLDS = WorldsDB(
    # items=[item() for item in ITEMS],
    # loaders=[parse_folder(item) for item in WORLD_FOLDERS],
    loader=folder_loader,
)
