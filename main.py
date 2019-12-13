import logging

from os import environ

from christmas import server

LOG_LEVEL = logging.getLevelName(environ.get('LOG_LEVEL', 'WARNING'))

if __name__ == "__main__":
    logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s christmas.%(module)s.%(funcName)s +%(lineno)s: '
                                  '%(levelname)-8s [%(process)d] %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(LOG_LEVEL)
    server.app.run(host="0.0.0.0", port=8000, access_log=False)
