# Generated by Django 5.0 on 2024-01-02 14:46

import core.models
import stdimage.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_servico_icone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipe',
            name='image',
            field=stdimage.models.StdImageField(force_min_size=False, upload_to=core.models.get_file_path, variations={'thumb': {'crop': True, 'height': 480, 'width': 480}}, verbose_name='Imagens'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='icone',
            field=models.CharField(choices=[('init-stats-up', 'Gráfico'), ('init-cog', 'Engrenagem'), ('init-layers', 'Desing'), ('init-users', 'Usuários'), ('init-rocket', 'Foguete'), ('init-mobile', 'Mobile')], max_length=13, verbose_name='Icone'),
        ),
    ]
