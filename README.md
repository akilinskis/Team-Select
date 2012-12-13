Team-Select
===========

Team Selection App
===========

How to run a server:

run: "python install.py"

When prompted, enter yes.
Then provide a username, email, and password for admin access
to your local server.

Next, the interactive python shell will be brought up.
Enter the following lines:

from django.contrib.sites.models import Site
Site.objects.create(name='example.com', domain='example.com')
exit()

Then, to actually run the server type: 
"python manage.py runserver"

Go to http://127.0.0.1:8000 in a browser to see your server.
Login using the username and password you set earlier.
