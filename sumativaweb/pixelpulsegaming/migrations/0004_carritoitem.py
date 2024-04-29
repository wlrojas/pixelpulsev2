# Generated by Django 5.0.4 on 2024-04-29 04:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixelpulsegaming', '0003_delete_clientes'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarritoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=1)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pixelpulsegaming.productos')),
            ],
        ),
    ]
