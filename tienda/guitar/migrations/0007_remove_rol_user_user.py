# Generated by Django 4.2.1 on 2023-05-27 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guitar', '0006_alter_rol_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rol',
            name='user',
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guitar.rol')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
