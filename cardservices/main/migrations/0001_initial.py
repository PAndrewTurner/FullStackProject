# Generated by Django 4.2.7 on 2023-11-10 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreditProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_dependents', models.IntegerField()),
                ('education', models.CharField(max_length=100)),
                ('self_employed', models.BooleanField()),
                ('annual_income', models.DecimalField(decimal_places=2, max_digits=10)),
                ('loan_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('credit_score', models.IntegerField()),
                ('res_assets', models.DecimalField(decimal_places=2, max_digits=10)),
                ('com_assets', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bank_assets', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_assets', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
