# Generated by Django 4.1.2 on 2022-10-27 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0007_remove_lyric_tag2_lyric_artiste_id_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Lyric',
        ),
    ]