# Generated by Django 4.2 on 2024-03-16 18:26

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_family_members_member_family'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='assessment',
            options={'ordering': ['-created_on']},
        ),
        migrations.AddField(
            model_name='assessment',
            name='created_on',
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='member',
            name='family',
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE,
                related_name='members', to='main.family'),
            preserve_default=False,
        ),
    ]
