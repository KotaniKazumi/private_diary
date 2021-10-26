from .settings_common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS')]

STATIC_ROOT = '/usr/share/nginx/html/static'
MEDIA_ROOT = '/usr/share/nginx/html/media'

AWS_SES_ACCESS_KEY_ID = os.environ.get('AWS_SES_ACCESS_KEY_ID')
AWS_SES_SECRET_ACCESS_KEY = os.environ.get('AWS_SES_SECRET_ACCESS_KEY')
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'ksys@kkotani.net'
EMAIL_HOST = 'kkotani.net'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'ksys@kkotani.net'
EMAIL_HOST_PASSWORD = 'kotani0721'
EMAIL_USE_TLS = False

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
        },
        'diary': {
            'handlers': ['file'],
            'level': 'INFO',
        },
    },

    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/django.log'),
#            'formatter': 'prod',
            'when': 'D',
            'interval': 1,
            'backupCount': 7,
        },
    },

    'formatters': {
        'dev': {
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s',
                '%(pathname)s(Line:%(lineno)d',
                '%(message)s'
            ])
        }
    }

}


