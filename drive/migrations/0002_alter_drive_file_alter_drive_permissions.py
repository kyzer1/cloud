# Generated by Django 4.0.1 on 2022-01-04 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drive', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drive',
            name='file',
            field=models.FileField(max_length=255, upload_to=''),
        ),
        migrations.AlterField(
            model_name='drive',
            name='permissions',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='drive.profile'),
        ),
    ]
