# Generated by Django 3.1.8 on 2021-05-04 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210504_0438'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrationform',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=19),
        ),
        migrations.AddField(
            model_name='registrationform',
            name='have_you_servered_in_any_islamic_organization',
            field=models.CharField(choices=[('no', 'No'), ('yes', 'Yes')], default='no', max_length=4),
        ),
        migrations.AddField(
            model_name='registrationform',
            name='islamic_knowledge',
            field=models.CharField(choices=[('none', 'None'), ('basic', 'Basic'), ('intermediate', 'Intermediate')], default='none', max_length=12),
        ),
        migrations.AddField(
            model_name='registrationform',
            name='marital_status',
            field=models.CharField(choices=[('single', 'Single'), ('married', 'Married'), ('divorce', 'Divorce')], default='single', max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='organization_1',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='position_held_1',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='position_held_2',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='position_held_3',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
