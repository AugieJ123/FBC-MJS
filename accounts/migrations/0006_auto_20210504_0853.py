# Generated by Django 3.1.8 on 2021-05-04 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210504_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationform',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]