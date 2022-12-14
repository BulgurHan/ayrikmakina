# Generated by Django 4.0.3 on 2022-11-13 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fidelik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=200)),
                ('yetkili', models.CharField(max_length=200)),
                ('tel', models.CharField(max_length=11)),
                ('mail', models.CharField(max_length=200)),
                ('adres', models.CharField(max_length=200)),
                ('mak_sayisi', models.PositiveIntegerField(default=0)),
                ('karistirici', models.CharField(blank=True, max_length=100, null=True)),
                ('makine', models.CharField(blank=True, max_length=200, null=True)),
                ('viyoller', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Urun',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=200)),
                ('fiyat', models.PositiveBigIntegerField()),
                ('kategori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.kategori')),
            ],
        ),
    ]
