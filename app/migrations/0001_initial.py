# Generated by Django 3.1 on 2020-08-11 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SocialUserSearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(db_index=True, default=None, max_length=255, null=True, unique=True)),
                ('search_status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('finished_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'tbl_social_username',
            },
        ),
        migrations.CreateModel(
            name='SocialUserFound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website_name', models.CharField(max_length=255)),
                ('website_url', models.TextField(max_length=2000)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.socialusersearch')),
            ],
            options={
                'db_table': 'tbl_social_found_username',
                'unique_together': {('username', 'website_name')},
            },
        ),
    ]
