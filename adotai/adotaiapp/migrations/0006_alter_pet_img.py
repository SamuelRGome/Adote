# Generated by Django 5.0.6 on 2024-05-18 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adotaiapp', '0005_alter_pet_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='Img',
            field=models.ImageField(upload_to='djangouploads/files/covers'),
        ),
    ]
