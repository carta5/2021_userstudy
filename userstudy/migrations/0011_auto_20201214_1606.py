# Generated by Django 3.1.2 on 2020-12-14 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userstudy', '0010_searchresult_is_public_institute'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskanswer',
            name='url',
            field=models.TextField(),
        ),
    ]
