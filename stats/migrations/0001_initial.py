# Generated by Django 5.1.4 on 2025-01-05 14:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sotuv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('miqdor', models.FloatField()),
                ('jami', models.FloatField()),
                ('tolandi', models.FloatField(default=0)),
                ('qarz', models.FloatField(default=0)),
                ('sana', models.DateField(auto_now_add=True)),
                ('bolim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.bolim')),
                ('mahsulot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.mahsulot')),
                ('mijoz', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.mijoz')),
            ],
        ),
    ]
