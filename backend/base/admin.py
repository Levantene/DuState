from django.contrib import admin

from .models import (
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

admin.site.register(RealEstate)
admin.site.register(PropertyType)
admin.site.register(RoomsNumber)
admin.site.register(AreaName)
admin.site.register(MasterProject)
admin.site.register(ProjectName)
admin.site.register(BuildingName)
admin.site.register(TransactionGroup)
admin.site.register(PropertyUsage)
admin.site.register(RegistrationType)
