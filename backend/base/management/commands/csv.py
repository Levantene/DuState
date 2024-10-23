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
        for row in read_csv('Transactions.csv'):

            # include only Residential deals
            if (row[15] != 'Residential'):
                pass
            ### use 10 and exclude Land and Building and then break Unit into Flat and Townhouse
            # exclude blank property types and include only Flat, Villa, Townhouse
            elif row[13] == '' or row[13] == 0:
                pass
            # exclude blank rooms number, exclude office, shop, single room and include only 1BR-9BR, Studio and Penthouse
            elif (row[36] == ''
                  or row[36] == 0
                  or row[36] == 'Office'
                  or row[36] == 'Shop'
                  or row[36] == 'Single Room'):
                pass

            # exclude blank master projects
            elif row[27] == '' or row[27] == 0:
                pass
            # exclude blank paster projects
            elif row[26] == '' or row[26] == 0:
                pass
            # keep blank building name and use it only for flat component - not applied for villa 
            # elif row[23] == '' or row[23] == 0:
            #     pass

            # condition is not necessary as there is no blanks
            elif row[21] == '' or row[21] == 0:
                pass
            else:
                TransactionGroup.objects.get_or_create(
                    name=row[4]
                )
                PropertyUsage.objects.get_or_create(
                    name=row[15]
                )
                RegistrationType.objects.get_or_create(
                    name=row[18]
                )
                PropertyType.objects.get_or_create(
                    name=row[13]
                )
                RoomsNumber.objects.get_or_create(
                    name=row[36]
                )
                AreaName.objects.get_or_create(
                    name=row[21]
                )
                MasterProject.objects.get_or_create(
                    name=row[27]
                )
                ProjectName.objects.get_or_create(
                    name=row[26]
                )
                BuildingName.objects.get_or_create(
                    name=row[23]
                )

                date = row[7].split('-')

                RealEstate.objects.get_or_create(
                    transaction_id=row[0],
                    transaction_date=f'{date[2]}-{date[1]}-{date[0]}',
                    building_name=BuildingName.objects.get(name=row[23]),
                    object_price=row[39],
                    object_size=row[38],
                    area_name=AreaName.objects.get(name=row[21]),
                    master_project=MasterProject.objects.get(name=row[27]),
                    project_name=ProjectName.objects.get(name=row[26]),
                    property_type=PropertyType.objects.get(name=row[13]),
                    rooms_number=RoomsNumber.objects.get(name=row[36]),

                    transaction_group=TransactionGroup.objects.get(
                        name=row[4]),
                    property_usage=PropertyUsage.objects.get(
                        name=row[15]),
                    registration_type=RegistrationType.objects.get(
                        name=row[18]),
                )
            print(trans_id)
            trans_id += 1
