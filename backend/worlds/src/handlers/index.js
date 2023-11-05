const path = require('path');

const index = function(req, res, next) {
  const {
    DIST_ROOT,
    ENV,
    FRONT,
  } = req.config;
  const {
    url,
  } = req.params;

  if (ENV === 'development') {
    const spa = {
      url: `${FRONT}${url}`,
    }; // axios.get(`${FRONT}${url}`);

    return res.json([
      spa.content,
      spa.statusCode,
      spa.headers,
    ]);
  }

  // sendfile
  const filename = path.join(DIST_ROOT, 'index.html');
  return res.json({ filename });
}

const notFound = function(req, res, next) {
  return res
    .status(404)
    .json({ error: 'Not found' });
}

const media = function(req, res, next) {
  const {
    MEDIA_FOLDER,
  } = req.config;
  const {
    url,
  } = req.params;

  const mediaPath = path.join(MEDIA_FOLDER, url);

  // if (!os.path.exists(mediaPath)) {
  if (!mediaPath) {
    return res
      .status(404)
      .json({ error: 'Media not found' });
  }

  // sendfile
  const filename = mediaPath;
  return res.json({ filename });
}
    
module.exports = {
  index,
  notFound,
  media,
};
