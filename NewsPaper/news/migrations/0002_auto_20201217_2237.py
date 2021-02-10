# Generated by Django 3.1.4 on 2020-12-17 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(blank=True, null=True, through='news.PostCategory', to='news.Category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
