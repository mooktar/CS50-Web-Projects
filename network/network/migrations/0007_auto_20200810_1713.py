# Generated by Django 3.0.6 on 2020-08-10 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0006_auto_20200810_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='post',
            field=models.TextField(blank=True, max_length=350, null=True),
        ),
    ]
