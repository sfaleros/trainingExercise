# Generated by Django 3.2.12 on 2022-04-05 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workerTree', '0004_auto_20220405_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workers',
            name='boss',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='workerTree.workers'),
        ),
    ]
