# Generated by Django 4.0.5 on 2022-11-11 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_autor_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='email',
            field=models.EmailField(blank=True, max_length=200, null=True),
        ),
    ]