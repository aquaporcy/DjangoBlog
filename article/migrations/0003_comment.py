# Generated by Django 3.0.6 on 2020-06-18 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20200611_1326'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_author', models.CharField(max_length=30, verbose_name='Name')),
                ('comment_content', models.CharField(max_length=200, verbose_name='Comment')),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='article.Article', verbose_name='Article')),
            ],
        ),
    ]
