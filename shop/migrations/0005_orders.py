# Generated by Django 4.1.7 on 2023-03-29 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(default='', max_length=5000)),
                ('name', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('phone', models.CharField(default='', max_length=50)),
                ('address', models.CharField(default='', max_length=100)),
                ('city', models.CharField(default='', max_length=20)),
                ('state', models.CharField(default='', max_length=20)),
                ('zip_code', models.CharField(default='', max_length=20)),
            ],
        ),
    ]
