from django.db import models
# Create your models here.
class Task(models.Model):
    CATEGORY_CHOICES = [
    ('Personal', 'Pessoal'),
    ('Work', 'Trabalho'),
    ('Education', 'Educação'),
]
    name = models.CharField(max_length=255)
    category = models.CharField(
        max_length=50, 
        choices=CATEGORY_CHOICES,   # efinindo o valor padrão
        )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
