# Generated by Django 4.0.5 on 2022-06-20 06:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_otp.plugins.otp_totp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TOTPDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='name')),
                ('confirmed', models.BooleanField(default=True, verbose_name='confirmed')),
                ('throttling_failure_timestamp', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Last failed attempt')),
                ('throttling_failure_count', models.PositiveIntegerField(default=0, verbose_name='Number of attempts')),
                ('key', models.CharField(default=django_otp.plugins.otp_totp.models.default_key, help_text='40-letter secret key based on hex', max_length=80, validators=[django_otp.plugins.otp_totp.models.key_validator], verbose_name='key')),
                ('step', models.PositiveSmallIntegerField(default=30, help_text='Per second', verbose_name='Validity time')),
                ('t0', models.BigIntegerField(default=0, help_text='In terms of Unix time.', verbose_name='Start time origin')),
                ('digits', models.PositiveSmallIntegerField(choices=[(6, 6), (8, 8)], default=6, verbose_name='Number of digits')),
                ('tolerance', models.PositiveSmallIntegerField(default=1, verbose_name='Number of authorized use')),
                ('drift', models.SmallIntegerField(default=0, help_text='Per second', verbose_name='Permitted delay')),
                ('last_t', models.BigIntegerField(default=-1, help_text='The value of the latest verified token.The next token must be at a higher time step.')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'OTP Device',
                'verbose_name_plural': 'OTP Device',
            },
        ),
    ]
