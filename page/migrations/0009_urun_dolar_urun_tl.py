# Generated by Django 4.0.3 on 2022-12-05 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0008_alter_urun_kategori_delete_kategori'),
    ]

    operations = [
        migrations.AddField(
            model_name='urun',
            name='dolar',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='urun',
            name='tl',
            field=models.BooleanField(default=False),
        ),
    ]
