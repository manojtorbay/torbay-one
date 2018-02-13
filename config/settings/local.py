from .base import *
SECRET_KEY = env('DJANGO_SECRET_KEY', default='7bu3l^0ji&a$&hdxgba)vs5h-q0n9y8!!m0ez^=r(g2uc3fv&@')
DEBUG = env.bool('DJANGO_DEBUG', default=True)
