from django.db import models

class Book(models.Model):
    title= models.CharField("Book Name", max_length=255, unique=True)
    description= models.TextField()
    rate= models.IntegerField(default=0)
    views= models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return f"Book: {self.title}"
    