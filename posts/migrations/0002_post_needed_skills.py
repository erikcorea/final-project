# Generated by Django 3.1.4 on 2020-12-18 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='needed_skills',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]