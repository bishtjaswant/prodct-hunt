# Generated by Django 2.1.8 on 2019-04-02 06:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=244)),
                ('pub_date', models.DateTimeField()),
                ('votes_total', models.IntegerField(default=0)),
                ('body', models.TextField()),
                ('url', models.TextField()),
                ('icons', models.ImageField(upload_to='uploads')),
                ('image', models.ImageField(upload_to='uploads')),
                ('hunter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
