# Generated by Django 2.2.1 on 2019-06-23 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('users', '0003_auto_20190623_1536'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Entrepreneur',
            new_name='EntrepreneurProfile',
        ),
    ]
