import logging

logger = logging.getLogger(__name__)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',  # Change the file path to your desired location
        },
    },
    'root': {
        'handlers': ['file'],
        'level': 'DEBUG',
    },
}
