# Generated by Django 3.0.3 on 2020-05-08 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User_Profile', '0001_initial'),
        ('Course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursedetail',
            name='student_agreed',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='agreed_Student', to='User_Profile.Student', verbose_name='成功匹配'),
        ),
        migrations.AddField(
            model_name='coursedetail',
            name='student_applied',
            field=models.ManyToManyField(related_name='applied_Student', to='User_Profile.Student', verbose_name='申请学员'),
        ),
        migrations.AddField(
            model_name='coursedetail',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='User_Profile.Teacher'),
        ),
    ]
