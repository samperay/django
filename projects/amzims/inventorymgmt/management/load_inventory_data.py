from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from inventorymgmt.models import InvetoryList, KeyPair
from pytz import UTC


#DATETIME_FORMAT = '%m/%d/%Y %H:%M'

KEYPAIR_NAMES = [
    'test123',
    'mytest123',
    'test567',
    'test888',
    'Linuxkey',
    'Windowskey',
    'Fedorakey'
]

ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the pet data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from instances.csv into our InvetoryList model"

    def handle(self, *args, **options):
        if InvetoryList.objects.exists() or KeyPair.objects.exists():
            print('Inventory List already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        print("Creating Inventory data")
        for keypair_name in KEYPAIR_NAMES:
            keypair = KeyPair(instanceid=keypair_name)
            keypair.save()
        print("Loading Inventory data for Inventory available for AWS")
        for row in DictReader(open('./instances.csv')):
            inventorylist = InvetoryList()
            inventorylist.instanceid = row['instanceid']
            inventorylist.instancetype = row['instancetype']
            inventorylist.amiid = row['amiid']
            inventorylist.instancestatus = row['instancestatus']
            inventorylist.az = row['az']
            inventorylist.privateip = row['privateip']
            inventorylist.privatednsname = row['privatednsname']
            inventorylist.publicdnsname = row['publicdnsname']
            inventorylist.publicip = row['publicip']
            inventorylist.save()

            key_pair_names = row['keypair']
            keypair_names = [name for name in key_pair_names.split('| ') if name]
            for keypair_name in keypair_names:
                key = KeyPair.objects.get(instanceid=keypair_name)
                inventorylist.vaccinations.add(key)
            inventorylist.save()
