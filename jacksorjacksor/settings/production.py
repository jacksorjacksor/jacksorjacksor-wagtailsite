from jacksorjacksor.settings.dev_1 import ALLOWED_HOSTS, SECRET_KEY
from .base import *

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
