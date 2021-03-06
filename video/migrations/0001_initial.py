# Generated by Django 4.0.5 on 2022-06-20 06:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfigVideoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty_most_views', models.PositiveSmallIntegerField(help_text='Number of videos in the most viewed.', verbose_name='Most viewed')),
                ('qty_video_in_page', models.PositiveSmallIntegerField(help_text='Number of videos in the every page.', verbose_name='Every Page')),
                ('status', models.CharField(blank=True, choices=[('p', 'publish'), (None, 'draft')], max_length=9, null=True, unique=True, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'config',
                'verbose_name_plural': 'configs',
                'db_table': 'video_config',
            },
        ),
        migrations.CreateModel(
            name='VideoPostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_video', models.CharField(max_length=100, verbose_name='Title video')),
                ('title_video_en', models.CharField(max_length=100, null=True, verbose_name='Title video')),
                ('title_video_fa', models.CharField(max_length=100, null=True, verbose_name='Title video')),
                ('slug_video', models.SlugField(allow_unicode=True, unique=True, verbose_name='Slug video')),
                ('description_video', models.TextField(verbose_name='Description video')),
                ('description_video_en', models.TextField(null=True, verbose_name='Description video')),
                ('description_video_fa', models.TextField(null=True, verbose_name='Description video')),
                ('poster_video', models.ImageField(upload_to='video/poster/%Y/%m', verbose_name='Poster Video')),
                ('video', models.FileField(upload_to='video/video/%Y/%m', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])], verbose_name='Video')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('is_important_video', models.BooleanField(default=False, verbose_name='Important videos')),
                ('position', models.CharField(blank=True, choices=[(None, '-'), ('0', 'Main'), ('1', 'subsidiary1'), ('2', 'subsidiary2'), ('3', 'subsidiary3'), ('4', 'subsidiary4')], max_length=8, null=True, unique=True, verbose_name='Position')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('category', models.ManyToManyField(related_name='video', to='base.categorymodel', verbose_name='Category')),
                ('ip_address', models.ManyToManyField(blank=True, editable=False, to='base.ipaddressmodel', verbose_name='Visit')),
            ],
            options={
                'verbose_name': 'News movie',
                'verbose_name_plural': 'News movies',
                'db_table': 'video_post',
                'ordering': ['status', '-created'],
            },
        ),
    ]
