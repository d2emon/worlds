const images = [
  'https://cdn.vuetifyjs.com/images/cards/house.jpg',
  'https://cdn.vuetifyjs.com/images/cards/road.jpg',
  'https://cdn.vuetifyjs.com/images/cards/plane.jpg',
];

const categories = [
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
];

export default {
  getCategories: () => Promise
    .resolve(categories.map(title => ({
      title,
      image: images[Math.floor(Math.random() * images.length)],
      to: '/',
    }))),
};
