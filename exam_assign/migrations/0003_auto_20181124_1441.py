# Generated by Django 2.1.3 on 2018-11-24 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_assign', '0002_examassign_submitted_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examassign',
            name='started_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='examassign',
            name='submitted_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]