# Generated by Django 4.1.3 on 2022-12-17 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_settings_contact_alter_settings_instagram_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='aboutus',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='settings',
            name='contact',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='settings',
            name='references',
            field=models.TextField(blank=True),
        ),
    ]
