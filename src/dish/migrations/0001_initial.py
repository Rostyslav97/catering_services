# Generated by Django 4.0.1 on 2022-03-21 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, unique=True)),
                ('description', models.TextField()),
                ('spicy', models.BooleanField(blank=True, default=None, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('output', models.CharField(max_length=20)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='category.category')),
            ],
        ),
    ]
