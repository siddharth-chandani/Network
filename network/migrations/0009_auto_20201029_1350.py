# Generated by Django 3.1 on 2020-10-29 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0008_auto_20201029_1123'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='like',
            unique_together={('user', 'comment'), ('user', 'post')},
        ),
    ]
