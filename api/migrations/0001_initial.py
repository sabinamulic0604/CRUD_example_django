# Generated by Django 4.1.3 on 2022-12-14 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lokacija',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lokacijaName', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proizvod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proizvodName', models.CharField(max_length=100)),
                ('datum_dodavanja', models.DateField(auto_now_add=True)),
                ('lokacijaProizvoda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.lokacija')),
            ],
        ),
    ]
