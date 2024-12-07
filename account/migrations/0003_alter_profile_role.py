# Generated by Django 5.1.2 on 2024-12-03 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_profile_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('performer', 'Performer'), ('judge', 'Judge')], max_length=10),
        ),
    ]