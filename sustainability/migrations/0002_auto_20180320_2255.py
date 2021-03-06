# Generated by Django 2.0.3 on 2018-03-21 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sustainability', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SustainableReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_Recorded_By', models.CharField(max_length=50)),
                ('account_No', models.CharField(max_length=70)),
                ('building', models.CharField(choices=[('3110 Regatta Bvld', '3110 Regatta Bvld'), ('2500 Atlas Rd', '2500 Atlas Rd'), ('6000 James Watson Dr', '6000 James Watson Dr'), ('4000', '4000'), ('2000', '2000'), ('800', '800'), ('825', '825'), ('875', '875'), ('925', '925'), ('1000', '1000'), ('225', '225'), ('235', '235'), ('245', '245'), ('255', '255'), ('265', '265'), ('800', '800'), ('825', '825'), ('875', '875'), ('925', '925'), ('5731', '5731'), ('487', '487'), ('5400', '5400'), ('5500', '5500')], max_length=100)),
                ('city', models.CharField(choices=[('Hercules', 'Hercules'), ('Richmond', 'Richmond'), ('Santa Rosa', 'Santa Rosa'), ('Pleasanton', 'Pleasanton'), ('Benicia', 'Benicia')], max_length=100)),
                ('region', models.CharField(choices=[('NorCal', 'NorCal'), ('NorWest', 'NorWest'), ('APAC', 'APAC'), ('Europe', 'Europe')], max_length=100)),
                ('Type', models.CharField(choices=[('Electricity', 'Electricity'), ('Gas', 'Gas'), ('Therms', 'Therms'), ('Water', 'Water')], max_length=100)),
                ('category', models.CharField(choices=[('Monthly Statement', 'Monthly Statement'), ('Quarterly Statement', 'Quarterly Statement'), ('Annual Statement', 'Annual Statement')], max_length=150)),
                ('Amount_Consumed', models.CharField(max_length=15)),
                ('Amount_Spent', models.CharField(max_length=15)),
                ('unit', models.CharField(choices=[('kWh', 'kWh'), ('Therms', 'Therms'), ('Gallons', 'Gallons')], max_length=16)),
                ('Billing_Period_Start_Date', models.DateField()),
                ('Billing_Period_End_Date', models.DateField()),
                ('status', models.CharField(choices=[('Not Started', 'Not Started'), ('In Progress', 'In Progress'), ('Pending Review', 'Pending Review'), ('On Hold', 'On Hold'), ('Approved', 'Approved'), ('Completed', 'Completed')], max_length=150)),
                ('comment', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Sustainable_Report',
        ),
    ]
