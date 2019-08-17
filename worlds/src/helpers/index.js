import Axios from './axios_helper';
import markdown from './markdown';
import Url from './url';

const localImage = /!\[(.*?)]\(\.\/(.*?)\)/g;
const localLink = /\[(.*?)]\(\.\/(.*?)\.md\)/g;

export const Api = Axios;
export const imageUrl = Url.imageUrl;
export const worldUrl = Url.worldUrl;
export const markdown2html = text => text && markdown(text);
export const wiki2html = (text, world) => text
  && markdown2html(
    text
      .replace(localImage, `![$1](${Url.mediaUrl}/wiki/${world}/$2)`)
      .replace(localLink, `[$1](#/wiki/${world}/$2)`)
  );
