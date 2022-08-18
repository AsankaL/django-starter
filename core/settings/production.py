from decouple import config

from .base import *  # noqa

DEBUG = False if config("DJANGO_DEBUG", default="False") == "False" else True

SECRET_KEY = config("SECRET_KEY")

ALLOWED_HOSTS = [
    i.strip() for i in config("ALLOWED_HOSTS", default="").split(",") if i.strip()
]

if (
    config("EMAIL_HOST", default=None)
    and config("EMAIL_HOST_USER", default=None)
    and config("EMAIL_HOST_PASSWORD", default=None)
):
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = config("EMAIL_HOST")
    EMAIL_PORT = config("EMAIL_POST", default=587)
    EMAIL_HOST_USER = config("EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")

# Rollbar error tracking
# Celery config for Rollbar is in celery.py
if config("ROLLBAR_ACCESS_TOKEN"):
    ROLLBAR = {
        "access_token": config("ROLLBAR_ACCESS_TOKEN"),
        "environment": config("ROLLBAR_ENVIRONMENT", default="production"),
        "root": BASE_DIR,  # noqa
    }
    import rollbar

    rollbar.init(**ROLLBAR)
