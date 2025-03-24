# Generated by Django 5.1.1 on 2025-03-24 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbdmsapp', '0052_alter_customuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(1, 'admin'), (3, 'requester'), (2, 'donor')], default=1, max_length=50),
        ),
    ]
