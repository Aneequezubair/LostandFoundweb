# Generated by Django 3.2.7 on 2021-09-17 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_alter_founditems_found_item_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='founditems',
            name='Found_Item_img',
            field=models.ImageField(default='', upload_to='media/items/image'),
        ),
    ]
