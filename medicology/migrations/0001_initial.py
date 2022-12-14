# Generated by Django 4.1.4 on 2022-12-15 11:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')),
                ('created_at_jalali', django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت')),
                ('updated_at_jalali', django_jalali.db.models.jDateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')),
                ('datetime', django_jalali.db.models.jDateTimeField(blank=True, null=True, verbose_name='زمان و تاریخ وقت')),
                ('status', models.CharField(choices=[('SET', 'Set'), ('DONE', 'Done'), ('ABSENT', 'Absent')], default='SET', max_length=50, verbose_name='وضعیت')),
                ('fee', models.IntegerField(default=85000, verbose_name='هزینه ویزیت به تومان')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ses_patient', to=settings.AUTH_USER_MODEL, verbose_name='بیمار')),
            ],
            options={
                'verbose_name': 'وقت',
                'verbose_name_plural': 'وقت ها',
            },
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')),
                ('created_at_jalali', django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت')),
                ('updated_at_jalali', django_jalali.db.models.jDateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')),
                ('description', models.TextField(verbose_name='توصبحات نسخه')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pre_patient', to=settings.AUTH_USER_MODEL, verbose_name='بیمار')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pre_session', to='medicology.session', verbose_name='وقت')),
            ],
            options={
                'verbose_name': 'نسخه',
                'verbose_name_plural': 'نسخه ها',
            },
        ),
    ]
