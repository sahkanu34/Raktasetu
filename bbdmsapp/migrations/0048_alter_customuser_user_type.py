# Generated by Django 5.1.1 on 2024-12-27 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbdmsapp', '0047_alter_customuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(3, 'requester'), (2, 'donor'), (1, 'admin')], default=1, max_length=50),
        ),
    ]
