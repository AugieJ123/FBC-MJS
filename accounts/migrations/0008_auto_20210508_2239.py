# Generated by Django 3.1.8 on 2021-05-08 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20210506_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationform',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=19),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='have_you_servered_in_any_islamic_organization',
            field=models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default='No', max_length=4),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='islamic_knowledge',
            field=models.CharField(choices=[('None', 'None'), ('Basic', 'Basic'), ('Intermediate', 'Intermediate')], default='None', max_length=12),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='marital_status',
            field=models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorce', 'Divorce')], default='Single', max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='organization_1',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='organization_2',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='organization_3',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='organization_address_1',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='organization_address_2',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='organization_address_3',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]