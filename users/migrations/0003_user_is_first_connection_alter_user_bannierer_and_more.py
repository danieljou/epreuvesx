# Generated by Django 4.1 on 2022-08-10 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_bannierer_user_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_first_connection',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='bannierer',
            field=models.ImageField(blank=True, upload_to='user_banner', verbose_name='Bannière'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_professeur',
            field=models.BooleanField(default=True, verbose_name='Professeur'),
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, upload_to='user_profile', verbose_name='Avatar'),
        ),
    ]