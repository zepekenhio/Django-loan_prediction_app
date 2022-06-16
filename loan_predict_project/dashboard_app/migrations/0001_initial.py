# Generated by Django 3.2.9 on 2022-04-09 10:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=100, null=True)),
                ('gender', models.PositiveBigIntegerField(choices=[(0, 'Female'), (1, 'Male')], null=True)),
                ('mstatus', models.PositiveBigIntegerField(choices=[(0, 'Single'), (1, 'Married')], null=True)),
                ('dependance', models.PositiveBigIntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('education', models.PositiveBigIntegerField(choices=[(0, 'Graduated'), (1, 'Not Graduated')], null=True)),
                ('self_employed', models.PositiveBigIntegerField(choices=[(0, 'No'), (1, 'Yes')], null=True)),
                ('appIncome', models.PositiveBigIntegerField(null=True, validators=[django.core.validators.MinValueValidator(100), django.core.validators.MaxValueValidator(10000000)])),
                ('co_appIncome', models.PositiveBigIntegerField(null=True, validators=[django.core.validators.MinValueValidator(100), django.core.validators.MaxValueValidator(10000000)])),
                ('loan_amount', models.PositiveBigIntegerField(null=True, validators=[django.core.validators.MinValueValidator(100), django.core.validators.MaxValueValidator(100000)])),
                ('loan_amount_term', models.PositiveBigIntegerField(null=True, validators=[django.core.validators.MinValueValidator(90), django.core.validators.MaxValueValidator(360)])),
                ('credit_history', models.PositiveBigIntegerField(choices=[(0, 'No'), (1, 'Yes')], null=True)),
                ('property_area', models.PositiveBigIntegerField(choices=[(0, 'Rural'), (1, 'Semi-urban'), (2, 'Urban')], null=True)),
                ('loan_status', models.CharField(blank=True, max_length=300)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
