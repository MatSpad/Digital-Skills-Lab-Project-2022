# Generated by Django 4.0.5 on 2022-06-19 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_department_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='image',
            field=models.ImageField(default='img/logo_luiss.png', upload_to='app/up'),
        ),
    ]
