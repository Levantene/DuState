import os
import csv
from pathlib import Path

from django.core.management.base import BaseCommand

from base.models import (
    RealEstate,
    PropertyType,
    RoomsNumber,
    AreaName,
    MasterProject,
    ProjectName,
    BuildingName,
    TransactionGroup,
    PropertyUsage,
    RegistrationType
)
# BASE_DIR = Path(__file__).resolve().parent.parent
STATICFILES_DIRS = "/home/levantene/dxbstates/backend/static/"


def read_csv(name):
    reader = csv.reader(open(
        os.path.join(
            STATICFILES_DIRS,
            'data',
            name),
        'r', encoding='utf-8'), delimiter=',')
    next(reader)
    return reader


class Command(BaseCommand):
    def handle(self, *args, **options):
        trans_id = 0
        for row in read_csv('transactions-clean.csv'):

            TransactionGroup.objects.get_or_create(
                name=row[5]
            )
            PropertyUsage.objects.get_or_create(
                name=row[16]
            )
            RegistrationType.objects.get_or_create(
                name=row[19]
            )
            PropertyType.objects.get_or_create(
                name=row[14]
            )
            RoomsNumber.objects.get_or_create(
                name=row[37]
            )
            AreaName.objects.get_or_create(
                name=row[22]
            )
            MasterProject.objects.get_or_create(
                name=row[28]
            )
            ProjectName.objects.get_or_create(
                name=row[27]
            )
            BuildingName.objects.get_or_create(
                name=row[24]
            )

            date = row[8].split('-')

            RealEstate.objects.get_or_create(
                transaction_id=row[1],
                transaction_date=f'{date[0]}-{date[1]}-{date[2]}',
                building_name=BuildingName.objects.get(name=row[24]),
                object_price=row[40],
                object_size=row[39],
                area_name=AreaName.objects.get(name=row[22]),
                master_project=MasterProject.objects.get(name=row[28]),
                project_name=ProjectName.objects.get(name=row[27]),
                property_type=PropertyType.objects.get(name=row[14]),
                rooms_number=RoomsNumber.objects.get(name=row[37]),

                transaction_group=TransactionGroup.objects.get(
                    name=row[5]),
                property_usage=PropertyUsage.objects.get(
                    name=row[16]),
                registration_type=RegistrationType.objects.get(
                    name=row[19]),
            )
            print(trans_id)
            trans_id += 1
        print('-----------------------------------------')
        print('THE DATA IS UPLOADED')
        print('-----------------------------------------')
