import realm from './realm';

const Item = (generatorId, groupId) => (text, itemId) => ({
  generatorId,
  groupId: groupId + 1,
  itemId: itemId + 1,
  text,
});
const ItemsList = (generatorId, groupId, data) => data.map(Item(generatorId, groupId));
const GeneratorData = (generatorId, items) => items.reduce((result, data, groupId) => [
  ...result,
  ...ItemsList(generatorId, groupId, data),
], []);

export default [
  ...GeneratorData('realm', realm),
];
