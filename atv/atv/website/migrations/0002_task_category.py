# Generated by Django 5.1.3 on 2024-11-23 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='category',
            field=models.CharField(choices=[('Personal', 'Pessoal'), ('Work', 'Trabalho'), ('Education', 'Educação')], default='Personal', max_length=50),
        ),
    ]
