# Generated by Django 4.0.5 on 2022-06-20 06:17

import base.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FooterModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Description footer')),
                ('description_en', models.TextField(null=True, verbose_name='Description footer')),
                ('description_fa', models.TextField(null=True, verbose_name='Description footer')),
                ('tel', models.CharField(max_length=11, validators=[base.validators.tel_validators], verbose_name='Tel')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('logo', models.ImageField(upload_to='footer', verbose_name='Logo')),
                ('status', models.CharField(blank=True, choices=[('p', 'Apply'), (None, 'Draft')], default=None, max_length=9, null=True, unique=True, verbose_name='Status publish')),
            ],
            options={
                'verbose_name': 'Footer',
                'verbose_name_plural': 'Footers',
                'db_table': 'footer',
                'ordering': ['-status'],
            },
        ),
        migrations.CreateModel(
            name='IpAddressModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField()),
            ],
        ),
        migrations.CreateModel(
            name='SocialNetworkModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='Title network')),
                ('title_en', models.CharField(max_length=80, null=True, verbose_name='Title network')),
                ('title_fa', models.CharField(max_length=80, null=True, verbose_name='Title network')),
                ('class_icon', models.CharField(max_length=100, verbose_name='Font awesome class')),
                ('address', models.URLField(unique=True, verbose_name='Address network')),
                ('status', models.BooleanField(default=True, verbose_name='Status publish')),
            ],
            options={
                'verbose_name': 'SocialNetwork',
                'verbose_name_plural': 'SocialNetworks',
                'db_table': 'social_network',
            },
        ),
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug category')),
                ('title', models.CharField(max_length=100, verbose_name='Title category')),
                ('title_en', models.CharField(max_length=100, null=True, verbose_name='Title category')),
                ('title_fa', models.CharField(max_length=100, null=True, verbose_name='Title category')),
                ('positions', models.IntegerField(verbose_name='Category position')),
                ('status', models.BooleanField(default='p', verbose_name='Status published')),
                ('have_children', models.BooleanField(default=False, verbose_name='Have children?')),
                ('publish_in_home', models.BooleanField(default=False, help_text='Publish the latest news of this category on the home page', verbose_name='Publish in home?')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='base.categorymodel', verbose_name='Parent category')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'db_table': 'category',
                'ordering': ['positions', '-status', '-title'],
            },
        ),
    ]
