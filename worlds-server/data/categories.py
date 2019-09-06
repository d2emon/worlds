import random
from .utils import ListDatabase


class CategoriesDB(ListDatabase):
    IMAGES = [
        'https://cdn.vuetifyjs.com/images/cards/house.jpg',
        'https://cdn.vuetifyjs.com/images/cards/road.jpg',
        'https://cdn.vuetifyjs.com/images/cards/plane.jpg',
    ]

    def __init__(self, titles):
        super().__init__([{
            'title': title,
            'image': random.choice(self.IMAGES),
            'to': '/',
        } for title in titles])

    @classmethod
    def sanitize(cls, data):
        return super().sanitize({
            'title': data.get('title'),
            'image': data.get('image'),
            'url': data.get('url')
        })


CATEGORIES = CategoriesDB([
  'Игры',
  'Искусство',
  'История',
  'Культура',
  'Луганск',
  'Экономика',
  'Менеджмент',
  'Психология',
  'Миры',
  'Наука',

  'Паранаучное',
  'Природа',
  'Работа',
  'Техника',
  'Цитаты',
  'Юмор',
  'Языки',
])
