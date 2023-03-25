"""
WSGI config for corridor_boilerplate project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from helpers.mongodb import MongoConnection
from corridor_boilerplate.settings import MONGODB_CONFIG

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'corridor_boilerplate.settings')

# Startup code that gets executed only once

from pymongo import MongoClient

mdb = MongoConnection()


if MONGODB_CONFIG['database'] not in mdb.getDatabaseList():
    print("Initializing database !")
    mdb.selectDatabase()
    mdb.db.initial_collection.insert_one({'name':'Initial Document for database'})
else:
    print("Database Already Created in MongoDB !")

mdb.close()

# Startup code ends here

application = get_wsgi_application()    


