# Generated by Django 3.2 on 2022-03-30 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designstore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='type_of_design_icon_logo_poster',
            field=models.CharField(max_length=255, null=True),
        ),
    ]