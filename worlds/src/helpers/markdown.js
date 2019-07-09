import showdown from 'showdown';

const converter = new showdown.Converter({
  tables: true,
});
export default markdown => converter.makeHtml(markdown);
