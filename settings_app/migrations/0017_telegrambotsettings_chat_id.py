# Generated by Django 5.0.6 on 2024-07-26 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings_app', '0016_telegrambotsettings_alter_errortexts_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegrambotsettings',
            name='chat_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Telegramdagi admin Chat ID'),
        ),
    ]