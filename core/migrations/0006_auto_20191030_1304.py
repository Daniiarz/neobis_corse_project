# Generated by Django 2.2.6 on 2019-10-30 07:04

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20191030_1156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='course',
        ),
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.UUID('f4a471b8-75c4-46c7-90ea-220febc34434'), editable=False),
        ),
    ]
