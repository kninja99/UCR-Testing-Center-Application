# Generated by Django 3.2.16 on 2023-02-02 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20230202_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userType',
            field=models.CharField(choices=[('student', 'student'), ('admin', 'admin'), ('proctor', 'proctor'), ('professor', 'professor')], default='student', max_length=50),
        ),
    ]
