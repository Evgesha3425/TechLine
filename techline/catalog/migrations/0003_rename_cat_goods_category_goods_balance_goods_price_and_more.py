# Generated by Django 4.1.7 on 2023-04-09 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_good_category_options_alter_goods_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goods',
            old_name='cat',
            new_name='category',
        ),
        migrations.AddField(
            model_name='goods',
            name='balance',
            field=models.IntegerField(default=0, verbose_name='Остаток'),
        ),
        migrations.AddField(
            model_name='goods',
            name='price',
            field=models.FloatField(default=0, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='good_category',
            name='name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Название категории'),
        ),
    ]
