from app import app
from ..utils import Database
from ..wikifiles import get_wiki


class WorldsDB(Database):
    @classmethod
    def image_url(cls, item):
        image = item.get('image', 'portal.jpg')
        return '{}/worlds/{}'.format(app.config.get('RESIZE_URL'), image)

    @classmethod
    def world_text(cls, item):
        wiki = item.get('wiki')
        if wiki is None:
            return item.get('text')
        return get_wiki(wiki)

    def by_slug(self, slug):
        return next((item for item in self.items if item.get('slug') == slug), None)


WORLDS = WorldsDB([
    {
        'title': 'Alternity',
        'image': 'alternity/al-logos.gif',
        'slug': 'alternity',
        'wiki': 'alternity/index.md',
    },
    {
        'title': 'Assassin\'s Creed',
        'image': 'assassins-creed/assassins.jpg',
        'slug': 'assassins-creed',
        'wiki': 'assassins-creed/index.md',
    },
    {
        'title': 'Birthright',
        'image': 'br-logos.gif',
        'slug': 'birthright',
        'wiki': 'birthright/index.md',
    },
    {
        'title': 'Blackmoor',
        'image': 'Blackmoor_logo.png',
        'slug': 'blackmoor',
        'wiki': 'blackmoor/index.md',
    },
    {
        'title': 'Council of Wyrms',
        'image': 'Council_of_Wyrms.jpg',
        'slug': 'council-of-wyrms',
        'wiki': 'council-of-wyrms/index.md',
    },
    {
        'title': 'Creature Crucible',
        'image': 'cc-logos.gif',
        'slug': 'creature-crucible',
        'wiki': 'creature-crucible/index.md',
    },
    {
        'title': 'Dangerous Fantasy 2',
        'image': 'df2.gif',
        'slug': 'dangerous-fantasy-2',
        'wiki': 'dangerous-fantasy-2/index.md',
    },
    {
        'title': 'Dark Sun',
        'image': 'ds-logos.gif',
        'slug': 'dark-sun',
        'wiki': 'dark-sun/index.md',
    },
    {
        'title': 'Dragon Fist',
        'image': 'DragonFist.jpg',
        'slug': 'dragon-fist',
        'wiki': 'dragon-fist/index.md',
    },
    {
        'title': 'Dragonlance',
        'image': 'fa-logos.gif',
        'slug': 'dragonlance',
        'wiki': 'dragonlance/index.md',
    },
    {
        'title': 'Ebberron',
        'image': 'eb-logos.gif',
        'slug': 'ebberron',
    },
    {
        'title': 'Forgotten Realms',
        'image': 'fr-logos.gif',
        'slug': 'forgotten-realms',
    },
    {
        'title': 'Ghostwalk',
        'image': 'Ghostwalk_coverthumb.jpg',
        'slug': 'ghostwalk',
    },
    {
        'title': 'Greyhawk',
        'image': 'gh-logos.gif',
        'slug': 'greyhawk',
    },
    {
        'title': 'Jakandor',
        'image': 'Jakandor.jpg',
        'slug': 'jakandor',
    },
    {
        'title': 'Kingdoms of Kalamar',
        'image': 'kk-logos.gif',
        'slug': 'kingdoms-of-kalamar',
    },
    {
        'title': 'Lankhmar',
        'image': 'lm-logos.gif',
        'slug': 'lankhmar',
    },
    {
        'title': 'Mahasarpa',
        'image': 'Mahasarpa.jpg',
        'slug': 'mahasarpa',
    },
    {
        'title': 'Mortal Kombat',
        'image': 'MortalKombat.jpg',
        'slug': 'mortal-kombat',
    },
    {
        'title': 'Mystara',
        'image': 'ms-logos.gif',
        'slug': 'mystara',
    },
    {
        'title': 'Nentir Vale',
        'image': 'NentirVale.jpg',
        'slug': 'nentir-vale',
    },
    {
        'title': 'Odyssey',
        'image': 'od-logos.gif',
        'slug': 'odyssey',
    },
    {
        'title': 'Oriental Adventures',
        'image': 'oa-logos.gif',
        'slug': 'oriental-adventures',
    },
    {
        'title': 'Pelinore',
        'image': 'Pelinore.jpg',
        'slug': 'pelinore',
    },
    {
        'title': 'Planescape',
        'image': 'PlanescapeLogo.jpg',
        'slug': 'planescape',
    },
    {
        'title': 'Ravenloft',
        'image': 'rv-logos.gif',
        'slug': 'ravenloft',
    },
    {
        'title': 'S.T.A.L.K.E.R.',
        'image': 'Stalker.jpg',
        'slug': 'stalker',
    },
    {
        'title': 'SCP Foundation',
    },
    {
        'title': 'Spelljammer',
        'image': 'sj-logos.gif',
        'slug': 'spelljammer',
    },
    {
        'title': 'Thunder Rift',
        'image': 'ThunderRift.jpg',
        'slug': 'thunder-rift',
    },
    {
        'title': 'Warcraft',
        'image': 'wc-logos.gif',
        'slug': 'warcraft',
    },
    {
        'title': 'Warhammer 40.000',
    },
    {
        'title': 'Warhammer Fantasy',
    },
    {
        'title': 'Wilderlands of High Fantasy',
        'image': 'WilderlandsOfHighFantasy.jpg',
        'slug': 'wilderlands-of-high-fantasy',
    },
    {
        'title': 'Авенхейм',
        'image': 'avenheim.jpg',
        'slug': 'avenheim',
    },
    {
        'title': 'Алиса Селезнева',
        'image': 'alice.png',
        'slug': 'alisa-seleznyeva',
    },
    {
        'title': 'Амбер',
        'image': 'amber.jpg',
        'slug': 'amber',
    },
    {
        'title': 'Арда',
        'image': 'tolkien.jpg',
        'slug': 'arda',
    },
    {
        'title': 'Белория',
        'image': 'beloria.jpg',
        'slug': 'beloria',
    },
    {
        'title': 'Вестерос',
    },
    {
        'title': 'Вечный Воитель',
        'image': 'eternal_warrior.jpg',
        'slug': 'vechnyy_voitel',
    },
    {
        'title': 'Волшебная Страна',
        'image': 'emerald.jpg',
        'slug': 'volshebnaya-strana',
    },
    {
        'title': 'Геройский Мир',
        'image': 'HoMM.jpg',
        'slug': 'geroyskiy_mir',
    },
    {
        'title': 'Дино',
    },
    { 'title': 'Звездные Войны' },
    { 'title': 'Кинг' },
    {
        'title': 'Конан',
        'image': 'cn-logos.gif',
        'slug': 'conan',
    },
    {
        'title': 'Король и Шут',
        'image': 'KiSh.jpg',
        'slug': 'korol-i-shut',
    },
    {
        'title': 'Крон',
        'image': 'chronos.jpg',
        'slug': 'chronos',
    },
    {
        'title': 'Мир Полудня',
        'image': 'midday.jpg',
        'slug': 'mir-poludnya',
    },
    {
        'title': 'Мир номер три',
        'image': 'TretiyMir.jpg',
        'slug': 'mir-nomer-tri',
    },
    { 'title': 'Миры Ктулху' },
    {
        'title': 'Москва Будущего',
        'image': 'Moscow.jpg',
        'slug': 'moskva-budushego',
    },
    { 'title': 'Плоский мир' },
    {
        'title': 'Путеводитель по коридорам Ада',
        'image': 'Hell.jpg',
        'slug': 'putevoditel_po_koridoram_ada',
    },
    { 'title': 'Рик и Морти' },
    {
        'title': 'Спектр',
        'image': 'Spectre.jpg',
        'slug': 'spectre',
    },
])
# 'image': '3e-logos.gif',
# 'image': 'hw-logos.gif',
# 'image': 'dd-logos.gif',
# 'image': 'gz-logos.gif',
# 'image': 'cm-logos.gif',
# 'image': 'd20-logos.jpg',
