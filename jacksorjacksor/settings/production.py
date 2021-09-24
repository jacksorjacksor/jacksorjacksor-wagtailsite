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

HCAPTCHA_SITEKEY = "adfdf8e1-ab50-4853-ae70-1579532b0a77"
HCAPTCHA_SECRET = "0xa4d4d0eD872D985d6788591627b134339486b156"
