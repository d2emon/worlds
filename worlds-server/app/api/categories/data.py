import random
import uuid


IMAGES = [
  'https://cdn.vuetifyjs.com/images/cards/house.jpg',
  'https://cdn.vuetifyjs.com/images/cards/road.jpg',
  'https://cdn.vuetifyjs.com/images/cards/plane.jpg',
]

TITLES = [
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
]


def make_category(title):
    return {
        'id': uuid.uuid4().hex,
        'title': title,
        'image': random.choice(IMAGES),
        'to': '/',
    }


CATEGORIES = list(map(make_category, TITLES))


def add(**data):
    CATEGORIES.append({
        'id': uuid.uuid4().hex,
        'title': data.get('title'),
        'image': data.get('image'),
        'url': data.get('url')
    })
    return True


def delete(item_id):
    for item in CATEGORIES:
        if item['id'] == item_id:
            CATEGORIES.remove(item)
            return True
    return False


def edit_book(item_id, **data):
    delete(item_id)
    return add(**data)
