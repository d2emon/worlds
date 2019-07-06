import {itemIds, getRandomItem} from './data/portal';

const validate5 = (item, items) => item && (items[4].negative === item.negative);
const validate8 = (item, items) => item && (items[7].hostile === item.hostile);

const generate5 = (item, items) => validate5(item, items) ? item : generate5(getRandomItem(5), items);
const generate8 = (item, items) => validate8(item, items) ? item : generate8(getRandomItem(8), items);
const generateMultiple = (itemId, count) => {
  const items = [];
  for (let i = 0; i < count; i++) {
    let item = null;
    while ((!item) || (items.indexOf(item) > 0)) {
      item = getRandomItem(itemId);
    }
    items.push(item);
  }
  return items;
};

const generate = () => {
  const items = itemIds.map((itemId) => {
    if ([17, 20].indexOf(itemId) > 0) return generateMultiple(itemId, 3);

    return getRandomItem(itemId);
  });
  items[5] = generate5(items[5], items);
  items[8] = generate8(items[8], items);

  return items.map((item) => {
    if (!item) return null;
    if (Array.isArray(item)) return item.map(subitem => subitem.text);
    return item.text;
  });
};

export default {
  getPortal: () => Promise.resolve(generate())
    .then(names => [
      `You ${names[1]} forward through the ${names[2]} portal ${names[3]}.
       You're immediately met by ${names[4]} world. ${names[5]}.
       ${names[6]}.`,
      `${names[7]}${names[8]}.
       This world is ${names[9]}${names[10]}.`,
      `${names[11]} you ${names[12]} of ${names[13]}.
       ${names[14]}, ${names[15]}.
       ${names[16]} ${names[17][0]} creatures, ${names[17][1]} creatures, and what you think might be ${names[17][2]}
       creatures of some sort.`,
      `${names[18]} as ${names[19]}.
       But, with ${names[20][0]}, ${names[20][1]}, and ${names[20][2]}, ${names[21]}.`,
    ]),
};
