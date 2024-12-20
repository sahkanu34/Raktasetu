# Generated by Django 5.1.1 on 2024-10-01 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbdmsapp', '0019_alter_customuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodrequest',
            name='mobno',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(3, 'requester'), (2, 'donor'), (1, 'admin')], default=1, max_length=50),
        ),
    ]
