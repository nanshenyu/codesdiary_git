# Generated by Django 2.0.6 on 2018-06-24 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_article_auther'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='auther',
            new_name='author',
        ),
    ]
