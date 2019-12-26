import Axios from './axios_helper';
import markdown from './markdown';
import Url from './url';

const localImage = /!\[(.*?)]\(\.\/(.*?)\)/g;
const localLink = /\[(.*?)]\(\.\/(.*?)\.md\)/g;

export const Api = Axios;

export const {
  imageUrl,
  mediaUrl,
  planetUrl,
  worldUrl,
} = Url;

export const markdown2html = text => text && markdown(text);
export const wiki2html = (text, world) => text
  && markdown2html(
    text
      .replace(localImage, `![$1](${mediaUrl}/wiki/${world}/$2)`)
      .replace(localLink, `[$1](#/world/${world}/wiki/$2)`),
  );
