import Axios from './axios_helper';
import markdown from './markdown';
import Url from './url';

const local = /\[(.*)]\(\.\/(.*)\)/g;

export const Api = Axios;
export const imageUrl = Url.imageUrl;
export const worldUrl = Url.worldUrl;
export const markdown2html = text => text && markdown(text);
export const wiki2html = (text, world) => {
  const prepared = text && text.replace(local, `[$1](${Url.mediaUrl}/wiki/${world}/$2)`);
  return markdown2html(prepared);
};
