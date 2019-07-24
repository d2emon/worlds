from ..utils import Database
from ..wikifiles import wikis
from .world import World, SluggedWorld

from .futureMoscow import future_moscow
from .spectre import spectre


class WorldsDB(Database):
    @classmethod
    def world(cls, item):
        return World(**item)


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
    {
        'title': 'Council of Wyrms',
        'image': 'council-of-wyrms/images/Council_of_Wyrms.jpg',
        'slug': 'council-of-wyrms',
        'index_page': 'council-of-wyrms/index.md',
    },
    {
        'title': 'Creature Crucible',
        'image': 'creature-crucible/images/cc-logos.gif',
        'slug': 'creature-crucible',
        'index_page': 'creature-crucible/index.md',
    },
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
    {
        'title': 'Dragon Fist',
        'image': 'dragon-fist/images/DragonFist.jpg',
        'slug': 'dragon-fist',
        'index_page': 'dragon-fist/index.md',
    },
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
    {
        'title': 'Jakandor',
        'image': 'jakandor/images/Jakandor.jpg',
        'slug': 'jakandor',
        'index_page': 'jakandor/index.md',
    },
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
    {
        'title': 'S.T.A.L.K.E.R.',
        'image': 'stalker/images/Stalker.jpg',
        'slug': 'stalker',
        'index_page': 'stalker/index.md',
    },
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
    {
        'title': 'Warhammer Fantasy',
        'slug': 'warhammer-fantasy',
        'index_page': 'warhammer-fantasy/index.md',
    },
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
    {
        'title': 'Алиса Селезнева',
        'image': 'alisa-seleznyova/images/alice.png',
        'slug': 'alisa-seleznyova',
        'index_page': 'alisa-seleznyova/index.md',
    },
    {
        'title': 'Амбер',
        'image': 'amber/images/amber.jpg',
        'slug': 'amber',
        'index_page': 'amber/index.md',
    },
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
    {
        'title': 'Вестерос',
        'index_page': 'vesteros/index.md',
    },
    {
        'title': 'Вечный Воитель',
        'image': 'vechnyy-voitel/images/eternal_warrior.jpg',
        'slug': 'vechnyy-voitel',
        'index_page': 'vechnyy-voitel/index.md',
    },
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
        title='Плоский мир',
        slug='discworld',
        image='images/discworld-wallpaper-768x480.jpg',
        wiki=wikis(
            'Плоский мир',
            en="https://discworld.fandom.com/",
            ru="https://discworld.fandom.com/ru/",
            disc="https://disc.fandom.com/ru/",
        ),
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
        wiki=wikis(
            'Рик и Морти',
            en="https://rickandmorty.fandom.com/",
            ru="https://rickandmorty.fandom.com/ru/",
        ),
        pages={
            'science': '«Рик и Морти» с точки зрения науки',
            'references': 'Obscure Pop Culture References From Rick And Morty, Explained',
            'easter-eggs': '13 Important "Rick And Morty" Easter Eggs That Prove '
                           'It\'s The Smartest Show On Television',
            'universes': 'Вселенные',
        },
    ),
    spectre,
]
# 'image': '3e-logos.gif',
# 'image': 'hw-logos.gif',
# 'image': 'dd-logos.gif',
# 'image': 'gz-logos.gif',
# 'image': 'cm-logos.gif',
# 'image': 'd20-logos.jpg',

WORLDS = WorldsDB([world.fields if isinstance(world, World) else world for world in WORLDS_DATA])
