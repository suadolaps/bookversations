# Generated by Django 3.0.3 on 2020-03-07 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookversations', '0004_auto_20200307_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readinglist',
            name='book_image',
            field=models.ImageField(null=True, upload_to='images/book_covers/'),
        ),
    ]
