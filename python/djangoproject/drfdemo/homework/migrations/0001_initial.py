# Generated by Django 3.2.4 on 2022-07-17 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='课程名称')),
                ('description', models.TextField(default='暂无', max_length=1000, verbose_name='课程详情')),
                ('outtime', models.TimeField(verbose_name='下课时间')),
                ('ontime', models.TimeField(verbose_name='上课时间')),
                ('duration', models.DurationField(verbose_name='课程时间')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='价格')),
            ],
            options={
                'verbose_name': '学生',
                'verbose_name_plural': '学生',
                'db_table': 'hk_course',
            },
        ),
    ]
