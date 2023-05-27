# Generated by Django 4.2.1 on 2023-05-27 22:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('guitar', '0008_user_email_user_username_alter_user_rol'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
        migrations.AddField(
            model_name='rol',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]