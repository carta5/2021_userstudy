# Generated by Django 3.1.2 on 2020-12-06 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userstudy', '0002_prequestionnaireanswer_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='pre_infomation',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='userstudy.description'),
            preserve_default=False,
        ),
    ]
