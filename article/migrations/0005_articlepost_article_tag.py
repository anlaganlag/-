# Generated by Django 3.0 on 2020-02-07 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepost',
            name='article_tag',
            field=models.ManyToManyField(blank=True, related_name='article_tag', to='article.ArticleTag'),
        ),
    ]
