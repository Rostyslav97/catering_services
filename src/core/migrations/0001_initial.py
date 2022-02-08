# Generated by Django 4.0.1 on 2022-02-08 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('CS', 'Cold Snack'), ('HS', 'Hot Snack'), ('S', 'Salads'), ('PD', 'Pork dishes'), ('CD', 'Chicken dishes'), ('BD', 'Bird dishes'), ('SD', 'Side dishes'), ('D', 'Desserts'), ('DR', 'Drinks'), ('SN', 'Snacks')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, unique=True)),
                ('description', models.TextField()),
                ('spicy', models.BooleanField(blank=True, default=None, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('output', models.CharField(max_length=20)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.category')),
            ],
        ),
    ]