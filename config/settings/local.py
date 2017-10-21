from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY', default='ubw$_z9uq^+ccz24musiaxb-ga9bo2p1dux^_%@ea=045z263-')
DEBUG = env.bool('DJANGO_DEBUG', default=True)
