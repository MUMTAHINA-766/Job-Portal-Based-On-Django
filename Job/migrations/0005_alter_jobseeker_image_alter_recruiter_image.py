# Generated by Django 4.1.7 on 2023-04-13 07:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_apply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobseeker',
            name='image',
            field=models.FileField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recruiter',
            name='image',
            field=models.FileField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]