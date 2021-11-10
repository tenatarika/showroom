from django.db import models


class CreatedAt(models.Model):
    added_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UpdatedAt(models.Model):
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SoftDelete(models.Model):
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True