# Generated by Django 5.1.1 on 2024-11-19 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbdmsapp', '0028_alter_customuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(2, 'donor'), (3, 'requester'), (1, 'admin')], default=1, max_length=50),
        ),
    ]
