# Generated by Django 3.0.8 on 2020-07-31 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obodo', '0030_auto_20200731_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestofferpost',
            name='post_image',
            field=models.ImageField(default='default.jpg', upload_to='images'),
        ),
    ]
