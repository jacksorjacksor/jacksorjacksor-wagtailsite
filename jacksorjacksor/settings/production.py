from jacksorjacksor.settings.dev import ALLOWED_HOSTS_FOR_PROD, SECRET_KEY_FOR_PROD
from .base import *

ALLOWED_HOSTS = ALLOWED_HOSTS_FOR_PROD
SECRET_KEY = SECRET_KEY_FOR_PROD

DEBUG = False

try:
    from .local import *
except ImportError:
    pass

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "jacksorjacksor",
        "USER": "jacksorjacksor",
        "PASSWORD": "y&@qLDq$5?&e$DFM",
        "HOST": "jacksorjacksor-119.postgres.eu.pythonanywhere-services.com",
        "PORT": 10119,
    }
}
