from logging.handlers import SMTPHandler


def mail_handler(config):
    if config['MAIL_SERVER']:
        return None

    if config['MAIL_USERNAME'] or config['MAIL_PASSWORD']:
        credentials = (config['MAIL_USERNAME'], config['MAIL_PASSWORD'])
    else:
        credentials = None

    return SMTPHandler(
        mailhost=(config['MAIL_SERVER'], config['MAIL_PORT']),
        fromaddr="no-reply@{}".format(config['MAIL_SERVER']),
        toaddrs=config['ADMINS'],
        subject="Blog Failure",
        credentials=credentials,
        secure=config['MAIL_USE_TLS'] and (),
    )
