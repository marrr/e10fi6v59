# Generated by Django 3.2.4 on 2021-07-08 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateur', '0004_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='avatars/default.jpg', upload_to='avatars'),
        ),
    ]
