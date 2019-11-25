import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'ex2.settings')


import django
django.setup()
settings.configure()

from apptwo.models import USER
from faker import Faker


fakegen =fake()

def populate(N=5):


    for entery in range(N):
        fake_name = fakegen.name.split()
        fake_first_name = fakegen_name[0]
        fake_last_name =fakegen_name[1]
        fake_email = fakegen_email()


user = User.object.get_or_create(
first_name=fake_first_name,
last_name=fake_last_name,
Email = fake_email )

if __name__ == '__main__':
    print("POPULATING DATABASE")
    populate(20)
    print("POPULATING COMPLETE")
