# Generated by Django 3.1.4 on 2020-12-19 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_auto_20201219_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='article_or_news',
            field=models.CharField(choices=[('AR', 'Статья'), ('NE', 'Новость')], default='AR', max_length=2),
        ),
    ]
