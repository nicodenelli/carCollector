# Generated by Django 4.2 on 2023-04-12 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_car_link_filling'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='accss',
            field=models.ManyToManyField(to='main_app.accs'),
        ),
    ]
