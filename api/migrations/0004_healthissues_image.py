# Generated by Django 5.0.3 on 2024-03-05 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_user_groups_user_is_superuser_user_user_permissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthissues',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='health_issue'),
        ),
    ]
