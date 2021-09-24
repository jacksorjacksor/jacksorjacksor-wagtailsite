from jacksorjacksor.settings.dev import ALLOWED_HOSTS, SECRET_KEY
from .base import *

DEBUG = False

SECRET_KEY = "hrad1^10y^r+ne_l1p96()@d46=58-k&7+$c+zt)d-55uwh%ij"

ALLOWED_HOSTS = [
    "jacksorjacksor.eu.pythonanywhere.com",
    "www.jacksorjacksor.xyz",
    "jacksorjacksor.xyz",
]
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
