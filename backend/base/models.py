from django.db import models
# https://django-import-export.readthedocs.io/en/stable/advanced_usage.html


class TransactionGroup(models.Model):
    name = models.CharField(
        'TransactionGroup',
        max_length=200,
        blank=False
    )

    def __str__(self):
        return self.name


class PropertyUsage(models.Model):
    name = models.CharField(
        'PropertyUsage',
        max_length=200,
        blank=False
    )

    def __str__(self):
        return self.name


class RegistrationType(models.Model):
    name = models.CharField(
        'RegistrationType',
        max_length=200,
        blank=False
    )

    def __str__(self):
        return self.name


class PropertyType(models.Model):
    name = models.CharField(
        'Propery Type',
        max_length=200,
        blank=False
    )

    def __str__(self):
        return self.name


class RoomsNumber(models.Model):
    name = models.CharField(
        'Number of Rooms',
        max_length=200,
        blank=False
    )

    def __str__(self):
        return self.name


class AreaName(models.Model):
    name = models.CharField(
        'Area Name',
        max_length=200,
        blank=False
    )

    def __str__(self):
        return self.name


class MasterProject(models.Model):
    name = models.CharField(
        'Master Project',
        max_length=200,
        blank=False
    )

    def __str__(self):
        return self.name


class ProjectName(models.Model):
    name = models.CharField(
        'Project Name',
        max_length=200,
        blank=False
    )

    def __str__(self):
        return self.name    


class BuildingName(models.Model):
    name = models.CharField(
        'Building Name',
        max_length=200,
        blank=False
    )

    def __str__(self):
        return self.name


class RealEstate(models.Model):
    transaction_id = models.CharField(
        'Transaction ID',
        max_length=200,
        blank=False
    )
    transaction_date = models.DateField(
        'Transaction Date',
    )
    transaction_group = models.ForeignKey(
        TransactionGroup,
        on_delete=models.CASCADE
    )
    property_usage = models.ForeignKey(
        PropertyUsage,
        on_delete=models.CASCADE
    )
    registration_type = models.ForeignKey(
        RegistrationType,
        on_delete=models.CASCADE
    )
    building_name = models.ForeignKey(
        BuildingName,
        on_delete=models.CASCADE
    )
    object_price = models.FloatField(
        'Object Price',
        null=True,
        blank=True
    )
    object_size = models.FloatField(
        'Object Size',
        null=True,
        blank=True
    )
    area_name = models.ForeignKey(
        AreaName,
        on_delete=models.CASCADE
    )
    master_project = models.ForeignKey(
        MasterProject,
        on_delete=models.CASCADE
    )
    project_name = models.ForeignKey(
        ProjectName,
        on_delete=models.CASCADE
    )
    property_type = models.ForeignKey(
        PropertyType,
        on_delete=models.CASCADE
    )
    rooms_number = models.ForeignKey(
        RoomsNumber,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.transaction_id

    def get_year(self):
        return self.transaction_date.year

    class Meta:
        ordering = ('-transaction_date',)


# class Yearly_Trend(models.Model):
#     year = models.IntegerField





    # def save(self, *args, **kwargs):
    #     qs_purchase = self.category.purchase_set.all().filter(date__year = self.budget.date.year, date__month = self.budget.date.month)
    #     if qs_purchase.exists():
    #         self.purchase_total = qs_purchase.aggregate(purchase_total = Sum('price'))['purchase_total']
    #     else:
    #         self.purchase_total = 0

    #     self.difference = self.amount - self.purchase_total
    #     return super().save(*args, **kwargs)