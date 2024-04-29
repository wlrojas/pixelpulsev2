# Generated by Django 5.0.4 on 2024-04-16 02:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('idCategoria', models.AutoField(primary_key=True, serialize=False)),
                ('nombreCategoria', models.CharField(max_length=50, verbose_name='Nombre de categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre del cliente')),
                ('apellido', models.CharField(max_length=50, verbose_name='Apellido del cliente')),
                ('telefono', models.CharField(blank=True, max_length=100, null=True, verbose_name='Telefono del cliente')),
                ('correo', models.EmailField(max_length=254, unique=True, verbose_name='Correo electronico')),
                ('direccion', models.CharField(max_length=100, verbose_name='Direccion del cliente')),
                ('contrasena', models.CharField(max_length=50, verbose_name='Contrasena del cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('idProducto', models.AutoField(primary_key=True, serialize=False)),
                ('nombreProducto', models.CharField(max_length=50, verbose_name='Nombre del producto')),
                ('precio', models.IntegerField(verbose_name='Precio del producto')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pixelpulsegaming.categorias')),
            ],
        ),
    ]
