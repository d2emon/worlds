const express = require('express');
const indexHandlers = require('../handlers/index');
const router = express.Router();

router.get('/files/:url', indexHandlers.media);

router.get('/:url', indexHandlers.index);
router.get('/', indexHandlers.index);

// @app.errorhandler(404)
// router.get('/', indexHandlers.notFound);

module.exports = router;
