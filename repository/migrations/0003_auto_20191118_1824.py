# Generated by Django 2.2.7 on 2019-11-18 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0002_auto_20191107_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repository',
            name='description',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='repository',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
