# Generated by Django 5.0.7 on 2024-07-20 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0002_alter_student_roll_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='roll_no',
            field=models.IntegerField(),
        ),
    ]
