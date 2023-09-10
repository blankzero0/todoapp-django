from .base import *
from .base_proxied_https import *

import os


SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
DEBUG = False
ALLOWED_HOSTS = [os.environ['HOST']]
