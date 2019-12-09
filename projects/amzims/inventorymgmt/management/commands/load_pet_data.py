from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from inventorymgmt.models import Inventory
from pytz import UTC


#DATETIME_FORMAT = '%m/%d/%Y %H:%M'

# KEYPAIR_NAMES = [
#     'test123',
#     'mytest123',
#     'test567',
#     'test888',
#     'Linuxkey',
#     'Windowskey',
#     'Fedorakey'
# ]

ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the pet data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from instances.csv into our InvetoryList model"

    def handle(self, *args, **options):
        if Inventory.objects.exists():
            print('Inventory List already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return

        print("Creating Inventory data")

        print("Loading Inventory data for Inventory available for AWS")
        for row in DictReader(open('./instances.csv')):
            inventorylist = Inventory()
            inventorylist.instanceid = row['instanceid']
            inventorylist.instancetype = row['instancetype']
            inventorylist.amiid = row['amiid']
            inventorylist.instancestatus = row['instancestatus']
            inventorylist.az = row['az']
            inventorylist.privateip = row['privateip']
            inventorylist.privatednsname = row['privatednsname']
            inventorylist.publicdnsname = row['publicdnsname']
            inventorylist.publicip = row['publicip']
            inventorylist.keypair = row['keypair']
            inventorylist.save()
