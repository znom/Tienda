# Generated by Django 4.2.1 on 2023-05-28 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guitar', '0012_alter_trabajador_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=60)),
                ('direccion', models.CharField(max_length=100)),
            ],
        ),
    ]