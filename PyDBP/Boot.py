"""
WSGI config for FarmaApp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/

Author: Carlos Eduardo da Silva <carlosedasilva@gmail.com>
"""

import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('/Users/carlosdasilva/Documents/Google Drive/PROJETOS/web/p/pydbp/.virtualenvs/lib/python3.7/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('/Users/carlosdasilva/Documents/Google Drive/PROJETOS/web/p/pydbp/apps_wsgi')
sys.path.append('/Users/carlosdasilva/Documents/Google Drive/PROJETOS/web/p/pydbp/apps_wsgi/PyDBP')

# Defing the Django settings path
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PyDBP.settings')

# Activate your virtual env
# - Check if this part of the code is really necessary. 
#activate_env=os.path.expanduser("~/.virtualenvs/myprojectenv/bin/activate_this.py")
#execfile(activate_env, dict(__file__=activate_env))

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()