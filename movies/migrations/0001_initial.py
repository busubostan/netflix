# Generated by Django 4.2.1 on 2023-06-10 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filmismi', models.CharField(max_length=100, verbose_name='Film Adi')),
                ('aciklama', models.TextField(max_length=400, verbose_name='Film Aciklamasi')),
                ('afis', models.FileField(blank=True, null=True, upload_to='afisler', verbose_name='Film Afişi')),
            ],
        ),
    ]
