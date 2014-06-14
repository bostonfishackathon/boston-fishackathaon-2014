import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'ffv.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

path = '/home/ubuntu/boston-fishackathaon-2014/surveytool/'
if path not in sys.path:
    sys.path.append(path)
