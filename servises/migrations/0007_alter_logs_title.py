# Generated by Django 4.2.3 on 2023-07-19 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servises', '0006_alter_logs_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logs',
            name='title',
            field=models.CharField(default='<function now at 0x7fd4c85f7a60>', max_length=63, verbose_name='Название'),
        ),
    ]
