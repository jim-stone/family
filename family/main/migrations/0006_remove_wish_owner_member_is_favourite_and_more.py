# Generated by Django 4.2 on 2024-03-20 18:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0005_member_is_boss_wish'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wish',
            name='owner',
        ),
        migrations.AddField(
            model_name='member',
            name='is_favourite',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='wish',
            name='owner_member',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='my_wishes', to='main.member'),
        ),
        migrations.AddField(
            model_name='wish',
            name='owner_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='my_wishes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='wish',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Created'), (2, 'In Progress'), (3, 'Completed')], db_index=True, default=1),
        ),
    ]