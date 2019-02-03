# Generated by Django 2.1.1 on 2019-02-03 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personsapp', '0003_person_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='scan',
            field=models.FileField(blank=True, null=True, upload_to='files/'),
        ),
        migrations.AlterField(
            model_name='person',
            name='start_education',
            field=models.DateField(),
        ),
    ]