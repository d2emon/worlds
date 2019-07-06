import Axios from './axios_helper';
import markdown from './markdown';
import Url from './url';

export const Api = Axios;
export const imageUrl = Url.imageUrl;
export const worldUrl = Url.worldUrl;
export const markdown2html = text => text && markdown(text);
