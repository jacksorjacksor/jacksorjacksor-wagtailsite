from .base import *

ALLOWED_HOSTS = [
    "jacksorjacksor.eu.pythonanywhere.com",
    "www.jacksorjacksor.xyz",
    "jacksorjacksor.xyz",
]
SECRET_KEY = os.getenv("REMOTE_SECRET_KEY")  ###

DEBUG = False

try:
    from .local import *
except ImportError:
    pass

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("REMOTE_NAME"),  ###
        "USER": os.getenv("REMOTE_USER"),  ###
        "PASSWORD": os.getenv("REMOTE_PASSWORD"),  ###
        "HOST": os.getenv("REMOTE_HOST"),  ###
        "PORT": 10119,  ###
    }
}
