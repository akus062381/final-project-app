# Generated by Django 3.0.8 on 2020-07-20 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('obodo', '0004_photo_member'),
        ('users', '0003_auto_20200720_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='obodo.Photo'),
        ),
    ]
