# Generated by Django 3.1.2 on 2020-12-06 13:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userstudy', '0004_postquestionnaireanswer_taskanswer'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExitQuestionnaireAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_health_literacy_q1', models.IntegerField(default=0)),
                ('e_health_literacy_q2', models.IntegerField(default=0)),
                ('e_health_literacy_q3', models.IntegerField(default=0)),
                ('e_health_literacy_q4', models.IntegerField(default=0)),
                ('e_health_literacy_q5', models.IntegerField(default=0)),
                ('e_health_literacy_q6', models.IntegerField(default=0)),
                ('e_health_literacy_q7', models.IntegerField(default=0)),
                ('e_health_literacy_q8', models.IntegerField(default=0)),
                ('age', models.IntegerField(default=0)),
                ('sex', models.IntegerField(default=0)),
                ('education', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
