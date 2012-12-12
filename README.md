Team-Select
===========

Team Selection App

===========

How to run a server:

If you haven't built a db, type: "python manage.py syncdb"
I highly recommend setting up a superuser at this point

For now, run: "python manage.py shell"
then enter these two lines:
from django.contrib.sites.models import Site
Site.objects.create(name='example.com', domain='example.com')
TODO: Put this somewhere it belongs.

Then run: "python manage.py runserver"
Go to http://127.0.0.1:8000 in a browser
