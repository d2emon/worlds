const express = require('express');
const path = require('path');
const cookieParser = require('cookie-parser');
const logger = require('morgan');

const indexRouter = require('./routes/index');
const usersRouter = require('./routes/users');

// Instantiate the app
const app = express();

// Configuration
// app.config.from_object('config.Config')
// if app.debug:
//     app.logger.info('Config: {}'.format(app.config))

// Modules
// CORS(app)
// resize = Resize(app)
app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

// Blueprints
// from .images import blueprint as images
// app.register_blueprint(images)

// API
// from .api.categories import blueprint as categories
// app.register_blueprint(categories)

// from .api.portal import blueprint as portal
// app.register_blueprint(portal)

// from .api.worlds import blueprint as worlds
// app.register_blueprint(worlds)

// from .api.generated import blueprint as generated
// app.register_blueprint(generated)

// Walk
// from .walk import blueprint as walk
// app.register_blueprint(walk)

app.use('/users', usersRouter);
app.use('/', indexRouter);

module.exports = app;
