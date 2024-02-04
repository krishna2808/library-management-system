# Generated by Django 4.0 on 2024-02-03 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0013_alter_user_image_delete_friend'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('data_of_publish', models.DateTimeField(auto_now=True)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('auther', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_auther', to='account.user')),
            ],
        ),
        migrations.CreateModel(
            name='BookCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(blank=True, max_length=100, null=True)),
                ('modifed_datetime', models.DateTimeField(auto_now=True)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='LibraryRule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=300)),
                ('amount_fine', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BookBorrower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_datetime', models.DateTimeField()),
                ('return_datetime', models.DateTimeField()),
                ('is_return', models.BooleanField(default=False)),
                ('modified_datetime', models.DateTimeField(auto_now=True)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('amount_fine', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='library_rule_book', to='lms.libraryrule')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='book_borrower', to='lms.book')),
                ('borrow_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='book_borrower_user', to='account.user')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_category', to='lms.bookcategory'),
        ),
    ]