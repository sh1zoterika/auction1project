# Generated by Django 4.2.16 on 2024-11-14 08:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monetaapp', '0007_user_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='img_proof',
        ),
        migrations.RemoveField(
            model_name='report',
            name='type',
        ),
        migrations.RemoveField(
            model_name='report',
            name='username',
        ),
        migrations.AddField(
            model_name='report',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='reason',
            field=models.CharField(blank=True, choices=[('reject', 'Отказ от получения/отправки'), ('harassment', 'Оскорбления'), ('scam', 'Мошенничество'), ('other', 'Другое')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='report_type',
            field=models.CharField(blank=True, choices=[('user', 'Жалоба на пользователя'), ('seller_admin', 'Жалоба на продавца или администратора')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='reported_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reports_sent', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='report',
            name='reported_on',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reports_received', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='report',
            name='status',
            field=models.CharField(choices=[('pending', 'Ожидание'), ('reviewed', 'Рассмотрено'), ('rejected', 'Отклонено')], default='pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='report',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='ReportImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='report_images/')),
                ('report', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='monetaapp.report')),
            ],
        ),
    ]
