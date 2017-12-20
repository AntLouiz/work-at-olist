# Generated by Django 2.0 on 2017-12-20 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('channels', '0002_auto_20171220_1839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='channel',
            name='father',
        ),
        migrations.AddField(
            model_name='channel',
            name='parent_channel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='channels', to='channels.Channel'),
        ),
    ]