# Generated by Django 2.2.1 on 2019-06-23 15:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accomplishment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('acc_type', models.CharField(choices=[('Startup', 'Startup'), ('License', 'License'), ('Education', 'Education')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to='portfolio/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Entrepreneur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(blank=True, max_length=100, null=True)),
                ('location', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('email_notif_on', models.BooleanField(default=False)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photo/%Y/%m/%d')),
                ('date_joined', models.DateField(auto_now_add=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('url', models.SlugField(unique=True)),
                ('accomplishnment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Accomplishment')),
                ('portfolio', models.ManyToManyField(blank=True, null=True, to='users.Portfolio')),
                ('skills', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
