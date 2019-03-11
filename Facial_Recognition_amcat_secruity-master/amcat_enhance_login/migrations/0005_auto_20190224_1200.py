# Generated by Django 2.0.6 on 2019-02-24 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amcat_enhance_login', '0004_auto_20190224_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amcat_login_with_face_tracker',
            name='course',
            field=models.CharField(choices=[('btech', 'B-Tech'), ('bcom', 'B-Com'), ('mba', 'MBA')], default='btech', max_length=10),
        ),
        migrations.AlterField(
            model_name='amcat_login_with_face_tracker',
            name='model_pic',
            field=models.ImageField(upload_to='pic_folder/'),
        ),
    ]
