# Generated by Django 3.2.10 on 2021-12-27 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translate', '0003_alter_language_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(choices=[(None, 'Choose Language'), ('en', 'en'), ('fr', 'fr')], max_length=254),
        ),
    ]
