import showdown from 'showdown';

const converter = new showdown.Converter();
export default markdown => converter.makeHtml(markdown);
