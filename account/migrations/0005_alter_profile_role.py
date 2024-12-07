# Generated by Django 5.1.2 on 2024-12-03 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_profile_password_profile_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('performer', 'Performer'), ('judge', 'Judge')], default='performer', max_length=10),
        ),
    ]
