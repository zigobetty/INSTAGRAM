# Generated by Django 4.2.18 on 2025-02-02 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instagram_main', '0009_user_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='instagram_main.userpost')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instagram_main.user')),
            ],
        ),
    ]
