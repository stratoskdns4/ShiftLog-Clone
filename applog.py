import os

import logging
from logging import handlers
# You can set up different handlers so that - e.g. you can print debug logs
# to stdout, and save INFO or higher to normal logs, etc.
def setup_logging(log_folder='logs'):
    logger = logging.getLogger(__name__)
    folderPath=os.path.basename(os.path.join(os.getcwd(), log_folder))
    s_handler = logging.StreamHandler()
    f_handler = handlers.RotatingFileHandler(
        os.path.join(folderPath, f'{__name__}.log'), 
        maxBytes=20480
    )
    d_handler = handlers.RotatingFileHandler(
        os.path.join(folderPath, f'{__name__}.debug.log')
    )
    f_handler.setLevel(logging.WARNING)
    d_handler.setLevel(logging.DEBUG)
    s_handler.setLevel(logging.DEBUG)
    d_format = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s: %(message)s')
    f_format = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s: %(message)s')
    s_format = logging.Formatter('%(asctime)s:%(levelname)s: %(message)s')
    f_handler.setFormatter(f_format)
    d_handler.setFormatter(d_format)
    s_handler.setFormatter(s_format)
    logger.addHandler(f_handler)
    logger.addHandler(d_handler)
    logger.addHandler(s_handler)
    logger.warning(f'Logger Starting!!!')
    return logger


if __name__=='__main__':
    print('Module intended to be imported!')
