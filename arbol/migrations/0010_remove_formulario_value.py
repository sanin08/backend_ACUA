# Generated by Django 3.0.6 on 2020-05-29 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arbol', '0009_auto_20200529_1342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formulario',
            name='value',
        ),
    ]
