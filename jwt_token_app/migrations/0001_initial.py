# Generated by Django 3.1.5 on 2021-04-04 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.IntegerField()),
                ('book_name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollnumber', models.IntegerField()),
                ('std_name', models.CharField(max_length=120)),
                ('std_class', models.CharField(max_length=120)),
                ('joining_date', models.DateField()),
                ('lib', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jwt_token_app.library')),
            ],
        ),
    ]
