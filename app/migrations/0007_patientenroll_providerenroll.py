# Generated by Django 2.0.7 on 2018-07-15 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_vaccinelist'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientEnroll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(choices=[('female', 'Female'), ('male', 'Male')], max_length=20)),
                ('Are you pregnant or planning to be pregnant?', models.BooleanField()),
                ('Please select from the following:', models.CharField(choices=[('mom', 'Mom'), ('dad', 'Dad'), ('single', 'Single'), ('caretaker', 'Caretaker')], max_length=20)),
                ('What calendar do you currently use?', models.CharField(choices=[('google', 'Google Calendar'), ('apple', 'Apple Calendar'), ('outlook', 'Outlook Calendar'), ('desk', 'Desk Calendar')], max_length=20)),
                ('May we import your schedule?', models.BooleanField()),
                ('May we track your location?', models.BooleanField()),
                ('How do you feel about vaccines?', models.TextField(choices=[('trust', 'I trust my doctor will make the decisions that are of best interest to me.'), ('opinions', 'I have opinions on the matter and would like to learn more about vaccinations.'), ('oppose', 'I am opposed to how often vaccines are administered and would like more information.'), ('none', 'I am not interested in vaccinating my child, myself, my parent.')], max_length=200)),
                ('Would you like more info about vaccines?', models.BooleanField()),
                ('How would you like to learn more about vaccines?', models.CharField(max_length=500)),
                ('Would you be interested in taking part in advocacy?', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='ProviderEnroll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
