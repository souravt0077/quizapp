# Generated by Django 4.1.7 on 2023-02-19 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='quizModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=250, null=True)),
                ('option1', models.CharField(max_length=250, null=True)),
                ('option2', models.CharField(max_length=250, null=True)),
                ('option3', models.CharField(max_length=250, null=True)),
                ('option4', models.CharField(max_length=250, null=True)),
                ('ans', models.CharField(max_length=250, null=True)),
            ],
        ),
    ]
