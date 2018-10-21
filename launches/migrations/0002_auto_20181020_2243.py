# Generated by Django 2.1.2 on 2018-10-20 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ports', '0003_auto_20181020_2042'),
        ('launches', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='launch',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='launch',
            name='lng',
        ),
        migrations.RemoveField(
            model_name='launch',
            name='location',
        ),
        migrations.AddField(
            model_name='launch',
            name='destination',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='launch',
            name='payload',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='launch',
            name='port',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ports.Port'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='launch',
            name='when',
            field=models.DateTimeField(default='2018-12-31'),
            preserve_default=False,
        ),
    ]