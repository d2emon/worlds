import showdown from 'showdown';

/*
const localImages = {
  type: 'lang',
  filter: (text, converter) => text.replace(/!\[(.*)]\(\.\/(.*?)\)/g, '<h1>Test success!</h1>'),
};
*/

// showdown.extension('testext', testExt);

const converter = new showdown.Converter({
  parseImgDimensions: true,
  simplifiedAutoLink: true,
  tables: true,
  /*
  extensions: [
    'testext',
  ],
   */
});
export default markdown => converter.makeHtml(markdown);
