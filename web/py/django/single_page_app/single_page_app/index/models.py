from django.db import models

# class Person(models.Model):
#    first_name = models.CharField(max_length=30)
#    last_name = models.CharField(max_length=30)
#
#
# class Musician(models.Model):
#    SHIRT_SIZES = (
#        ('S', 'Small'),
#        ('M', 'Medium'),
#        ('L', 'Large'),
#    )
#    id = models.BigAutoField(primary_key=True)
#    first_name = models.CharField(max_length=50)
#    person = models.ForeignKey(
#        Person,
#        on_delete=models.CASCADE,
#        verbose_name="the related person",
#    )
#    MedalType = models.TextChoices('MedalType', 'GOLD SILVER BRONZE')
#    medal = models.CharField(
#        blank=True, choices=MedalType.choices, max_length=10)
#    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
