# Generated by Django 3.2.12 on 2022-04-04 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workerTree', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workers',
            name='boss',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='workerTree.workers'),
        ),
    ]
