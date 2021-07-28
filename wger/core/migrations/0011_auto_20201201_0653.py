# Generated by Django 3.1.3 on 2020-12-01 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0008_auto_20190618_1617'),
        ('core', '0010_auto_20170403_0144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gym',
            field=models.ForeignKey(
                blank=True,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to='gym.gym'
            ),
        ),
    ]
