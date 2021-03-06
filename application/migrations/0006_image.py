# Generated by Django 2.2.10 on 2021-07-14 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('application', '0005_delete_place_information'),
    ]

    operations = [
        migrations.CreateModel(
            name='image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.ImageField(upload_to='all_images')),
                ('is_background_correct', models.BooleanField()),
                ('is_facemask_exists', models.BooleanField()),
                ('is_obstacle_exists', models.BooleanField()),
                ('is_face_clearly_shown', models.BooleanField()),
                ('added_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
