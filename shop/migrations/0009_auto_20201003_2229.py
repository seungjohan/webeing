# Generated by Django 3.1 on 2020-10-03 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20201003_2150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='restaurant',
        ),
        migrations.AddField(
            model_name='register',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Registers', to='shop.product'),
        ),
    ]