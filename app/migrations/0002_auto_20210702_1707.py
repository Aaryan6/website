# Generated by Django 3.2.4 on 2021-07-02 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='htmldata',
            name='css_code',
            field=models.TextField(default='', max_length=999999999),
        ),
        migrations.AlterField(
            model_name='htmldata',
            name='html_code',
            field=models.TextField(default='', max_length=999999999),
        ),
        migrations.AlterField(
            model_name='htmldata',
            name='js_code',
            field=models.TextField(default='', max_length=999999999),
        ),
    ]