# Generated by Django 4.0.5 on 2022-06-20 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='title')),
                ('title_en', models.CharField(max_length=120, null=True, verbose_name='title')),
                ('title_fa', models.CharField(max_length=120, null=True, verbose_name='title')),
                ('image', models.ImageField(upload_to='Photo_news/%Y/%m', verbose_name='image')),
                ('status', models.BooleanField(default=False, verbose_name='status publish')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
            ],
            options={
                'verbose_name': 'Photos',
                'verbose_name_plural': 'Photo',
                'db_table': 'photo',
                'ordering': ['-status', '-created', 'title'],
            },
        ),
        migrations.CreateModel(
            name='PhotoNewsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='title')),
                ('title_en', models.CharField(max_length=120, null=True, verbose_name='title')),
                ('title_fa', models.CharField(max_length=120, null=True, verbose_name='title')),
                ('slug', models.SlugField(allow_unicode=True, max_length=200, unique=True, verbose_name='slug')),
                ('body', models.TextField(verbose_name='body')),
                ('body_en', models.TextField(null=True, verbose_name='body')),
                ('body_fa', models.TextField(null=True, verbose_name='body')),
                ('photo', models.ImageField(upload_to='photo_news/%Y/%m', verbose_name='main photo')),
                ('is_important_photo', models.BooleanField(default=False, verbose_name='important-photo')),
                ('status', models.BooleanField(default=False, verbose_name='status publish')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='created date')),
                ('is_slider_home', models.BooleanField(default=False, verbose_name='Home slider')),
                ('important_photo_home', models.CharField(blank=True, choices=[(None, '-'), ('1', 'important image1'), ('2', 'important image2'), ('3', 'important image3')], max_length=1, null=True, unique=True, verbose_name='Important home photo')),
                ('photographer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='photo_news', to='employee.employeesmodel', verbose_name='photographer')),
                ('sub_photo', models.ManyToManyField(related_name='photo_news', to='photo.photomodel', verbose_name='more photo')),
            ],
            options={
                'verbose_name': 'photo news',
                'verbose_name_plural': 'photo news',
                'db_table': 'photo_news',
                'ordering': ['-status', '-updated', 'photographer'],
            },
        ),
    ]