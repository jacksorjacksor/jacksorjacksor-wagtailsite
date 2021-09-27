from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-#$s)ra8cc%nz3-o7+qq&wsy!=$4xkaf)i1=@#k5zkhhi+d!6$u"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass

### PA:
"""
PA un; jacksorjacksor
PA sudo password:y&@qLDq$5?&e$DFM

"""
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "jacksorjacksor",  # db name
        "USER": "jacksorjacksor",  # username
        "PASSWORD": "root",  # pw (how to set this privately when deployed?)
        "HOST": "127.0.0.1",
        "PORT": "5433",  # specifically 5433, not 5432
    }
}
