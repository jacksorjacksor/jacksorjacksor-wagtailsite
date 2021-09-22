from jacksorjacksor.settings.dev import SECRET_KEY
from .base import *

DEBUG = False

SECRET_KEY = 'hrad1^10y^r+ne_l1p96()@d46=58-k&7+$c+zt)d-55uwh%ij'

try:
    from .local import *
except ImportError:
    pass
