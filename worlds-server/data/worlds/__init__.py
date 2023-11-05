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
        'books',
        'created_at',
        'image',
        'image_url',
        'isbn',
        # 'index_page',
        'language',
        '__links',
        'media',
        'order',
        'origin',
        'pages',
        'publisher',
        'series',
        # 'slug',
        'title',
        'wiki',
    ]
    serializable = [
        'author',
        'book_pages',
        'books',
        'created_at',
        'image',
        'image_url',
        'index_page',
        'isbn',
        'language',
        'media',
        'order',
        'origin',
        'pages',
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
    def books(self):
        def parse_book(book_id):
            return {
                'book_id': book_id,
                'title': books.get(book_id),
            }

        def parse_category(category):
            subcategory = category.get('categories')
            return {
                'title': category.get('title'),
                'books': [parse_book(b) for b in category.get('books', [])],
                'categories': subcategory and [parse_category(c) for c in subcategory],
            }

        filename = os.path.join(self.root, 'books.json')
        if not os.path.isfile(filename):
            return []
        with open(filename, "r", encoding='utf-8') as fp:
            data = json.load(fp)
            books = data.get('books', {})
            categories = data.get('categories', [])
            return [parse_category(c) for c in categories]

    @property
    def image_url(self):
        image_url = self.fields.get('image')
        return "{}/images/{}".format(self.slug, image_url) if image_url else None

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
            yield Planet.load(path, self.slug, os.path.splitext(os.path.basename(file))[0])

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
            'books': self.books,
            'image_url': self.image_url,
            'index_page': self.index_page,
            'planets': [__planet.fields for __planet in self.planets],
            'slug': self.slug,
            'title': self.title,
            'wiki': self.wiki,
        }
        print(computed)
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
    # https://rpg.fandom.com/ru/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%A1%D0%B5%D1%82%D1%82%D0%B8%D0%BD%D0%B3%D0%B8
    # https://rpg.fandom.com/ru/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%AD%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D1%8B_%D1%81%D0%B5%D1%82%D1%82%D0%B8%D0%BD%D0%B3%D0%BE%D0%B2

    {'title': 'Al-Qadim'},
    {'title': 'Ashen Stars'},
    # {
    #     # !
    #     'title': 'Birthright',
    #     'image': 'birthright/images/br-logos.gif',
    #     'slug': 'birthright',
    #     'index_page': 'birthright/index.md',
    # },
    # {
    #     # !
    #     'title': 'Blackmoor',
    #     'image': 'blackmoor/images/Blackmoor_logo.png',
    #     'slug': 'blackmoor',
    #     'index_page': 'blackmoor/index.md',
    # },
    {'title': 'Bulldogs!'},
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
    # SluggedWorld(
    #     title='Cyberpunk20XX',
    #     slug='cyberpunk-20xx',
    # ),
    # {
    #     'title': 'Dangerous Fantasy 2',
    #     'image': 'dangerous-fantasy-2/images/df2.gif',
    #     'slug': 'dangerous-fantasy-2',
    #     'index_page': 'dangerous-fantasy-2/index.md',
    # },
    # {
    #     # !
    #     'title': 'Dark Sun',
    #     'image': 'dark-sun/images/ds-logos.gif',
    #     'slug': 'dark-sun',
    #     'index_page': 'dark-sun/index.md',
    # },
    {'title': 'Dawn of the Emperors'},
    {'title': 'Deadlands'},

    {'title': 'Demon: The Fallen'},
    {'title': 'Don\'t Rest Your Head'},
    {'title': 'Dracurouge'},
    {'title': 'Dragon Age'},
    # {
    #     'title': 'Dragon Fist',
    #     'image': 'dragon-fist/images/DragonFist.jpg',
    #     'slug': 'dragon-fist',
    #     'index_page': 'dragon-fist/index.md',
    # },
    # {
    #     # !
    #     'title': 'Dragonlance',
    #     'image': 'dragonlance/images/fa-logos.gif',
    #     'slug': 'dragonlance',
    #     'index_page': 'dragonlance/index.md',
    # },
    {'title': 'Dragonstar'},
    # {
    #     'title': 'Eberron',
    #     'image': 'eberron/images/eb-logos.gif',
    #     'slug': 'eberron',
    #     'index_page': 'eberron/index.md',
    # },
    {'title': 'Exalted'},
    {'title': 'Fading Suns'},

    {'title': 'Fallout'},
    # {
    #     # !
    #     'title': 'Forgotten Realms',
    #     'image': 'forgotten-realms/images/fr-logos.gif',
    #     'slug': 'forgotten-realms',
    #     'index_page': 'forgotten-realms/index.md',
    #
    #     'link': 'https://rpg.fandom.com/ru/wiki/Forgotten_Realms',
    # },
    {'title': 'Gamma World'},
    # {
    #     'title': 'Ghostwalk',
    #     'image': 'ghostwalk/images/Ghostwalk_coverthumb.jpg',
    #     'slug': 'ghostwalk',
    #     'index_page': 'ghostwalk/index.md',
    # },
    # {
    #     # !
    #     'title': 'Greyhawk',
    #     'image': 'greyhawk/images/gh-logos.gif',
    #     'slug': 'greyhawk',
    #     'index_page': 'greyhawk/index.md',
    # },
    {'title': 'Hellfrost'},
    {'title': 'Hellfrost: Land of Fire'},
    {'title': 'Hollow World'},
    {'title': 'Houses of the Blooded'},

    {'title': 'Iron Kingdoms'},
    {'title': 'Jakandor'},
    # {
    #     'title': 'Jakandor',
    #     'image': 'jakandor/images/Jakandor.jpg',
    #     'slug': 'jakandor',
    #     'index_page': 'jakandor/index.md',
    # },
    # {
    #     # !
    #     'title': 'Kingdoms of Kalamar',
    #     'image': 'kingdoms-of-kalamar/images/kk-logos.gif',
    #     'slug': 'kingdoms-of-kalamar',
    #     'index_page': 'kingdoms-of-kalamar/index.md',
    # },
    # {
    #     # !
    #     'title': 'Lankhmar',
    #     'image': 'lankhmar/images/lm-logos.gif',
    #     'slug': 'lankhmar',
    #     'index_page': 'lankhmar/index.md',
    # },
    {'title': 'Legends of Anglerre'},
    # {
    #     'title': 'Mahasarpa',
    #     'image': 'mahasarpa/images/Mahasarpa.jpg',
    #     'slug': 'mahasarpa',
    #     'index_page': 'mahasarpa/index.md',
    # },
    {'title': 'Категория:Megaverse'},
    {'title': 'Mekton'},
    {'title': 'Mighty Fortress'},

    # {
    #     'title': 'Mortal Kombat',
    #     'image': 'mortal-kombat/images/MortalKombat.jpg',
    #     'slug': 'mortal-kombat',
    #     'index_page': 'mortal-kombat/index.md',
    # },
    {'title': 'Mutant City Blues'},
    # {
    #     # !
    #     'title': 'Mystara',
    #     'image': 'mystara/images/ms-logos.gif',
    #     'slug': 'mystara',
    #     'index_page': 'mystara/index.md',
    # },
    {'title': 'Mythic Vistas'},
    {'title': 'Necessary Evil'},
    {'title': 'Necropolis (Savage Worlds)'},
    {'title': 'Numenera'},
    # {
    #     'title': 'Nentir Vale',
    #     'image': 'nentir-vale/images/NentirVale.jpg',
    #     'slug': 'nentir-vale',
    #     'index_page': 'nentir-vale/index.md',
    # },
    # {
    #     'title': 'Odyssey',
    #     'image': 'odyssey/images/od-logos.gif',
    #     'slug': 'odyssey',
    #     'index_page': 'odyssey/index.md',
    # },
    # {
    #     'title': '',
    #     'image': 'oriental-adventures/images/oa-logos.gif',
    #     'slug': 'oriental-adventures',
    #     'index_page': 'oriental-adventures/index.md',
    # },
    {'title': 'Paranoia'},
    # {
    #     'title': 'Pelinore',
    #     'image': 'pelinore/images/Pelinore.jpg',
    #     'slug': 'pelinore',
    #     'index_page': 'pelinore/index.md',
    # },
    {'title': 'Pirates of the Spanish Main'},

    # {
    #     # !
    #     'title': 'Planescape',
    #     'image': 'planescape/images/PlanescapeLogo.jpg',
    #     'slug': 'planescape',
    #     'index_page': 'planescape/index.md',
    #
    #     'link': 'https://rpg.fandom.com/ru/wiki/Planescape',
    # },
    {'title': 'Points of Light'},
    {'title': 'Ptolus'},
    # {
    #     # !
    #     'title': 'Ravenloft',
    #     'image': 'ravenloft/images/rv-logos.gif',
    #     'slug': 'ravenloft',
    #     'index_page': 'ravenloft/index.md',
    #
    #     'link': 'https://rpg.fandom.com/ru/wiki/Ravenloft',
    # },
    {'title': 'Rippers'},
    {'title': 'Rippers Resurrected'},
    # {
    #     'title': 'S.T.A.L.K.E.R.',
    #     'image': 'stalker/images/Stalker.jpg',
    #     'slug': 'stalker',
    #     'index_page': 'stalker/index.md',
    # },
    {'title': 'Savage Coast'},
    # {
    #     'title': 'SCP Foundation',
    #     'slug': 'scp-foundation',
    #     'index_page': 'scp-foundation/index.md',
    # },
    # {'title': 'Shadowrun', 'link': 'https://rpg.fandom.com/ru/wiki/Shadowrun'},

    {'title': 'Shaintar: Immortal Legends'},
    {'title': 'Spellbound Kingdoms'},
    # {
    #     # !
    #     'title': 'Spelljammer',
    #     'image': 'spelljammer/images/sj-logos.gif',
    #     'slug': 'spelljammer',
    #     'index_page': 'spelljammer/index.md',
    # },
    {'title': 'Sundered Skies'},
    {'title': 'Terah'},
    # SluggedWorld(
    #     title='The Elder Scrolls',
    #     slug='the-elder-scrolls',
    # ),
    # {
    #     'title': 'Thunder Rift',
    #     'image': 'thunder-rift/images/ThunderRift.jpg',
    #     'slug': 'thunder-rift',
    #     'index_page': 'thunder-rift/index.md',
    # },
    {'title': 'Unhallowed Metropolis'},
    {'title': 'Urban Arcana'},
    # {'title': 'Vampire: The Masquerade', 'link': 'https://rpg.fandom.com/ru/wiki/Vampire:_The_Masquerade'},

    {'title': 'Vampire: The Requiem'},
    # {'title': 'Категория:Warcraft'},
    # {
    #     'title': 'Warcraft',
    #     'image': 'warcraft/images/wc-logos.gif',
    #     'slug': 'warcraft',
    #     'index_page': 'warcraft/index.md',
    # },
    # {'title': 'Warhammer'},
    # {
    #     'title': 'Warhammer 40.000',
    #     'slug': 'warhammer-40000',
    #     'index_page': 'warhammer-40000/index.md',
    # },
    # SluggedWorld(
    #     title='Warhammer Fantasy Battles',
    #     slug='warhammer-fantasy',
    #     image=None,
    #
    #     links={
    #         'en': "https://warhammerfantasy.fandom.com/",
    #         'ru': "https://warhammerfantasy.fandom.com/ru/",
    #     },
    #
    #     lurkmore=False,
    # ),
    {'title': 'Weird Wars'},
    {'title': 'Werewolf: The Apocalypse'},
    # {
    #     'title': 'Wilderlands of High Fantasy',
    #     'image': 'wilderlands-of-high-fantasy/images/WilderlandsOfHighFantasy.jpg',
    #     'slug': 'wilderlands-of-high-fantasy',
    #     'index_page': 'wilderlands-of-high-fantasy/index.md',
    # },
    {'title': 'World’s Largest Dungeon'},
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
    {'title': 'Анакен'},
    {'title': 'Анима'},

    {'title': 'Арадия'},
    {
        'title': 'Арда',
        'image': 'arda/images/tolkien.jpg',
        'slug': 'arda',
        'index_page': 'arda/index.md',
    },
    {'title': 'АРРРГХЪ!'},
    {
        'title': 'Белория',
        'image': 'beloriya/images/beloria.jpg',
        'slug': 'beloriya',
        'index_page': 'beloriya/index.md',
    },
    {'title': 'Вавилон-5'},
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
    {'title': 'Волчье солнце'},
    {
        'title': 'Волшебная Страна',
        'image': 'volshebnaya-strana/images/emerald.jpg',
        'slug': 'volshebnaya-strana',
        'index_page': 'volshebnaya-strana/index.md',
    },
    {'title': 'Вселенная Warcraft'},
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
    {'title': 'Глоранта'},
    {'title': 'Голарион'},
    {'title': 'Горная ведьма'},

    {'title': 'Грань Вселенной'},
    {'title': 'Дзайбацу'},
    {
        'title': 'Дино',
        'slug': 'dino',
        'index_page': 'dino/index.md',
    },
    {'title': 'Замок Фалькенштайн'},
    {
        'title': 'Звездные Войны',
        'slug': 'star-wars',
        'index_page': 'star-wars/index.md',
    },
    {'title': 'Звёздный путь'},
    {'title': 'Земля (BESM)'},
    # SluggedWorld(
    #     title='Земноморье',
    #     slug='zemnomorye',
    #     # image='images/Pet9.png',
    # ),
    {'title': 'Известный мир'},
    {'title': 'Искусство волшебства'},
    {'title': 'Исторический сеттинг'},

    {'title': 'История сеттинга Greyhawk'},
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
    {'title': 'Красная земля'},
    {
        'title': 'Крон',
        'image': 'kron/images/chronos.jpg',
        'slug': 'kron',
        'index_page': 'kron/index.md',
    },
    {'title': 'Категория:Лаар'},
    {'title': 'Лавикандия'},
    {'title': 'Лайран'},
    {'title': 'Маска Красной Смерти'},
    # {
    #     'title': 'Мир номер три',
    #     'image': 'mir-nomer-tri/images/TretiyMir.jpg',
    #     'slug': 'mir-nomer-tri',
    #     'index_page': 'mir-nomer-tri/index.md',
    # },
    {
        'title': 'Мир Полудня',
        'image': 'mir-poludnya/images/midday.jpg',
        'slug': 'mir-poludnya',
        'index_page': 'mir-poludnya/index.md',
    },
    {'title': 'Мир Тьмы'},
    {
        'title': 'Миры Ктулху',
        'slug': 'mir-ktulhu',
        'index_page': 'mir-ktulhu/index.md',
    },
    future_moscow,
    {'title': 'Муршамбала'},

    SluggedWorld(
        title='Нарния',
        slug='narniya',
    ),
    SluggedWorld(
        title='Невендаар',
        slug='nevendaar',
    ),
    {'title': 'Неизвестные армии'},
    {'title': 'Новый Мир Тьмы'},
    {'title': 'Нудмер'},
    {'title': 'Ньямбе'},
    {'title': 'Оборотни въ фофудьяхъ'},
    {'title': 'Перекрёсток миров'},
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
    {'title': 'Полночь'},
    {'title': 'Порох и хлеб'},

    {'title': 'Рокуган'},
    {'title': 'Категория:Сады Ислага'},
    {'title': 'Сальвеблюз'},
    # spectre,
    {'title': 'Категория:Старый Мир Тьмы'},
    {'title': 'Странствующие миры'},
    {'title': 'Категория:Текумель'},
    {'title': 'Фэн Шуй'},
    {'title': 'Категория:Храмовники Рока'},
    {'title': 'Шандария'},
    {'title': 'Эберрон', 'link': 'https://rpg.fandom.com/ru/wiki/%D0%AD%D0%B1%D0%B5%D1%80%D1%80%D0%BE%D0%BD'},
    {'title': 'Эра Водолея'},
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
    folders = list(os.listdir(Config.WIKI_ROOT))
    for slug in folders:
        if not os.path.isdir(os.path.join(Config.WIKI_ROOT, slug)):
            continue
        yield parse_folder(WorldFolder(slug))

    for world in worlds:
        slug = world.get('slug') or world.get('title')
        if slug in folders:
            continue
        yield lambda: {
            'slug': slug,
            **world,
        }


WORLDS = WorldsDB(
    # items=[item() for item in ITEMS],
    # loaders=[parse_folder(item) for item in WORLD_FOLDERS],
    loader=folder_loader,
)
