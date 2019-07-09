from app import app
from ..utils import Database
from ..wikifiles import get_wiki

from .spectre import spectre


class WorldsDB(Database):
    @classmethod
    def get_text_loader(cls, item):
        loader = item.get('loader')
        if loader is not None:
            return loader

        wiki = item.get('wiki')
        if wiki is not None:
            def wiki_loader():
                return get_wiki(wiki)

            return wiki_loader

        def text_loader():
            text = item.get('text')
            return text
        return text_loader

    @classmethod
    def image_url(cls, item):
        image = item.get('image', 'portal.jpg')
        return '{}/worlds/{}'.format(app.config.get('RESIZE_URL'), image)

    @classmethod
    def world_text(cls, item):
        text_loader = cls.get_text_loader(item)
        if text_loader is None:
            return None
        return text_loader()

    def by_slug(self, slug):
        return next((item for item in self.items if item.get('slug') == slug), None)


WORLDS_DATA = [
    {
        'title': 'Assassin\'s Creed',
        'image': 'assassins-creed/assassins.jpg',
        'slug': 'assassins-creed',
        'wiki': 'assassins-creed/index.md',
    },
    {
        'title': 'Birthright',
        'image': 'birthright/br-logos.gif',
        'slug': 'birthright',
        'wiki': 'birthright/index.md',
    },
    {
        'title': 'Blackmoor',
        'image': 'blackmoor/Blackmoor_logo.png',
        'slug': 'blackmoor',
        'wiki': 'blackmoor/index.md',
    },
    {
        'title': 'Council of Wyrms',
        'image': 'council-of-wyrms/Council_of_Wyrms.jpg',
        'slug': 'council-of-wyrms',
        'wiki': 'council-of-wyrms/index.md',
    },
    {
        'title': 'Creature Crucible',
        'image': 'creature-crucible/cc-logos.gif',
        'slug': 'creature-crucible',
        'wiki': 'creature-crucible/index.md',
    },
    {
        'title': 'Dangerous Fantasy 2',
        'image': 'dangerous-fantasy-2/df2.gif',
        'slug': 'dangerous-fantasy-2',
        'wiki': 'dangerous-fantasy-2/index.md',
    },
    {
        'title': 'Dark Sun',
        'image': 'dark-sun/ds-logos.gif',
        'slug': 'dark-sun',
        'wiki': 'dark-sun/index.md',
    },
    {
        'title': 'Dragon Fist',
        'image': 'dragon-fist/DragonFist.jpg',
        'slug': 'dragon-fist',
        'wiki': 'dragon-fist/index.md',
    },
    {
        'title': 'Dragonlance',
        'image': 'dragonlance/fa-logos.gif',
        'slug': 'dragonlance',
        'wiki': 'dragonlance/index.md',
    },
    {
        'title': 'Eberron',
        'image': 'eberron/eb-logos.gif',
        'slug': 'eberron',
        'wiki': 'eberron/index.md',
    },
    {
        'title': 'Forgotten Realms',
        'image': 'forgotten-realms/fr-logos.gif',
        'slug': 'forgotten-realms',
        'wiki': 'forgotten-realms/index.md',
    },
    {
        'title': 'Ghostwalk',
        'image': 'ghostwalk/Ghostwalk_coverthumb.jpg',
        'slug': 'ghostwalk',
        'wiki': 'ghostwalk/index.md',
    },
    {
        'title': 'Greyhawk',
        'image': 'greyhawk/gh-logos.gif',
        'slug': 'greyhawk',
        'wiki': 'greyhawk/index.md',
    },
    {
        'title': 'Jakandor',
        'image': 'jakandor/Jakandor.jpg',
        'slug': 'jakandor',
        'wiki': 'jakandor/index.md',
    },
    {
        'title': 'Kingdoms of Kalamar',
        'image': 'kingdoms-of-kalamar/kk-logos.gif',
        'slug': 'kingdoms-of-kalamar',
        'wiki': 'kingdoms-of-kalamar/index.md',
    },
    {
        'title': 'Lankhmar',
        'image': 'lankhmar/lm-logos.gif',
        'slug': 'lankhmar',
        'wiki': 'lankhmar/index.md',
    },
    {
        'title': 'Mahasarpa',
        'image': 'mahasarpa/Mahasarpa.jpg',
        'slug': 'mahasarpa',
        'wiki': 'mahasarpa/index.md',
    },
    {
        'title': 'Mortal Kombat',
        'image': 'mortal-kombat/MortalKombat.jpg',
        'slug': 'mortal-kombat',
        'wiki': 'mortal-kombat/index.md',
    },
    {
        'title': 'Mystara',
        'image': 'mystara/ms-logos.gif',
        'slug': 'mystara',
        'wiki': 'mystara/index.md',
    },
    {
        'title': 'Nentir Vale',
        'image': 'nentir-vale/NentirVale.jpg',
        'slug': 'nentir-vale',
        'wiki': 'nentir-vale/index.md',
    },
    {
        'title': 'Odyssey',
        'image': 'odyssey/od-logos.gif',
        'slug': 'odyssey',
        'wiki': 'odyssey/index.md',
    },
    {
        'title': 'Oriental Adventures',
        'image': 'oriental-adventures/oa-logos.gif',
        'slug': 'oriental-adventures',
        'wiki': 'oriental-adventures/index.md',
    },
    {
        'title': 'Pelinore',
        'image': 'pelinore/Pelinore.jpg',
        'slug': 'pelinore',
        'wiki': 'pelinore/index.md',
    },
    {
        'title': 'Planescape',
        'image': 'planescape/PlanescapeLogo.jpg',
        'slug': 'planescape',
        'wiki': 'planescape/index.md',
    },
    {
        'title': 'Ravenloft',
        'image': 'ravenloft/rv-logos.gif',
        'slug': 'ravenloft',
        'wiki': 'ravenloft/index.md',
    },
    {
        'title': 'S.T.A.L.K.E.R.',
        'image': 'stalker/Stalker.jpg',
        'slug': 'stalker',
        'wiki': 'stalker/index.md',
    },
    {
        'title': 'SCP Foundation',
        'slug': 'scp-foundation',
        'wiki': 'scp-foundation/index.md',
    },
    {
        'title': 'Spelljammer',
        'image': 'spelljammer/sj-logos.gif',
        'slug': 'spelljammer',
        'wiki': 'spelljammer/index.md',
    },
    {
        'title': 'Thunder Rift',
        'image': 'thunder-rift/ThunderRift.jpg',
        'slug': 'thunder-rift',
        'wiki': 'thunder-rift/index.md',
    },
    {
        'title': 'Warcraft',
        'image': 'warcraft/wc-logos.gif',
        'slug': 'warcraft',
        'wiki': 'warcraft/index.md',
    },
    {
        'title': 'Warhammer 40.000',
        'slug': 'warhammer-40000',
        'wiki': 'warhammer-40000/index.md',
    },
    {
        'title': 'Warhammer Fantasy',
        'slug': 'warhammer-fantasy',
        'wiki': 'warhammer-fantasy/index.md',
    },
    {
        'title': 'Wilderlands of High Fantasy',
        'image': 'wilderlands-of-high-fantasy/WilderlandsOfHighFantasy.jpg',
        'slug': 'wilderlands-of-high-fantasy',
        'wiki': 'wilderlands-of-high-fantasy/index.md',
    },
    {
        'title': 'Авенхейм',
        'image': 'avenheim/avenheim.jpg',
        'slug': 'avenheim',
        'wiki': 'avenheim/index.md',
    },
    {
        'title': 'Алиса Селезнева',
        'image': 'alisa-seleznyova/alice.png',
        'slug': 'alisa-seleznyova',
        'wiki': 'alisa-seleznyova/index.md',
    },
    {
        'title': 'Амбер',
        'image': 'amber/amber.jpg',
        'slug': 'amber',
        'wiki': 'amber/index.md',
    },
    {
        'title': 'Арда',
        'image': 'arda/tolkien.jpg',
        'slug': 'arda',
        'wiki': 'arda/index.md',
    },
    {
        'title': 'Белория',
        'image': 'beloriya/beloria.jpg',
        'slug': 'beloriya',
        'wiki': 'beloriya/index.md',
    },
    {
        'title': 'Вестерос',
        'wiki': 'vesteros/index.md',
    },
    {
        'title': 'Вечный Воитель',
        'image': 'vechnyy-voitel/eternal_warrior.jpg',
        'slug': 'vechnyy-voitel',
        'wiki': 'vechnyy-voitel/index.md',
    },
    {
        'title': 'Волшебная Страна',
        'image': 'volshebnaya-strana/emerald.jpg',
        'slug': 'volshebnaya-strana',
        'wiki': 'volshebnaya-strana/index.md',
    },
    {
        'title': 'Геройский Мир',
        'image': 'geroyskiy-mir/HoMM.jpg',
        'slug': 'geroyskiy-mir',
        'wiki': 'geroyskiy-mir/index.md',
    },
    {
        'title': 'Дино',
        'slug': 'dino',
        'wiki': 'dino/index.md',
    },
    {
        'title': 'Звездные Войны',
        'slug': 'star-wars',
        'wiki': 'star-wars/index.md',
    },
    {
        'title': 'Кинг',
        'slug': 'king',
        'wiki': 'king/index.md',
    },
    {
        'title': 'Конан',
        'image': 'conan/cn-logos.gif',
        'slug': 'conan',
        'wiki': 'conan/index.md',
    },
    {
        'title': 'Король и Шут',
        'image': 'korol-i-shut/KiSh.jpg',
        'slug': 'korol-i-shut',
        'wiki': 'korol-i-shut/index.md',
    },
    {
        'title': 'Крон',
        'image': 'kron/chronos.jpg',
        'slug': 'kron',
        'wiki': 'kron/index.md',
    },
    {
        'title': 'Мир Полудня',
        'image': 'mir-poludnya/midday.jpg',
        'slug': 'mir-poludnya',
        'wiki': 'mir-poludnya/index.md',
    },
    {
        'title': 'Мир номер три',
        'image': 'mir-nomer-tri/TretiyMir.jpg',
        'slug': 'mir-nomer-tri',
        'wiki': 'mir-nomer-tri/index.md',
    },
    {
        'title': 'Миры Ктулху',
        'slug': 'mir-ktulhu',
        'wiki': 'mir-ktulhu/index.md',
    },
    {
        'title': 'Москва Будущего',
        'image': 'moskva-budushego/Moscow.jpg',
        'slug': 'moskva-budushego',
        'wiki': 'moskva-budushego/index.md',
    },
    {
        'title': 'Плоский мир',
        'slug': 'discworld',
        'wiki': 'discworld/index.md',
    },
    {
        'title': 'Путеводитель по коридорам Ада',
        'image': 'putevoditel-po-koridoram-ada/Hell.jpg',
        'slug': 'putevoditel-po-koridoram-ada',
        'wiki': 'putevoditel-po-koridoram-ada/index.md',
    },
    {
        'title': 'Рик и Морти',
        'slug': 'rick-and-morty',
        'wiki': 'rick-and-morty/index.md',
    },
    spectre,
]
# 'image': '3e-logos.gif',
# 'image': 'hw-logos.gif',
# 'image': 'dd-logos.gif',
# 'image': 'gz-logos.gif',
# 'image': 'cm-logos.gif',
# 'image': 'd20-logos.jpg',

print(WORLDS_DATA)

WORLDS = WorldsDB(WORLDS_DATA)
