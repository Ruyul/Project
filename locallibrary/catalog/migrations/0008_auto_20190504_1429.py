# Generated by Django 2.2 on 2019-05-04 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20190504_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='School',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='catalog.School'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='student',
            unique_together={('first_name', 'last_name', 'School')},
        ),
    ]
