# Generated by Django 3.0.3 on 2020-03-07 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookversations', '0002_subscribe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='readinglist',
            old_name='book_name',
            new_name='book_title',
        ),
        migrations.RemoveField(
            model_name='readinglist',
            name='book',
        ),
        migrations.AddField(
            model_name='readinglist',
            name='book_image',
            field=models.ImageField(default='https://images-eu.ssl-images-amazon.com/images/I/51JRn3-%2BtuL.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='subscribe',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
