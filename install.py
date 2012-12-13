'''
Attempt #1 at trying to automate the initial 
configurations needed to get the server up and running.

Damn you manage.py and your interactive python!
'''

import os
import sys

# Initial database construction
os.system("python manage.py syncdb")

# Database configuration
os.system("python manage.py shell")

# sys.stdout.write("from django.contrib.sites.models import Site")
# os.system('echo	"Site.objects.create(name=\'example.com\', domain=\'example.com\'"')
# os.system('echo "exit()"')

