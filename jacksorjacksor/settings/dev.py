from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("LOCAL_SECRET_KEY")  ###

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("LOCAL_NAME"),  # db name    ###
        "USER": os.getenv("LOCAL_USER"),  # username   ###
        "PASSWORD": os.getenv("LOCAL_PASSWORD"),  ### pw
        "HOST": os.getenv("LOCAL_HOST"),  ###
        "PORT": os.getenv("LOCAL_PORT"),  ###
    }
}

# print(DATABASES["default"])
