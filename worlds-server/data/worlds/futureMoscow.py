from helpers import show_book, show_facts, show_planets
from .world import SluggedWorld


class PostCard:
    def __init__(self, image, title, text):
        self.__image = image
        self.title = title
        self.text = text

    def row(self):
        return "|![](http://127.0.0.1:5000/thumbs/worlds/moskva-budushego/moscow-xxiii/{})<br />{}|{}|".format(self.__image, self.title, self.text)

    @property
    def image(self):
        return "http://127.0.0.1:5000/media/images/worlds/moskva-budushego/moscow-xxiii/{}".format(self.__image)

    @property
    def thumb(self):
        return "http://127.0.0.1:5000/thumbs/worlds/moskva-budushego/moscow-xxiii/{}".format(self.__image)

    def as_dict(self):
        return {
            'thumb': self.thumb,
            'image': self.image,
            'title': self.title,
            'text': self.text,
        }


class FutureMoscow(SluggedWorld):
    def __init__(self, **data):
        data['data_loader'] = self.__custom_data_loader
        super().__init__(**data)

    def __custom_data_loader(self):
        return {
            'cards': [card.as_dict() for card in self.data.get('cards', [])],
        }


future_moscow = FutureMoscow(
    title='Москва Будущего',
    slug='moskva-budushego',
    image='Moscow.jpg',
    pages={
        'moscow20': "Каким виделось будущее Москвы из 1920-30-х годов",
        'moscow45': "Москва в 1945 году",
        'moscow50': "Какой виделась Москва будущего из 1950-60-х годов",
        'moscow-xxiii': "Москва в XXIII веке",
        'russia2017': "А.Лиговский: Россия в 2017 году. Новогодняя фантазия",
    },
    wiki={},

    # Data
    cards=[
        PostCard(
            "Moscow_in_XXIII_Century._Central_Air_Vokzal._1914.jpg",
            "Центральный вокзал",
            "Зима такая же, как и при нас 200 лет назад. Снег такой же белый и холодный. Центральный Вокзал Земных и "
            "Воздушных Путей Сообщения. Десятки тысяч приезжающих и уезжающих, все идет чрезвычайно быстро, "
            "планомерно и удобно. К услугам пассажиров — земля и воздух. Желающие могут двигаться с быстротою "
            "телеграмм",
        ),
        PostCard(
            "Moscow_in_XXIII_Century._Kremlin._1914.jpg",
            "Москворецкий мост",
            "Кремль так же украшает древнюю Белокаменную и с золотыми куполами представляет феерическое зрелище. Тут "
            "же у Москворецкого моста мы видим новые огромные здания торговых предприятий, трестов, обществ, "
            "синдикатов и т. д. На фоне неба стройно скользят вагоны подвесной воздушной дороги…",
        ),
        PostCard(
            "Moscow_in_XXIII_Century._Lubianka._1914.jpg",
            "Лубянская площадь",
            "Ясный вечер. Лубянская площадь. Синеву неба чертят четкие линии светящихся аэропланов, дирижаблей и "
            "вагонов воздушной дороги. Из-под мостовой площади вылетают длинные вагоны Московского Метрополитена, о "
            "котором при нас в 1914-м году только говорили. По мосту над Метрополитеном мы видим стройный отряд "
            "доблестного русского войска, сохранившего свою форму ещё с наших времен. В синем воздухе мы замечаем "
            "товарный дирижабль Эйнем, летающий в Тулу с запасом шоколада для розничных магазинов",
        ),
        PostCard(
            "Moscow_in_XXIII_Century._Moscow_River._1914.jpg",
            "Река Москва",
            "Оживленные, шумные берега большой судоходной Москвы-реки. По прозрачным глубоким волнам широкого "
            "торгового порта несутся огромные транспортные и торговые крейсеры и многоэтажные пассажирские пароходы. "
            "Весь флот мира — исключительно торговый. Военный упразднен после мирного договора в Гааге. В шумной "
            "гавани видны разнохарактерные костюмы всех народов земного шарa, ибо Москва-река сделалась мировым "
            "торговым портом",
        ),
        PostCard(
            "Moscow_in_XXIII_Century._Petrovsky_Park._1914.jpg",
            "Петровский парк",
            "Мы переносимся мысленно в Петровский парк. Аллеи расширены до неузнаваемости. Древний Петровский "
            "дворец реставрирован, и в нём сосредоточен Музей Петровской эпохи. Повсюду бьют, сверкая, дивные "
            "фонтаны. Лишенный микробов и пыли, совершенно чистый воздух прорезывают дирижабли и аэропланы. Толпы "
            "людей в ярких костюмах XXIII века наслаждаются дивной природою на том же месте, где, бывало, гуляли мы, "
            "пра-пра-прадеды",
        ),
        PostCard(
            "Moscow_in_XXIII_Century._Red_Square._1914.jpg",
            "Красная площадь",
            "Красная площадь. Шум крыльев, звон трамваев, рожки велосипедистов, сирены автомобилей, треск моторов, "
            "крики публики. Минин и Пожарский. Тени дирижаблей. В центре — полицейский с саблей. Робкие пешеходы "
            "спасаются на лобном месте. Так будет лет через 200",
        ),
        PostCard(
            "Moscow_in_XXIII_Century._SPb_Shosse._1914.jpg",
            "Петербургское шоссе",
            "Красивая ясная зима 2259-го года. Уголок «старой» веселящейся Москвы, древний «Яр» по-прежнему служит "
            "местом широкого веселья москвичей, как было и при нас 300 с лишним лет тому назад. Для удобства и "
            "приятности сообщения Санкт-Петербургское шоссе целиком превращено в кристально-ледяное зеркало, по "
            "которому летят, скользя, изящные аэросани. Тут же на маленьких аэросалазках шмыгают традиционные "
            "сбитенщики и продавцы горячих аэросаек. И в XXIII веке Москва верна своим обычаям",
        ),
        PostCard(
            "Moscow_in_XXIII_Century._Theatral_Square_and_TcsUM._1914.jpg",
            "Театральная площадь",
            "Театральная площадь. Темп жизни усилился в сто раз. Всюду молниеносное движение колесных, крылатых, "
            "пропеллерных и прочих аппаратов. Существовавший ещё в 1846 году Торговый дом Мюр и Мерлиз в настоящее "
            "время разросся до баснословных размеров, причем главные отделы его соединены с воздушными железными "
            "дорогами. Из-под мостовой вылетают многочисленные моторы. Где-то вдали пожар. Мы видим автомобильную "
            "пожарную команду, которая через мгновение прекратит бедствие. На пожар же спешат бипланы, монопланы и "
            "множество воздушных пролёток",
        ),
    ],
)
