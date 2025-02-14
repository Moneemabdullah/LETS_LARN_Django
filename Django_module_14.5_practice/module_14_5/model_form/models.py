from django.db import models

class MyModel(models.Model):
    auto_field = models.IntegerField(primary_key=True)
    big_integer_field = models.BigIntegerField(default=690)
    # binary_field = models.BinaryField(default=b'')
    char_field = models.CharField(max_length=255, default='')
    number = models.IntegerField(default=0)
    agreed = models.BooleanField(default=False)
    name = models.CharField(max_length=50, default='')
    # published = models.DateTimeField(default=None)
    email = models.EmailField(default='')
    ip_address = models.GenericIPAddressField(default='0.0.0.0')
    price = models.PositiveBigIntegerField(default=0)
    slug = models.SlugField(default='')
    # time_in_day = models.TimeField(default=None)
    url = models.URLField(default='')
    # json_field = models.JSONField(default=dict)
    
    def __str__(self) -> str:
        return f'{self.name}'
