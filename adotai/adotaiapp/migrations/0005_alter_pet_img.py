# Generated by Django 5.0.6 on 2024-05-17 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adotaiapp', '0004_alter_pet_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='Img',
            field=models.ImageField(blank=True, null=True, upload_to='djangouploads/files/covers'),
        ),
    ]
