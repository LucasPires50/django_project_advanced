# Generated by Django 5.0 on 2024-01-03 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_alter_recurso_icone_alter_servico_icone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipe',
            name='bio',
            field=models.TextField(max_length=100, verbose_name='Bio'),
        ),
        migrations.AlterField(
            model_name='recurso',
            name='icone',
            field=models.CharField(choices=[('lni-stats-up', 'Gráfico'), ('lni-layers', 'Design'), ('lni-users', 'Usuários'), ('lni-cog', 'Engrenagem'), ('lni-rocket', 'Foguete'), ('lni-leaf', 'Folha'), ('lni-laptop-phone', 'Celular'), ('lni-mobile', 'Mobile'), ('lni-layers', 'Camadas')], max_length=16, verbose_name='Icone'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='icone',
            field=models.CharField(choices=[('lni-stats-up', 'Gráfico'), ('lni-layers', 'Design'), ('lni-users', 'Usuários'), ('lni-cog', 'Engrenagem'), ('lni-rocket', 'Foguete'), ('lni-leaf', 'Folha'), ('lni-laptop-phone', 'Celular'), ('lni-mobile', 'Mobile'), ('lni-layers', 'Camadas')], max_length=16, verbose_name='Icone'),
        ),
    ]
