# Generated by Django 4.0.5 on 2022-06-20 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('subject', models.CharField(max_length=100, verbose_name='subject')),
                ('massage', models.TextField(verbose_name='massage')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('reviewed', models.BooleanField(default=False, verbose_name='reviewed')),
            ],
            options={
                'verbose_name': 'ContactUs',
                'verbose_name_plural': 'ContactUs',
                'db_table': 'contact_us',
                'ordering': ['-reviewed', '-created'],
            },
        ),
    ]