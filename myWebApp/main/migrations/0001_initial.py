# Generated by Django 3.0.4 on 2020-03-19 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=200)),
                ('productDescription', models.TextField()),
                ('productCost', models.IntegerField()),
                ('datePublished', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
