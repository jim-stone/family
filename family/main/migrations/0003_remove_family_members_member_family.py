# Generated by Django 4.2 on 2024-03-13 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_family_options_alter_member_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='family',
            name='members',
        ),
        migrations.AddField(
            model_name='member',
            name='family',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='members', to='main.family'),
        ),
    ]
