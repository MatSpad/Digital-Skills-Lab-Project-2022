# Generated by Django 4.0.5 on 2022-06-19 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_department_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='image',
            field=models.ImageField(default='app/static/uploads/logo_luiss.png', upload_to='app/static/uploads'),
        ),
    ]
