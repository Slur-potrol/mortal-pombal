TOKEN ='919374257:AAFqWjpfomFjqu1DgGcbniD9jS1UH4laRq0'

YANDEX_TRANSLATE_KEY = 'trnsl.1.1.20200118T103247Z.ccfc3cf8b7826e1f.7accea379f31254506d5363bd4c0b848747d6ff8'


if db.is_exist(text):
    logger.debug('found pair in database')
    translation = get_trans_from_db(text)
    logger.debug("got translation from database")
else:
    logger.debug("calling yandex.com")
    translation = get_trans_from_yandex(text)
    logger.debug('retrieved translation from yandex.com')
    db.save_pair(text, translation)
    logger.debug("saved pair to database")
translate()