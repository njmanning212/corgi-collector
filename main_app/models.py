from django.db import models
from django.urls import reverse

MEALS = (
  ('B', 'Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner')
)

class Corgi(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
      return self.name
    
    def get_absolute_url(self):
      return reverse('corgi-detail', kwargs={'corgi_id': self.id})

class Feeding(models.Model):
    date = models.DateField('Feeding date')
    meal = models.CharField(
      max_length=1,
      choices=MEALS,
      default=MEALS[0][0]
    )

    corgi = models.ForeignKey(Corgi, on_delete=models.CASCADE)

    def __str__(self):
      return f"{self.get_meal_display()} on {self.date}"

    class Meta:
      ordering = ['-date']