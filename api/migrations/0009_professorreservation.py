# Generated by Django 3.2.16 on 2023-03-12 23:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0008_delete_professorreservation'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfessorReservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved', models.BooleanField(default=True)),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('room_aval', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.testingroomavailability')),
            ],
        ),
    ]
