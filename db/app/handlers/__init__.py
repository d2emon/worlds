import logging
from app import app
from .file_handler import file_handler
from .mail_handler import mail_handler


handlers = (
    app.debug and {
        'handler': file_handler,
        'formatter': logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'),
        'level': logging.INFO,
    },
    app.debug and {
        'handler': mail_handler,
        # 'level': logging.ERROR,
        'level': logging.INFO,
    },
)


for handler_data in handlers:
    if not handler_data or not handler_data.get('handler'):
        continue

    handler = handler_data.get('handler')
    if not handler:
        continue

    handler = handler(app.config)
    if not handler:
        continue

    formatter = handler_data.get('formatter')
    if formatter:
        handler.setFormatter(formatter)

    level = handler_data.get('level')
    if level:
        handler.setLevel(level)

    app.logger.addHandler(handler)


if not app.debug:
    app.logger.setLevel(logging.INFO)


app.logger.info('Blog startup')
app.logger.debug(app.config)
