# Generated by Django 3.2.12 on 2022-04-05 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workerTree', '0003_auto_20220405_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workers',
            name='boss',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='workerTree.workers'),
        ),
        migrations.AlterField(
            model_name='workers',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='workers',
            name='salary',
            field=models.IntegerField(verbose_name='salay'),
        ),
    ]
