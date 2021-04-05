# Generated by Django 3.1.5 on 2021-04-04 11:44

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('jwt_token_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='userdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.BigIntegerField(max_length=10)),
                ('username', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=6)),
                ('state', models.CharField(max_length=20)),
            ],
            managers=[
                ('obeject', django.db.models.manager.Manager()),
            ],
        ),
    ]