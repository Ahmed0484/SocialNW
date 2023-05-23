# Generated by Django 4.2.1 on 2023-05-22 20:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_A', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_A', to=settings.AUTH_USER_MODEL)),
                ('user_B', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_B', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
