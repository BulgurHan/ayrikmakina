# Generated by Django 4.0.3 on 2022-11-18 14:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('page', '0004_not'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=50)),
                ('konu', models.CharField(max_length=200)),
                ('goruldu', models.BooleanField(default=False)),
                ('alici', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('konu', models.CharField(max_length=500)),
                ('goruldu', models.BooleanField(default=False)),
                ('alici', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Alıcı', to=settings.AUTH_USER_MODEL)),
                ('gonderen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Gönderen', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
