# Generated by Django 5.1.3 on 2024-12-13 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='birthday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_email', models.EmailField(max_length=255)),
                ('receiver_email', models.EmailField(max_length=255)),
                ('message', models.TextField()),
                ('date', models.DateTimeField()),
                ('image', models.ImageField(upload_to='uploads/images/')),
            ],
            options={
                'db_table': 'births',
            },
        ),
    ]
