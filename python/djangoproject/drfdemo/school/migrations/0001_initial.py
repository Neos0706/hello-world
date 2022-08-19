# Generated by Django 3.2.4 on 2022-07-16 15:59

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='姓名')),
                ('age', models.SmallIntegerField(verbose_name='年龄')),
                ('sex', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'sch_student',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='姓名')),
                ('sex', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'sch_teacher',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='课程名称')),
                ('teacher', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='course', to='school.teacher')),
            ],
            options={
                'db_table': 'sch_course',
            },
        ),
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_dtime', models.DateTimeField(auto_created=datetime.datetime.now)),
                ('score', models.DecimalField(decimal_places=1, default=0, max_digits=4, verbose_name='成绩')),
                ('course', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='c_achievement', to='school.course')),
                ('student', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='s_achievement', to='school.student')),
            ],
            options={
                'db_table': 'sch_achievement',
            },
        ),
    ]
