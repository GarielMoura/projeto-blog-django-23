# Generated by Django 4.2.11 on 2024-03-19 13:16

from django.db import migrations, models
import utils.model_validators


class Migration(migrations.Migration):

    dependencies = [
        ('site_setup', '0004_menulink_site_setup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesetup',
            name='favicon',
            field=models.ImageField(
                blank=True, default='',
                upload_to='assets/favicon/%Y/%m/',
                validators=[utils.model_validators.validate_png]),
        ),
    ]
