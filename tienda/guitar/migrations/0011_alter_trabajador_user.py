# Generated by Django 4.2.1 on 2023-05-27 22:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('guitar', '0010_rename_rol_trabajador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabajador',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
