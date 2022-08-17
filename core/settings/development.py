from decouple import config

from .base import *  # noqa

DEBUG = True

SECRET_KEY = config(
    "DJANGO_SECRET_KEY",
    default="!!!SET DJANGO_SECRET_KEY!!!",
)
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]


# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#internal-ips
INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]

INSTALLED_APPS += [  # noqa
    "debug_toolbar",
    "django_extensions",
]  # noqa
