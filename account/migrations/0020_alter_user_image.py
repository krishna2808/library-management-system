# Generated by Django 4.0 on 2024-02-04 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0019_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/account/2024-02-04 18:11:08.418025/'),
        ),
    ]
