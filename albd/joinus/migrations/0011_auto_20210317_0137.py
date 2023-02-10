# Generated by Django 3.1.7 on 2021-03-16 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('joinus', '0010_auto_20180130_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joinus',
            name='constituency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='members', to='joinus.constituency'),
        ),
        migrations.AlterField(
            model_name='joinus',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='members', to='joinus.district'),
        ),
        migrations.AlterField(
            model_name='joinus',
            name='division',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='members', to='joinus.division'),
        ),
    ]