"""
WSGI config for loginSignup project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'loginSignup.settings')

application = get_wsgi_application()

#import os
#from django.core.wsgi import get_wsgi_application

#def get_internal_wsgi_application():
   # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'loginSignup.settings')
    #return get_wsgi_application()

#application = get_internal_wsgi_application()
