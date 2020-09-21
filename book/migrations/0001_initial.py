# Generated by Django 3.0.3 on 2020-09-21 07:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('author', '0001_initial'),
        ('publisher', '0001_initial'),
        ('shelf', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('pages', models.PositiveSmallIntegerField(default=1)),
                ('description', models.TextField()),
                ('isbn', models.CharField(max_length=13)),
                ('read', models.BooleanField(default=False)),
                ('lent', models.BooleanField(default=False)),
                ('cover', models.ImageField(blank=True, null=True, upload_to='covers')),
                ('private', models.BooleanField(default=False)),
                ('authors', models.ManyToManyField(related_name='books', to='author.Author')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publisher.Publisher')),
                ('shelves', models.ManyToManyField(to='shelf.Shelf')),
            ],
        ),
    ]
