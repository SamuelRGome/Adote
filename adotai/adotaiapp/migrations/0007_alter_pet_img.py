# Generated by Django 5.0.3 on 2024-05-23 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adotaiapp', '0006_alter_pet_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='Img',
            field=models.ImageField(upload_to='static/imagens/imgpets'),
        ),
    ]
