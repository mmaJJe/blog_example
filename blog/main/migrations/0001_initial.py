# Generated by Django 3.0.8 on 2020-07-30 07:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=10)),
                ('content', models.TextField()),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
