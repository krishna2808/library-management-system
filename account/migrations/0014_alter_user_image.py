# Generated by Django 4.0 on 2024-02-03 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_alter_user_image_delete_friend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/account/2024-02-03 08:15:08.497473/'),
        ),
    ]
