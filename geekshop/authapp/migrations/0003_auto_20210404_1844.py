# Generated by Django 3.1.7 on 2021-04-04 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_auto_20210404_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]