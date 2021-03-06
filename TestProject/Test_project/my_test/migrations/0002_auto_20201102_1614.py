# Generated by Django 3.1.3 on 2020-11-02 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_test', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departments', to='my_test.company'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Employees', to='my_test.department'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Employees', to='my_test.status'),
        ),
    ]
