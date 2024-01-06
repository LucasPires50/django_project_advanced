# Generated by Django 5.0 on 2024-01-02 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_servico_icone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='icone',
            field=models.CharField(choices=[('init-cog', 'Engrenagem'), ('init-rocket', 'Foguete'), ('init-layers', 'Desing'), ('init-mobile', 'Mobile'), ('init-stats-up', 'Gráfico'), ('init-users', 'Usuários')], max_length=13, verbose_name='Icone'),
        ),
    ]