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


class DecimalRangeField(models.DecimalField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value = min_value
        self.max_value = max_value
        models.DecimalField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(DecimalRangeField, self).formfield(**defaults)